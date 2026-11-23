# Activation Steering（激活值操控）

> 一句話：不改模型權重、也不改 prompt，而是在模型「想到一半」時，把它腦中的某個方向推大或推小。

## 跟其他控制方法比
- 傳統控制模型的方法有 finetuning、RLHF、prompt engineering [src:s5]
- activation engineering 是在推論時直接修改 activation，來可預期地改變行為 [src:s5]
- 它比 finetuning 或 RLHF 省很多計算和實作工夫 [src:s5]

## 前提
- 如果概念是 activation 空間裡的方向（見 [[linear-representation]]），ActAdd 的做法就是把這種方向的向量加回 activation [src:s1][src:s5]

## 方向從哪來
- 用對比的 prompt 算出來：[[actadd]] [src:s5]
- 用很多對比例子平均出來：[[caa]] [src:s6]

## 相關頁面
來源：[[s5]]、[[s6]]
[[feature-steering]]、[[linear-representation]]
