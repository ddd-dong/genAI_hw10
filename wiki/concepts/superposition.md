# Superposition（疊加）

> 一句話：模型用比較少的維度，塞進比較多的特徵，因為大部分特徵很少同時出現。

## Toy model 實驗
- 把 5 個重要性不同的特徵壓進 2 維空間來觀察 [src:s1]
- 特徵很密集時，模型只保留最重要的 2 個，像 PCA 一樣 [src:s1]
- 特徵變稀疏時，模型開始把更多特徵疊進去，代價是特徵互相干擾，要靠非線性（ReLU）過濾 [src:s1]
- 從「不疊」到「疊」之間有相變（phase change） [src:s1]

## 意義
- 假說：實際的網路是在有雜訊地模擬一個更大、更稀疏的網路 [src:s1]
- 這解釋了為什麼神經元是多義的，見 [[neuron-vs-feature]] [src:s1]
- 想看懂模型，就要把疊在一起的特徵拆開，論文提出 dictionary learning 是一條路 [src:s1]
- 後續 Towards Monosemanticity 就是用 SAE 把疊加的特徵拆開，見 [[sparse-autoencoder]] [src:s2]

## 相關頁面
來源：[[s1]]、[[s2]]
[[neuron-vs-feature]]、[[linear-representation]]
