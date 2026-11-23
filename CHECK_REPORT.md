# 檢查報告：一次實際執行（第二版，SAE & Steering）

執行日期：2026-11-23。每一行都能在 `runs/` 找到原始輸出。

| 節點 | 檢查 | 結果 | 處理 | 原始輸出 |
|---|---|---|---|---|
| D Lint（s1 到 s8，8 圈） | 壞連結、缺 [src]、數字不在 raw、孤兒頁、index 漏頁 | 8 圈都是 0 error；warning 只有「還沒 ingest 的來源」，從 7 降到 0 | 不用改 | runs/lint_01_s1.txt 到 lint_08_s8.txt |
| E Fact-check | 98 條條列 + 12 句「一句話」對回 raw | 6 個問題 | 全部修掉，lint 重跑 0 | runs/factcheck_01_wiki.md、lint_09_after_factcheck.txt |
| G 大綱檢查 | 每張有沒有對到存在的 wiki 頁、概念頁有沒有都用到 | 16 張 0 error | 不用改 | runs/outline_check_01.txt |
| J 簡報檢查（第 1 次） | data-wiki 頁存在、數字在引用頁、術語有 dfn | 2 error | 投影片 6「80 億」、投影片 12「ACL 2024」改引正確的 wiki 頁 | runs/slides_check_01.txt |
| J 簡報檢查（第 2 次） | 同上 | 0 error | | runs/slides_check_02.txt |
| K 截圖檢查 | 每張截圖、偵測超出版面 | 0 overflow，但目測 3 張卡片撐太高 | 改 CSS（不撐滿 + 垂直置中） | runs/visual_check_01.txt 到 03 |
| L 清稿檢查（第 1 輪） | 流程用語、制式 AI 句型 | 9 個 flag | 交給 M | runs/clean_check_01.txt |
| M 清稿改寫 + 人讀 | | 人讀補抓 4 個 regex 漏掉的 | 刪 8 句、改寫 5 句；「10 倍」回原文核對，拿掉待確認 | runs/clean_check_log.md |
| L 清稿檢查（第 2 輪） | | 2 個 flag（1 誤報、1 參考資料頁） | 改寫法、參考資料頁加白名單 | runs/clean_check_02.txt |
| L 清稿檢查（第 3 輪） | | 0 | | runs/clean_check_03.txt |
| J 簡報檢查（清稿後） | | 0 error | | runs/slides_check_05.txt |

## Fact-check 抓到的 6 個問題

| 頁面 | 問題 | 類型 |
|---|---|---|
| caa 一句話 | 「更穩的方向」raw 沒說 | 多加詮釋 |
| actadd | 「讓方向更穩」 | 多加詮釋 |
| neuron-vs-feature | 自己想的比喻標成 [src:s1] | 假引用 |
| linear-representation | 「SAE 和 steering 的共同前提」標 s1，s1 沒講 | 引錯來源 |
| activation-steering | 線性表示只標 s5 | 引用不完整 |
| steering-evaluation 一句話 | s7 ingest 時就寫進 s8 的內容 | 提前寫入 |

## 第一版（Prompt Injection）對照

| 節點 | 第一版 | 第二版 | 差在哪 |
|---|---|---|---|
| D Lint | 1 warning（孤兒頁）+ 2 error（連到還沒建的頁） | 0 error | 第一版的教訓寫進 AGENTS.md 規則 |
| E Fact-check | 3 個問題 | 6 個問題 | 第二版主題更技術，詮釋更容易多講 |
| G 大綱檢查 | 1 error（一張沒 wiki 支撐，刪掉） | 0 error | 大綱時就照 wiki 頁寫 |

原始輸出在 runs/prev/。

## 最後狀態
lint 0 error、fact-check 無未解問題、大綱檢查 0、簡報檢查 0、清稿 0 flag、截圖 0 overflow
