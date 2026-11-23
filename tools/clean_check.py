"""Clean-up check for slides: flag text that the audience doesn't need.
META: notes about our own pipeline (wiki, 待確認, sources, 示意...) leaking into the slide body
AI:   stock phrasing that reads like generated text
Footer (.src-foot) and slides marked data-allow-meta are skipped.
"""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_slides import SlideParser

ROOT = Path(__file__).resolve().parent.parent
RULES = {
    "META": [r"wiki", r"待確認", r"第三方", r"示意", r"自己想的", r"來源", r"按 ?S", r"\bs\d\b", r"摘要頁"],
    "AI": [r"這就是", r"核心(問題|在於)", r"只有一個", r"關鍵(是|在於)", r"本質上", r"值得注意", r"總(結|之)",
           r"簡單來說", r"換句話說", r"不只.{0,12}而是", r"比較穩的結論", r"讓我們", r"站在.{0,8}上",
           r"——|—", r"其實", r"真正的", r"可以說", r"一句話"],
}


def sentences(text):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[。？！])", text) if s.strip()]


def main():
    html = (ROOT / "slides" / "index.html").read_text(encoding="utf-8")
    allow = set(re.findall(r'id="([^"]+)"[^>]*data-allow-meta', html))
    sp = SlideParser()
    sp.feed(html)
    hits = []
    for n, s in enumerate(sp.slides, 1):
        if s["id"] in allow:
            continue
        for sent in sentences(s["text"]):
            for cat, pats in RULES.items():
                for pat in pats:
                    if re.search(pat, sent, re.I):
                        hits.append((n, s["id"], cat, pat, sent[:70]))
                        break
    print(f"flags={len(hits)}")
    for h in hits:
        print("FLAG slide %d (%s) [%s] /%s/ : %s" % h)
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
