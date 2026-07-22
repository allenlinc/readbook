#!/usr/bin/env python3
# Build the RAZ-Z2 quiz site from _quizdata/*.json
#   - raz-z2-quiz/index.html        (hub: search + skill filter + grid)
#   - raz-z2-quiz/books/<slug>.html  (one interactive page per book)
import json, os, glob, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_quizdata")
BOOKS_DIR = os.path.join(HERE, "books")

SKILL_LABELS = {
    "Key Ideas and Details": "Key Ideas & Details",
    "Craft and Structure": "Craft & Structure",
    "Integration of Knowledge and Ideas": "Integration of Knowledge",
    "Author's Purpose and Perspective": "Author's Purpose",
    "Other": "Other",
}

def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip()).lower()

def validate(b, slugfile):
    errs = []
    if len(b.get("questions", [])) != 10:
        errs.append("questions != 10 (%d)" % len(b.get("questions", [])))
    for i, q in enumerate(b.get("questions", [])):
        if not isinstance(q.get("options"), list) or len(q["options"]) != 4:
            errs.append("q%d options != 4" % i); continue
        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a <= 3):
            errs.append("q%d answer bad" % i)
        for k in ("q", "explain"):
            f = q.get(k) or {}
            if not f.get("en"): errs.append("q%d %s.en missing" % (i, k))
        for oi, o in enumerate(q["options"]):
            if not (o.get("en")): errs.append("q%d opt%d.en missing" % (i, oi))
    if not b.get("extended", {}).get("prompt", {}).get("en"):
        errs.append("extended.prompt.en missing")
    return errs

def safe_json(obj):
    s = json.dumps(obj, ensure_ascii=False)
    return s.replace("</", "<\\/")

# ---- load + validate quiz data ----
books = []
for fp in sorted(glob.glob(os.path.join(DATA, "*.json"))):
    if os.path.basename(fp).startswith("_"):
        continue  # skip helper json (e.g. _titles.json)
    try:
        b = json.load(open(fp, encoding="utf-8"))
    except Exception as e:
        print("BAD JSON:", os.path.basename(fp), e); continue
    errs = validate(b, fp)
    if errs:
        print("INVALID", b.get("slug", fp), "->", "; ".join(errs)); continue
    books.append(b)

print("Loaded %d valid books from _quizdata/." % len(books))
books.sort(key=lambda b: b["title"])

# ---- skill set for filter ----
skills = set()
for b in books:
    if b.get("mainSkill"): skills.add(b["mainSkill"])
    for q in b["questions"]:
        if q.get("skill"): skills.add(q["skill"])
skill_opts = "".join(
    '<option value="%s">%s</option>' % (s, SKILL_LABELS.get(s, s))
    for s in sorted(skills)
)

# ---- hub cards ----
cards = []
for b in books:
    slug = b["slug"]
    genre = b.get("genre", "")
    ms = b.get("mainSkill", "")
    cards.append(
        '<article class="book">'
        '<div class="tt en">%s</div>' % html.escape(b["title"]) +
        ('<div class="zz zh">%s</div>' % html.escape(b.get("titleZh", "")) if b.get("titleZh") else "") +
        '<div class="meta">' +
        ('<span class="chip">%s</span>' % html.escape(ms) if ms else "") +
        ('<span class="chip gen">%s</span>' % html.escape(genre) if genre else "") +
        "</div>" +
        '<a class="go" href="books/%s.html"><span class="en">Start ▶</span><span class="zh">开始 ▶</span></a>' % slug +
        "</article>"
    )
cards_html = "\n".join(cards)

HUB = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RAZ-Z2 阅读理解 · Reading by Level</title>
<link rel="stylesheet" href="assets/style.css?v=11">
</head>
<body class="lang-en">
<div class="wrap">
  <div class="topbar">
    <button class="langBtn" id="langBtn">🌐 EN</button>
    <a class="homeBtn" href="../../index.html"><span class="en">🏠 Home</span><span class="zh">🏠 首页</span></a>
  </div>
  <div class="hub-hero">
    <h1><span class="en">RAZ Level Z² · Reading Comprehension</span><span class="zh">RAZ Level Z² · 阅读理解练习</span></h1>
    <p><span class="en">__COUNT__ leveled readers — 10 bilingual questions + 1 open-ended question each. Choose a book to start!</span><span class="zh">__COUNT__ 本分级读物，每本 10 道理解题 + 1 道思考题。选一本开始吧！</span></p>
  </div>
  <div class="controls">
    <input id="q" type="search" placeholder="🔍 Search title…" autocomplete="off">
    <select id="sk"><option value="">全部技能 All skills</option>__SKILLS__</select>
  </div>
  <div class="grid" id="grid">
__CARDS__
  </div>
  <footer><span class="en">RAZ-Z2 Quick Check · questions written from the original books</span><span class="zh">RAZ-Z2 阅读理解 · 题目依据原书内容编写</span></footer>
</div>
<script>
var BOOKS = __BOOKS__;
var grid = document.getElementById('grid');
var q = document.getElementById('q'), sk = document.getElementById('sk');
function card(b){
  return '<article class="book"><div class="tt en">'+esc(b.title)+'</div>'+
    (b.titleZh?'<div class="zz zh">'+esc(b.titleZh)+'</div>':'')+
    '<div class="meta">'+
      (b.mainSkill?'<span class="chip">'+esc(b.mainSkill)+'</span>':'')+
      (b.genre?'<span class="chip gen">'+esc(b.genre)+'</span>':'')+
    '</div><a class="go" href="books/'+b.slug+'.html"><span class="en">Start ▶</span><span class="zh">开始 ▶</span></a></article>';
}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function render(){
  var t=q.value.trim().toLowerCase(), s=sk.value, out=[];
  BOOKS.forEach(function(b){
    var hay=(b.title+' '+(b.titleZh||'')+' '+(b.mainSkill||'')).toLowerCase();
    var okT = !t || hay.indexOf(t)>=0;
    var okS = !s || (b.mainSkill===s) || b.questions.some(function(x){return x.skill===s;});
    if(okT&&okS) out.push(b);
  });
  grid.innerHTML = out.length? out.map(card).join('') : '<div class="empty">'+bi('No matches.','没有找到匹配的书籍')+'</div>';
}
function bi(s1,s2){return '<span class="en">'+s1+'</span><span class="zh">'+s2+'</span>';}
function setPH(){q.placeholder=document.body.classList.contains('lang-zh')?'🔍 搜索书名…':'🔍 Search title…';}
q.addEventListener('input', render); sk.addEventListener('change', render);
var lb=document.getElementById('langBtn');
lb.addEventListener('click',function(){var zh=document.body.classList.toggle('lang-zh');document.body.classList.toggle('lang-en',!zh);lb.textContent=zh?'🌐 中文':'🌐 EN';setPH();});
setPH();
render();
</script>
</body>
</html>
"""

HUB = (HUB
       .replace("__COUNT__", str(len(books)))
       .replace("__SKILLS__", skill_opts)
       .replace("__CARDS__", cards_html)
       .replace("__BOOKS__", safe_json([{"slug": b["slug"], "title": b["title"],
                                          "titleZh": b.get("titleZh", ""),
                                          "mainSkill": b.get("mainSkill", ""),
                                          "genre": b.get("genre", ""),
                                          "questions": b["questions"]} for b in books])))

with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
    f.write(HUB)

# ---- book pages ----
BOOK_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ · RAZ-Z2</title>
<link rel="stylesheet" href="../assets/style.css?v=11">
</head>
<body class="lang-en">
<div class="wrap">
  <div class="topbar">
    <button class="langBtn" id="langBtn">🌐 EN</button>
    <a class="homeBtn" href="../../../index.html"><span class="en">🏠 Home</span><span class="zh">🏠 首页</span></a>
  </div>
  <div id="app"></div>
  <footer><a href="../index.html"><span class="en">← Back to RAZ-Z2</span><span class="zh">← 返回 RAZ-Z2 书单</span></a></footer>
</div>
<script>window.BOOK = __BOOK__;</script>
<script src="../assets/quiz.js?v=5"></script>
</body>
</html>
"""

os.makedirs(BOOKS_DIR, exist_ok=True)
for b in books:
    page = (BOOK_TPL
            .replace("__TITLE__", html.escape(b["title"]))
            .replace("__BOOK__", safe_json(b)))
    with open(os.path.join(BOOKS_DIR, b["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(page)

print("\nGenerated: index.html + %d book pages (books/)." % len(books))
