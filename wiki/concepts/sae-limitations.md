# SAE 的限制

> 一句話：SAE 能找到很多看得懂的特徵，但不保證找齊，也還不確定它真的反映模型怎麼算。

- 特徵集合不完整，有些概念可能根本沒被拆出來 [src:s3]
- 還沒有嚴謹的方法評估特徵是否忠實反映模型的計算 [src:s3]

## 成本
- SAE 訓練成本很高，比 steering vector 或 probing 貴很多也難訓練 [src:s4]
- Gemma Scope 作者也說 SAE 仍是不成熟的技術，有很多開放問題 [src:s4]

## 拿來 steering 的表現
- AxBench 的比較中，SAE 在 steering 和概念偵測都輸給簡單 baseline，見 [[steering-evaluation]] [src:s7]
- 2026 年有論文反駁：特徵挑得好的話 SAE 可以接近 LoRA [src:s8]

## 相關頁面
來源：[[s3]]、[[s4]]、[[s7]]、[[s8]]
[[sparse-autoencoder]]
