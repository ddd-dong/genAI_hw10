# fact-check 01：wiki 對 raw 的語意檢查（lint 0 error 之後做）

方法：98 條有 [src] 的條列 + 12 句「一句話」，逐條對回 raw。

| # | 頁面 | 問題 | 類型 | 處理 |
|---|---|---|---|---|
| 1 | caa 一句話 | 「更穩的方向」raw 沒說 | 多加詮釋 | 刪掉「更穩」 |
| 2 | actadd | 「讓方向更穩」同上 | 多加詮釋 | 改成「不是只用一對」 |
| 3 | neuron-vs-feature | 自己想的倉庫比喻標成 [src:s1] | 假引用 | 移到「比喻（自己想的）」區，lint 加豁免 |
| 4 | linear-representation | 「SAE 和 steering 的共同前提」標 s1，但 s1 沒講 SAE/steering | 引錯來源 | 拆兩句，改引 s2、s5 |
| 5 | activation-steering | 線性表示的說法只標 s5 | 引用不完整 | 改成 [src:s1][src:s5] |
| 6 | steering-evaluation 一句話 | s7 ingest 時就寫了「跟怎麼挑特徵有關」，這是 s8 的內容 | 提前寫入未 ingest 的內容 | s8 進來後有支撐了；schema 加規則，一句話也要檢查 |
| 補 | feature-steering | 「10 倍」只來自第三方摘要 | 來源可信度 | 加到「待確認」 |

lint 都抓不到這些，因為格式、數字、連結都是對的。
