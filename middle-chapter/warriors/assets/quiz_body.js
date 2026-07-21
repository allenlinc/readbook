let lang = "en";
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

render();