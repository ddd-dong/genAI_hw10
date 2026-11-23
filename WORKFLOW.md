# Loop / Graph 設計

![workflow](workflow.png)

## 節點

| # | 節點 | 做什麼 | 工具 | 檢查 | 失敗時回到 |
|---|---|---|---|---|---|
| A | 討論 | 定主題、對象、資料清單、概念頁清單 | 人 + LLM | 人看過才往下 | A |
| B | 取得資料 | 搜尋、讀原文，寫 raw/sX 筆記 | web search / fetch | 有 URL、日期，最多一句短引文 | B |
| C | Ingest | 寫 source 頁、更新概念頁、index、log | LLM + addfact.py | | |
| D | Lint | 壞連結、缺 [src]、數字不在 raw、孤兒頁、index 漏頁 | lint_wiki.py | error = 0 | C |
| E | Fact-check | 每條條列和「一句話」對回 raw，抓多加的詮釋 | LLM 人工對照 | 沒有無來源的說法 | C |
| F | 大綱 | 每張投影片 = 一個問題 + 用到的 wiki 頁 | LLM | | |
| G | 大綱檢查 | 每張都對得到存在的 wiki 頁、每個概念頁都有用到 | check_outline.py | error = 0 | F（刪掉那張）或 B（補資料） |
| H | 查 wiki | 依大綱把每張用到的條列抽成 context.md | query_wiki.py | | |
| I | 生成簡報 | 只用 context.md 寫 HTML，每張標 data-wiki | LLM | | |
| J | 簡報檢查 | 引用頁存在、數字都在引用頁裡、術語第一次出現有 &lt;dfn&gt; | check_slides.py | error = 0 | I（只重生那張） |
| L | 清稿檢查 | 抓流程用語外流（wiki、待確認、示意）和制式 AI 句型 | clean_check.py | flags = 0 | M |
| M | 清稿改寫 | 被標的句子：不影響教學就刪，否則改直白；再人讀一遍抓 regex 漏的 | LLM + 人 | 改完回 J、L | J |
| K | 視覺檢查 | 每張截圖、偵測超出版面 | shoot.py | 沒有 overflow | I |

## 流程

```
A 討論
 |
 +-- 每篇資料一圈（loop x8）
 |     B 取得資料
 |     C ingest
 |     D lint ---- fail ---> C
 |
 E fact-check ---- fail ---> C
 |
 F 大綱
 G 大綱檢查 ---- fail ---> F（刪掉）或 B（補資料）
 H 查 wiki
 I 生成簡報
 J 簡報檢查 ---- fail ---> I
 L 清稿檢查 ---- flag ---> M 清稿改寫 ---> 回 J、L（最多 3 輪）
 K 視覺檢查 ---- fail ---> I
```

## 重複的部分
- B、C、D 每篇資料跑一次，8 篇就是 8 圈。一次只 ingest 一篇，lint 過了才進下一篇，錯誤才不會累積。
- D、J 失敗就回到上一個生成節點，只改出錯的頁或那張投影片。
- L、M 是一個小 loop：改寫可能把數字改掉，所以每輪改完都回 J 再檢查一次。
- 「待確認」的東西在 H（查 wiki）就被擋掉，不會進到簡報；要嘛回 B 對原文解決，要嘛不講。

## 為什麼這樣設計
- 能用程式檢查的（連結、數字、格式）就用程式，便宜又穩定，每圈都跑。
- 程式抓不到的（多加的詮釋、引錯來源）放一個 LLM fact-check，在 wiki 完成後、做簡報前做一次。
- 「有沒有 wiki 支撐」在大綱階段就檢查，不要等 HTML 生成完才發現某張是硬寫的。
- 生成簡報時以 context.md 為準，再用 J 檢查數字有沒有跑出引用頁以外，擋住 LLM 自己補的內容。
- 投影片是給學生看的，不是給助教看流程的。流程證據（來源、待確認）只放 footer 和 wiki，本體只放教學內容。
