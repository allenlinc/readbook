# RAZ-Z1 Quiz JSON Generation — Instructions

You are generating bilingual (English / 中文) reading-comprehension quizzes for RAZ Level Z1 books.
Each book becomes ONE JSON file at:  <OUT>/<slug>.json

## 1) Get the book text — RESOLVE media_id YOURSELF (do not trust any pre-written id)
The books live in IMA knowledge base id "7485022235801010" (RAZ-Z1).
 a) Call IMA MCP `mcp__ima-mcp__get_knowledge_list` with knowledge_base_id="7485022235801010", limit=50, cursor="".
    Then call AGAIN with cursor="CDI=". This returns ALL entries (~83 total).
 b) Build a map: normalized title (lowercase, strip trailing ".pdf", collapse spaces) -> media_id.
 c) For each assigned book, find the entry whose title matches the assigned title. Use THAT media_id.
    (The batch JSON also gives a media_id hint — but ALWAYS re-verify by title; never use a hint blindly.)
 d) Call `mcp__ima-mcp__fetch_media_content` with that media_id to get the book text.
 e) SANITY CHECK: the first ~150 chars of the returned text should clearly be the expected book
    (e.g. for "Stonehenge" it should mention Stonehenge). If it looks like a DIFFERENT book,
    re-find by title and refetch. If you get a 220030 / timeout error, retry the fetch up to 3 times.
    If still failing, report that slug as FAILED (do NOT write a guessed file).

## 2) JSON schema — match the example file EXACTLY
Read `<OUT>/stonehenge.json` as the FORMAT EXAMPLE (it is a correct, complete sample).
Your output must have exactly this shape:
{
  "slug": "<exact slug; equals filename without .json>",
  "title": "<exact book title, no '.pdf'>",
  "titleZh": "<natural Chinese translation of the title>",
  "level": "Z1",
  "genre": "Informational",   // one of: Informational | Narrative | Folktale | Biography | Classic Novel | Classic Poetry | Play | Poetry
  "mainSkill": "Key Ideas and Details",
  "questions": [  // EXACTLY 10 objects
    { "q": {"en":"...","zh":"..."}, "options":[{"en":"...","zh":"..."},{"en":"...","zh":"..."},{"en":"...","zh":"..."},{"en":"...","zh":"..."}], "answer": 0, "skill":"<one of 4 RAZ skills>", "explain":{"en":"...","zh":"..."} }
    // ... 9 more
  ],
  "extended": { "prompt": {"en":"...","zh":"..."}, "guidance": {"en":["tip1","tip2"],"zh":["提示1","提示2"]} }
}

The 4 RAZ skills (use these EXACT strings):
- "Key Ideas and Details"
- "Craft and Structure"
- "Integration of Knowledge and Ideas"
- "Author's Purpose and Perspective"
Distribute the 10 questions across these skills (mix them; do not put all 10 on one skill).
`genre` and `mainSkill` must be from the allowed enums.

## 3) Quality rules
- Questions must be answerable from the FETCHED book text (faithful, not invented).
- Both `en` and `zh` must be present and non-empty for: every q, every option, every explain,
  extended.prompt, and BOTH guidance arrays (en + zh, each >=1 item).
- Options en/zh must be parallel; the correct option's en/zh must agree.
- Distractors plausible but clearly wrong per the text.
- English natural for a ~5th-grade reader; Chinese should read naturally (not machine-stiff).
- Write each file with: json.dump(obj, open(path,"w",encoding="utf-8"), ensure_ascii=False, indent=2).
- After writing, re-load each file with json.load to confirm it parses.

## 4) Output & report
- Write files to <OUT>/<slug>.json (one per assigned book). Do NOT edit build.py, assets/, index.html, or run git.
- When done, report (under ~400 words): for each assigned slug -> OK or FAILED, plus the first ~120 chars
  of the fetched text you used (for verification). If any FAILED, say why.
