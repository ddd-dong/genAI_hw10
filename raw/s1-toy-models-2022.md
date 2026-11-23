# s1 Elhage et al., "Toy Models of Superposition"
- URL: https://transformer-circuits.pub/2022/toy_model/index.html ；arXiv 2209.10652
- 日期: 2022-09-14；Anthropic, Harvard
- 擷取: 2026-11-23

## 筆記（改寫）
- 神經網路常把很多不相關的概念塞進同一個神經元，這叫 polysemanticity（多義性），讓可解釋性變得很難。
- 理想情況是每個神經元只對一種東西有反應（例如影像分類器裡只看紅色、只看狗鼻子），但在大型語言模型裡，神經元剛好對應乾淨特徵的情況其實很少見。
- 論文用小型 ReLU 網路加上合成的稀疏特徵資料做 toy model，研究模型什麼時候會表示「比維度還多的特徵」，這個現象叫 superposition（疊加）。
- 例子：把 5 個重要性不同的特徵壓到 2 維。特徵很密集時，模型只保留最重要的 2 個（像 PCA）；特徵變稀疏時，模型開始把更多特徵疊進去，代價是特徵之間互相干擾，要靠非線性過濾。
- 觀察到相變（phase change）、跟均勻多面體幾何的關聯，以及跟 adversarial examples 的可能關聯。
- 假說：實際的網路某種程度上是在「有雜訊地模擬一個更大、更稀疏的網路」。
- 支持 linear representation hypothesis：特徵對應到 activation 空間裡的方向。
- 文中提出三條路找回特徵：做沒有疊加的模型、用 dictionary learning 找過完備的特徵基底、或兩者混合。
