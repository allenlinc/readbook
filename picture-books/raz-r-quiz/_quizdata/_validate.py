# -*- coding: utf-8 -*-
import json, os

OUT = r"D:\AI\readbook\raz-r-quiz\_quizdata"
SKILLS = {"Key Ideas and Details", "Craft and Structure",
          "Integration of Knowledge and Ideas", "Author's Purpose and Perspective"}

my_slugs = ["how-the-robin-stole-fire", "hillary-clinton", "hansel-and-gretel",
            "hiking-the-appalachian-trail", "golf", "going-to-the-super-bowl",
            "ghost-towns", "glow-in-the-dark-animals", "foods-around-the-world",
            "george-washington-carver"]

ok = True
for slug in my_slugs:
    fp = os.path.join(OUT, slug + ".json")
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    errs = []
    for k in ["slug", "title", "titleZh", "level", "genre", "mainSkill", "questions", "extended"]:
        if k not in d:
            errs.append("missing key " + k)
    if d.get("level") != "R":
        errs.append("level not R")
    if d.get("mainSkill") not in SKILLS:
        errs.append("bad mainSkill")
    if d.get("slug") != slug:
        errs.append("slug mismatch")
    qs = d.get("questions", [])
    if len(qs) != 10:
        errs.append("questions != 10: %d" % len(qs))
    skill_counts = {}
    for i, q in enumerate(qs):
        if len(q.get("options", [])) != 4:
            errs.append("Q%d options != 4" % (i+1))
        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a <= 3):
            errs.append("Q%d answer not int 0-3: %r" % (i+1, a))
        if q.get("skill") not in SKILLS:
            errs.append("Q%d bad skill" % (i+1))
        for fld in ["q", "explain"]:
            for lang in ["en", "zh"]:
                v = q.get(fld, {}).get(lang, "")
                if not isinstance(v, str) or v.strip() == "":
                    errs.append("Q%d %s.%s empty" % (i+1, fld, lang))
        opts = q.get("options", [])
        for oi, opt in enumerate(opts):
            for lang in ["en", "zh"]:
                v = opt.get(lang, "")
                if not isinstance(v, str) or v.strip() == "":
                    errs.append("Q%d opt%d.%s empty" % (i+1, oi, lang))
        # check answer points to a valid option with content
        if isinstance(a, int) and 0 <= a < len(opts):
            # ensure correct option text is non-empty (already checked)
            pass
        skill_counts[q.get("skill")] = skill_counts.get(q.get("skill"), 0) + 1
    ext = d.get("extended", {})
    for fld in ["prompt", "guidance"]:
        if fld not in ext:
            errs.append("extended missing " + fld)
    for lang in ["en", "zh"]:
        if ext.get("prompt", {}).get(lang, "").strip() == "":
            errs.append("extended.prompt.%s empty" % lang)
        g = ext.get("guidance", {}).get(lang, [])
        if not isinstance(g, list) or len([x for x in g if isinstance(x, str) and x.strip()]) < 1:
            errs.append("extended.guidance.%s bad" % lang)
    if len(skill_counts) != 4:
        errs.append("skills not all 4 used: %s" % skill_counts)
    status = "OK" if not errs else "FAIL"
    if errs:
        ok = False
    print("%-32s %s  skills=%s" % (slug, status, skill_counts))
    for e in errs:
        print("   -", e)
print("\nALL 10 VALID" if ok else "\nSOME FAILED")
