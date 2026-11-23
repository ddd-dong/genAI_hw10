# s7 Wu, Arora, Geiger, Wang, Huang, Jurafsky, Manning, Potts, "AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders"
- URL: https://arxiv.org/abs/2501.17148 ；ICML 2025（PMLR 267）
- 日期: 2025-01-28
- 擷取: 2026-11-23

## 筆記（改寫）
- 在這之前沒有 benchmark 可以直接比較各種 steering 方法，所以做了 AxBench：大規模的 steering 和概念偵測 benchmark。
- 在 Gemma-2-2B 和 9B 上實驗。
- Steering：prompting 贏過所有方法，第二名是 finetuning。
- 概念偵測（判斷某概念有沒有出現）：difference-in-means（DiffMean）這種表示法方法最好。
- 兩項評估裡 SAE 都沒有競爭力。
- 提出 ReFT-r1（rank-1 representation finetuning），兩項都有競爭力，又保有可解釋性。
- 作者自己的結論：這是 steering 技術目前限制的「清醒證據」，但同時學偵測和 steering 可能是方向。
