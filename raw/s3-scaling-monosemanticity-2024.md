# s3 Templeton, Conerly et al., "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"
- URL: https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
- 日期: 2024-05-21；Anthropic（arXiv 版 2605.29358 於 2026-05 上傳）
- 擷取: 2026-11-23

## 筆記（改寫）
- 證明 SAE 可以放大到正式上線等級的模型：Claude 3 Sonnet（3.0 版）。
- 在模型中間層的 residual stream 上訓練三個 SAE：1M、4M、34M（3400 萬）個特徵，用 scaling laws 決定超參數。
- SAE 結構：encoder 把 activation 映到高維的特徵層，decoder 用線性轉換把特徵還原回 activation；sparsity penalty 讓每個輸入只有很少數特徵非零。
- 特徵很抽象：名人、國家城市、程式碼裡的型別、諷刺、程式錯誤。而且是多語言、多模態的。
- Golden Gate Bridge 特徵：中文、日文、韓文、俄文的金門大橋維基百科第一句都會讓它強烈觸發。
- 把 Golden Gate 特徵強制放大到訓練資料中最大值的 10 倍，模型會說自己就是金門大橋（這個來自整理頁 ckodser 的摘要）。
- 找到跟安全相關的特徵：欺騙、權力追求、諂媚（sycophancy）、偏見、危險內容；操控這些特徵會因果性地改變模型輸出。
- 限制：特徵集合不完整，也還沒有嚴謹的方法評估特徵是否忠實反映模型的計算。

## 核對（2026-11-23，清稿 loop 回頭補）
- 原文確認：Golden Gate 特徵被 clamp 到最大 activation 的 10 倍（10×），模型開始說自己是金門大橋。不再只靠第三方摘要。
