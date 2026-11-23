"""Helper: add a bullet under a section of a wiki page, and add a source to its 來源 line.
usage: addfact.py PAGE "SECTION" "BULLET TEXT [src:sX]"
"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
page, section, bullet = sys.argv[1], sys.argv[2], sys.argv[3]
path = next(ROOT.joinpath("wiki").rglob(f"{page}.md"))
lines = path.read_text(encoding="utf-8").splitlines()
head = f"## {section}"
if head not in lines:
    rel = lines.index("## 相關頁面")
    lines[rel:rel] = [head, ""]
i = lines.index(head) + 1
while i < len(lines) and not lines[i].startswith("## "):
    i += 1
while lines[i-1].strip() == "":
    i -= 1
lines.insert(i, "- " + bullet)
if i < len(lines) and lines[i+1:i+2] != [""] and lines[i+1].startswith("## "):
    lines.insert(i+1, "")
for sid in re.findall(r"\[src:(s\d+)\]", bullet):
    for j, l in enumerate(lines):
        if l.startswith("來源：") and f"[[{sid}]]" not in l:
            lines[j] = l + f"、[[{sid}]]"
path.write_text("\n".join(lines) + "\n", encoding="utf-8")
