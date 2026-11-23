"""Draw the workflow graph as SVG (and PNG via headless Chrome). Numbers come from the actual v2 run."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1130
CX, NW, NH = 470, 250, 46
COL = {"human": ("#eceff3", "#6b778a"), "gen": ("#e6eefc", "#2f6fdb"),
       "prog": ("#e3f4ea", "#2f8f5b"), "llm": ("#fcebe1", "#d9662b")}
nodes = [  # key, y, label, kind, note (left), x-offset
    ("A", 60, "A 討論（先討論、後生成）", "human", "主題、對象、8 篇資料、12 個概念頁先定好"),
    ("B", 175, "B 取得資料、寫 raw 筆記", "gen", ""),
    ("C", 245, "C 寫入 wiki", "gen", ""),
    ("D", 315, "D 格式檢查", "prog", "8 次都是 0 錯誤"),
    ("E", 420, "E 內容核對（對照原文筆記）", "llm", "98 條 + 12 句摘要：6 個問題，已修正"),
    ("F", 510, "F 寫大綱", "gen", ""),
    ("G", 580, "G 大綱檢查", "prog", "16 張 0 錯誤"),
    ("H", 650, "H 取出內容", "prog", "只取已核對原文的內容"),
    ("I", 720, "I 生成 HTML 簡報", "gen", ""),
    ("J", 790, "J 簡報檢查", "prog", "第 1 次 2 個錯誤（數字標錯 wiki 頁），修正後 0"),
    ("L", 860, "L 用字檢查", "prog", "3 輪被標出：9、2、0 句"),
    ("K", 960, "K 版面檢查", "prog", "沒有超出版面；3 張留白過多已調整"),
    ("Z", 1050, "輸出：Wiki + 教學簡報", "human", ""),
]
pos = {k: y for k, y, *_ in nodes}
s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="PingFang TC, Noto Sans TC, Microsoft JhengHei, sans-serif">',
     '<rect width="100%" height="100%" fill="#fbfaf7"/>',
     '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#5f6b7d"/></marker>',
     '<marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#b5462f"/></marker></defs>',
     f'<text x="40" y="34" font-size="22" font-weight="700" fill="#1d2330">SAE &amp; Steering LLM Wiki：workflow</text>']
# loop box for B-C-D
s.append(f'<rect x="{CX-NW//2-24}" y="118" width="{NW+48}" height="236" rx="14" fill="none" stroke="#2f6fdb" stroke-dasharray="6 5"/>')
s.append(f'<text x="{CX-NW//2-36}" y="140" font-size="14" text-anchor="end" fill="#2f6fdb">每篇資料各跑一次，共 8 次</text>')
# section labels
s.append('<text x="40" y="130" font-size="15" font-weight="700" fill="#5f6b7d">建 Wiki</text>')
s.append('<line x1="40" y1="475" x2="1040" y2="475" stroke="#d9dee6"/>')
s.append('<text x="40" y="500" font-size="15" font-weight="700" fill="#5f6b7d">做簡報</text>')
def box(k, y, label, kind, x=CX):
    f, st = COL[kind]
    return (f'<rect x="{x-NW//2}" y="{y-NH//2}" width="{NW}" height="{NH}" rx="10" fill="{f}" stroke="{st}" stroke-width="2"/>'
            f'<text x="{x}" y="{y+6}" font-size="17" text-anchor="middle" fill="#1d2330">{label}</text>')
for k, y, label, kind, note in nodes:
    s.append(box(k, y, label, kind))
    if note:
        s.append(f'<text x="{CX-NW//2-36}" y="{y+5}" font-size="13.5" text-anchor="end" fill="#5f6b7d">{note}</text>')
# M node to the right of L
MX = 820
s.append(box("M", 910, "M 用字修改（刪除或改寫）", "llm", MX))
s.append(f'<text x="{MX}" y="950" font-size="13.5" text-anchor="middle" fill="#5f6b7d">刪除 8 句、改寫 5 句；人工閱讀另找到 4 句</text>')
# main down arrows
order = [k for k, *_ in nodes]
for a, b in zip(order, order[1:]):
    s.append(f'<line x1="{CX}" y1="{pos[a]+NH//2}" x2="{CX}" y2="{pos[b]-NH//2-2}" stroke="#5f6b7d" stroke-width="2" marker-end="url(#a)"/>')
R = CX + NW // 2
def back(frm, to, x, label, ly=None, d1=0, d2=0):
    y1, y2 = pos[frm] + d1, pos[to] + d2
    s.append(f'<path d="M{R} {y1} H{x} V{y2} H{R+4}" fill="none" stroke="#b5462f" stroke-width="2" marker-end="url(#r)"/>')
    s.append(f'<text x="{x+8}" y="{(ly or (y1+y2)//2)+5}" font-size="13.5" fill="#b5462f">{label}</text>')
back("D", "C", 640, "有錯誤：修正", d2=-8)
back("E", "C", 770, "超出來源、標錯：修正", d2=8)
back("G", "F", 640, "沒有 wiki 內容：刪掉那張")
s.append(f'<path d="M{R} {pos["G"]+8} H{1000} V{pos["B"]} H{R+28}" fill="none" stroke="#b5462f" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#r)"/>')
s.append(f'<text x="1006" y="{pos["B"]+30}" font-size="13" fill="#b5462f" transform="rotate(90 1006 {pos["B"]+30})">或回 B 補資料</text>')
back("J", "I", 640, "數字不在標明的頁：修正", d1=-10)
# L -> M
s.append(f'<path d="M{R} {pos["L"]} H{MX} V{910-NH//2-2}" fill="none" stroke="#b5462f" stroke-width="2" marker-end="url(#r)"/>')
s.append(f'<text x="{R+10}" y="{pos["L"]-8}" font-size="13.5" fill="#b5462f">有句子被標出</text>')
# M -> back to J (max 3 rounds)
s.append(f'<path d="M{MX+NW//2} 910 H{1000} V{pos["J"]+10} H{R+4}" fill="none" stroke="#d9662b" stroke-width="2" marker-end="url(#r)"/>')
s.append(f'<text x="{MX+NW//2-118}" y="{pos["J"]-8}" font-size="13.5" fill="#d9662b">改完回 J、L 重新檢查（最多 3 輪）</text>')
L = CX - NW // 2
s.append(f'<path d="M{L} {pos["K"]} H{L-12} V{pos["I"]} H{L-4}" fill="none" stroke="#b5462f" stroke-width="2" marker-end="url(#r)"/>')
s.append(f'<text x="{L-20}" y="{pos["K"]+26}" font-size="13.5" text-anchor="end" fill="#b5462f">超出版面：回 I 修正</text>')
# legend
lx, ly = 40, 1100
for i, (kind, name) in enumerate([("human", "人 / 輸出"), ("gen", "LLM 生成"), ("prog", "程式檢查"), ("llm", "LLM + 人檢查")]):
    f, st = COL[kind]
    s.append(f'<rect x="{lx+i*170}" y="{ly-14}" width="22" height="18" rx="4" fill="{f}" stroke="{st}" stroke-width="2"/><text x="{lx+i*170+30}" y="{ly+1}" font-size="14" fill="#1d2330">{name}</text>')
s.append(f'<line x1="{lx+690}" y1="{ly-5}" x2="{lx+730}" y2="{ly-5}" stroke="#b5462f" stroke-width="2" marker-end="url(#r)"/><text x="{lx+740}" y="{ly+1}" font-size="14">失敗時回去</text>')
s.append("</svg>")
svg = "\n".join(s)
(ROOT / "workflow.svg").write_text(svg, encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
    pg.screenshot(path=str(ROOT / "workflow.png"))
    b.close()
print("ok")
