#!/usr/bin/env python3
# Ground-truth validator for RAZ-W _quizdata. Compares against _titles.json.
import json, os, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_quizdata")

expected = json.load(open(os.path.join(DATA, "_titles.json"), encoding="utf-8"))
expected_slugs = {e["slug"] for e in expected}

# load actual json files (exclude helper _*.json)
actual = {}
for fp in glob.glob(os.path.join(DATA, "*.json")):
    name = os.path.basename(fp)
    if name.startswith("_"):
        continue
    slug = name[:-5]
    try:
        b = json.load(open(fp, encoding="utf-8"))
    except Exception as e:
        actual[slug] = ("BROKEN", str(e))
        continue
    errs = []
    qs = b.get("questions", [])
    if len(qs) != 10:
        errs.append("questions=%d" % len(qs))
    for i, q in enumerate(qs):
        opts = q.get("options") or []
        if len(opts) != 4:
            errs.append("q%d opts=%d" % (i, len(opts))); continue
        if not isinstance(q.get("answer"), int) or not (0 <= q["answer"] <= 3):
            errs.append("q%d answer" % i)
        if not (q.get("q") or {}).get("en"): errs.append("q%d q.en" % i)
        if not (q.get("explain") or {}).get("en"): errs.append("q%d explain.en" % i)
        for oi, o in enumerate(opts):
            if not o.get("en"): errs.append("q%d opt%d.en" % (i, oi))
    if not (b.get("extended") or {}).get("prompt", {}).get("en"):
        errs.append("ext.prompt.en")
    if errs:
        actual[slug] = ("INVALID", "; ".join(errs))
    else:
        actual[slug] = ("VALID", "")

valid = [s for s, v in actual.items() if v[0] == "VALID"]
broken = [s for s, v in actual.items() if v[0] == "BROKEN"]
invalid = [s for s, v in actual.items() if v[0] == "INVALID"]
missing = sorted(expected_slugs - set(actual.keys()))
unexpected = sorted(set(actual.keys()) - expected_slugs)

print("expected slugs :", len(expected_slugs))
print("actual json    :", len(actual))
print("VALID          :", len(valid))
print("BROKEN         :", len(broken), broken)
print("INVALID        :", len(invalid))
for s in invalid:
    print("   INVALID", s, "->", actual[s][1])
print("MISSING        :", len(missing), missing)
print("UNEXPECTED     :", len(unexpected), unexpected)
print("\nRESULT:", "ALL GOOD" if (not broken and not invalid and not missing) else "NEEDS FIX")
