# ActAdd（Activation Addition）

> 一句話：拿「Love」和「Hate」各跑一次模型，把中間層的差值記下來，生成時加回去，模型就會講得比較正向。

## 步驟
- 拿一對對比的 prompt，例如 Love 和 Hate，各跑一次 forward pass [src:s5]
- 把某一層的 activation 相減，得到 steering vector [src:s5]
- 生成時把這個向量（乘上係數）加回同一層 [src:s5]

## 特色
- 之前的方法用反向傳播「學」出 steering vector；ActAdd 只用 forward pass「算」，一對例子就夠 [src:s5]
- 不需要最佳化，也不需要標註資料 [src:s5]
- 能控制輸出的高層屬性，同時保留不相關主題的表現 [src:s5]

## 結果
- 在 GPT-2 上展示，並在 Llama-13B、GPT-J-6B 上重現 [src:s5]
- 新版在 LLaMA-3、OPT 上做到情緒轉正向和去毒性的 SOTA [src:s5]
- 後續的 [[caa]] 改成平均很多對例子，而不是只用一對 [src:s6]

## 相關頁面
來源：[[s5]]、[[s6]]
[[activation-steering]]
