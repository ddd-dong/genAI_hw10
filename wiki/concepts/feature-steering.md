# 用 SAE 特徵 steering（Feature Steering）

> 一句話：找到某個概念的特徵後，把它手動調大或調小，模型的行為就跟著變。

## Golden Gate Bridge 的例子
- Claude 3 Sonnet 裡有一個 Golden Gate Bridge 特徵，中文、日文、韓文、俄文的金門大橋介紹都會讓它強烈觸發 [src:s3]
- 把這個特徵強制放大到訓練資料最大值的 10 倍，模型會說自己就是金門大橋 [src:s3]

## 安全相關的特徵
- 也找到欺騙、權力追求、諂媚、偏見等特徵，操控它們會因果性地改變模型輸出 [src:s3]

## 跟一般 steering 的關係
- 這其實是 [[activation-steering]] 的一種：差別只在方向是從 SAE 特徵來，不是從對比 prompt 算的 [src:s3][src:s5]
- 但在 AxBench 的公平比較裡，SAE steering 沒有贏過 prompting，見 [[steering-evaluation]] [src:s7]

## 相關頁面
來源：[[s3]]、[[s5]]、[[s7]]
[[sae-features]]、[[sparse-autoencoder]]
