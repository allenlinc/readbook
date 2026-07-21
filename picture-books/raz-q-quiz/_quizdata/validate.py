#!/usr/bin/env python3
# Validate raz-q-quiz JSON files. Usage:
#   python validate.py                 -> check every *.json in this folder
#   python validate.py file.json ...  -> check given files
# Prints PASS/FAIL per file with reasons. Exits non-zero if any FAIL.
import json, os, sys, glob

SKILLS = {
    "Key Ideas and Details", "Craft and Structure",
    "Integration of Knowledge and Ideas", "Author's Purpose and Perspective",
    "Other",
}
VALID = True

def err(b, msg):
    global VALID
    VALID = False
    print("  FAIL:", msg)

def check(path):
    try:
        b = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print("FAIL  %s -> JSON error: %s" % (os.path.basename(path), e)); global VALID; VALID=False; return
    slug = os.path.splitext(os.path.basename(path))[0]
    if b.get("slug") != slug:
        err(b, "slug %r != filename %r" % (b.get("slug"), slug))
    for k in ("slug","title","level","genre","mainSkill"):
        if not b.get(k): err(b, "missing field %s" % k)
    if b.get("level") != "Q":
        err(b, "level should be 'Q' (got %r)" % b.get("level"))
    if b.get("mainSkill") not in SKILLS:
        err(b, "mainSkill %r not in allowed set" % b.get("mainSkill"))
    if not b.get("titleZh"): err(b, "missing titleZh")
    qs = b.get("questions", [])
    if len(qs) != 10:
        err(b, "questions != 10 (got %d)" % len(qs))
    for i, q in enumerate(qs):
        qn = "q%d" % i
        if not isinstance(q.get("q"), dict) or not (q["q"].get("en") and q["q"].get("zh")):
            err(b, "%s.q needs both en and zh" % qn)
        opts = q.get("options", [])
        if not isinstance(opts, list) or len(opts) != 4:
            err(b, "%s.options must be exactly 4" % qn); continue
        for oi, o in enumerate(opts):
            if not isinstance(o, dict) or not (o.get("en") and o.get("zh")):
                err(b, "%s.opt%d needs both en and zh" % (qn, oi))
        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a <= 3):
            err(b, "%s.answer must be int 0-3 (got %r)" % (qn, a))
        elif not (0 <= a < len(opts)):
            err(b, "%s.answer %d out of range for %d options" % (qn, a, len(opts)))
        if q.get("skill") not in SKILLS:
            err(b, "%s.skill %r not allowed" % (qn, q.get("skill")))
        ex = q.get("explain", {})
        if not isinstance(ex, dict) or not (ex.get("en") and ex.get("zh")):
            err(b, "%s.explain needs both en and zh" % qn)
    ext = b.get("extended")
    if not ext or not isinstance(ext, dict):
        err(b, "missing extended block")
    else:
        if not (ext.get("prompt", {}).get("en") and ext.get("prompt", {}).get("zh")):
            err(b, "extended.prompt needs en+zh")
        gd = ext.get("guidance", {})
        if not (gd.get("en") and gd.get("zh")):
            err(b, "extended.guidance needs en+zh arrays")
    if VALID:
        print("PASS  %s (%s)" % (slug, b.get("title","?")))

if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.json")))
    for f in files:
        if os.path.basename(f).startswith("_"): continue
        check(f)
    sys.exit(0 if VALID else 1)
