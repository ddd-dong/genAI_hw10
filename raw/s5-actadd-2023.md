# s5 Turner, Thiergart, Leech, Udell, Vazquez, Mini, MacDiarmid, "Activation Addition: Steering Language Models Without Optimization"（v5 改名 Steering Language Models With Activation Engineering）
- URL: https://arxiv.org/abs/2308.10248
- 日期: 2023-08-20（v5 2024-10-10）
- 擷取: 2026-11-23

## 筆記（改寫）
- 提出 activation engineering：在推論時修改模型的 activation，來可預期地改變模型行為。
- ActAdd：拿一對 prompt（例如 "Love" 和 "Hate"）各跑一次 forward pass，把中間層 activation 相減得到 steering vector，生成時加回去。
- 之前的方法是用反向傳播「學」出 steering vector；ActAdd 只用 forward pass「算」出來，不需要最佳化也不需要標註資料，一對例子就夠。
- 在 GPT-2（OpenWebText、ConceptNet）上展示，並在 Llama-13B、GPT-J-6B 上重現；v5 版在 LLaMA-3、OPT 上做到情緒轉正向和去毒性的 SOTA。
- 優點：比 finetuning 或 RLHF 省很多計算和實作工夫，使用者可以用自然語言指定方向，額外成本隨模型變大是穩定或下降的。
- 能控制輸出的高層屬性，同時保留不相關主題的表現。
