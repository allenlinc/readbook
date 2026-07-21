#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Warriors (猫武士) quiz static site generator.
Data-driven: embed the full 77-book catalogue (grouped by 11 series) here,
and load per-book description + 10 questions from _bookdata/<slug>.json.
Generates one quiz HTML per book + a grouped hub index.html.

Uses plain .replace() token injection (not str.format) so that curly braces
inside CSS or quiz text never break generation.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "_bookdata")
ASSETS = os.path.join(HERE, "assets")
HOMELINK = "../../index.html"

# ---- Series catalogue -------------------------------------------------------
# Each series: (key, en_name, zh_name, [ (slug, en_title, zh_title, accent, emoji) ])
SERIES = [
    ("arc1", "The Prophecy Begins", "预言开始", [
        ("into-the-wild", "Into the Wild", "呼唤野性", "#e67e22", "🔥"),
        ("fire-and-ice", "Fire and Ice", "寒冰烈火", "#c0392b", "❄️"),
        ("forest-of-secrets", "Forest of Secrets", "秘密森林", "#8e44ad", "🌲"),
        ("rising-storm", "Rising Storm", "风暴将临", "#2980b9", "🌩️"),
        ("a-dangerous-path", "A Dangerous Path", "险路惊魂", "#5e35b1", "⚠️"),
        ("the-darkest-hour", "The Darkest Hour", "黑暗时刻", "#1f6b41", "🌑"),
    ]),
    ("arc2", "The New Prophecy", "新预言", [
        ("midnight", "Midnight", "午夜追踪", "#16a085", "🌊"),
        ("moonrise", "Moonrise", "月升之处", "#1abc9c", "🌙"),
        ("dawn", "Dawn", "黎明曙光", "#27ae60", "🌅"),
        ("starlight", "Starlight", "星光闪烁", "#2ecc71", "⭐"),
        ("twilight", "Twilight", "暮色降临", "#2980b9", "🌆"),
        ("sunset", "Sunset", "日落和平", "#3498db", "🌇"),
    ]),
    ("arc3", "Power of Three", "三力量", [
        ("the-sight", "The Sight", "预视力量", "#8e44ad", "👁️"),
        ("dark-river", "Dark River", "暗河汹涌", "#9b59b6", "🌊"),
        ("outcast", "Outcast", "放逐之星", "#c0392b", "🚫"),
        ("eclipse", "Eclipse", "日蚀遮蔽", "#d35400", "🌘"),
        ("long-shadows", "Long Shadows", "长影静默", "#e67e22", "🌑"),
        ("sunrise", "Sunrise", "日出风暴", "#e74c3c", "🌅"),
    ]),
    ("arc4", "Omen of the Stars", "星预言", [
        ("the-fourth-apprentice", "The Fourth Apprentice", "第四学徒", "#2c3e50", "🐾"),
        ("fading-echoes", "Fading Echoes", "消逝回音", "#34495e", "🌫️"),
        ("night-whispers", "Night Whispers", "夜语私语", "#16a085", "🌙"),
        ("sign-of-the-moon", "Sign of the Moon", "月亮征兆", "#2980b9", "🗡️"),
        ("the-forgotten-warrior", "The Forgotten Warrior", "被遗忘的武士", "#8e44ad", "⚔️"),
        ("the-last-hope", "The Last Hope", "最后的希望", "#c0392b", "🌟"),
    ]),
    ("arc5", "Dawn of the Clans", "族群黎明", [
        ("the-sun-trail", "The Sun Trail", "太阳踪迹", "#d35400", "☀️"),
        ("thunder-rising", "Thunder Rising", "雷鸣崛起", "#e67e22", "⚡"),
        ("the-first-battle", "The First Battle", "第一场战斗", "#f39c12", "⚔️"),
        ("the-blazing-star", "The Blazing Star", "炽烈之星", "#f1c40f", "✦"),
        ("a-forest-divided", "A Forest Divided", "分裂森林", "#27ae60", "🌳"),
        ("path-of-stars", "Path of Stars", "群星之路", "#16a085", "✨"),
    ]),
    ("arc6", "A Vision of Shadows", "暗影幻象", [
        ("the-apprentices-quest", "The Apprentice's Quest", "学徒的追寻", "#6c3483", "🔍"),
        ("thunder-and-shadow", "Thunder and Shadow", "雷影交加", "#8e44ad", "⚡"),
        ("shattered-sky", "Shattered Sky", "破碎天空", "#a569bd", "💥"),
        ("darkest-night", "Darkest Night", "最黑暗的夜晚", "#c39bd3", "🌑"),
        ("river-of-fire", "River of Fire", "火焰之河", "#1f6b41", "🔥"),
        ("the-raging-storm", "The Raging Storm", "狂暴风暴", "#2ecc71", "🌪️"),
    ]),
    ("arc7", "The Broken Code", "破灭守则", [
        ("lost-stars", "Lost Stars", "失落群星", "#154360", "⭐"),
        ("the-silent-thaw", "The Silent Thaw", "寂静融雪", "#1a5276", "❄️"),
        ("veil-of-shadows", "Veil of Shadows", "暗影之纱", "#2471a3", "🌫️"),
        ("darkness-within", "Darkness Within", "内心黑暗", "#2e86c1", "🌑"),
        ("the-place-of-no-stars", "The Place of No Stars", "无星之地", "#5dade2", "🕳️"),
        ("a-light-in-the-mist", "A Light in the Mist", "迷雾微光", "#aed6f1", "💡"),
    ]),
    ("arc8", "A Starless Clan", "无星之族", [
        ("river", "River", "河浪", "#1a5276", "🌊"),
        ("sky", "Sky", "天空", "#5dade2", "☁️"),
    ]),
    ("super", "Super Editions", "超级外传", [
        ("firestars-quest", "Firestar's Quest", "火星的使命", "#922b21", "🦁"),
        ("bluestars-prophecy", "Bluestar's Prophecy", "蓝星的预言", "#b03a2e", "⭐"),
        ("crookedstars-promise", "Crookedstar's Promise", "钩星的承诺", "#ca6f1e", "🐟"),
        ("skyclans-destiny", "SkyClan's Destiny", "天族的命运", "#d68910", "🌳"),
        ("yellowfangs-secret", "Yellowfang's Secret", "黄牙的秘密", "#7d6608", "🦷"),
        ("tallstars-revenge", "Tallstar's Revenge", "高星的复仇", "#9c640c", "🐭"),
        ("bramblestars-storm", "Bramblestar's Storm", "棘星的暴风雨", "#616a6b", "🔥"),
        ("moth-flights-vision", "Moth Flight's Vision", "蛾飞的幻象", "#7d6e4e", "🦋"),
        ("hawkwings-journey", "Hawkwing's Journey", "鹰翅的旅程", "#4a235a", "🦅"),
        ("tigerhearts-shadow", "Tigerheart's Shadow", "虎心的影子", "#633974", "🐯"),
        ("crowfeathers-trial", "Crowfeather's Trial", "鸦羽的考验", "#7e5109", "🐦"),
        ("leopardstars-honor", "Leopardstar's Honor", "豹星的荣耀", "#b9770e", "🐆"),
        ("squirrelflights-hope", "Squirrelflight's Hope", "松鼠飞的希望", "#117864", "🐿️"),
        ("graystripes-vow", "Graystripe's Vow", "灰条的誓言", "#0e6655", "🐺"),
        ("onestars-confession", "Onestar's Confession", "一根须的忏悔", "#1e8449", "📜"),
    ]),
    ("novellas", "Novellas", "外传短篇", [
        ("hollyleafs-story", "Hollyleaf's Story", "冬青叶的故事", "#117a65", "🍃"),
        ("mistystars-omen", "Mistystar's Omen", "雾星的预兆", "#148f77", "🌊"),
        ("cloudstars-journey", "Cloudstar's Journey", "云星的旅程", "#c39bd3", "🚀"),
        ("tigerclaws-fury", "Tigerclaw's Fury", "虎掌的愤怒", "#af7ac5", "😡"),
        ("leafpools-wish", "Leafpool's Wish", "叶池的愿望", "#7e5109", "🌿"),
        ("dovewings-silence", "Dovewing's Silence", "鸽翅的沉默", "#b9770e", "🔇"),
        ("mapleshades-vengeance", "Mapleshade's Vengeance", "枫荫的复仇", "#cb4335", "⚔️"),
        ("goosefeathers-curse", "Goosefeather's Curse", "鹅羽的诅咒", "#e74c3c", "🌀"),
        ("ravenpaws-farewell", "Ravenpaw's Farewell", "鸦爪的告别", "#7d3c98", "👋"),
        ("path-of-a-warrior", "Path of a Warrior", "武士之路", "#8e44ad", "🛤️"),
        ("legends-of-the-clans", "Legends of the Clans", "族群的传说", "#1f618d", "📜"),
        ("a-warriors-spirit", "A Warrior's Spirit", "武士之魂", "#2e86c1", "✨"),
        ("a-warriors-choice", "A Warrior's Choice", "武士的抉择", "#a04000", "⚖️"),
    ]),
    ("field", "Field Guides", "设定指南", [
        ("secrets-of-the-clans", "Secrets of the Clans", "族群的秘密", "#7d6608", "📖"),
        ("cats-of-the-clans", "Cats of the Clans", "族群猫", "#b7950b", "🐱"),
        ("code-of-the-clans", "Code of the Clans", "族群守则", "#9c640c", "📜"),
        ("battles-of-the-clans", "Battles of the Clans", "族群之战", "#784212", "⚔️"),
        ("the-ultimate-guide", "The Ultimate Guide", "终极指南", "#1b4f72", "📚"),
    ]),
]

ALL_BOOKS = [(s[0], s[1], s[2], b) for s in SERIES for b in s[3]]


def load_book_data(slug):
    with open(os.path.join(DATA_DIR, slug + ".json"), "r", encoding="utf-8") as f:
        return json.load(f)


def read_asset(name):
    with open(os.path.join(ASSETS, name), "r", encoding="utf-8") as f:
        return f.read()


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fill(tmpl, **kw):
    out = tmpl
    for k, v in kw.items():
        out = out.replace("__%s__" % k.upper(), str(v))
    return out


# ---- Templates --------------------------------------------------------------
QUIZ_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__EN_TITLE__ · 猫武士 Warriors Quiz</title>
<style>
__CSS__
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topbar">
      <button class="langBtn" id="langBtn">🌐 中文</button>
      <h1>__EN_TITLE__</h1>
      <a class="homeBtn" href="__HOMELINK__" title="Home / 首页" aria-label="Home">🏠</a>
    </div>
    <p id="subtitle">Comprehension Quiz • 10 Questions • by Erin Hunter</p>
    <p class="bookzh">__ZH_TITLE__</p>
    <div class="mark">__EMOJI__</div>
  </header>
  <main>
    <p style="text-align:center;color:#555;font-size:.9rem;margin:-2px 0 16px;line-height:1.5">__DESC__<br><span style="color:#a06a1f">__DESCZH__</span></p>
    <div id="questions"></div>
    <div id="result"></div>
    <div id="scoreDetail"></div>
    <div class="actions">
      <button class="go" id="checkBtn">Check My Answers</button>
      <button class="go" id="resetBtn">Try Again</button>
    </div>
  </main>
  <footer>Based on <em>Warriors: __SERIES_EN__ — __EN_TITLE__</em> (HarperCollins)</footer>
</div>
<script>
__JS__
</script>
</body>
</html>
"""

HUB_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Warriors · 猫武士 — All Series</title>
<style>
  :root{
    --forest:#2f5d3a; --forest-dark:#1e3f27; --ember:#d35400;
    --cream:#fbf7ee; --ink:#2a2118; --gold:#e0a82e;
  }
  *{box-sizing:border-box;}
  body{
    margin:0; font-family:"Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--forest),var(--forest-dark));
    color:var(--ink); min-height:100vh; padding:0 0 40px;
  }
  header{ background:var(--ember); color:#fff; text-align:center; padding:26px 18px 20px; position:relative; }
  .topbar{display:flex;align-items:center;justify-content:space-between;gap:10px;}
  .topbar h1{margin:0;font-size:1.5rem;flex:1;text-align:center;}
  .homeBtn{font-size:1.35rem;text-decoration:none;background:#fff;border-radius:50%;width:40px;height:40px;
    display:inline-flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.2);transition:transform .12s;}
  .homeBtn:hover{transform:translateY(-1px);}
  header p{margin:10px 0 0;font-size:.92rem;opacity:.94;}
  header .arc{font-weight:bold;letter-spacing:1px;}
  .wrap{max-width:1040px;margin:26px auto 0;padding:0 18px;}
  .intro{background:var(--cream);border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.3);
    padding:18px 22px;font-size:.95rem;line-height:1.6;color:#444;}
  .intro b{color:var(--forest-dark);}
  .series{margin-top:30px;}
  .series h2{color:#fff;font-size:1.2rem;letter-spacing:.5px;border-left:6px solid var(--gold);
    padding-left:12px;margin:0 0 4px;}
  .series .sub{color:rgba(255,255,255,.85);font-size:.86rem;margin:0 0 14px;padding-left:18px;}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;}
  .book{background:var(--cream);border-radius:16px;overflow:hidden;box-shadow:0 8px 20px rgba(0,0,0,.28);
    display:flex;flex-direction:column;border-top:6px solid var(--accent,var(--forest));transition:transform .15s,box-shadow .15s;}
  .book:hover{transform:translateY(-4px);box-shadow:0 12px 26px rgba(0,0,0,.34);}
  .book .top{padding:14px;text-align:center;background:linear-gradient(180deg,var(--accent,#2f5d3a),transparent);}
  .book .emoji{font-size:2rem;}
  .book .title{margin:6px 0 2px;font-size:1.02rem;font-weight:bold;line-height:1.3;padding:0 12px;text-align:center;}
  .book .titleZh{margin:0 0 6px;font-size:.82rem;color:#a06a1f;text-align:center;font-weight:bold;}
  .book .body{padding:4px 14px 14px;flex:1;display:flex;flex-direction:column;}
  .book .desc{font-size:.8rem;color:#555;line-height:1.42;margin:0 0 12px;flex:1;padding:0 4px;}
  .start{display:block;text-align:center;text-decoration:none;font-family:inherit;font-size:.92rem;font-weight:bold;
    color:#fff;background:var(--accent,#2f5d3a);padding:9px;border-radius:30px;box-shadow:0 4px 12px rgba(0,0,0,.2);transition:filter .15s;}
  .start:hover{filter:brightness(1.08);}
  footer{text-align:center;color:rgba(255,255,255,.85);font-size:.8rem;margin-top:32px;}
</style>
</head>
<body>
<header>
  <div class="topbar">
    <a class="homeBtn" href="__HOMELINK__" title="Home / 首页" aria-label="Home">🏠</a>
    <h1>Warriors · 猫武士</h1>
    <span style="width:40px"></span>
  </div>
  <p class="arc">全系列中英双语阅读理解测验</p>
  <p>中章书 · Middle Chapter — by Erin Hunter · 共 __TOTAL__ 本</p>
</header>
<div class="wrap">
  <div class="intro">
    🐾 <b>__TOTAL__ 本《猫武士》中英双语阅读理解测验，分 __NSERIES__ 个系列。</b><br>
    __TOTAL__ bilingual (English / 中文) comprehension quizzes across every Warriors series. Pick a book, answer 10 questions, then check your answers!
  </div>
__SECTIONS__
</div>
<footer>Part of 分级阅读乐园 · Reading by Level</footer>
</body>
</html>
"""


def gen_quiz_page(series_en, book):
    slug, en_title, zh_title, accent, emoji = book
    data = load_book_data(slug)
    css = read_asset("quiz.css")
    js_tmpl = read_asset("quiz_body.js")
    questions = data.get("questions", [])
    js = js_tmpl.replace("__QUIZJSON__", json.dumps(questions, ensure_ascii=False))
    desc = data.get("desc", "")
    desczh = data.get("descZh", "")
    return fill(QUIZ_PAGE,
                EN_TITLE=esc(en_title), ZH_TITLE=esc(zh_title), EMOJI=emoji,
                SERIES_EN=esc(series_en), DESC=esc(desc), DESCZH=esc(desczh),
                CSS=css, JS=js, HOMELINK=HOMELINK)


def gen_hub():
    sections_html = []
    for key, en_name, zh_name, books in SERIES:
        cards = []
        for slug, en_title, zh_title, accent, emoji in books:
            try:
                d = load_book_data(slug)
                desc = d.get("desc", "")
            except Exception:
                desc = ""
            card = fill(
                '    <article class="book" style="--accent:__ACC__">\n'
                '      <div class="top"><div class="emoji">__EMOJI__</div></div>\n'
                '      <div class="body">\n'
                '        <h3 class="title">__EN__</h3>\n'
                '        <p class="titleZh">__ZH__</p>\n'
                '        <p class="desc">__DESC__</p>\n'
                '        <a class="start" href="__SLUG__-quiz.html">做测验 Take Quiz →</a>\n'
                '      </div>\n'
                '    </article>',
                ACC=accent, EMOJI=emoji, EN=esc(en_title), ZH=esc(zh_title),
                DESC=esc(desc), SLUG=slug)
            cards.append(card)
        section = fill(
            '  <section class="series">\n'
            '    <h2>__EN__ · __ZH__</h2>\n'
            '    <p class="sub">__N__ 本 · __N__ books</p>\n'
            '    <div class="grid">\n__CARDS__\n    </div>\n'
            '  </section>',
            EN=esc(en_name), ZH=esc(zh_name), N=len(books), CARDS="\n".join(cards))
        sections_html.append(section)
    total = len(ALL_BOOKS)
    return fill(HUB_PAGE, HOMELINK=HOMELINK, TOTAL=total, NSERIES=len(SERIES),
                SECTIONS="\n".join(sections_html))


def main():
    missing = []
    built = 0
    for key, en_name, zh_name, books in SERIES:
        for slug, en_title, zh_title, accent, emoji in books:
            try:
                html = gen_quiz_page(en_name, (slug, en_title, zh_title, accent, emoji))
            except FileNotFoundError:
                missing.append(slug)
                continue
            with open(os.path.join(HERE, slug + "-quiz.html"), "w", encoding="utf-8") as f:
                f.write(html)
            built += 1
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(gen_hub())
    print("Built %d quiz pages + hub (index.html)." % built)
    if missing:
        print("Missing _bookdata for: " + ", ".join(missing))


if __name__ == "__main__":
    main()
