#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for the Magic Tree House quiz site (early-chapter, by Mary Pope Osborne).

1. gen_quizzes() -> reads _quizdata/<NN>.json and emits one self-contained
                    bilingual (EN/ZH) quiz HTML per book into books/.
2. gen_hub()     -> rebuilds index.html listing ALL books.

Theme: forest green + oak brown + gold medallion (🌳). Source books are local
PDFs in the user's Downloads (not committed).

Run:  python3 build.py
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")
BOOKS = os.path.join(BASE, "books")
AUTHOR = "Mary Pope Osborne"

# Per-number accent colors (green / oak / gold friendly palette).
PALETTE = ["#15803d", "#0d9488", "#7c3aed", "#16a085", "#b45309", "#2563eb",
           "#65a30d", "#db2777", "#0891b2", "#d97706", "#0e7490", "#9333ea",
           "#ca8a04", "#059669"]


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "book"


def accent_for(num):
    try:
        idx = int(num) - 1
    except Exception:
        idx = 0
    return PALETTE[idx % len(PALETTE)]


# ---------------------------------------------------------------------------
# Book quiz HTML
# ---------------------------------------------------------------------------
BOOK_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ — Quiz</title>
<style>
  :root{
    --mth:#15803d; --mth-dark:#14532d; --gold:#d97706; --brown:#92400e;
    --cream:#f7fbf6; --ink:#1f2937;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    font-family:"Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--mth),var(--mth-dark));
    color:var(--ink); min-height:100vh; padding:24px 12px;
  }
  .wrap{max-width:780px;margin:0 auto;background:var(--cream);border-radius:18px;
    box-shadow:0 12px 40px rgba(0,0,0,.35);overflow:hidden;}
  header{background:linear-gradient(135deg,var(--mth),var(--mth-dark));color:#fff;
    padding:22px 28px 18px;text-align:center;position:relative;}
  .topbar{display:flex;align-items:center;justify-content:space-between;gap:10px;}
  header h1{margin:0;font-size:1.5rem;letter-spacing:.5px;flex:1;text-align:center;}
  .langBtn{font-family:inherit;font-size:.85rem;font-weight:bold;color:var(--mth-dark);
    background:#fff;border:none;padding:8px 14px;border-radius:20px;cursor:pointer;
    white-space:nowrap;box-shadow:0 2px 8px rgba(0,0,0,.2);transition:transform .12s;}
  .langBtn:hover{transform:translateY(-1px);}
  .homeBtn{font-size:1.35rem;text-decoration:none;background:#fff;border-radius:50%;
    width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;
    box-shadow:0 2px 8px rgba(0,0,0,.2);transition:transform .12s;}
  .homeBtn:hover{transform:translateY(-1px);}
  .backBtn{font-size:1.35rem;text-decoration:none;background:#fff;border-radius:50%;
    width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;
    box-shadow:0 2px 8px rgba(0,0,0,.2);transition:transform .12s;}
  .backBtn:hover{transform:translateY(-1px);}
  header p{margin:10px 0 0;font-size:.92rem;opacity:.92;}
  .logo{width:54px;height:54px;border-radius:50%;
    background:radial-gradient(circle at 35% 30%, #fff, #dcfce7);
    margin:0 auto 10px;display:flex;align-items:center;justify-content:center;
    font-size:1.7rem;box-shadow:0 0 0 3px rgba(255,255,255,.55) inset;}
  main{padding:22px 28px 30px;}
  .q{border:1px solid #d6e6df;border-radius:12px;padding:16px 18px;margin:16px 0;
    background:#fff;transition:border-color .2s;}
  .q.correct{border-color:var(--mth);background:#eef9f0;}
  .q.wrong{border-color:#dc2626;background:#fdf3f2;}
  .q h3{margin:0 0 12px;font-size:1.02rem;line-height:1.45;}
  .q h3 span{color:var(--mth);font-weight:bold;margin-right:6px;}
  label{display:block;padding:9px 12px;margin:7px 0;border-radius:8px;background:#eef4f0;
    cursor:pointer;border:1px solid transparent;transition:background .15s,border-color .15s;
    font-size:.96rem;line-height:1.4;}
  label:hover{background:#e2ede7;}
  input[type=radio]{margin-right:9px;transform:translateY(1px);}
  label.picked{background:#fff4cc;border-color:var(--gold);}
  label.right{background:#d7f0df;border-color:var(--mth);font-weight:600;}
  label.picked-wrong{background:#f7d4d0;border-color:#dc2626;}
  .explain{display:none;margin-top:10px;padding:12px 14px;background:#f0f7f2;
    border-left:4px solid var(--mth);border-radius:6px;font-size:.9rem;line-height:1.5;}
  .explain.show{display:block;}
  .explain .en{margin-bottom:6px;}
  .explain .zh{color:#444;}
  .explain b{color:var(--mth-dark);}
  .actions{text-align:center;margin-top:24px;}
  button.go{font-family:inherit;font-size:1.05rem;font-weight:bold;color:#fff;background:var(--mth);
    border:none;padding:13px 34px;border-radius:30px;cursor:pointer;
    box-shadow:0 4px 14px rgba(21,128,61,.4);transition:transform .12s,box-shadow .12s;}
  button.go:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(21,128,61,.5);}
  button.go:active{transform:translateY(0);}
  #resetBtn{display:none;background:#555;box-shadow:0 4px 14px rgba(0,0,0,.3);}
  #result{text-align:center;margin:22px auto 4px;font-size:1.3rem;font-weight:bold;
    color:var(--mth-dark);min-height:1.4em;}
  #scoreDetail{text-align:center;color:#666;font-size:.92rem;margin-bottom:6px;}
  footer{text-align:center;font-size:.8rem;color:#9aa6ad;padding:14px;border-top:1px solid #eee;}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topbar">
      <a class="backBtn" href="__BACK__" title="Back / 返回系列" aria-label="Back">📚</a>
      <h1>#__NUMBER__ · __TITLE__</h1>
      <a class="homeBtn" href="__HOME__" title="Home / 首页" aria-label="Home">🏠</a>
    </div>
    <p id="subtitle">Comprehension Quiz • 10 Questions • by __AUTHOR__</p>
    <div class="logo">🌳</div>
  </header>
  <main>
    <div id="questions"></div>
    <div id="result"></div>
    <div id="scoreDetail"></div>
    <div class="actions">
      <button class="go" id="checkBtn">Check My Answers</button>
      <button class="go" id="resetBtn">Try Again</button>
    </div>
  </main>
  <footer>Based on <em>Magic Tree House #__NUMBER__: __TITLE__</em> (Random House, __YEAR__) — by __AUTHOR__</footer>
</div>

<script>
let lang = "en";
const picked = {};
let submitted = false;
let score = 0;

const L = {
  en: {
    subtitle: "Comprehension Quiz • 10 Questions • by __AUTHOR__",
    check: "Check My Answers", retry: "Try Again", langBtn: "🌐 中文",
    result: (s) => `You scored ${s} / 10`,
    perfect: "Perfect! You really know your Magic Tree House adventure.",
    great: "Great job — you understood the story well.",
    ok: "Not bad — but a few clues slipped past you.",
    low: "Time for a re-read! The answers are in the details.",
    ansLabel: "Answer"
  },
  zh: {
    subtitle: "阅读理解测验 • 共10题 • 作者：__AUTHOR__",
    check: "提交答案", retry: "再做一次", langBtn: "🌐 English",
    result: (s) => `你的得分：${s} / 10`,
    perfect: "满分！你完全读懂了这次神奇树屋冒险。",
    great: "很棒——你已经读懂了这个故事。",
    ok: "不错——不过有几条线索被你漏掉了。",
    low: "该重读一遍啦！答案都藏在细节里。",
    ansLabel: "正确答案"
  }
};

const quiz = __QUIZ__;

const qEl = document.getElementById("questions");
const resultEl = document.getElementById("result");
const detailEl = document.getElementById("scoreDetail");
const checkBtn = document.getElementById("checkBtn");
const resetBtn = document.getElementById("resetBtn");
const langBtn = document.getElementById("langBtn");

function render(){
  qEl.innerHTML = "";
  document.getElementById("subtitle").textContent = L[lang].subtitle;
  langBtn.textContent = L[lang].langBtn;
  quiz.forEach((item, i) => {
    const qDiv = document.createElement("div");
    qDiv.className = "q"; qDiv.id = "q" + i;
    let html = `<h3><span>Q${i+1}.</span>${item.q[lang]}</h3>`;
    item.options.forEach((opt, j) => {
      const isPicked = picked[i] === j;
      const checked = isPicked ? "checked" : "";
      html += `<label data-q="${i}" data-o="${j}" class="${isPicked?'picked':''}">
        <input type="radio" name="q${i}" value="${j}" ${checked}> ${opt[lang]}
      </label>`;
    });
    html += `<div class="explain" id="ex${i}">
      <div class="en"><b>${L[lang].ansLabel}:</b> ${item.options[item.answer][lang]}<br>${item.explain.en}</div>
      <div class="zh">${item.options[item.answer][lang]}<br>${item.explain.zh}</div>
    </div>`;
    qDiv.innerHTML = html;
    qEl.appendChild(qDiv);
    if (submitted){
      qDiv.classList.add(picked[i] === item.answer ? "correct" : "wrong");
      document.getElementById("ex"+i).classList.add("show");
      const labels = qDiv.querySelectorAll("label");
      labels[item.answer].classList.add("right");
      if (picked[i] !== item.answer && picked[i] !== undefined)
        labels[picked[i]].classList.add("picked-wrong");
    }
  });
  qEl.querySelectorAll('input[type=radio]').forEach(r => {
    r.addEventListener("change", e => {
      if (submitted) return;
      picked[+e.target.name.slice(1)] = +e.target.value;
      const qDiv = e.target.closest(".q");
      qDiv.querySelectorAll("label").forEach(l => {
        const inp = l.querySelector("input");
        l.classList.toggle("picked", inp.checked);
      });
    });
  });
}

function check(){
  if (submitted) return;
  submitted = true; score = 0;
  quiz.forEach((item, i) => {
    if (picked[i] === item.answer) score++;
  });
  render();
  resultEl.textContent = L[lang].result(score);
  let msg = score === 10 ? L[lang].perfect : score >= 7 ? L[lang].great :
            score >= 4 ? L[lang].ok : L[lang].low;
  detailEl.textContent = msg;
  checkBtn.style.display = "none";
  resetBtn.style.display = "inline-block";
  window.scrollTo({top:0, behavior:"smooth"});
}

function reset(){
  submitted = false; score = 0;
  for (const k in picked) delete picked[k];
  render();
  resultEl.textContent = ""; detailEl.textContent = "";
  checkBtn.style.display = "inline-block";
  resetBtn.style.display = "none";
}

checkBtn.addEventListener("click", check);
resetBtn.addEventListener("click", reset);
langBtn.addEventListener("click", () => { lang = lang === "en" ? "zh" : "en"; render(); });
render();
</script>
</body>
</html>
"""


def gen_quizzes():
    books = []
    files = sorted(os.listdir(DATA))
    for fn in files:
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        path = os.path.join(DATA, fn)
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as e:
            print("SKIP (bad json)", path, e)
            continue
        if not isinstance(data, dict) or "questions" not in data:
            continue
        num = str(data.get("number", "")).zfill(2)
        title = data.get("title", "")
        slug = slugify(title)
        data["slug"] = slug
        data["file"] = f"{slug}-quiz.html"
        quiz_json = json.dumps(data["questions"], ensure_ascii=False)
        html = (BOOK_TPL
                .replace("__TITLE__", title)
                .replace("__NUMBER__", str(data.get("number", "")))
                .replace("__YEAR__", str(data.get("year", "")))
                .replace("__AUTHOR__", AUTHOR)
                .replace("__QUIZ__", quiz_json)
                .replace("__BACK__", "../index.html")
                .replace("__HOME__", "../../index.html"))
        out = os.path.join(BOOKS, data["file"])
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"  wrote books/{data['file']}")
        books.append(data)
    books.sort(key=lambda b: int(b.get("number", 0) or 0))
    return books


# ---------------------------------------------------------------------------
# Hub (index.html)
# ---------------------------------------------------------------------------
HUB_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Magic Tree House — Quizzes</title>
<style>
  :root{--mth:#15803d;--mth-dark:#14532d;--gold:#d97706;--cream:#f7fbf6;--ink:#1f2937;}
  *{box-sizing:border-box;}
  body{margin:0;font-family:"Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--mth),var(--mth-dark));color:var(--ink);min-height:100vh;padding:24px 12px;}
  .wrap{max-width:1000px;margin:0 auto;background:var(--cream);border-radius:18px;
    box-shadow:0 12px 40px rgba(0,0,0,.35);overflow:hidden;}
  header{background:linear-gradient(135deg,var(--mth),var(--mth-dark));color:#fff;padding:24px 28px 20px;text-align:center;position:relative;}
  .topbar{display:flex;align-items:center;justify-content:space-between;}
  header h1{margin:0;font-size:1.6rem;flex:1;text-align:center;}
  .homeBtn{font-size:1.35rem;text-decoration:none;background:#fff;border-radius:50%;width:40px;height:40px;
    display:inline-flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.2);}
  .logo{width:60px;height:60px;border-radius:50%;background:radial-gradient(circle at 35% 30%, #fff, #dcfce7);
    margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:2rem;
    box-shadow:0 0 0 3px rgba(255,255,255,.55) inset;}
  header p{margin:10px 0 0;font-size:.95rem;opacity:.92;}
  .wrap .intro{padding:18px 28px 4px;font-size:.95rem;line-height:1.6;color:#374151;}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;padding:20px 28px 30px;}
  .card{display:block;text-decoration:none;color:var(--ink);background:#fff;border:1px solid #d6e6df;
    border-radius:14px;padding:16px;transition:transform .12s,box-shadow .12s;border-top:5px solid var(--accent);}
  .card:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(21,128,61,.25);}
  .card .num{font-size:.8rem;color:#6b7280;font-weight:bold;}
  .card .emoji{font-size:1.8rem;float:right;}
  .card h3{margin:6px 0 4px;font-size:1.05rem;line-height:1.3;}
  .card .zh{color:#6b7280;font-size:.85rem;margin-bottom:6px;}
  .card .meta{font-size:.75rem;color:#9ca3af;}
  footer{text-align:center;font-size:.8rem;color:#9aa6ad;padding:14px;border-top:1px solid #eee;}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topbar">
      <span style="width:40px"></span>
      <h1>🌳 Magic Tree House</h1>
      <a class="homeBtn" href="../../index.html" title="Home / 首页" aria-label="Home">🏠</a>
    </div>
    <p>初章书 · 魔法冒险 · Early Chapter / Adventure — by Mary Pope Osborne</p>
    <div class="logo">🌳</div>
  </header>
  <div class="intro">
    🌳 <b>__COUNT__ 本 Magic Tree House 神奇树屋（#__LO__–#__HI__）__MISS__，每本都有中英双语阅读理解测验。</b><br>
    __COUNT__ Magic Tree House adventures by Mary Pope Osborne — Jack and Annie discover a magic tree house
    that whisks them through time and around the world. Each book has a bilingual (English / 中文) comprehension quiz.
    Tap a book, read the questions, then check your answers!
  </div>
  <div class="grid">
__CARDS__
  </div>
  <footer>Part of 英语分级阅读乐园 · Reading by Level</footer>
</div>
</body>
</html>
"""


def gen_hub(books):
    cards = []
    for b in books:
        num = str(b.get("number", "")).zfill(2)
        accent = accent_for(b.get("number", "1"))
        emoji = b.get("emoji", "🌳")
        title = b.get("title", "")
        zh = b.get("titleZh", "")
        year = b.get("year", "")
        cards.append(
            f'    <a class="card" style="--accent:{accent}" href="books/{b["file"]}">\n'
            f'      <span class="emoji">{emoji}</span>\n'
            f'      <div class="num">#{num}</div>\n'
            f'      <h3>{title}</h3>\n'
            f'      <div class="zh">{zh}</div>\n'
            f'      <div class="meta">Mary Pope Osborne · {year}</div>\n'
            f'    </a>'
        )
    nums = [int(b.get("number", 0) or 0) for b in books]
    lo = min(nums) if nums else 1
    hi = max(nums) if nums else 1
    hub = (HUB_TPL
           .replace("__CARDS__", "\n".join(cards))
           .replace("__COUNT__", str(len(books)))
           .replace("__LO__", str(lo))
           .replace("__HI__", str(hi))
           .replace("__MISS__", ""))
    out = os.path.join(BASE, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(hub)
    print(f"\n=== gen_hub: wrote index.html with {len(books)} books ===")


if __name__ == "__main__":
    os.makedirs(BOOKS, exist_ok=True)
    man = gen_quizzes()
    gen_hub(man)
    with open(os.path.join(BASE, "_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(man, fh, ensure_ascii=False, indent=2)
    print("Done.")
