"""Lint the LLM wiki. Exit code 1 if there are errors."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
SRC_RE = re.compile(r"\[src:(s\d+)\]")
NUM_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+)?%?")
EXEMPT_SECTIONS = ("相關頁面", "待確認", "比喻")


def load_pages():
    pages = {}
    for p in WIKI.rglob("*.md"):
        pages[p.stem] = p
    return pages


def raw_sources():
    out = {}
    for p in RAW.glob("s*.md"):
        sid = p.stem.split("-")[0]
        out[sid] = p.read_text(encoding="utf-8")
    return out


def strip_marks(line):
    line = SRC_RE.sub("", line)
    line = LINK_RE.sub("", line)
    return line


def main():
    pages = load_pages()
    raws = raw_sources()
    errors, warnings = [], []
    inbound = {name: 0 for name in pages}

    for name, path in pages.items():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target not in pages:
                errors.append(f"{rel}: broken link [[{target}]]")
            elif target != name and name not in ("log", "index"):
                inbound[target] += 1

        if name in ("index", "log"):
            continue

        if path.parent.name == "concepts" and "> 一句話：" not in text:
            errors.append(f"{rel}: missing '> 一句話：' line")

        section = ""
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith("## "):
                section = line[3:].strip()
                continue
            if not line.lstrip().startswith("- "):
                continue
            if section.startswith(EXEMPT_SECTIONS):
                continue
            srcs = SRC_RE.findall(line)
            if not srcs:
                errors.append(f"{rel}:{i}: bullet has no [src:...] tag")
                continue
            for s in srcs:
                if s not in raws:
                    errors.append(f"{rel}:{i}: unknown source id {s}")
            cited_text = "\n".join(raws.get(s, "") for s in srcs)
            for num in NUM_RE.findall(strip_marks(line)):
                if len(num.rstrip("%")) < 2:
                    continue
                if num not in cited_text:
                    errors.append(f"{rel}:{i}: number '{num}' not found in cited raw {srcs}")

    index_text = (WIKI / "index.md").read_text(encoding="utf-8") if "index" in pages else ""
    for name in pages:
        if name in ("index", "log"):
            continue
        if f"[[{name}]]" not in index_text:
            errors.append(f"index.md: page '{name}' not listed")
        if inbound[name] == 0:
            warnings.append(f"orphan page: '{name}' has no inbound links except index")

    for sid in raws:
        if sid not in pages:
            warnings.append(f"raw {sid} has no wiki/sources/{sid}.md yet")

    print(f"pages={len(pages)} raw={len(raws)} errors={len(errors)} warnings={len(warnings)}")
    for e in errors:
        print("ERROR", e)
    for w in warnings:
        print("WARN ", w)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
