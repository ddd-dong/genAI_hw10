"""Check slides/outline.md against the wiki before generating slides."""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
pages = {p.stem for p in (ROOT / "wiki").rglob("*.md")}
concepts = {p.stem for p in (ROOT / "wiki" / "concepts").glob("*.md")}
text = (ROOT / "slides" / "outline.md").read_text(encoding="utf-8")
slides = re.split(r"^## ", text, flags=re.M)[1:]
errors, used = [], set()
for s in slides:
    title = s.splitlines()[0]
    q = re.search(r"^- q: (.+)$", s, re.M)
    w = re.search(r"^- wiki: (.+)$", s, re.M)
    if not q:
        errors.append(f"slide '{title}': no question")
    if not w:
        errors.append(f"slide '{title}': no wiki pages")
        continue
    for name in [x.strip() for x in w.group(1).split(",")]:
        if name not in pages:
            errors.append(f"slide '{title}': wiki page '{name}' does not exist (need ingest or drop slide)")
        used.add(name)
missing = sorted(concepts - used)
print(f"slides={len(slides)} errors={len(errors)} unused_concepts={missing}")
for e in errors:
    print("ERROR", e)
sys.exit(1 if errors else 0)
