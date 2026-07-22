#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for the Captain Underpants quiz site (Dav Pilkey's comedy series).

1. gen_quizzes()  -> reads _quizdata/<NN>.json and emits one self-contained
                     bilingual (EN/ZH) quiz HTML per book.
2. gen_hub()      -> rebuilds index.html listing ALL books.

Pattern mirrors middle-chapter/geronimostilton/build.py, re-themed for
Captain Underpants (comic-book humor => bold red/blue "superhero" palette).

Run:  python3 build.py
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")

# Per-book accent colors (comic-book friendly, red/blue heavy palette).
ACCENT = {
    "1":  "#e11d48", "2":  "#2563eb", "3":  "#f59e0b", "4":  "#16a34a",
    "5":  "#7c3aed", "6":  "#0891b2", "7":  "#db2777", "8":  "#ea580c",
    "9":  "#4f46e5", "10": "#0d9488", "11": "#dc2626", "12": "#0e7490",
}
# Cyclic palette for books beyond #12 so the grid stays colorful.
PALETTE = ["#e11d48", "#2563eb", "#f59e0b", "#16a34a", "#7c3aed", "#0891b2",
           "#db2777", "#ea580c", "#4f46e5", "#0d9488", "#dc2626", "#0e7490",
           "#ca8a04", "#9333ea", "#0284c7", "#be185d"]

def accent_for(num):
    s = str(num)
    if s in ACCENT:
        return ACCENT[s]
    return PALETTE[int(num) % len(PALETTE)]

AUTHOR = "Dav Pilkey"

QUIZ_CSS = """  :root{
    --cu-red:#e11d48;
    --cu-blue:#2563eb;
    --cu-dark:#7f1d1d;
    --cream:#fffdf7;
    --ink:#1f2937;
    --gold:#f59e0b;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    font-family:"Comic Sans MS","Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--cu-red),#9f1239);
    color:var(--ink);
    min-height:100vh;
    padding:24px 12px;
  }
  .wrap{
    max-width:780px;
    margin:0 auto;
    background:var(--cream);
    border-radius:18px;
    box-shadow:0 12px 40px rgba(0,0,0,.35);
    overflow:hidden;
  }
  header{
    background:linear-gradient(135deg,var(--cu-red),var(--cu-blue));
    color:#fff;
    padding:22px 28px 18px;
    text-align:center;
    position:relative;
  }
  .topbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
  }
  header h1{
    margin:0;
    font-size:1.5rem;
    letter-spacing:.5px;
    flex:1;
    text-align:center;
  }
  .langBtn{
    font-family:inherit;
    font-size:.85rem;
    font-weight:bold;
    color:#b91c1c;
    background:#fff;
    border:none;
    padding:8px 14px;
    border-radius:20px;
    cursor:pointer;
    white-space:nowrap;
    box-shadow:0 2px 8px rgba(0,0,0,.2);
    transition:transform .12s;
  }
  .langBtn:hover{transform:translateY(-1px);}
  .homeBtn{
    font-size:1.35rem;
    text-decoration:none;
    background:#fff;
    border-radius:50%;
    width:40px;height:40px;
    display:inline-flex;align-items:center;justify-content:center;
    box-shadow:0 2px 8px rgba(0,0,0,.2);
    transition:transform .12s;
  }
  .homeBtn:hover{transform:translateY(-1px);}
  header p{
    margin:10px 0 0;
    font-size:.92rem;
    opacity:.92;
  }
  .logo{
    width:54px;height:54px;border-radius:50%;
    background:radial-gradient(circle at 35% 30%, #fff, #fee2e2);
    margin:0 auto 10px;display:flex;align-items:center;justify-content:center;
    font-size:1.7rem;box-shadow:0 0 0 3px rgba(255,255,255,.55) inset;
  }
  main{padding:22px 28px 30px;}
  .q{
    border:1px solid #f3c9c9;
    border-radius:12px;
    padding:16px 18px;
    margin:16px 0;
    background:#fff;
    transition:border-color .2s;
  }
  .q.correct{border-color:var(--cu-blue);background:#eef5ff;}
  .q.wrong{border-color:#dc2626;background:#fdf3f2;}
  .q h3{
    margin:0 0 12px;
    font-size:1.02rem;
    line-height:1.45;
  }
  .q h3 span{color:var(--cu-red);font-weight:bold;margin-right:6px;}
  label{
    display:block;
    padding:9px 12px;
    margin:7px 0;
    border-radius:8px;
    background:#fef2f2;
    cursor:pointer;
    border:1px solid transparent;
    transition:background .15s,border-color .15s;
    font-size:.96rem;
    line-height:1.4;
  }
  label:hover{background:#fee2e2;}
  input[type=radio]{margin-right:10px;width:18px;height:18px;vertical-align:middle;accent-color:var(--cu-red);cursor:pointer;}
  label.picked{background:#fff7cc;border-color:var(--gold);}
  label.right{background:#d7f0df;border-color:var(--cu-blue);font-weight:600;}
  label.picked-wrong{background:#f7d4d0;border-color:#dc2626;}
  .explain{
    display:none;
    margin-top:10px;
    padding:12px 14px;
    background:#fff7ed;
    border-left:4px solid var(--cu-red);
    border-radius:6px;
    font-size:.9rem;
    line-height:1.5;
  }
  .explain.show{display:block;}
  .explain .en{margin-bottom:6px;}
  .explain .zh{color:#444;}
  .explain b{color:var(--cu-dark);}
  .actions{text-align:center;margin-top:24px;}
  button.go{
    font-family:inherit;
    font-size:1.05rem;
    font-weight:bold;
    color:#fff;
    background:var(--cu-red);
    border:none;
    padding:13px 34px;
    border-radius:30px;
    cursor:pointer;
    box-shadow:0 4px 14px rgba(225,29,72,.4);
    transition:transform .12s,box-shadow .12s;
  }
  button.go:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(225,29,72,.5);}
  button.go:active{transform:translateY(0);}
  #resetBtn{display:none;background:#555;box-shadow:0 4px 14px rgba(0,0,0,.3);}
  #result{
    text-align:center;
    margin:22px auto 4px;
    font-size:1.3rem;
    font-weight:bold;
    color:var(--cu-dark);
    min-height:1.4em;
  }
  #scoreDetail{text-align:center;color:#666;font-size:.92rem;margin-bottom:6px;}
  footer{
    text-align:center;
    font-size:.8rem;
    color:#b08a8a;
    padding:14px;
    border-top:1px solid #eee;
  }"""

QUIZ_JS_BODY = """let lang = "en";
const picked = {};
let submitted = false;
let score = 0;

const L = {
  en: {
    subtitle: "Comprehension Quiz • 10 Questions • by __AUTHOR__",
    check: "Check My Answers",
    retry: "Try Again",
    langBtn: "🌐 中文",
    result: (s) => `You scored ${s} / 10`,
    perfect: "Perfect! You really know your Captain Underpants trivia.",
    great: "Great job — you understood the adventure well.",
    ok: "Not bad — but a few sneaky details slipped past you.",
    low: "Time for a re-read! The answers are in the comic.",
    ansLabel: "Answer"
  },
  zh: {
    subtitle: "阅读理解测验 • 共10题 • 作者：__AUTHOR__",
    check: "提交答案",
    retry: "再做一次",
    langBtn: "🌐 English",
    result: (s) => `你的得分：${s} / 10`,
    perfect: "满分！你完全读懂了内裤队长的搞笑冒险。",
    great: "很棒——你已经读懂了这个冒险故事。",
    ok: "不错——不过有几个小细节被你漏掉了。",
    low: "该重读一遍啦！答案都藏在漫画里。",
    ansLabel: "正确答案"
  }
};

const quiz = __QUIZJSON__;

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
    qDiv.className = "q";
    qDiv.id = "q" + i;
    let html = `<h3><span>Q${i+1}.</span>${item.q[lang]}</h3>`;
    item.options.forEach((opt, j) => {
      const isPicked = picked[i] === j;
      const checked = isPicked ? "checked" : "";
      html += `<label data-q="${i}" data-o="${j}" class="${isPicked?'picked':''}>
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

  if (submitted){
    resultEl.textContent = L[lang].result(score);
    let msg = score===10 ? L[lang].perfect : score>=7 ? L[lang].great : score>=4 ? L[lang].ok : L[lang].low;
    detailEl.textContent = msg;
  } else {
    resultEl.textContent = "";
    detailEl.textContent = "";
  }
}

checkBtn.addEventListener("click", () => {
  submitted = true;
  score = 0;
  quiz.forEach((item,i) => { if (picked[i] === item.answer) score++; });
  render();
  checkBtn.style.display = "none";
  resetBtn.style.display = "inline-block";
});

resetBtn.addEventListener("click", () => {
  location.reload();
});

langBtn.addEventListener("click", () => {
  lang = (lang === "en") ? "zh" : "en";
  render();
});

// Delegated listener survives re-renders: any radio selection (mouse or keyboard) updates state.
qEl.addEventListener("change", e => {
  if (submitted) return;
  const inp = e.target;
  if (!inp || inp.type !== "radio") return;
  const label = inp.closest("label[data-q]");
  if (!label) return;
  const qi = +label.dataset.q;
  const oi = +label.dataset.o;
  picked[qi] = oi;
  qEl.querySelectorAll(`label[data-q="${qi}"]`).forEach(l => l.classList.remove("picked"));
  label.classList.add("picked");
});

render();"""


def slugify(title):
    t = re.sub(r'^The\s+', '', title)
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", '-', t).strip('-')
    return t


def validate(d):
    errs = []
    if not d.get("number") or not d.get("title"):
        errs.append("missing number/title")
    qs = d.get("questions", [])
    if len(qs) != 10:
        errs.append(f"expected 10 questions, got {len(qs)}")
    for i, q in enumerate(qs):
        if not isinstance(q.get("q"), dict) or "en" not in q["q"] or "zh" not in q["q"]:
            errs.append(f"Q{i+1} bad q")
            continue
        opts = q.get("options", [])
        if len(opts) != 4:
            errs.append(f"Q{i+1} options != 4")
        for o in opts:
            if not isinstance(o, dict) or "en" not in o or "zh" not in o:
                errs.append(f"Q{i+1} bad option")
        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a < len(opts)):
            errs.append(f"Q{i+1} bad answer index {a}")
        ex = q.get("explain", {})
        if not isinstance(ex, dict) or "en" not in ex or "zh" not in ex:
            errs.append(f"Q{i+1} bad explain")
    return errs


def gen_quizzes():
    files = sorted(
        f for f in os.listdir(DATA) if f.endswith(".json")
    )
    print(f"\n=== gen_quizzes: found {len(files)} JSON files ===")
    manifest = []
    for f in files:
        path = os.path.join(DATA, f)
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        errs = validate(d)
        number = str(d.get("number", f.replace(".json", "")))
        if errs:
            print(f"  [SKIP] {f}: {'; '.join(errs)}")
            continue
        slug = slugify(d["title"])
        year = d.get("year", "")
        title = d["title"]
        author = d.get("author", AUTHOR)

        quiz_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<title>__TITLE__ — Quiz</title>
<style>
__CSS__
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topbar">
      <button class="langBtn" id="langBtn">🌐 中文</button>
      <h1>#__NUM__ · __TITLE__</h1>
      <a class="homeBtn" href="../../index.html" title="Home / 首页" aria-label="Home">🏠</a>
    </div>
    <p id="subtitle">Comprehension Quiz • 10 Questions • by __AUTHOR__</p>
    <div class="logo">🦸</div>
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
  <footer>Based on <em>Captain Underpants: __TITLE__</em> (Scholastic, __YEAR__) — by __AUTHOR__</footer>
</div>

<script>
__JS__
</script>
</body>
</html>"""

        quiz_js = QUIZ_JS_BODY.replace("__AUTHOR__", author)
        quiz_html = (quiz_html
                     .replace("__TITLE__", title)
                     .replace("__NUM__", number)
                     .replace("__CSS__", QUIZ_CSS)
                     .replace("__AUTHOR__", author)
                     .replace("__YEAR__", str(year))
                     .replace("__JS__", quiz_js)
                     .replace("__QUIZJSON__", json.dumps(d["questions"], ensure_ascii=False)))

        out_name = f"{slug}-quiz.html"
        out_path = os.path.join(BASE, out_name)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(quiz_html)
        print(f"  [OK] #{number} -> {out_name}  (source: {d.get('source','?')})")
        manifest.append({
            "number": number,
            "title": title,
            "titleZh": d.get("titleZh", ""),
            "slug": slug,
            "year": year,
            "author": author,
            "emoji": d.get("emoji", "🦸"),
            "desc": d.get("desc", ""),
            "source": d.get("source", "ima-pdf"),
            "file": out_name,
        })
    return manifest


def gen_hub(manifest):
    books = {m["number"]: m for m in manifest}
    nums = sorted(books.keys(), key=lambda x: int(x))

    cards = []
    for n in nums:
        b = books[n]
        accent = accent_for(n)
        cards.append(f"""    <article class="book" style="--accent:{accent}">
      <div class="top"><div class="num">{b['number']}</div><div class="emoji">{b['emoji']}</div></div>
      <div class="body">
        <h3 class="title">{b['title']}</h3>
        <p class="titleZh">{b.get('titleZh','')}</p>
        <p class="desc">{b['desc']}</p>
        <a class="start" href="{b['file']}">做测验 Take Quiz →</a>
      </div>
    </article>""")

    count = len(cards)
    lo = int(nums[0])
    hi = int(nums[-1])
    missing = [n for n in range(lo, hi + 1) if str(n) not in books]
    miss_txt = ("（缺 #" + "、#".join(str(m) for m in missing) + "）") if missing else ""

    hub = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<title>Captain Underpants — Books</title>
<style>
  :root{{
    --cu-red:#e11d48;
    --cu-blue:#2563eb;
    --cu-dark:#7f1d1d;
    --cream:#fffdf7;
    --ink:#1f2937;
  }}
  *{{box-sizing:border-box;}}
  body{{
    margin:0;
    font-family:"Comic Sans MS","Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--cu-red),#9f1239);
    color:var(--ink);min-height:100vh;padding:0 0 40px;
  }}
  header{{
    background:linear-gradient(135deg,var(--cu-red),var(--cu-blue));color:#fff;text-align:center;
    padding:26px 18px 20px;position:relative;
  }}
  .topbar{{display:flex;align-items:center;justify-content:space-between;gap:10px;}}
  .topbar h1{{margin:0;font-size:1.5rem;flex:1;text-align:center;}}
  .homeBtn{{
    font-size:1.35rem;text-decoration:none;background:#fff;border-radius:50%;
    width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;
    box-shadow:0 2px 8px rgba(0,0,0,.2);transition:transform .12s;
  }}
  .homeBtn:hover{{transform:translateY(-1px);}}
  header p{{margin:10px 0 0;font-size:.92rem;opacity:.92;}}
  .logo{{
    width:56px;height:56px;border-radius:50%;margin:14px auto 4px;
    background:radial-gradient(circle at 35% 30%, #fff, #fee2e2);
    display:flex;align-items:center;justify-content:center;font-size:1.8rem;
    box-shadow:0 0 0 3px rgba(255,255,255,.55) inset;
  }}
  .wrap{{max-width:1000px;margin:26px auto 0;padding:0 18px;}}
  .intro{{
    background:var(--cream);border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.3);
    padding:18px 22px;font-size:.95rem;line-height:1.6;color:#444;
  }}
  .intro b{{color:var(--cu-dark);}}
  .grid{{
    margin-top:22px;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;
  }}
  .book{{
    background:var(--cream);border-radius:16px;overflow:hidden;
    box-shadow:0 8px 20px rgba(0,0,0,.28);
    display:flex;flex-direction:column;border-top:6px solid var(--accent,var(--cu-red));
    transition:transform .15s,box-shadow .15s;
  }}
  .book:hover{{transform:translateY(-4px);box-shadow:0 12px 26px rgba(0,0,0,.34);}}
  .book .top{{padding:16px;text-align:center;background:linear-gradient(180deg,var(--accent,#e11d48),transparent);}}
  .num{{
    width:54px;height:54px;line-height:54px;border-radius:50%;background:#fff;
    color:var(--accent,#e11d48);font-size:1.5rem;font-weight:bold;margin:0 auto 8px;
    border:3px solid #fff;box-shadow:0 4px 10px rgba(0,0,0,.2);
  }}
  .book .emoji{{font-size:1.7rem;}}
  .book .title{{margin:4px 0;font-size:1.02rem;font-weight:bold;line-height:1.3;padding:0 12px;}}
  .book .titleZh{{margin:0 0 6px;font-size:.82rem;color:#888;padding:0 12px;}}
  .book .body{{padding:6px 14px 16px;flex:1;display:flex;flex-direction:column;}}
  .book .desc{{font-size:.82rem;color:#555;line-height:1.45;margin:0 0 12px;flex:1;padding:0 6px;}}
  .start{{
    display:block;text-align:center;text-decoration:none;font-family:inherit;
    font-size:.95rem;font-weight:bold;color:#fff;background:var(--accent,#e11d48);
    padding:10px;border-radius:30px;box-shadow:0 4px 12px rgba(0,0,0,.2);transition:filter .15s;
  }}
  .start:hover{{filter:brightness(1.08);}}
  footer{{text-align:center;color:rgba(255,255,255,.85);font-size:.8rem;margin-top:32px;}}
</style>
</head>
<body>
<header>
  <div class="topbar">
    <a class="homeBtn" href="../../index.html" title="Home / 首页" aria-label="Home">🏠</a>
    <h1>Captain Underpants</h1>
    <span style="width:40px"></span>
  </div>
  <div class="logo">🦸</div>
  <p>初章书 · 搞笑漫画冒险 · Early Chapter / Comedy — by {AUTHOR}</p>
</header>

<div class="wrap">
  <div class="intro">
    🦸 <b>{count} 本 Captain Underpants 内裤队长搞笑冒险（#{lo}–#{hi}）{miss_txt}，每本都有中英双语阅读理解测验。</b><br>
    {count} Captain Underpants comedy adventures by Dav Pilkey — troublemakers George &amp; Harold hypnotize grumpy Principal Krupp into the waistband-wearing superhero Captain Underpants. Each book has a bilingual (English / 中文) comprehension quiz. Tap a book, read the questions, then check your answers!
  </div>

  <div class="grid">
{os.linesep.join(cards)}
  </div>
</div>

<footer>Part of 英语分级阅读乐园 · Reading by Level</footer>
</body>
</html>
"""
    out = os.path.join(BASE, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(hub)
    print(f"\n=== gen_hub: wrote index.html with {count} books ===")


if __name__ == "__main__":
    man = gen_quizzes()
    gen_hub(man)
    with open(os.path.join(BASE, "_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(man, fh, ensure_ascii=False, indent=2)
    print("Done.")
