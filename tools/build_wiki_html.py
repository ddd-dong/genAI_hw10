"""Bundle the whole wiki (schema, discussion, wiki pages, raw notes, run logs) into one browsable HTML page."""
import base64
import html
import json
import re
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
groups = [
    ("作業說明", [ROOT / "REQUIREMENTS.md", ROOT / "AGENTS.md", ROOT / "WORKFLOW.md", ROOT / "CHECK_REPORT.md", ROOT / "00_discussion.md"]),
    ("Wiki", [ROOT / "wiki/index.md"] + sorted((ROOT / "wiki/concepts").glob("*.md")) + sorted((ROOT / "wiki/sources").glob("*.md")) + [ROOT / "wiki/log.md"]),
    ("Raw 來源筆記", sorted((ROOT / "raw").glob("*.md"))),
    ("簡報", [ROOT / "slides/outline.md", ROOT / "slides/context.md"]),
    ("執行紀錄", sorted((ROOT / "runs").glob("*.md")) + sorted((ROOT / "runs").glob("*.txt")) + sorted((ROOT / "runs/prev").glob("*"))),
]
pages, nav = {}, []
for gname, files in groups:
    items = []
    for f in files:
        key = f.stem if f.parent.name in ("concepts", "sources", "wiki") else re.sub(r"[^A-Za-z0-9-]", "-", f.relative_to(ROOT).as_posix().rsplit(".", 1)[0])
        text = f.read_text(encoding="utf-8")
        if f.suffix == ".txt" or f.parent.name == "prev":
            body = "<pre>" + html.escape(text) + "</pre>"
        else:
            text = re.sub(r"^(來源：.*)$", r"\1  ", text, flags=re.M)
            text = re.sub(r"\[\[([^\]]+)\]\]", lambda m: f'<a class="wl" href="#{m.group(1)}">{m.group(1)}</a>', text)
            text = re.sub(r"\[src:(s\d+)\]", lambda m: f'<a class="src" href="#{m.group(1)}">{m.group(1)}</a>', text)
            body = markdown.markdown(text, extensions=["tables", "fenced_code"])
        title = f.relative_to(ROOT).as_posix()
        pages[key] = {"title": title, "html": body}
        items.append((key, f.stem if gname == "Wiki" else title))
    nav.append((gname, items))
nav_html = "".join(
    f'<details open><summary>{g}</summary>' + "".join(f'<a href="#{k}">{html.escape(t)}</a>' for k, t in items) + "</details>"
    for g, items in nav)
tpl = (ROOT / "tools" / "wiki_template.html").read_text(encoding="utf-8")
svg_uri = "data:image/svg+xml;base64," + base64.b64encode((ROOT / "workflow.svg").read_bytes()).decode()
for v in pages.values():
    v["html"] = v["html"].replace('src="workflow.png"', f'src="{svg_uri}" style="max-width:100%"')
out = tpl.replace("/*PAGES*/", json.dumps(pages, ensure_ascii=False)).replace("<!--NAV-->", nav_html)
(ROOT / "wiki.html").write_text(out, encoding="utf-8")
print("pages:", len(pages))
