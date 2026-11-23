# Sparse Autoencoder（SAE，稀疏自編碼器）

> 一句話：一個外掛的小網路，把模型的 activation「展開」成很多特徵，而且每次只讓少數特徵亮起來。

## 為什麼需要它
- 神經元因為 [[superposition]] 是多義的，所以要另外學一組「比神經元更多」的單位來拆開它們 [src:s2]
- SAE 是一種弱的 dictionary learning 演算法，學出來的特徵比神經元本身更單義 [src:s2]
- 作者試過做沒有疊加的稀疏架構，擋不住多義性；標準 dictionary learning 又會嚴重 overfitting，所以選 SAE [src:s2]

## 怎麼運作
- 特徵是神經元 activation 的線性組合 [src:s2]
- encoder 把 activation 映到很高維的特徵層，decoder 再用線性轉換還原回原本的 activation [src:s3]
- 訓練時加 sparsity penalty，讓每個輸入只有很少數特徵是非零的 [src:s3]
- JumpReLU SAE：每個特徵有可學習的門檻，低於門檻輸出 0，高於門檻照原值輸出 [src:s4]

## 第一次成功
- 實驗對象是一層的 transformer，MLP 有 512 個神經元，SAE 用 80 億筆 activation 訓練 [src:s2]

## 放大到大模型
- 2024 年在 Claude 3 Sonnet 中間層的 residual stream 上訓練了 1M、4M、34M 個特徵的三個 SAE [src:s3]

## 相關頁面
來源：[[s2]]、[[s3]]、[[s4]]
[[sae-features]]、[[superposition]]、[[feature-steering]]、[[sae-limitations]]、[[open-tools]]
