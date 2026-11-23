# 00 討論紀錄（先討論、後生成）

## Q1 主題
- 第一版選 Prompt Injection，做到一半覺得太簡單，換掉。（那次跑出來的經驗有留下來，見 runs/00_previous_attempt.md）
- 新主題：SAE（Sparse Autoencoder）與 Activation Steering。
- 兩個主題一起講：SAE 是「看懂」模型內部，steering 是「改動」模型內部，最後接到「SAE 拿來 steering 到底好不好用」的爭議。

## Q2 對象
- 修過一點 ML（知道 neural network、embedding 是什麼）但沒碰過 interpretability 的人。
- 每個概念頁要有一句話白話解釋 + 一個比喻或例子。

## Q3 資料（8 篇）
| id | 資料 | 角色 |
|---|---|---|
| s1 | Elhage et al. 2022, Toy Models of Superposition | 為什麼神經元難懂 |
| s2 | Bricken et al. 2023, Towards Monosemanticity | SAE 第一次在 transformer 上成功 |
| s3 | Templeton et al. 2024, Scaling Monosemanticity | 放大到 Claude 3 Sonnet、Golden Gate |
| s4 | Lieberum et al. 2024, Gemma Scope | 開源 SAE、工具 |
| s5 | Turner et al. 2023, ActAdd | steering vector 的起點 |
| s6 | Rimsky et al. 2024, CAA | 用很多對比例子做 steering |
| s7 | Wu et al. 2025, AxBench | SAE steering 輸給簡單 baseline |
| s8 | Jørgensen & Hansen 2026, 反駁 AxBench | 爭議還沒結束 |

## Q4 概念頁清單（先定好再寫）
neuron-vs-feature, superposition, linear-representation, sparse-autoencoder, sae-features, feature-steering, activation-steering, actadd, caa, steering-evaluation, sae-limitations, open-tools

## Q5 規則沿用第一版學到的
- source 頁要被概念頁連到（第一版 lint 抓到孤兒頁）
- 不能先連還沒建的頁（第一版 lint 抓到）
- lint 全過不代表內容對，ingest 完要另外做語意檢查（第一版抓到 3 句多加的詮釋）
- 大綱階段就檢查每張投影片有沒有 wiki 支撐（第一版刪掉一張）
