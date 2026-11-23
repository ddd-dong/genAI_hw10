"""Render every slide to PNG and flag slides whose content overflows the 1280x720 stage."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent
out = ROOT / "runs" / "shots"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1280, "height": 728})
    pg.goto((ROOT / "slides" / "index.html").as_uri())
    n = pg.eval_on_selector_all(".slide", "els => els.length")
    bad = []
    for i in range(n):
        pg.evaluate(f"location.hash='#{i+1}'; dispatchEvent(new KeyboardEvent('keydown',{{key:'Home'}}));")
        for _ in range(i):
            pg.keyboard.press("ArrowRight")
        over = pg.evaluate("""() => { const s=document.querySelector('.slide.active');
          const r=s.getBoundingClientRect(); let worst=0;
          s.querySelectorAll('*').forEach(e=>{ if(e.closest('.src-foot')) return; const q=e.getBoundingClientRect();
            if(q.height>0) worst=Math.max(worst, q.bottom - (r.bottom - 44*r.height/720)); });
          return worst; }""")
        if over > 1:
            bad.append((i + 1, round(over)))
        pg.screenshot(path=str(out / f"slide{i+1:02d}.png"))
    b.close()
print("overflow:", bad if bad else "none")
