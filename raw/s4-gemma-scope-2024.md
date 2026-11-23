# s4 Lieberum, Rajamanoharan, Conmy, Smith, ..., Nanda, "Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2"
- URL: https://arxiv.org/abs/2408.05147 ；部落格 https://deepmind.google/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/
- 日期: 2024-07-31 公布（arXiv 2024-08-09）；Google DeepMind；BlackboxNLP 2024
- 擷取: 2026-11-23

## 筆記（改寫）
- 公開一整套 JumpReLU SAE，訓練在 Gemma 2 2B 和 9B 的每一層、每個子層，以及 27B 的部分層。
- 超過 400 個 SAE，總共超過 3000 萬（30 million）個特徵。
- 權重用 CC-BY-4.0 授權放在 HuggingFace；Neuronpedia 上有互動 demo。
- 動機：SAE 訓練成本很高，之前大多是在不公開的模型上做，學界很難跟進。
- 跟 steering vector、probing 比起來，SAE 貴很多也難訓練。
- 作者也說 SAE 還是不成熟的技術，有很多開放問題。
- JumpReLU：每個特徵有一個可學習的門檻，低於門檻就輸出 0，高於門檻就照原值輸出。
- 部落格比喻：SAE 像一台「顯微鏡」，讓研究者看進語言模型內部。
