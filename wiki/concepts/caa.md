# CAA（Contrastive Activation Addition）

> 一句話：ActAdd 的加強版，不只用一對例子，而是用很多對例子平均出一個方向。

## 步驟
- 準備很多對對比例子，例如事實回答 vs 幻覺回答 [src:s6]
- 取 residual stream activation 差值的平均，當作 steering vector [src:s6]
- 推論時在使用者 prompt 之後的每個 token 位置加上這個向量，乘正係數加強、乘負係數減弱 [src:s6]

## 結果
- 在 Llama 2 Chat（7B 到 70B）上測六種行為，加向量讓行為變多、減向量讓行為變少 [src:s6]
- 例子：在 Llama 2 7B 第 13 層對 sycophancy（諂媚）做 steering [src:s6]
- 疊在 finetuning 和 system prompt 之上仍然有效，對模型能力影響很小 [src:s6]

## 跟 ActAdd 的差別
- [[actadd]] 用一對 prompt，CAA 平均很多對比例子 [src:s6]

## 相關頁面
來源：[[s6]]
[[activation-steering]]、[[actadd]]
