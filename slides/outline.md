# 簡報大綱：SAE 與 Steering

對象：學過一點 ML、沒碰過 interpretability 的人。

## 1 SAE 與 Steering：看懂並操控模型的腦袋
- q: 這份簡報要講什麼
- wiki: linear-representation, sparse-autoencoder, activation-steering

## 2 問題：神經元看不懂
- q: 為什麼不能直接看神經元就知道模型在想什麼
- wiki: neuron-vs-feature

## 3 原因：Superposition
- q: 為什麼神經元會是多義的
- wiki: superposition

## 4 關鍵假設：概念 = 方向
- q: 後面所有方法共同的前提是什麼
- wiki: linear-representation

## 5 SAE 是什麼
- q: SAE 的結構和訓練目標
- wiki: sparse-autoencoder

## 6 第一次成功：512 個神經元變 4000 多個特徵
- q: 2023 年小模型上的結果
- wiki: sae-features, s2

## 7 放大到 Claude 3 Sonnet
- q: 大模型上找到什麼樣的特徵
- wiki: sparse-autoencoder, sae-features

## 8 Golden Gate Bridge 特徵
- q: 調整一個特徵會發生什麼
- wiki: feature-steering

## 9 自己也能看：Gemma Scope
- q: 一般人怎麼玩 SAE
- wiki: open-tools

## 10 另一條路：Activation Steering
- q: 不用 SAE 也能操控模型嗎
- wiki: activation-steering

## 11 ActAdd：Love 減 Hate
- q: 最簡單的 steering vector 怎麼算
- wiki: actadd

## 12 CAA：很多對例子取平均
- q: CAA 跟 ActAdd 差在哪、效果如何
- wiki: caa

## 13 SAE steering 好用嗎？AxBench
- q: 公平比較下誰贏
- wiki: steering-evaluation

## 14 爭議還沒結束
- q: 反駁說了什麼、SAE 還有哪些限制
- wiki: steering-evaluation, sae-limitations

## 15 重點回顧 + 小測驗
- q: 三件一定要記住的事
- wiki: superposition, sparse-autoencoder, activation-steering, steering-evaluation

## 16 參考資料
- q: 想深入要看什麼
- wiki: index
