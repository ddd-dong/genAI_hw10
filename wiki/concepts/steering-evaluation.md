# Steering 到底好不好用？（評估與爭議）

> 一句話：在公平比較下，直接寫 prompt 往往比改 activation 更有效；但用 SAE 好不好，跟怎麼挑特徵很有關。

## AxBench（2025）
- 之前沒有 benchmark 能直接比較各種 steering 方法，AxBench 補上這個缺 [src:s7]
- 在 Gemma-2-2B 和 9B 上，steering 任務 prompting 贏過所有方法，第二名是 finetuning [src:s7]
- 概念偵測任務（判斷某個概念有沒有出現）DiffMean 最好 [src:s7]
- SAE 在兩項任務都沒有競爭力 [src:s7]
- 作者提出 ReFT-r1，兩項都有競爭力，又保有 prompting 沒有的可解釋性 [src:s7]

## 這代表什麼
- 作者自己說這是 steering 技術目前限制的清醒證據 [src:s7]
- SAE steering 好不好，很大部分取決於怎麼挑特徵，爭議還沒結束 [src:s8]

## 反駁（2026）
- Jørgensen & Hansen 認為 AxBench 沒有公平對待 SAE [src:s8]
- 用監督式方法挑選並標註特徵後，SAE 在 AxBench 上可以接近 LoRA 參考線的表現 [src:s8]

## 相關頁面
來源：[[s7]]、[[s8]]
[[feature-steering]]、[[activation-steering]]、[[sae-limitations]]
