# Captain Underpants 测验作者简报 (Authoring Brief)

为 **Captain Underpants**（Dav Pilkey 的搞笑漫画冒险系列，初章书/漫画）制作中英双语阅读理解测验。
站点模式沿用 `geronimostilton` / `andrewlost`，每本书一个 `_quizdata/<NN>.json`（10 道中英双语选择题 + 解析），由 `build.py` 生成每本书的 `<slug>-quiz.html` + 枢纽页 `index.html`。

## 系列书目（IMA KB 7485774517786213，全部已解析，共 12 本）

| # | 英文标题 | media_id (KB 后缀 7485774517786213) |
|---|----------|--------------------------------------|
| 1 | The Adventures Of Captain Underpants | pdf_1cf4518dc1013027392f52c26c388a53_e50e8355a292bdde125a8f4fbd0120fd7485774517786213 |
| 2 | Captain Underpants and the Attack of the Talking Toilets | pdf_1cf4518dc1013027392f52c26c388a53_b0a30883c907325ab108e68788f9027e7485774517786213 |
| 3 | Captain Underpants and the Invasion of the Incredibly Naughty Cafeteria Ladies from Outer Space | pdf_1cf4518dc1013027392f52c26c388a53_ff84c2d964064f574f928593fedee59e7485774517786213 |
| 4 | Captain Underpants and the Perilous Plot of Professor Poopypants | pdf_1cf4518dc1013027392f52c26c388a53_91b966a0c1bd453ae56622ba166894547485774517786213 |
| 5 | Captain Underpants and the Wrath of the Wicked Wedgie Women | pdf_1cf4518dc1013027392f52c26c388a53_ba0585acbf25d78a962dbad3f3ec57f77485774517786213 |
| 6 | Captain Underpants And The Big Bad Battle Of The Bionic Booger Boy Part 1 - The Night Of The Nasty Nostril Nuggets | pdf_1cf4518dc1013027392f52c26c388a53_6ec541ad7252c6b1b79926fcb37b5b6f7485774517786213 |
| 7 | Captain Underpants And The Big, Bad Battle Of The Bionic Booger Boy Part 2 - The Revenge Of The Ridiculous Robo Boogers | pdf_1cf4518dc1013027392f52c26c388a53_11a4967697ab8b71d5fda128a4f917a87485774517786213 |
| 8 | Captain Underpants and the Preposterous Plight of the Purple Potty People | pdf_1cf4518dc1013027392f52c26c388a53_036eae448fe898554d3f5ad094b903a17485774517786213 |
| 9 | Captain Underpants and the Terrifying Return of Tippy Tinkletrousers | pdf_1cf4518dc1013027392f52c26c388a53_90c03c35e8c182e38df6434d43bbed937485774517786213 |
| 10 | Captain Underpants and the Revolting Revenge of the Radioactive Robo-Boxers | pdf_1cf4518dc1013027392f52c26c388a53_cab6c845958a133aacb3c19ffb739e027485774517786213 |
| 11 | Captain Underpants and the Tyrannical Retaliation of the Turbo Toilet 2000 | pdf_1cf4518dc1013027392f52c26c388a53_29cda638e437e91be2ca782ba1ba1cf47485774517786213 |
| 12 | Captain Underpants and the Sensational Saga of Sir Stinks-A-Lot | pdf_1cf4518dc1013027392f52c26c388a53_f8544684a7bbecf4ce31daa648f6ffe37485774517786213 |

## 取文本方式
- 用 IMA 工具 `mcp__ima-mcp__fetch_media_content`（经 DeferExecuteTool 调用），传 `media_id`（上表完整 id，末尾含 KB 后缀）。
- 返回的 `content` 是正文文本，可能含 `![](...)` 图片占位与 OCR 噪声——忽略图片，依上下文推断文字。
- **IMA 偶发不稳定**：`code:220030`（"该文件获取失败"）或 `content` 为空是**瞬时**的，同一 media_id 重试 6–10 次通常能成功。务必重试。

## JSON 结构 — 每本写为 `_quizdata/<NN>.json`（NN 两位，如 `01.json`）
```json
{
  "number": 1,
  "title": "The Adventures Of Captain Underpants",
  "titleZh": "内裤队长历险记",
  "year": 1997,
  "author": "Dav Pilkey",
  "emoji": "🦸",
  "desc": "George & Harold hypnotize Principal Krupp into Captain Underpants!",
  "source": "ima-pdf",
  "questions": [
    {
      "q": {"en": "...", "zh": "..."},
      "options": [
        {"en": "...", "zh": "..."},
        {"en": "...", "zh": "..."},
        {"en": "...", "zh": "..."},
        {"en": "...", "zh": "..."}
      ],
      "answer": 0,
      "explain": {"en": "...", "zh": "..."}
    }
  ]
}
```

## 规则
- **正好 10 道题**，每题**正好 4 个选项**。`answer` = 0 起下标（0/1/2/3）。
- 每道题的 `q`、`options` 每个元素、`explain` 都必须**同时有 `en` 和 `zh`**（完整双语）。
- `title` 用上表英文标题原样；`titleZh` 自然语言中文；`year` 取版权页年份（#1=1997, #2=1999, #3=1999, #4=2000, #5=2001, #6=2003, #7=2003, #8=2006, #9=2012, #10=2013, #11=2014, #12=2015）；`emoji` 一个贴切表情；`desc` 一句简短英文。
- 每题必须**基于书的实际内容**（角色、情节、笑话、设置）。混合约 6 道"故事/角色"题 + 约 4 道"书中真实知识点/事实"题（如 George & Harold 做漫画、催眠、3-D 催眠戒指、Wonkie 等设定细节）。干扰项要"看似合理但按文本明显错误"。**不得编造书中没有的事实。**
- 英文用初章书阅读水平；中文用孩子友好的自然中文。
- **防伪作弊**：正确选项的位置要打散（不要总在第 0 项）；不要刻意让正确选项永远是"最长"的那条。

## 完成前校验（每文件，managed venv）
```bat
C:/Users/allen/.workbuddy/binaries/python/envs/default/Scripts/python.exe -c "
import json
d=json.load(open('_quizdata/<NN>.json',encoding='utf-8'))
qs=d['questions']
assert len(qs)==10, 'need 10'
for q in qs:
    assert len(q['options'])==4
    assert 0<=q['answer']<4
    assert set(q['q'])>= {'en','zh'}
    assert all(set(o)>= {'en','zh'} for o in q['options'])
    assert set(q['explain'])>= {'en','zh'}
print('VALID', d['title'])
"
```
修掉任何失败。报告完成的书号+标题，并确认全部文件 VALID。

## 范围
只写 `_quizdata/<NN>.json`，不要运行 build.py、不要 git、不要改其它文件。
若某本书在 ~12 次重试后确实取不到（一直为空），跳过并注明是哪一本——**绝不编造内容**。
