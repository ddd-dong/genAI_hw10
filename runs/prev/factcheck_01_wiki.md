# fact-check 01：wiki 對 raw 的語意檢查（lint 全過之後做）

方法：把每個 wiki 條列跟它標的 raw 筆記逐條對照，問「raw 裡有沒有這句話的意思」。

| 頁面 | 原本的句子 | 問題 | 處理 |
|---|---|---|---|
| sources/s2 | 第一批系統化研究 prompt injection 的論文之一 | raw 沒說「第一批」，是寫的時候自己加的 | 改成「用框架化方式測試」 |
| concepts/prompt-injection | PromptInject 證明不是偶發現象 | raw 沒有這個結論，是推論 | 改成 raw 的結論：能力不高的攻擊者用簡單輸入就能做到 |
| concepts/real-world-incidents | ……所以很容易擴散 | raw 筆記沒寫擴散（原文續篇有提，但 raw 沒收） | 刪掉後半句 |

其他 81 條條列對得上 raw。3 個問題都屬於「寫的時候多加一點詮釋」，lint 抓不到，因為來源標記、數字、連結都是對的。
