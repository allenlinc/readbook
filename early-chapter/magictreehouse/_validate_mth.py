#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent anti-cheat + structure validation for MTH quiz JSON (NN=01..55).
Flags (does NOT auto-fix):
  - JSON parse error
  - missing top-level keys / wrong types
  - questions != 10, options != 4, answer out of range, options not distinct
  - missing en/zh in q/options/explain
  - distractor contains forbidden book-attestation phrasing (false authority)
  - correct option is the UNIQUE longest (the guessable "longest = right" pattern)
Prints a per-file report and a totals line; exits non-zero if any hard violation.
"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")

FORBIDDEN = [
    "书上说", "书里说", "书中说", "书本说", "书上讲",
    "the book says", "according to the book", "the story says",
    "the book states", "book says", "the book tells",
    "as the book says", "per the book",
]

def lens(s):
    return len(s.get("en", "")), len(s.get("zh", ""))

def validate_file(path):
    errs = []
    warns = []
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return [f"PARSE_FAIL: {e}"], []

    for k in ("number", "title", "titleZh", "year", "author", "emoji", "desc", "source", "questions"):
        if k not in d:
            errs.append(f"missing top key '{k}'")
    qs = d.get("questions", [])
    if not isinstance(qs, list) or len(qs) != 10:
        errs.append(f"questions != 10 (got {len(qs) if isinstance(qs,list) else 'n/a'})")
        return errs, warns

    for i, q in enumerate(qs):
        tag = f"Q{i+1}"
        qtext = q.get("q", {})
        if not isinstance(qtext, dict) or not qtext.get("en") or not qtext.get("zh"):
            errs.append(f"{tag}: bad q en/zh")
        opts = q.get("options", [])
        if not isinstance(opts, list) or len(opts) != 4:
            errs.append(f"{tag}: options != 4")
            continue
        # distinctness
        ens = [o.get("en", "") for o in opts]
        zhs = [o.get("zh", "") for o in opts]
        if len(set(ens)) != 4:
            errs.append(f"{tag}: duplicate EN options {ens}")
        if len(set(zhs)) != 4:
            errs.append(f"{tag}: duplicate ZH options")
        for j, o in enumerate(opts):
            if not isinstance(o, dict) or not o.get("en") or not o.get("zh"):
                errs.append(f"{tag}: opt{j} bad en/zh")
        a = q.get("answer")
        if not isinstance(a, int) or not (0 <= a < 4):
            errs.append(f"{tag}: answer out of range {a}")
            continue
        ex = q.get("explain", {})
        if not isinstance(ex, dict) or not ex.get("en") or not ex.get("zh"):
            errs.append(f"{tag}: bad explain en/zh")
        # forbidden attestation in DISTRACTORS only
        for j, o in enumerate(opts):
            if j == a:
                continue
            blob = (o.get("en", "") + " " + o.get("zh", "")).lower()
            for f in FORBIDDEN:
                if f in blob:
                    errs.append(f"{tag}: distractor opt{j} has forbidden '{f}'")
                    break
        # longest check (EN and ZH): correct must not be the unique max length
        en_lens = [len(o.get("en", "")) for o in opts]
        zh_lens = [len(o.get("zh", "")) for o in opts]
        if en_lens[a] == max(en_lens) and en_lens.count(en_lens[a]) == 1:
            warns.append(f"{tag}: correct EN is unique-longest ({en_lens[a]} vs {en_lens})")
        if zh_lens[a] == max(zh_lens) and zh_lens.count(zh_lens[a]) == 1:
            warns.append(f"{tag}: correct ZH is unique-longest ({zh_lens[a]} vs {zh_lens})")
    return errs, warns


def main():
    files = sorted(f for f in os.listdir(DATA) if f.endswith(".json") and not f.startswith("_"))
    total_err = 0
    total_warn = 0
    bad_files = []
    for f in files:
        errs, warns = validate_file(os.path.join(DATA, f))
        if errs or warns:
            print(f"\n=== {f} ===")
            for e in errs:
                print("  ERR ", e)
            for w in warns:
                print("  WARN", w)
        total_err += len(errs)
        total_warn += len(warns)
        if errs:
            bad_files.append(f)
    print(f"\nTOTAL files={len(files)} errs={total_err} warns(longest)={total_warn} bad_files={bad_files}")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
