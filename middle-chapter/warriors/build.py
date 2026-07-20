#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for the Warriors (猫武士 · The Prophecy Begins) quiz site.

Mirrors early-chapter/atozmysteries/build.py but for the 6-book first arc.
All quiz data lives in the BOOKS list below; running this script:

  1. gen_data()  -> writes _quizdata/<slug>.json (record, like a-to-z)
  2. gen_quizzes()-> emits one self-contained bilingual (EN/ZH) quiz HTML per book
  3. gen_hub()   -> rebuilds index.html listing all books

Run:  python3 build.py
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")

ARC = "The Prophecy Begins"
ARC_ZH = "预言开始"

# Per-book accent colors (forest + ember palette).
ACCENT = {
    "1": "#e67e22",  # Into the Wild — ember
    "2": "#c0392b",  # Fire and Ice — red
    "3": "#8e44ad",  # Forest of Secrets — purple
    "4": "#2980b9",  # Rising Storm — blue
    "5": "#5e35b1",  # A Dangerous Path — indigo
    "6": "#1f6b41",  # The Darkest Hour — deep green
}

QUIZ_CSS = """  :root{
    --forest:#2f5d3a;
    --forest-dark:#1e3f27;
    --ember:#d35400;
    --cream:#fbf7ee;
    --ink:#2a2118;
    --gold:#e0a82e;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    font-family:"Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--forest),var(--forest-dark));
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
    background:var(--ember);
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
    font-size:1.55rem;
    letter-spacing:.5px;
    flex:1;
    text-align:center;
  }
  .langBtn{
    font-family:inherit;
    font-size:.85rem;
    font-weight:bold;
    color:var(--ember);
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
    opacity:.94;
  }
  .bookzh{margin:2px 0 0 !important;font-weight:bold;letter-spacing:1px;}
  .mark{
    width:54px;height:54px;border-radius:50%;
    background:#fff;margin:12px auto 0;
    display:flex;align-items:center;justify-content:center;
    font-size:1.8rem;
    box-shadow:0 3px 10px rgba(0,0,0,.25);
  }
  main{padding:22px 28px 30px;}
  .q{
    border:1px solid #e3ddc8;
    border-radius:12px;
    padding:16px 18px;
    margin:16px 0;
    background:#fff;
    transition:border-color .2s;
  }
  .q.correct{border-color:var(--forest);background:#f3fbf6;}
  .q.wrong{border-color:var(--ember);background:#fdf3f2;}
  .q h3{
    margin:0 0 12px;
    font-size:1.02rem;
    line-height:1.45;
  }
  .q h3 span{color:var(--ember);font-weight:bold;margin-right:6px;}
  label{
    display:block;
    padding:9px 12px;
    margin:7px 0;
    border-radius:8px;
    background:#f7f5ec;
    cursor:pointer;
    border:1px solid transparent;
    transition:background .15s,border-color .15s;
    font-size:.96rem;
    line-height:1.4;
  }
  label:hover{background:#efe9d4;}
  input[type=radio]{margin-right:9px;transform:translateY(1px);}
  label.picked{background:#fff4cc;border-color:var(--gold);}
  label.right{background:#d7f0df;border-color:var(--forest);font-weight:600;}
  label.picked-wrong{background:#f7d4d0;border-color:var(--ember);}
  .explain{
    display:none;
    margin-top:10px;
    padding:12px 14px;
    background:#f0f4ff;
    border-left:4px solid #4a6fc9;
    border-radius:6px;
    font-size:.9rem;
    line-height:1.5;
  }
  .explain.show{display:block;}
  .explain .en{margin-bottom:6px;}
  .explain .zh{color:#444;}
  .explain b{color:var(--forest-dark);}
  .actions{text-align:center;margin-top:24px;}
  button.go{
    font-family:inherit;
    font-size:1.05rem;
    font-weight:bold;
    color:#fff;
    background:var(--ember);
    border:none;
    padding:13px 34px;
    border-radius:30px;
    cursor:pointer;
    box-shadow:0 4px 14px rgba(211,84,0,.4);
    transition:transform .12s,box-shadow .12s;
  }
  button.go:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(211,84,0,.5);}
  button.go:active{transform:translateY(0);}
  #resetBtn{display:none;background:#555;box-shadow:0 4px 14px rgba(0,0,0,.3);}
  #result{
    text-align:center;
    margin:22px auto 4px;
    font-size:1.3rem;
    font-weight:bold;
    color:var(--forest-dark);
    min-height:1.4em;
  }
  #scoreDetail{text-align:center;color:#666;font-size:.92rem;margin-bottom:6px;}
  footer{
    text-align:center;
    font-size:.8rem;
    color:#9a9486;
    padding:14px;
    border-top:1px solid #eee;
  }"""

QUIZ_JS_BODY = """let lang = "en";
const picked = {};
let submitted = false;
let score = 0;

const L = {
  en: {
    subtitle: "Comprehension Quiz • 10 Questions • by Erin Hunter",
    check: "Check My Answers",
    retry: "Try Again",
    langBtn: "🌐 中文",
    result: (s) => `You scored ${s} / 10`,
    perfect: "Perfect! You really read every page.",
    great: "Great job — you understood the story well.",
    ok: "Not bad — but a few clues slipped past you.",
    low: "Time for a re-read! The prophecy is in the details.",
    ansLabel: "Answer"
  },
  zh: {
    subtitle: "阅读理解测验 • 共10题 • 作者：Erin Hunter",
    check: "提交答案",
    retry: "再做一次",
    langBtn: "🌐 English",
    result: (s) => `你的得分：${s} / 10`,
    perfect: "满分！你每一页都读得很仔细。",
    great: "很棒——你已经读懂了这本书。",
    ok: "不错——不过有几处细节被你漏掉了。",
    low: "该重读一遍啦！真相藏在细节里。",
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
      const qi = +e.target.name.replace("q","");
      picked[qi] = +e.target.value;
      qEl.querySelectorAll(`label[data-q="${qi}"]`).forEach(l=>l.classList.remove("picked"));
      e.target.closest("label").classList.add("picked");
    });
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

render();"""

# ---------------------------------------------------------------------------
# Quiz data — 6 books of The Prophecy Begins (猫武士·预言开始)
# ---------------------------------------------------------------------------
BOOKS = [
  {
    "num": "1", "slug": "into-the-wild", "title": "Into the Wild", "titleZh": "呼唤野性",
    "year": 2003, "emoji": "🔥",
    "desc": "A housecat named Rusty joins ThunderClan as Firepaw — and a prophecy says fire will save the Clan. 🔥",
    "descZh": "家猫 Rusty 以 Firepaw 之名加入雷族——预言说，火将拯救族群。",
    "questions": [
      {"q":{"en":"What is the housecat Rusty's name BEFORE he joins ThunderClan?","zh":"家猫 Rusty 在加入雷族之前叫什么名字？"},
       "options":[{"en":"Rusty","zh":"Rusty（小锈）"},{"en":"Firepaw","zh":"Firepaw（火爪）"},{"en":"Cloudtail","zh":"Cloudtail（云尾）"},{"en":"Scourge","zh":"Scourge（长鞭）"}],
       "answer":0,
       "explain":{"en":"Rusty is a kittypet (housecat) who is invited to join ThunderClan and is renamed Firepaw.","zh":"Rusty 是一只家猫，被邀请加入雷族后改名为 Firepaw（火爪）。"}},
      {"q":{"en":"Which of the four forest Clans does Rusty join?","zh":"Rusty 加入的是森林四大猫族中的哪一个？"},
       "options":[{"en":"ThunderClan","zh":"ThunderClan（雷族）"},{"en":"RiverClan","zh":"RiverClan（河族）"},{"en":"ShadowClan","zh":"ShadowClan（影族）"},{"en":"WindClan","zh":"WindClan（风族）"}],
       "answer":0,
       "explain":{"en":"He joins ThunderClan, one of the four Clans (Thunder, River, Shadow, Wind) that share the forest.","zh":"他加入了雷族——与河族、影族、风族共享森林的四大猫族之一。"}},
      {"q":{"en":"Who is Firepaw's first mentor in ThunderClan?","zh":"Firepaw 在雷族的第一位导师是谁？"},
       "options":[{"en":"Lionheart","zh":"Lionheart（狮心）"},{"en":"Tigerclaw","zh":"Tigerclaw（虎掌）"},{"en":"Bluestar","zh":"Bluestar（蓝星）"},{"en":"Graystripe","zh":"Graystripe（灰条）"}],
       "answer":0,
       "explain":{"en":"Bluestar assigns Lionheart (and Tigerclaw) to mentor Firepaw; Lionheart is his primary mentor until he dies.","zh":"蓝星安排狮心（与虎掌）教导 Firepaw；狮心是他主要的导师，直到牺牲。"}},
      {"q":{"en":"What prophecy does Spottedleaf share that points to Firepaw?","zh":"Spottedleaf 分享的、指向 Firepaw 的预言是什么？"},
       "options":[{"en":"Fire alone can save our Clan","zh":"唯有火能拯救我们的族群"},{"en":"Water will drown the forest","zh":"水将淹没森林"},{"en":"The wind will carry us home","zh":"风将带我们回家"},{"en":"Ice shall rule the Clan","zh":"冰将统治族群"}],
       "answer":0,
       "explain":{"en":"Spottedleaf's prophecy — 'Fire alone can save our Clan' — refers to the flame-colored newcomer, Firepaw.","zh":"Spottedleaf 的预言“唯有火能拯救我们的族群”，指的就是这只火色的新成员 Firepaw。"}},
      {"q":{"en":"Which ShadowClan cat kills Spottedleaf and steals the ThunderClan kits?","zh":"哪个影族猫杀死了 Spottedleaf 并偷走了雷族的幼猫？"},
       "options":[{"en":"Clawface","zh":"Clawface（利爪）"},{"en":"Blackfoot","zh":"Blackfoot（黑脚）"},{"en":"Brokenstar","zh":"Brokenstar（碎星）"},{"en":"Tigerclaw","zh":"Tigerclaw（虎掌）"}],
       "answer":0,
       "explain":{"en":"Clawface raids the camp, kills Spottedleaf the medicine cat, and carries off the four ThunderClan kits.","zh":"利爪突袭营地，杀死了巫医斑叶，并叼走了雷族的四只幼猫。"}},
      {"q":{"en":"Who is Tigerclaw's apprentice that secretly witnesses Redtail's murder?","zh":"谁是虎掌的学徒，暗中目睹了红尾被杀？"},
       "options":[{"en":"Ravenpaw","zh":"Ravenpaw（鸦爪）"},{"en":"Graypaw","zh":"Graypaw（灰爪）"},{"en":"Dustpaw","zh":"Dustpaw（尘爪）"},{"en":"Sandpaw","zh":"Sandpaw（沙爪）"}],
       "answer":0,
       "explain":{"en":"Ravenpaw sees Tigerclaw kill Redtail and is terrified into silence; he later flees to live as a kittypet.","zh":"鸦爪亲眼看见虎掌杀死红尾，吓得不敢声张，后来逃去做了宠物猫。"}},
      {"q":{"en":"Who actually killed Redtail, the ShadowClan deputy?","zh":"真正杀死影族副族长红尾的是谁？"},
       "options":[{"en":"Tigerclaw","zh":"Tigerclaw（虎掌）"},{"en":"Oakheart","zh":"Oakheart（橡心）"},{"en":"Lionheart","zh":"Lionheart（狮心）"},{"en":"A monster (car)","zh":"怪兽（汽车）"}],
       "answer":0,
       "explain":{"en":"Tigerclaw killed Redtail at the gorge and blamed Oakheart; Ravenpaw saw the truth.","zh":"虎掌在峡谷边杀死了红尾，并嫁祸给橡心；鸦爪目睹了真相。"}},
      {"q":{"en":"What is the name of the old ShadowClan medicine cat prisoner who becomes ThunderClan's medicine cat?","zh":"那位后来成为雷族巫医的、被囚禁的老影族猫叫什么？"},
       "options":[{"en":"Yellowfang","zh":"Yellowfang（黄牙）"},{"en":"Spottedleaf","zh":"Spottedleaf（斑叶）"},{"en":"Cinderpelt","zh":"Cinderpelt（炭毛）"},{"en":"Leopardfoot","zh":"Leopardfoot（豹足）"}],
       "answer":0,
       "explain":{"en":"Yellowfang, a captured ShadowClan medicine cat, stays with ThunderClan and becomes its new medicine cat.","zh":"黄牙是被俘的影族巫医，留在雷族后成为了新的巫医。"}},
      {"q":{"en":"Whose kit does Firepaw rescue and bring into ThunderClan — his own nephew?","zh":"Firepaw 救下并带进雷族的幼猫（他的亲外甥）是谁？"},
       "options":[{"en":"Cloudkit, his sister Princess's kit","zh":"云崽，他姐姐 Princess 的孩子"},{"en":"Brackenkit","zh":"Brackenkit（蕨崽）"},{"en":"Swiftkit","zh":"Swiftkit（捷崽）"},{"en":"Tiny","zh":"Tiny（小不点）"}],
       "answer":0,
       "explain":{"en":"Firepaw's kittypet sister Princess gives him one of her kits; he brings the kit (Cloudkit, later Cloudtail) to ThunderClan.","zh":"Firepaw 的家猫姐姐 Princess 送给他一只幼猫，他把云崽（后来的云尾）带进了雷族。"}},
      {"q":{"en":"What warrior name does Firepaw receive at the end of the book?","zh":"在书末，Firepaw 获得了什么武士名？"},
       "options":[{"en":"Fireheart","zh":"Fireheart（火星）"},{"en":"Firestorm","zh":"Firestorm（火暴）"},{"en":"Emberpaw","zh":"Emberpaw（余烬爪）"},{"en":"Flamefur","zh":"Flamefur（焰毛）"}],
       "answer":0,
       "explain":{"en":"Firepaw becomes the warrior Fireheart; his friend Graypaw becomes Graystripe. (Ravenpaw leaves to live as a kittypet with Barley.)","zh":"Firepaw 成为武士火星，好友灰爪成为灰条。（鸦爪则离开，与大麦一起做了宠物猫。）"}},
    ]
  },
  {
    "num": "2", "slug": "fire-and-ice", "title": "Fire and Ice", "titleZh": "寒冰烈火",
    "year": 2003, "emoji": "❄️",
    "desc": "Fireheart is a warrior now — but his best friend Graystripe loves a RiverClan cat, and Tigerclaw's treachery grows. ❄️",
    "descZh": "火星如今是武士——但好友灰条爱上了河族的猫，虎掌的背叛也愈演愈烈。",
    "questions": [
      {"q":{"en":"Which RiverClan cat does Graystripe fall in love with?","zh":"灰条爱上了河族的哪只猫？"},
       "options":[{"en":"Silverstream","zh":"Silverstream（银溪）"},{"en":"Mistyfoot","zh":"Mistyfoot（雾脚）"},{"en":"Leopardstrike","zh":"Leopardstrike（豹纹）"},{"en":"Willowbreeze","zh":"Willowbreeze（柳风）"}],
       "answer":0,
       "explain":{"en":"Graystripe secretly meets and falls in love with Silverstream, a RiverClan she-cat, at the river.","zh":"灰条在河边秘密邂逅并爱上了河族母猫银溪。"}},
      {"q":{"en":"Who is Silverstream's father, the leader of RiverClan?","zh":"银溪的父亲、河族族长是谁？"},
       "options":[{"en":"Crookedstar","zh":"Crookedstar（曲星）"},{"en":"Oakheart","zh":"Oakheart（橡心）"},{"en":"Leopardstar","zh":"Leopardstar（豹星）"},{"en":"Blackclaw","zh":"Blackclaw（黑爪）"}],
       "answer":0,
       "explain":{"en":"Silverstream is the daughter of Crookedstar, RiverClan's leader. (Oakheart was Crookedstar's brother.)","zh":"银溪是河族族长曲星的女儿。（橡心是曲星的弟弟。）"}},
      {"q":{"en":"Which Clan was driven out of its territory and helped home by Fireheart and Graystripe?","zh":"哪个族群被赶出领地，并由火星和灰条护送回家？"},
       "options":[{"en":"WindClan","zh":"WindClan（风族）"},{"en":"ShadowClan","zh":"ShadowClan（影族）"},{"en":"SkyClan","zh":"SkyClan（天族）"},{"en":"BloodClan","zh":"BloodClan（血族）"}],
       "answer":0,
       "explain":{"en":"Brokenstar's ShadowClan drove WindClan out; Fireheart and Graystripe help Tallstar's WindClan return home.","zh":"碎星统领的影族把风族赶了出去；火星和灰条帮助高星的风族重返家园。"}},
      {"q":{"en":"What evil ShadowClan leader is defeated during this book?","zh":"本书中被击败的邪恶影族族长是谁？"},
       "options":[{"en":"Brokenstar","zh":"Brokenstar（碎星）"},{"en":"Tigerstar","zh":"Tigerstar（虎星）"},{"en":"Blackfoot","zh":"Blackfoot（黑脚）"},{"en":"Nightstar","zh":"Nightstar（夜星）"}],
       "answer":0,
       "explain":{"en":"Brokenstar, the cruel ShadowClan leader, is deposed and later killed for his crimes.","zh":"残暴的影族族长碎星被推翻，后来因其罪行被处死。"}},
      {"q":{"en":"What kind of animals does Tigerclaw use to try to kill Bluestar?","zh":"虎掌利用什么动物来企图杀害蓝星？"},
       "options":[{"en":"A pack of dogs","zh":"一群狗"},{"en":"A fox","zh":"一只狐狸"},{"en":"Twoleg traps","zh":"两脚兽的陷阱"},{"en":"A badger","zh":"一只獾"}],
       "answer":0,
       "explain":{"en":"Tigerclaw trains and uses a pack of dogs near the territory as part of his plot against Bluestar.","zh":"虎掌在领地附近驯养并利用一群狗，作为谋害蓝星计划的一部分。"}},
      {"q":{"en":"After Tigerclaw is exposed and exiled, what new rank does Fireheart receive?","zh":"虎掌被揭穿并流放后，火星获得了什么新职位？"},
       "options":[{"en":"Deputy","zh":"Deputy（副族长）"},{"en":"Leader","zh":"Leader（族长）"},{"en":"Medicine cat","zh":"Medicine cat（巫医）"},{"en":"Warrior","zh":"Warrior（武士）"}],
       "answer":0,
       "explain":{"en":"With Tigerclaw gone, Bluestar names Fireheart her new deputy of ThunderClan.","zh":"虎掌离开后，蓝星任命火星为雷族的新任副族长。"}},
      {"q":{"en":"Who confirms the truth that Tigerclaw killed Redtail?","zh":"是谁证实了虎掌杀死红尾的真相？"},
       "options":[{"en":"Ravenpaw","zh":"Ravenpaw（鸦爪）"},{"en":"Graystripe","zh":"Graystripe（灰条）"},{"en":"Bluestar","zh":"Bluestar（蓝星）"},{"en":"Yellowfang","zh":"Yellowfang（黄牙）"}],
       "answer":0,
       "explain":{"en":"Ravenpaw finally tells the Clan what he saw: Tigerclaw murdered Redtail at the gorge.","zh":"鸦爪终于把所见告诉族群：虎掌在峡谷边谋杀了红尾。"}},
      {"q":{"en":"What is the name of Fireheart's nephew, the young apprentice who keeps visiting Twolegs?","zh":"火星那个总跑去两脚兽家、惹麻烦的年轻学徒外甥叫什么？"},
       "options":[{"en":"Cloudpaw (later Cloudtail)","zh":"Cloudpaw（云爪，后为云尾）"},{"en":"Brightpaw","zh":"Brightpaw（亮爪）"},{"en":"Thornpaw","zh":"Thornpaw（刺爪）"},{"en":"Dustpaw","zh":"Dustpaw（尘爪）"}],
       "answer":0,
       "explain":{"en":"Cloudpaw, Fireheart's nephew, is tempted by the easy life of kittypets and is caught eating Twoleg food.","zh":"云爪是火星的外甥，被宠物猫的安逸生活吸引，还被抓到偷吃两脚兽的食物。"}},
      {"q":{"en":"Why is Graystripe's romance with Silverstream forbidden?","zh":"为什么灰条和银溪的恋情是被禁止的？"},
       "options":[{"en":"Because they are from different Clans","zh":"因为他们来自不同的族群"},{"en":"Because she is a medicine cat","zh":"因为她是个巫医"},{"en":"Because he is a kittypet","zh":"因为他是个宠物猫"},{"en":"Because she is too young","zh":"因为她太年幼"}],
       "answer":0,
       "explain":{"en":"Clan law forbids mating between cats of different Clans; Graystripe is ThunderClan, Silverstream is RiverClan.","zh":"族规禁止不同族群的猫相恋；灰条属雷族，银溪属河族。"}},
      {"q":{"en":"What does Fireheart struggle with because of his loyalty to Graystripe?","zh":"因为对朋友灰条的忠诚，火星陷入什么两难？"},
       "options":[{"en":"Whether to report Graystripe's forbidden love to Bluestar","zh":"是否要把灰条禁忌的恋情报告给蓝星"},{"en":"Whether to leave the Clan","zh":"是否离开族群"},{"en":"Whether to fight Tigerclaw","zh":"是否去和虎掌战斗"},{"en":"Whether to become leader","zh":"是否成为族长"}],
       "answer":0,
       "explain":{"en":"As deputy, Fireheart must decide whether to betray his best friend by reporting his cross-Clan love to Bluestar.","zh":"身为副族长，火星必须在“是否向蓝星告发好友的跨族恋情”之间抉择。"}},
    ]
  },
  {
    "num": "3", "slug": "forest-of-secrets", "title": "Forest of Secrets", "titleZh": "秘密森林",
    "year": 2003, "emoji": "🌲",
    "desc": "Long-held secrets burst into the open — Bluestar's hidden kits, Yellowfang's past, and Tigerclaw's betrayal. 🌲",
    "descZh": "尘封已久的秘密一一揭开——蓝星的私生幼猫、黄牙的过去，以及虎掌的背叛。",
    "questions": [
      {"q":{"en":"What happens to Silverstream, and what kits are born?","zh":"银溪遭遇了什么？哪两只幼猫出生了？"},
       "options":[{"en":"She dies giving birth to Featherkit and Stormkit","zh":"她在生产羽崽和暴崽时死去"},{"en":"She leaves with Graystripe","zh":"她和灰条一起离开了"},{"en":"She becomes a medicine cat","zh":"她成了巫医"},{"en":"She is exiled","zh":"她被流放"}],
       "answer":0,
       "explain":{"en":"Silverstream dies while giving birth; Graystripe brings their two half-Clan kits, Featherkit and Stormkit, to ThunderClan.","zh":"银溪在生产时死去；灰条把两只混族幼猫羽崽和暴崽带回了雷族。"}},
      {"q":{"en":"What terrible injury does Cinderpaw suffer that ends her warrior path?","zh":"Cinderpaw 受了什么伤，断送了她的武士之路？"},
       "options":[{"en":"Hit by a monster (car) on the Thunderpath","zh":"在雷道上被怪兽（汽车）撞伤"},{"en":"Caught in a fox trap","zh":"被狐狸陷阱夹住"},{"en":"Poisoned by a rival","zh":"被对手下毒"},{"en":"Bitten by a dog","zh":"被狗咬伤"}],
       "answer":0,
       "explain":{"en":"Cinderpaw is struck by a monster on the Thunderpath; her leg is ruined and she trains as medicine cat Cinderpelt.","zh":"Cinderpaw 在雷道上被怪兽撞伤，腿废了，于是转而作巫医炭毛。"}},
      {"q":{"en":"Whose kits does Bluestar reveal she secretly gave birth to?","zh":"蓝星透露自己暗中生下的幼猫是谁？"},
       "options":[{"en":"Mistyfoot and Stonefur (with Oakheart of RiverClan)","zh":"雾脚和石毛（与河族橡心所生）"},{"en":"Featherkit and Stormkit","zh":"羽崽和暴崽"},{"en":"Brightheart and Cloudtail","zh":"亮心和云尾"},{"en":"Swiftpaw and Longtail","zh":"捷爪和长尾"}],
       "answer":0,
       "explain":{"en":"Bluestar reveals her kits were fathered by Oakheart of RiverClan and grew up as Mistyfoot and Stonefur of RiverClan.","zh":"蓝星透露她的幼猫是和河族橡心所生，后来作为雾脚和石毛在河族长大。"}},
      {"q":{"en":"Who is Fireheart's kittypet sister whose kit became Cloudtail?","zh":"火星那只家猫姐姐是谁，她的孩子成了云尾？"},
       "options":[{"en":"Princess","zh":"Princess（公主）"},{"en":"Smudge","zh":"Smudge（污点）"},{"en":"Nutmeg","zh":"Nutmeg（肉豆蔻）"},{"en":"Cody","zh":"Cody（科迪）"}],
       "answer":0,
       "explain":{"en":"Princess is Fireheart's sister; she gave one of her kits to Fireheart, who brought Cloudtail into ThunderClan.","zh":"公主是火星的姐姐，她把一只幼猫交给火星，也就是后来被带进雷族的云尾。"}},
      {"q":{"en":"What shocking secret does Yellowfang reveal about Brokenstar?","zh":"黄牙关于碎星，透露了什么惊人的秘密？"},
       "options":[{"en":"She is his mother and killed him to stop his cruelty","zh":"她是碎星的母亲，并杀了他以制止其暴行"},{"en":"He is Bluestar's son","zh":"他是蓝星之子"},{"en":"He was a kittypet","zh":"他曾是宠物猫"},{"en":"He saved the Clan","zh":"他拯救了族群"}],
       "answer":0,
       "explain":{"en":"Yellowfang confesses she is Brokenstar's mother and killed him to end his evil reign over ShadowClan.","zh":"黄牙坦白自己是碎星的母亲，并为了结束他对影族的暴政而杀了他。"}},
      {"q":{"en":"Which Clan does the traitor Tigerclaw (now Tigerstar) lead by this book?","zh":"叛徒虎掌（现为虎星）在本书中统领哪个族群？"},
       "options":[{"en":"ShadowClan","zh":"ShadowClan（影族）"},{"en":"ThunderClan","zh":"ThunderClan（雷族）"},{"en":"RiverClan","zh":"RiverClan（河族）"},{"en":"WindClan","zh":"WindClan（风族）"}],
       "answer":0,
       "explain":{"en":"After being exiled from ThunderClan, Tigerclaw becomes Tigerstar, the leader of ShadowClan.","zh":"被雷族流放后，虎掌成为虎星，当上了影族的族长。"}},
      {"q":{"en":"Who kills Brokenstar, the imprisoned evil former leader?","zh":"谁杀死了被囚禁的邪恶前任族长碎星？"},
       "options":[{"en":"Yellowfang","zh":"Yellowfang（黄牙）"},{"en":"Fireheart","zh":"Fireheart（火星）"},{"en":"Tigerstar","zh":"Tigerstar（虎星）"},{"en":"Graystripe","zh":"Graystripe（灰条）"}],
       "answer":0,
       "explain":{"en":"Yellowfang kills Brokenstar in his prison to stop his plots against the Clans.","zh":"黄牙在囚室里杀死了碎星，以阻止他继续危害各族。"}},
      {"q":{"en":"What does Cinderpaw become after her injury?","zh":"Cinderpaw 受伤后成了什么？"},
       "options":[{"en":"Medicine cat apprentice (Cinderpelt)","zh":"巫医学徒（炭毛）"},{"en":"A warrior","zh":"一名武士"},{"en":"A queen","zh":"一位猫后"},{"en":"An elder","zh":"一位长老"}],
       "answer":0,
       "explain":{"en":"Unable to be a warrior, Cinderpaw trains under Yellowfang and becomes Cinderpelt, ThunderClan's medicine cat.","zh":"无法成为武士的 Cinderpaw 跟随黄牙学习，成为了雷族巫医炭毛。"}},
      {"q":{"en":"Why is this book called 'Forest of Secrets'?","zh":"为什么这本书叫《秘密森林》？"},
       "options":[{"en":"Because many hidden truths come to light (Bluestar's kits, Yellowfang's past, Tigerstar's betrayal)","zh":"因为许多隐藏的真相被揭开（蓝星的幼猫、黄牙的过去、虎星的背叛）"},{"en":"Because it is set in a secret part of the forest","zh":"因为它发生在森林中隐秘的一处"},{"en":"Because the cats hide from Twolegs","zh":"因为猫们在躲避两脚兽"},{"en":"Because of a hidden treasure","zh":"因为有一笔隐藏的宝藏"}],
       "answer":0,
       "explain":{"en":"The book uncovers several long-buried secrets that change the fate of all four Clans.","zh":"本书揭开了几桩埋藏已久的秘密，改变了四大猫族共同的命运。"}},
      {"q":{"en":"What name does Tigerclaw take after leaving ThunderClan and joining ShadowClan?","zh":"虎掌离开雷族、加入影族后，采用了什么名号？"},
       "options":[{"en":"Tigerstar","zh":"Tigerstar（虎星）"},{"en":"Tigerclaw (unchanged)","zh":"仍是 Tigerclaw（虎掌）"},{"en":"Shadowstar","zh":"Shadowstar（影星）"},{"en":"Brokenstar","zh":"Brokenstar（碎星）"}],
       "answer":0,
       "explain":{"en":"He renames himself Tigerstar and becomes the leader of ShadowClan, sharpening his plan against the other Clans.","zh":"他改名虎星，成为影族族长，并加紧策划对付其他族群。"}},
    ]
  },
  {
    "num": "4", "slug": "rising-storm", "title": "Rising Storm", "titleZh": "风暴将临",
    "year": 2003, "emoji": "🌩️",
    "desc": "A lightning fire sweeps the forest, and Bluestar's trust in her Clan begins to crack. 🌩️",
    "descZh": "一道闪电击燃森林大火，蓝星对族群的信任也开始崩塌。",
    "questions": [
      {"q":{"en":"What natural disaster strikes the forest in this book?","zh":"本书中森林遭遇了什么自然灾害？"},
       "options":[{"en":"A forest fire (and later a flood)","zh":"一场森林大火（以及之后的洪水）"},{"en":"An earthquake","zh":"地震"},{"en":"A hurricane","zh":"飓风"},{"en":"Only a long drought","zh":"仅仅是一场久旱"}],
       "answer":0,
       "explain":{"en":"A lightning-sparked forest fire forces ThunderClan to flee; a flood follows the fire.","zh":"闪电引发的森林大火逼雷族撤离，大火之后又来了洪水。"}},
      {"q":{"en":"How does Bluestar's behavior change after the dangers her Clan faces?","zh":"在族群历经危难后，蓝星的行为发生了什么变化？"},
       "options":[{"en":"She becomes paranoid and distrustful of her Clan","zh":"她变得多疑、不信任自己的族群"},{"en":"She becomes kinder","zh":"她变得更仁慈"},{"en":"She leaves the Clan","zh":"她离开了族群"},{"en":"She retires as an elder","zh":"她退为长老"}],
       "answer":0,
       "explain":{"en":"Bluestar loses faith in her Clan and grows suspicious even of her loyal deputy, Fireheart.","zh":"蓝星对族群失去信心，甚至开始怀疑忠诚的副族长火星。"}},
      {"q":{"en":"Who is ThunderClan's medicine cat by this book?","zh":"本书中雷族的巫医是谁？"},
       "options":[{"en":"Cinderpelt","zh":"Cinderpelt（炭毛）"},{"en":"Spottedleaf","zh":"Spottedleaf（斑叶）"},{"en":"Yellowfang","zh":"Yellowfang（黄牙）"},{"en":"Leafpool","zh":"Leafpool（叶池）"}],
       "answer":0,
       "explain":{"en":"After Spottedleaf's death and Yellowfang's passing, Cinderpelt serves as ThunderClan's medicine cat.","zh":"斑叶死后、黄牙也离去，炭毛接任雷族的巫医。"}},
      {"q":{"en":"What rank does Fireheart hold during this book?","zh":"本书中火星担任什么职位？"},
       "options":[{"en":"Deputy","zh":"Deputy（副族长）"},{"en":"Leader","zh":"Leader（族长）"},{"en":"Warrior","zh":"Warrior（武士）"},{"en":"Medicine cat","zh":"Medicine cat（巫医）"}],
       "answer":0,
       "explain":{"en":"Fireheart serves as Bluestar's deputy throughout the crisis.","zh":"在整个危机中，火星一直担任蓝星的副族长。"}},
      {"q":{"en":"Which she-cat grows close to Fireheart and later becomes his mate?","zh":"哪只母猫逐渐与火星亲近，后来成为他的伴侣？"},
       "options":[{"en":"Sandstorm","zh":"Sandstorm（沙暴）"},{"en":"Spottedleaf","zh":"Spottedleaf（斑叶）"},{"en":"Cinderpelt","zh":"Cinderpelt（炭毛）"},{"en":"Frostfur","zh":"Frostfur（霜毛）"}],
       "answer":0,
       "explain":{"en":"Sandstorm and Fireheart's bond deepens across these books; she becomes his mate and close partner.","zh":"沙暴与火星的感情在几本书中逐渐加深，后来成了他的伴侣。"}},
      {"q":{"en":"What caused the great fire that threatened the Clans?","zh":"威胁族群的这场大火是由什么引起的？"},
       "options":[{"en":"A lightning strike during a storm","zh":"风暴中的一道闪电击中"},{"en":"Twolegs on purpose","zh":"两脚兽故意纵火"},{"en":"Tigerstar's trap","zh":"虎星的陷阱"},{"en":"A volcano","zh":"火山"}],
       "answer":0,
       "explain":{"en":"Lightning from the rising storm ignites the forest, giving the book its name.","zh":"风暴中的闪电点燃了森林，这也正是书名《风暴将临》的由来。"}},
      {"q":{"en":"After the fire, what second disaster hits the forest?","zh":"大火之后，森林又遭遇了什么二次灾难？"},
       "options":[{"en":"A flood","zh":"一场洪水"},{"en":"A blizzard","zh":"一场暴风雪"},{"en":"Another fire","zh":"又一场大火"},{"en":"A drought","zh":"一场旱灾"}],
       "answer":0,
       "explain":{"en":"Heavy rain after the fire swells the river and floods the low parts of the forest.","zh":"大火过后暴雨倾盆，河水上涨，淹没了森林低洼处。"}},
      {"q":{"en":"Which Clan does Tigerstar now lead and threaten the others with?","zh":"虎星此时统领并用来威胁其他族群的，是哪个族群？"},
       "options":[{"en":"ShadowClan","zh":"ShadowClan（影族）"},{"en":"ThunderClan","zh":"ThunderClan（雷族）"},{"en":"RiverClan","zh":"RiverClan（河族）"},{"en":"WindClan","zh":"WindClan（风族）"}],
       "answer":0,
       "explain":{"en":"Tigerstar rules ShadowClan and begins plotting to dominate the other three Clans.","zh":"虎星统治着影族，并开始图谋吞并其他三个族群。"}},
      {"q":{"en":"What threat begins to appear at the edges of the territory by the end of the book?","zh":"到本书结尾，领地边缘开始出现什么威胁？"},
       "options":[{"en":"A pack of dogs","zh":"一群狗"},{"en":"A fox","zh":"一只狐狸"},{"en":"BloodClan","zh":"BloodClan（血族）"},{"en":"Twolegs","zh":"两脚兽"}],
       "answer":0,
       "explain":{"en":"Tigerstar begins gathering a pack of dogs to use against ThunderClan — the danger fully erupts in the next book.","zh":"虎星开始纠集一群狗来对付雷族——危机在下一本书中全面爆发。"}},
      {"q":{"en":"How does Bluestar treat Fireheart, her loyal deputy, as her paranoia grows?","zh":"随着蓝星愈发多疑，她如何对待忠诚的副族长火星？"},
       "options":[{"en":"She distrusts him and questions his loyalty","zh":"她不信任他，质疑他的忠诚"},{"en":"She promotes him","zh":"她提拔了他"},{"en":"She makes him leader","zh":"她让他当族长"},{"en":"She ignores him","zh":"她无视他"}],
       "answer":0,
       "explain":{"en":"Convinced the Clan has betrayed her, Bluestar turns on even Fireheart, the cat most loyal to her.","zh":"蓝星认定族群背叛了自己，连最忠诚的火星也遭到了她的猜忌。"}},
    ]
  },
  {
    "num": "5", "slug": "a-dangerous-path", "title": "A Dangerous Path", "titleZh": "险路惊魂",
    "year": 2003, "emoji": "⚠️",
    "desc": "Tigerstar unleashes a dog pack on ThunderClan — and Bluestar makes the ultimate sacrifice. ⚠️",
    "descZh": "虎星放出狗群扑向雷族——而蓝星做出了最崇高的牺牲。",
    "questions": [
      {"q":{"en":"What does Tigerstar use to try to destroy ThunderClan?","zh":"虎星利用什么来试图摧毁雷族？"},
       "options":[{"en":"A pack of dogs","zh":"一群狗"},{"en":"A flood","zh":"一场洪水"},{"en":"A fire","zh":"一场火"},{"en":"BloodClan","zh":"BloodClan（血族）"}],
       "answer":0,
       "explain":{"en":"Tigerstar lures a pack of dogs into ThunderClan's territory with a trail of prey, planning to wipe out the Clan.","zh":"虎星用一串猎物把狗群引向雷族领地，企图灭掉整个族群。"}},
      {"q":{"en":"How does Bluestar save her Clan from the dogs?","zh":"蓝星是如何从狗群手中拯救族群的？"},
       "options":[{"en":"She leads the dogs over the cliff into the gorge, sacrificing herself","zh":"她把狗群引下悬崖坠入峡谷，牺牲了自己"},{"en":"She fights them all alone and wins","zh":"她独自战胜了所有狗"},{"en":"She asks RiverClan for help","zh":"她向河族求援"},{"en":"She traps them in a cave","zh":"她把它们困进洞穴"}],
       "answer":0,
       "explain":{"en":"Bluestar leads the dog pack over the edge of the gorge, dying to save ThunderClan.","zh":"蓝星把狗群引下峡谷悬崖，为拯救雷族而牺牲。"}},
      {"q":{"en":"What new rank does Fireheart receive after Bluestar's death?","zh":"蓝星死后，火星获得了什么新职位？"},
       "options":[{"en":"Leader (Firestar)","zh":"Leader（Firestar 火星）"},{"en":"Deputy","zh":"Deputy（副族长）"},{"en":"Warrior","zh":"Warrior（武士）"},{"en":"Elder","zh":"Elder（长老）"}],
       "answer":0,
       "explain":{"en":"Fireheart becomes Firestar, the new leader of ThunderClan.","zh":"Fireheart 成为雷族新任族长——火星（Firestar）。"}},
      {"q":{"en":"Who becomes Firestar's mate / close partner?","zh":"谁成了 Firestar 的伴侣／亲密伙伴？"},
       "options":[{"en":"Sandstorm","zh":"Sandstorm（沙暴）"},{"en":"Cinderpelt","zh":"Cinderpelt（炭毛）"},{"en":"Spottedleaf","zh":"Spottedleaf（斑叶）"},{"en":"Mistyfoot","zh":"Mistyfoot（雾脚）"}],
       "answer":0,
       "explain":{"en":"Sandstorm stands beside Firestar and becomes his mate after he takes leadership.","zh":"在火星成为族长后，沙暴一直陪伴在他身边，成为他的伴侣。"}},
      {"q":{"en":"What does Firestar receive as the new leader of ThunderClan?","zh":"作为雷族新族长，Firestar 获得了什么？"},
       "options":[{"en":"Nine lives and a new name from StarClan","zh":"来自星族的九条命和新名字"},{"en":"A magic stone","zh":"一块魔法石"},{"en":"A tail of nine tails","zh":"九条尾巴"},{"en":"A crown","zh":"一顶王冠"}],
       "answer":0,
       "explain":{"en":"Like all leaders, Firestar receives nine lives and his leader name from StarClan.","zh":"和所有族长一样，火星从星族那里获得了九条命和族长之名。"}},
      {"q":{"en":"Where does Tigerstar set his deadly trap for the Clan and the dogs?","zh":"虎星把致命陷阱设在了哪里（对付族群和狗）？"},
       "options":[{"en":"At the gorge (a dead-end cliff)","zh":"在峡谷（一条死路悬崖）"},{"en":"In the river","zh":"在河里"},{"en":"In the camp","zh":"在营地里"},{"en":"In Twolegplace","zh":"在两脚兽地盘"}],
       "answer":0,
       "explain":{"en":"Tigerstar leads the dogs to a gorge that ends in a cliff, intending to wipe out ThunderClan — but Bluestar turns the trap on the dogs.","zh":"虎星把狗群引到尽头是悬崖的峡谷，想灭掉雷族——但蓝星将这陷阱反作用于狗群。"}},
      {"q":{"en":"Who leads RiverClan at this time?","zh":"此时的河族族长是谁？"},
       "options":[{"en":"Leopardstar","zh":"Leopardstar（豹星）"},{"en":"Crookedstar","zh":"Crookedstar（曲星）"},{"en":"Mistyfoot","zh":"Mistyfoot（雾脚）"},{"en":"Tigerstar","zh":"Tigerstar（虎星）"}],
       "answer":0,
       "explain":{"en":"Crookedstar has died (in the flood of the previous book), so Leopardstar now leads RiverClan.","zh":"曲星已死（死于上一本的洪水），此时由豹星统领河族。"}},
      {"q":{"en":"How does Tigerstar escape after the dog plan fails?","zh":"狗群计划失败后，虎星如何脱身？"},
       "options":[{"en":"He flees to gather more cats (BloodClan) for a bigger war","zh":"他逃走，去纠集更多猫（血族）准备更大的战争"},{"en":"He becomes a kittypet","zh":"他成了宠物猫"},{"en":"He dies","zh":"他死了"},{"en":"He joins WindClan","zh":"他加入了风族"}],
       "answer":0,
       "explain":{"en":"Tigerstar survives and later forms 'TigerClan' with BloodClan, setting up the final battle in book 6.","zh":"虎星活了下来，后来联合血族组成“虎族”，为第六本的决战埋下伏笔。"}},
      {"q":{"en":"What emotion drives Bluestar's dangerous choices in this book?","zh":"是什么情绪驱使蓝星在本书中做出危险的抉择？"},
       "options":[{"en":"Paranoia that StarClan and her Clan betrayed her","zh":"她认定星族和族群背叛了自己的偏执"},{"en":"Greed for power","zh":"对权力的贪婪"},{"en":"Love for Tigerstar","zh":"对虎星的爱"},{"en":"Fear of water","zh":"对水的恐惧"}],
       "answer":0,
       "explain":{"en":"Bluestar's growing belief that everyone has betrayed her leads her to make reckless, dangerous decisions.","zh":"蓝星越来越坚信所有人都背叛了她，这让她做出了鲁莽而危险的决断。"}},
      {"q":{"en":"What title does Fireheart take when he becomes leader?","zh":"火星成为族长时，采用了什么名号？"},
       "options":[{"en":"Firestar","zh":"Firestar（火星）"},{"en":"Fireheart (unchanged)","zh":"仍是 Fireheart（火星）"},{"en":"Flameleader","zh":"Flameleader（焰领导）"},{"en":"Emberstar","zh":"Emberstar（余烬星）"}],
       "answer":0,
       "explain":{"en":"As leader he takes the name Firestar, keeping the 'fire' of the prophecy that began his journey.","zh":"成为族长后他取名 Firestar，延续了开启他旅程的那道“火”的预言。"}},
    ]
  },
  {
    "num": "6", "slug": "the-darkest-hour", "title": "The Darkest Hour", "titleZh": "黑暗时刻",
    "year": 2003, "emoji": "🌑",
    "desc": "Tigerstar unites the Clans under 'TigerClan' with BloodClan's Scourge — and Firestar faces his darkest hour. 🌑",
    "descZh": "虎星联合血族长鞭，把各族统一到“虎族”旗下——火星迎来了最黑暗的时刻。",
    "questions": [
      {"q":{"en":"What ruthless cat from the city (Twolegplace) leads BloodClan?","zh":"来自城市（两脚兽地盘）、统领血族的冷酷猫是谁？"},
       "options":[{"en":"Scourge","zh":"Scourge（长鞭）"},{"en":"Bone","zh":"Bone（骨头）"},{"en":"Sasha","zh":"Sasha（萨莎）"},{"en":"Barley","zh":"Barley（大麦）"}],
       "answer":0,
       "explain":{"en":"Scourge is the small but deadly leader of BloodClan, a gang of city cats.","zh":"长鞭是血族（一群城市猫）的领袖，个头虽小却极其致命。"}},
      {"q":{"en":"How does Tigerstar die in this book?","zh":"本书中虎星是怎么死的？"},
       "options":[{"en":"Scourge kills him with one blow, taking all nine lives","zh":"长鞭一击杀了他，夺走全部九条命"},{"en":"Firestar kills him","zh":"火星杀了他"},{"en":"He falls in the gorge","zh":"他坠入峡谷"},{"en":"A dog kills him","zh":"一只狗杀了他"}],
       "answer":0,
       "explain":{"en":"Scourge, betrayed by Tigerstar, slits his throat and ends all nine of his lives at once.","zh":"被虎星背叛的长鞭割开他的喉咙，一次性夺走了他的九条命。"}},
      {"q":{"en":"What false sign does Tigerstar use to unite ShadowClan and RiverClan under him?","zh":"虎星用什么样的假象把影族和河族统一到自己麾下？"},
       "options":[{"en":"A fake omen / 'TigerClan' prophecy","zh":"一个伪造的预兆／“虎族”预言"},{"en":"A gift of prey","zh":"一份猎物礼物"},{"en":"A threat of fire","zh":"火灾威胁"},{"en":"A magic stone","zh":"一块魔法石"}],
       "answer":0,
       "explain":{"en":"Tigerstar forges a sign to convince the other Clans to merge into 'TigerClan' under his rule.","zh":"虎星伪造了一个预兆，诱使其他族群合并到他统治的“虎族”之下。"}},
      {"q":{"en":"Which Clans stand against Tigerstar's TigerClan?","zh":"哪两个族群站在虎星的“虎族”对立面？"},
       "options":[{"en":"ThunderClan and WindClan","zh":"雷族与风族"},{"en":"RiverClan and ShadowClan","zh":"河族与影族"},{"en":"BloodClan and SkyClan","zh":"血族与天族"},{"en":"All four against him","zh":"四大族群都反对他"}],
       "answer":0,
       "explain":{"en":"Firestar's ThunderClan and Tallstar's WindClan refuse to join TigerClan.","zh":"火星的雷族和高星的风族拒绝加入虎族。"}},
      {"q":{"en":"What does Scourge do to the Clans after killing Tigerstar?","zh":"长鞭杀死虎星后，对各族做了什么？"},
       "options":[{"en":"Demands the forest and attacks ThunderClan","zh":"要求占领森林并进攻雷族"},{"en":"Makes peace","zh":"讲和"},{"en":"Leaves the forest","zh":"离开森林"},{"en":"Joins StarClan","zh":"加入星族"}],
       "answer":0,
       "explain":{"en":"Scourge turns on all the Clans, demanding the forest for BloodClan and triggering the final battle.","zh":"长鞭转而对付所有族群，要求把森林交给血族，由此引发了最终决战。"}},
      {"q":{"en":"In the final battle, what happens to Firestar?","zh":"在最终决战中，火星遭遇了什么？"},
       "options":[{"en":"He is badly wounded and loses one of his nine lives","zh":"他身受重伤，失去九条命中的一条"},{"en":"He dies forever","zh":"他永远死了"},{"en":"He runs away","zh":"他逃跑了"},{"en":"He is unharmed","zh":"他毫发无伤"}],
       "answer":0,
       "explain":{"en":"Scourge's dog-tooth claws take one of Firestar's nine lives; he fights on.","zh":"长鞭用狗牙加固的爪子夺走了火星九条命中的一条；但他继续战斗。"}},
      {"q":{"en":"How does Firestar defeat Scourge?","zh":"火星是如何击败长鞭的？"},
       "options":[{"en":"He kills Scourge in the final duel","zh":"他在最终对决中杀死了长鞭"},{"en":"Scourge slips and falls","zh":"长鞭滑倒坠崖"},{"en":"StarClan saves him","zh":"星族救了他"},{"en":"Graystripe kills Scourge","zh":"灰条杀了长鞭"}],
       "answer":0,
       "explain":{"en":"Firestar strikes the killing blow against Scourge in the heart of the battle.","zh":"火星在战斗最激烈时给了长鞭致命一击。"}},
      {"q":{"en":"What is special about Scourge's claws?","zh":"长鞭的爪子有什么特别之处？"},
       "options":[{"en":"They are reinforced with dog teeth","zh":"用狗牙加固过"},{"en":"They are made of stone","zh":"由石头做成"},{"en":"They glow","zh":"会发光"},{"en":"They are poisonous","zh":"有毒"}],
       "answer":0,
       "explain":{"en":"Scourge fits his claws with sharpened dog teeth, making every scratch lethal.","zh":"长鞭把磨利的狗牙嵌在爪上，使每一爪都致命。"}},
      {"q":{"en":"Which friend fights loyally beside Firestar in the battle?","zh":"哪一位朋友在战斗中忠心地在火星身边并肩作战？"},
       "options":[{"en":"Graystripe","zh":"Graystripe（灰条）"},{"en":"Tigerstar","zh":"Tigerstar（虎星）"},{"en":"Scourge","zh":"Scourge（长鞭）"},{"en":"Brokenstar","zh":"Brokenstar（碎星）"}],
       "answer":0,
       "explain":{"en":"Graystripe stands by Firestar through the war, as he has since they were apprentices.","zh":"灰条从学徒时代起就与火星并肩，这场大战中也不例外。"}},
      {"q":{"en":"What is the outcome for the four Clans after the Darkest Hour?","zh":"黑暗时刻之后，四大猫族的结局是什么？"},
       "options":[{"en":"They survive and remain in the forest under Firestar's leadership","zh":"它们幸存下来，在火星的领导下继续留在森林"},{"en":"They scatter and leave","zh":"它们四散离去"},{"en":"BloodClan rules","zh":"血族统治森林"},{"en":"The forest is destroyed","zh":"森林被毁"}],
       "answer":0,
       "explain":{"en":"ThunderClan, led by Firestar, survives; the Clans keep their forest home and peace returns.","zh":"在火星的带领下，雷族得以幸存；各族保住了森林家园，和平重现。"}},
    ]
  },
]


def slugify(title):
    t = title.lower()
    t = re.sub(r'^the\s+', '', t)
    t = re.sub(r"[^a-z0-9]+", '-', t).strip('-')
    return t


def gen_data():
    os.makedirs(DATA, exist_ok=True)
    for b in BOOKS:
        rec = {
            "num": b["num"],
            "slug": b["slug"],
            "title": b["title"],
            "titleZh": b["titleZh"],
            "year": b["year"],
            "emoji": b["emoji"],
            "arc": ARC,
            "arcZh": ARC_ZH,
            "desc": b["desc"],
            "descZh": b["descZh"],
            "source": "warriors-plot",
            "questions": b["questions"],
        }
        out = os.path.join(DATA, b["slug"] + ".json")
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=2)
    print(f"  [OK] wrote {len(BOOKS)} JSON records to _quizdata/")


def gen_quizzes():
    count = 0
    for b in BOOKS:
        accent = ACCENT.get(b["num"], "#2f5d3a")
        quiz_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 猫武士 Quiz</title>
<style>
__CSS__
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="topbar">
      <button class="langBtn" id="langBtn">🌐 中文</button>
      <h1>__TITLE__</h1>
      <a class="homeBtn" href="../../index.html" title="Home / 首页" aria-label="Home">🏠</a>
    </div>
    <p id="subtitle">Comprehension Quiz • 10 Questions • by Erin Hunter</p>
    <p class="bookzh">__TITLEZH__</p>
    <div class="mark">__EMOJI__</div>
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
  <footer>Based on <em>Warriors: __ARC__ — __TITLE__</em> (HarperCollins, __YEAR__)</footer>
</div>

<script>
__JS__
</script>
</body>
</html>"""

        quiz_html = (quiz_html
                     .replace("__TITLE__", b["title"])
                     .replace("__TITLEZH__", b["titleZh"])
                     .replace("__EMOJI__", b["emoji"])
                     .replace("__ARC__", ARC)
                     .replace("__YEAR__", str(b["year"]))
                     .replace("__CSS__", QUIZ_CSS)
                     .replace("__JS__", QUIZ_JS_BODY)
                     .replace("__QUIZJSON__", json.dumps(b["questions"], ensure_ascii=False)))

        out_name = f"{b['slug']}-quiz.html"
        with open(os.path.join(BASE, out_name), "w", encoding="utf-8") as fh:
            fh.write(quiz_html)
        count += 1
        print(f"  [OK] {b['num']} -> {out_name}")
    print(f"\n=== gen_quizzes: wrote {count} quiz pages ===")


def gen_hub():
    cards = []
    for b in BOOKS:
        accent = ACCENT.get(b["num"], "#2f5d3a")
        cards.append(f"""    <article class="book" style="--accent:{accent}">
      <div class="top"><div class="letter">{b['num']}</div><div class="emoji">{b['emoji']}</div></div>
      <div class="body">
        <h3 class="title">{b['title']}</h3>
        <p class="titleZh">{b['titleZh']}</p>
        <p class="desc">{b['desc']}</p>
        <a class="start" href="{b['slug']}-quiz.html">做测验 Take Quiz →</a>
      </div>
    </article>""")

    count = len(BOOKS)

    hub = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Warriors · 猫武士 — The Prophecy Begins</title>
<style>
  :root{
    --forest:#2f5d3a;
    --forest-dark:#1e3f27;
    --ember:#d35400;
    --cream:#fbf7ee;
    --ink:#2a2118;
    --gold:#e0a82e;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    font-family:"Trebuchet MS","Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
    background:linear-gradient(160deg,var(--forest),var(--forest-dark));
    color:var(--ink);min-height:100vh;padding:0 0 40px;
  }
  header{
    background:var(--ember);color:#fff;text-align:center;
    padding:26px 18px 20px;position:relative;
  }
  .topbar{display:flex;align-items:center;justify-content:space-between;gap:10px;}
  .topbar h1{margin:0;font-size:1.5rem;flex:1;text-align:center;}
  .homeBtn{
    font-size:1.35rem;text-decoration:none;background:#fff;border-radius:50%;
    width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;
    box-shadow:0 2px 8px rgba(0,0,0,.2);transition:transform .12s;
  }
  .homeBtn:hover{transform:translateY(-1px);}
  header p{margin:10px 0 0;font-size:.92rem;opacity:.94;}
  header .arc{font-weight:bold;letter-spacing:1px;}
  .wrap{max-width:1000px;margin:26px auto 0;padding:0 18px;}
  .intro{
    background:var(--cream);border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.3);
    padding:18px 22px;font-size:.95rem;line-height:1.6;color:#444;
  }
  .intro b{color:var(--forest-dark);}
  .grid{
    margin-top:22px;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;
  }
  .book{
    background:var(--cream);border-radius:16px;overflow:hidden;
    box-shadow:0 8px 20px rgba(0,0,0,.28);
    display:flex;flex-direction:column;border-top:6px solid var(--accent,var(--forest));
    transition:transform .15s,box-shadow .15s;
  }
  .book:hover{transform:translateY(-4px);box-shadow:0 12px 26px rgba(0,0,0,.34);}
  .book .top{padding:16px;text-align:center;background:linear-gradient(180deg,var(--accent,#2f5d3a),transparent);}
  .letter{
    width:54px;height:54px;line-height:54px;border-radius:50%;background:#fff;
    color:var(--accent,#2f5d3a);font-size:1.5rem;font-weight:bold;margin:0 auto 8px;
    box-shadow:0 4px 10px rgba(0,0,0,.2);
  }
  .book .emoji{font-size:1.7rem;}
  .book .title{margin:4px 0;font-size:1.05rem;font-weight:bold;line-height:1.3;padding:0 12px;}
  .book .titleZh{margin:0 0 6px;font-size:.85rem;color:#a06a1f;text-align:center;font-weight:bold;}
  .book .body{padding:6px 14px 16px;flex:1;display:flex;flex-direction:column;}
  .book .desc{font-size:.82rem;color:#555;line-height:1.45;margin:0 0 12px;flex:1;padding:0 6px;}
  .start{
    display:block;text-align:center;text-decoration:none;font-family:inherit;
    font-size:.95rem;font-weight:bold;color:#fff;background:var(--accent,#2f5d3a);
    padding:10px;border-radius:30px;box-shadow:0 4px 12px rgba(0,0,0,.2);transition:filter .15s;
  }
  .start:hover{filter:brightness(1.08);}
  footer{text-align:center;color:rgba(255,255,255,.85);font-size:.8rem;margin-top:32px;}
</style>
</head>
<body>
<header>
  <div class="topbar">
    <a class="homeBtn" href="../../index.html" title="Home / 首页" aria-label="Home">🏠</a>
    <h1>Warriors · 猫武士</h1>
    <span style="width:40px"></span>
  </div>
  <p class="arc">The Prophecy Begins · 预言开始</p>
  <p>中章书 · Middle Chapter Books — by Erin Hunter</p>
</header>

<div class="wrap">
  <div class="intro">
    🐾 <b>{count} 本《猫武士·预言开始》中英双语阅读理解测验。</b><br>
    {count} bilingual (English / 中文) comprehension quizzes for the first arc of Warriors. Pick a book, answer 10 questions, then check your answers!
  </div>

  <div class="grid">
{CARDS}
  </div>
</div>

<footer>Part of 分级阅读乐园 · Reading by Level</footer>
</body>
</html>
"""
    hub = (hub.replace("{count}", str(count))
              .replace("{CARDS}", "\n".join(cards)))

    out = os.path.join(BASE, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(hub)
    print(f"\n=== gen_hub: wrote index.html with {count} books ===")


if __name__ == "__main__":
    gen_data()
    gen_quizzes()
    gen_hub()
    print("Done.")
