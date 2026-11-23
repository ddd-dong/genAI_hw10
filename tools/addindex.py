"""usage: addindex.py Sources|Concepts "[[name]]：summary" """
import sys
from pathlib import Path
p = Path(__file__).resolve().parent.parent / "wiki" / "index.md"
sec, entry = sys.argv[1], sys.argv[2]
if not p.exists():
    p.write_text("# SAE & Steering LLM Wiki：目錄\n\n## Sources\n\n## Concepts\n", encoding="utf-8")
lines = p.read_text(encoding="utf-8").splitlines()
i = lines.index(f"## {sec}") + 1
while i < len(lines) and lines[i].startswith("- "):
    i += 1
lines.insert(i, "- " + entry)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
