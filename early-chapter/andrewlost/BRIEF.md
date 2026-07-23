# Andrew Lost — Quiz Authoring Brief (for subagents)

You will author bilingual (English / 中文) reading-comprehension quizzes for the
**Andrew Lost** early-chapter science-adventure series by **J.C. Greenburg** (18 books).

## Where the book text comes from (IMA knowledge base)
The full text of each book lives in the IMA knowledge base **"Andrew Lost"** (kb_id `7485774949795645`).
Use the IMA MCP tools:
1. Call `mcp__ima-mcp__fetch_media_content` with `media_id = <the book's media_id>`.
   The media_id already includes the kb_id suffix, e.g.
   `pdf_1cf4518dc1013027392f52c26c388a53_<hash>7485774949795645`.
   (If you don't have the schema loaded, call ToolSearch with the IMA tool names first.)
2. The returned `content` is the book's story text (it may contain `![](...)` image
   markers and OCR noise — ignore images, infer intended words from context).
3. AUTHOR THE QUIZ FROM THIS TEXT. Do **not** invent facts, names, or numbers absent
   from the book. If a fact isn't in the text, don't ask about it.

Books & media_ids (number → title → media_id):
- 01 On the Dog → pdf_1cf4518dc1013027392f52c26c388a53_9707931c42989c8f1cecb1caf3289b2a7485774949795645
- 02 In the Bathroom → pdf_1cf4518dc1013027392f52c26c388a53_b6c7835ebf6f371ed28f0ffa4b3e96107485774949795645
- 03 In the Kitchen → pdf_1cf4518dc1013027392f52c26c388a53_2afd247180ae3602d772a368a150b6597485774949795645
- 04 In the Garden → pdf_1cf4518dc1013027392f52c26c388a53_fd3f8f2601f708bdb5344a69abd1faf87485774949795645
- 05 Under Water → pdf_1cf4518dc1013027392f52c26c388a53_56a231bd03efabb719de0f7bf12511d47485774949795645
- 06 In the Whale → pdf_1cf4518dc1013027392f52c26c388a53_5411a85142d7db15ce00a8af594aea737485774949795645
- 07 On the Reef → pdf_1cf4518dc1013027392f52c26c388a53_a3c3f0f7dd5433ab1cc9c4fa480c98777485774949795645
- 08 In the Deep → pdf_1cf4518dc1013027392f52c26c388a53_e11d8fdb9a5428c7def5b6e31c36a26c74857749497995645
- 09 In Time → pdf_1cf4518dc1013027392f52c26c388a53_4cbee29a596fb5fca4e274d26942f77c74857749497995645
- 10 On Earth → pdf_1cf4518dc1013027392f52c26c388a53_1dab7e893a9f36317efc7e15fc2d3bf97485774949795645
- 11 With the Dinosaurs → pdf_1cf4518dc1013027392f52c26c388a53_f46fcb4eed4040a022f21c0c6939872c74857749497995645
- 12 In the Ice Age → pdf_1cf4518dc1013027392f52c26c388a53_23f75cfc7172319bfa27b25b562d345c74857749497995645
- 13 In the Garbage → pdf_1cf4518dc1013027392f52c26c388a53_6972c064d9b4c7d7d25ef980870fedb07485774949795645
- 14 With the Bats → pdf_1cf4518dc1013027392f52c26c388a53_6fe32c9efc0cdc4202eab74d3089fcfb74857749497995645
- 15 In the Jungle → pdf_1cf4518dc1013027392f52c26c388a53_64c449ac0ef37109ba6d3b9f1c371b9a74857749497995645
- 16 In Uncle Al → pdf_1cf4518dc1013027392f52c26c388a53_fa13ca451084444fd76f74e495dbe36174857749497995645
- 17 In the Desert → pdf_1cf4518dc1013027392f52c26c388a53_bbf036048f213004cba59e6f24c392e27485774949795645
- 18 With the Frogs → pdf_1cf4518dc1013027392f52c26c388a53_1ed97302fd89944b2a36f8fe812fa83f74857749497995645

## JSON schema (write to `_quizdata/<NN>.json`, NN = 2-digit book number)
```json
{
  "number": 2,
  "title": "In the Bathroom",
  "titleZh": "在浴室里",
  "year": 2002,
  "author": "J.C. Greenburg",
  "emoji": "🛁",
  "desc": "After Andrew's Atom Sucker shrinks them onto a dog getting a bath, Andrew, Judy & Thudd must survive bubbles, bacteria, spiders, and the toilet drain!",
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
    /* ... exactly 10 questions total ... */
  ]
}
```

## Rules
- **Exactly 10 questions**, each with **exactly 4 options**.
- `answer` is the 0-based index (0/1/2/3) of the correct option.
- Every `q`, every `option`, and `explain` must have BOTH `en` and `zh` (full bilingual).
- `number` = the book's number (int), `title` = English title exactly as listed above,
  `titleZh` = Chinese translation of the title, `year` = publication year (guess from
  copyright page / series order if unsure — usually 2002–2005), `emoji` = one fitting emoji,
  `desc` = one short English sentence summary (with an emoji ok).
- Ground every question + explanation in the actual book text. Spread questions across the
  whole book (characters, plot events, AND the real science facts in "True Stuff" / Thudd's
  facts). Aim for a mix: ~6 story/character questions + ~4 science-fact questions.
- Keep English at early-chapter reading level; Chinese should be natural kid-friendly 中文.
- Distractors (wrong options) must be plausible but clearly wrong per the text.

## Validate before finishing
Run this from `early-chapter/andrewlost/` with the managed venv:
```
C:/Users/allen/.workbuddy/binaries/python/envs/default/Scripts/python.exe -c "
import json
d=json.load(open('_quizdata/<NN>.json',encoding='utf-8'))
qs=d['questions']
assert len(qs)==10, 'need 10 questions'
for q in qs:
    assert len(q['options'])==4, 'need 4 options'
    assert 0<=q['answer']<4, 'answer index out of range'
    assert set(q['q'])>= {'en','zh'}, 'q missing en/zh'
    assert all(set(o)>= {'en','zh'} for o in q['options']), 'option missing en/zh'
    assert set(q['explain'])>= {'en','zh'}, 'explain missing en/zh'
print('VALID', d['title'])
"
```
Fix any failure, then report the book number + title you completed.

## Scope
Only fetch the assigned book(s) and write the assigned `_quizdata/<NN>.json` file(s).
Do NOT run build.py, do NOT run git, do NOT modify other files.
