# 第一版（Prompt Injection，6 篇）跑出來的問題

| 節點 | 問題 | 怎麼抓到的 | 改了什麼 |
|---|---|---|---|
| ingest s1 | source 頁沒被任何概念頁連到（孤兒頁） | lint WARN | schema 加規則：概念頁要列出 source 頁 |
| ingest s5 | 連到還不存在的 [[camel]] | lint ERROR x2 | 規則：只能連已經存在的頁 |
| ingest 全部 | 3 句多加了詮釋（例如「第一批」「證明不是偶發」） | lint 全過，人工語意檢查才抓到 | 加 fact-check 節點 |
| 大綱 | 「自己動手試試看」那張沒有任何 wiki 頁支撐 | check_outline ERROR | 刪掉，不硬寫 |

原始 lint 輸出在 runs/prev/。
