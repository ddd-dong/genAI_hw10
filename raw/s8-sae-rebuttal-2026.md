# s8 Jørgensen & Hansen, "Steering LLMs? Actually, Sparse Autoencoders can outperform simple baselines"
- URL: https://arxiv.org/abs/2605.31183
- 日期: 2026-05-29；DTU Compute
- 擷取: 2026-11-23

## 筆記（改寫）
- 定位是對 AxBench（s7）的部分反駁：認為 AxBench 沒有公平對待 SAE。
- 做法：用他們的監督式方法挑選並標註 SAE 特徵。
- 結果：這樣挑出來的 SAE 特徵在 AxBench 上可以接近 LoRA 參考線的表現。
- 意思是 SAE steering 好不好，很大部分取決於「怎麼挑特徵」。
