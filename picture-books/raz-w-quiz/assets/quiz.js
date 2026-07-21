/* RAZ-O quiz engine — reads window.BOOK, renders an interactive Quick Check. */
(function () {
  "use strict";
  var B = window.BOOK;
  if (!B) { document.getElementById("app").textContent = "No quiz data."; return; }
  var SKILLS = ["Key Ideas and Details", "Craft and Structure",
                "Integration of Knowledge and Ideas", "Author's Purpose and Perspective"];
  var state = [];           // selected index per question, or null
  var answered = 0;

  // Ensure a language mode is active (guard against any stale cached HTML).
  if (!document.body.classList.contains("lang-en") &&
      !document.body.classList.contains("lang-zh")) {
    document.body.classList.add("lang-en");
  }

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  // Render one bilingual line: English in .en, Chinese in .zh (one shown per mode).
  function line(en, zh, cls) {
    var h = '<div class="' + (cls || "txt") + '">';
    h += '<span class="en">' + esc(en) + "</span>";
    if (zh) h += '<span class="zh">' + esc(zh) + "</span>";
    return h + "</div>";
  }
  // Inline bilingual snippet (for headings / buttons).
  function bi(en, zh) {
    return '<span class="en">' + esc(en) + '</span><span class="zh">' + esc(zh) + "</span>";
  }

  function render() {
    var app = document.getElementById("app");
    var qn = B.questions || [];
    var html = "";

    // ---- hero ----
    html += '<div class="hero">' +
      '<div class="lvl"><b>' + esc(B.level || "O") + '</b><span>LEVEL</span></div>' +
      '<div><h1><span class="en">' + esc(B.title) + "</span>" +
      (B.titleZh ? '<span class="zh">' + esc(B.titleZh) + "</span>" : "") + "</h1>" +
      '<div class="tags">' +
        (B.genre ? '<span class="tag">' + esc(B.genre) + "</span>" : "") +
        (B.mainSkill ? '<span class="tag">' + esc(B.mainSkill) + "</span>" : "") +
        '<span class="tag">' + bi("10 Q", "10 题") + "</span>" +
      "</div></div>";

    // ---- questions ----
    html += '<div id="qs">';
    qn.forEach(function (q, i) {
      var chosen = state[i];
      var isAns = chosen !== null && chosen !== undefined;
      var correct = q.answer;
      html += '<div class="q" data-i="' + i + '">';
      html += '<div class="stem"><span class="num">' + (i + 1) + "</span>" +
              line(q.q.en, q.q.zh) + "</div>";
      html += '<div class="opts">';
      (q.options || []).forEach(function (o, j) {
        var cls = "opt";
        if (isAns) {
          cls += " locked";
          if (j === correct) cls += " correct";
          else if (j === chosen) cls += " wrong";
        }
        var letter = String.fromCharCode(65 + j);
        html += '<button class="' + cls + '" data-j="' + j + '">' +
                '<span class="mk">' + letter + "</span>" +
                line(o.en, o.zh) + "</button>";
      });
      html += "</div>";
      // feedback
      var fbShow = isAns ? " show" : "";
      var fbSkill = q.skill ? q.skill : "";
      var ex = q.explain || {};
      html += '<div class="feedback' + fbShow + '">' +
        (fbSkill ? '<span class="skill">' + esc(fbSkill) + "</span>" : "") +
        line((ex.en || ""), (ex.zh || ""), "exp") + "</div>";
      html += "</div>";
    });
    html += "</div>";

    // ---- extended response ----
    if (B.extended && B.extended.prompt) {
      var ep = B.extended.prompt, gd = B.extended.guidance || {};
      html += '<div class="ext"><h3>💡 ' + bi("Extended Response", "思考题") + "</h3>" +
        line(ep.en, ep.zh, "ep");
      if (ep.en) html += '<textarea placeholder="✍️"></textarea>';
      if (gd.en || gd.zh) {
        html += "<details><summary>" + bi("Reference points", "参考要点") + "</summary>" +
          line(gd.en || "", gd.zh || "", "gd") + "</details>";
      }
      html += "</div>";
    }

    // ---- summary ----
    html += '<div class="summary" id="sum"></div>';

    app.innerHTML = html;
    wire();
    if (answered === qn.length) showSummary();
  }

  function wire() {
    var qs = document.getElementById("qs");
    if (!qs) return;
    qs.querySelectorAll(".q").forEach(function (qel) {
      var i = +qel.getAttribute("data-i");
      qel.querySelectorAll(".opt").forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (state[i] !== null && state[i] !== undefined) return; // already answered
          var j = +btn.getAttribute("data-j");
          state[i] = j;
          answered++;
          // update classes on this question's options
          var opts = qel.querySelectorAll(".opt");
          var correct = B.questions[i].answer;
          opts.forEach(function (o, k) {
            o.classList.add("locked");
            if (k === correct) o.classList.add("correct");
            else if (k === j) o.classList.add("wrong");
          });
          qel.querySelector(".feedback").classList.add("show");
          if (answered === B.questions.length) showSummary();
        });
      });
    });
  }

  function showSummary() {
    var sum = document.getElementById("sum");
    if (!sum) return;
    var qn = B.questions, total = qn.length, correct = 0;
    qn.forEach(function (q, i) { if (state[i] === q.answer) correct++; });

    // per-skill breakdown
    var bySkill = {};
    qn.forEach(function (q, i) {
      var s = q.skill || "Other";
      if (!bySkill[s]) bySkill[s] = { tot: 0, ok: 0 };
      bySkill[s].tot++;
      if (state[i] === q.answer) bySkill[s].ok++;
    });
    var br = '<div class="breakdown">';
    Object.keys(bySkill).forEach(function (s) {
      var d = bySkill[s];
      var pct = d.tot ? Math.round(d.ok / d.tot * 100) : 0;
      br += '<div class="br"><span class="name">' + esc(s) + '</span>' +
        '<span class="bar"><i style="width:' + pct + '%"></i></span>' +
        '<span class="val">' + d.ok + "/" + d.tot + "</span></div>";
    });
    br += "</div>";

    var msgEn = correct === total ? "Perfect!" : correct >= total * 0.6 ? "Good job!" : "Keep practicing!";
    var msgZh = correct === total ? "太棒了！" : correct >= total * 0.6 ? "做得不错！" : "再练练！";
    sum.innerHTML = "<h2>" + bi(msgEn, msgZh) + "</h2>" +
      '<div class="score">' + correct + "<small> / " + total + "</small></div>" +
      "<p style='color:var(--muted);margin:6px 0 0'>" + bi("Your score", "你的得分") + "</p>" +
      br +
      '<button class="restart" id="restart">🔄 ' + bi("Restart", "重新开始") + "</button>";
    sum.classList.add("show");
    document.getElementById("restart").addEventListener("click", function () {
      state = []; answered = 0; sum.classList.remove("show"); render();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    sum.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  // language toggle: EN only  <->  中文 only  (default EN, set on <body> by build.py)
  var lb = document.getElementById("langBtn");
  if (lb) lb.addEventListener("click", function () {
    var zh = document.body.classList.toggle("lang-zh");
    document.body.classList.toggle("lang-en", !zh);
    lb.textContent = zh ? "🌐 中文" : "🌐 EN";
  });

  render();
})();
