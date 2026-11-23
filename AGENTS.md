# AGENTS.md：SAE & Steering LLM Wiki 的規則（schema）

你是這個 wiki 的維護者。使用者負責挑資料、問問題；你負責寫和整理 wiki。

## 目錄
- `raw/sX-*.md`：原始資料筆記。ingest 之後不改原本內容，回原文核對時只能在最後加 `## 核對` 段。
- `slides/`：大綱、查 wiki 的結果、HTML 簡報。
- `tools/`：lint、大綱檢查、查 wiki、簡報檢查、清稿檢查、截圖腳本。
- `runs/`：每次檢查的輸出。
- `wiki/sources/sX.md`：每篇資料一頁摘要。
- `wiki/concepts/*.md`：概念頁，可以被多篇資料更新。
- `wiki/index.md`：所有頁面的目錄，每頁一行摘要。
- `wiki/log.md`：每次操作的紀錄（ingest / query / lint）。

## 寫作規則
1. 概念頁開頭要有 `> 一句話：...`，用沒學過的人看得懂的話。
2. 每一條事實（以 `- ` 開頭的條列）結尾都要有來源標記 `[src:s1]`，可以多個 `[src:s1][src:s4]`。
3. 概念頁的「相關頁面」要列出用到的 source 頁（例如 [[s1]]），不然 source 頁會變孤兒。
4. 頁面之間用 `[[頁名]]` 互連，頁名就是檔名（不含 .md）。
5. 不能寫來源裡沒有的數字。數字一定要能在 raw/ 找到。
6. 不確定的東西寫在 `## 待確認`，不要混進事實條列。
7. 自己想的比喻放在 `## 比喻（自己想的，不是來源內容）`，不能標 [src]。
8. 「一句話」也要能從該頁條列推出來，不能偷放還沒 ingest 的內容。
9. 用繁體中文，術語第一次出現附英文。不要用破折號。

## 操作
### Ingest（一次一篇）
1. 讀 raw/sX，先列 3 個重點確認方向再寫。
2. 寫 wiki/sources/sX.md。
3. 更新或新增相關 concepts 頁（一篇資料通常會動到 3 到 5 頁）。
4. 更新 index.md、append log.md。
5. 跑 `python3 tools/lint_wiki.py`，有 error 就修到 0 才能 ingest 下一篇。
6. 連結只能連已經存在的頁；之後才會建的頁先寫純文字。
7. 全部 ingest 完做一次語意 fact-check：每條條列對回 raw，看有沒有多加詮釋。

### Query
回答問題時只能用 wiki 內容，並標出用到哪些頁。好的回答可以存成新頁。

### Lint
`tools/lint_wiki.py` 檢查：壞連結、缺來源標記、來源 id 不存在、孤兒頁、index 漏頁、數字不在 raw 裡。

### 產生簡報
1. 先寫 `slides/outline.md`：每張投影片要回答什麼問題、用到哪些 wiki 頁。
2. 跑 `tools/check_outline.py`，每張都要對到存在的 wiki 頁才可以生成。
3. 生成 `slides/index.html`，每張 `<section>` 要有 `data-wiki="頁名,頁名"`。
4. 跑 `tools/check_slides.py`：引用頁存在、投影片上的數字都在引用頁裡、術語有解釋。
5. 跑 `tools/clean_check.py`：投影片本體不能出現我們自己流程的話（wiki、待確認、來源、示意、按 S），也不能有制式 AI 句型（這就是、核心問題只有一個、比較穩的結論、站在……上、破折號等）。
   - 被標的句子先問「刪掉學生會少學到東西嗎？」不會就刪，會就改直白。
   - 改完要重跑 check_slides（數字可能被改掉）和 clean_check，最多 3 輪，還有就交給人看。
   - 來源標記只能放 footer。參考資料頁用 data-allow-meta 白名單。
6. 人讀一遍：regex 抓不到的擬人、重複前一句的總結句、裝飾性比喻。
7. 截圖看排版。
