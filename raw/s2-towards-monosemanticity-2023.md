# s2 Bricken, Templeton, Batson, Chen, Jermyn et al., "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
- URL: https://transformer-circuits.pub/2023/monosemantic-features/
- 日期: 2023-10-04；Anthropic
- 擷取: 2026-11-23

## 筆記（改寫）
- 用 sparse autoencoder（一種弱的 dictionary learning 演算法）從訓練好的模型裡學出特徵，這些特徵比神經元本身更「單義」（monosemantic）。
- 實驗對象：一層的 transformer，MLP 層有 512 個神經元。SAE 在 80 億筆（8 billion）MLP activation 上訓練。
- 把 512 個神經元拆成超過 4000 個特徵，各自代表 DNA 序列、法律用語、HTTP 請求、希伯來文、營養標示等。
- 特徵被定義為神經元 activation 的線性組合（pattern）。
- 作者原本試過「做沒有疊加的稀疏架構」，發現擋不住多義性；標準 dictionary learning 又有嚴重 overfitting，所以選了 SAE 這個折衷。
