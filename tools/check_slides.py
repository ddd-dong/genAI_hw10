"""Check slides/index.html against the wiki.
1. every <section class="slide"> has data-wiki, and every page exists
2. every number (2+ digits) shown on a slide appears in one of its cited wiki pages
3. every jargon term is wrapped in <dfn> the first time it appears in the deck
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = {p.stem: p.read_text(encoding="utf-8") for p in (ROOT / "wiki").rglob("*.md")}
TERMS = ["SAE", "steering", "polysemanticity", "superposition", "residual stream",
         "sparsity penalty", "steering vector", "forward pass", "JumpReLU", "benchmark"]
NUM_RE = re.compile(r"(?<![\w.#])\d+(?:\.\d+)?%?")


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth, self.skip = [], None, 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in a.get("class", ""):
            self.cur = {"wiki": a.get("data-wiki"), "text": "", "html": "", "id": a.get("id")}
            self.depth = 1
            return
        if self.cur is None:
            return
        if tag == "section":
            self.depth += 1
        if tag in ("script", "style") or "src-foot" in a.get("class", ""):
            self.skip += 1
        attr_txt = "".join(f' {k}="{v}"' for k, v in attrs)
        self.cur["html"] += f"<{tag}{attr_txt}>"

    def handle_endtag(self, tag):
        if self.cur is None:
            return
        if tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.slides.append(self.cur)
                self.cur = None
                return
        if self.skip and tag in ("script", "style", "footer"):
            self.skip -= 1
        self.cur["html"] += f"</{tag}>"

    def handle_data(self, data):
        if self.cur is not None:
            self.cur["html"] += data
            if not self.skip:
                self.cur["text"] += data


def main():
    html = (ROOT / "slides" / "index.html").read_text(encoding="utf-8")
    sp = SlideParser()
    sp.feed(html)
    errors = []
    seen_terms = set()
    for n, s in enumerate(sp.slides, 1):
        tag = f"slide {n} ({s['id']})"
        if not s["wiki"]:
            errors.append(f"{tag}: no data-wiki")
            continue
        names = [x.strip() for x in s["wiki"].split(",")]
        cited = ""
        for name in names:
            if name not in PAGES:
                errors.append(f"{tag}: wiki page '{name}' does not exist")
            else:
                cited += PAGES[name]
        for num in NUM_RE.findall(s["text"]):
            if len(num.rstrip("%")) < 2:
                continue
            if num not in cited:
                errors.append(f"{tag}: number '{num}' not in cited wiki pages {names}")
        for t in TERMS:
            if t in seen_terms:
                continue
            if re.search(re.escape(t), s["text"], re.I):
                seen_terms.add(t)
                if not re.search(r"<dfn[^>]*>[^<]*" + re.escape(t), s["html"], re.I):
                    errors.append(f"{tag}: first use of term '{t}' has no <dfn> explanation")
    print(f"slides={len(sp.slides)} errors={len(errors)}")
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
