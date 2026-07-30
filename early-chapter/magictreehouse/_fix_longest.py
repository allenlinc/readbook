#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anti-cheat fix: ensure the correct option is NEVER the unique-longest option.
For each question where the correct option is the sole longest (EN and/or ZH),
extend the longest DISTRACTOR with a natural storybook tail so it equals/exceeds
the correct length. Tails clearly mark the option as NOT this book's fact (no
false book-attestation). Options order / answer index preserved.
"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")

# (en_tail, zh_tail) pairs — natural narrative asides, never "the book says".
TAILS = [
    (", though that is another story", "，不过那是另一个故事了"),
    (", as someone else had told it", "，那是别人讲的版本"),
    (", from long, long ago", "，发生在很久很久以前"),
    (", in a place far away", "，在很远很远的地方"),
]

def fix_file(path):
    d = json.load(open(path, encoding="utf-8"))
    changed = 0
    for i, q in enumerate(d["questions"]):
        opts = q["options"]
        a = q["answer"]
        en_lens = [len(o["en"]) for o in opts]
        zh_lens = [len(o["zh"]) for o in opts]

        def need_en():
            return en_lens[a] == max(en_lens) and en_lens.count(en_lens[a]) == 1
        def need_zh():
            return zh_lens[a] == max(zh_lens) and zh_lens.count(zh_lens[a]) == 1

        if not need_en() and not need_zh():
            continue

        # pick the longest distractor (by combined length) to pad
        best = max((j for j in range(4) if j != a), key=lambda j: en_lens[j] + zh_lens[j])
        ti = (int(d.get("number", "0")) * 10 + i) % len(TAILS)
        guard = 0
        while (need_en() or need_zh()) and guard < 6:
            en_t, zh_t = TAILS[ti % len(TAILS)]
            if need_en():
                opts[best]["en"] += en_t
                en_lens[best] = len(opts[best]["en"])
            if need_zh():
                opts[best]["zh"] += zh_t
                zh_lens[best] = len(opts[best]["zh"])
            ti += 1
            guard += 1
        # ensure still distinct
        ens = [o["en"] for o in opts]
        zhs = [o["zh"] for o in opts]
        if len(set(ens)) != 4 or len(set(zhs)) != 4:
            # nudge with a unique marker
            opts[best]["en"] += " *"
            opts[best]["zh"] += "＊"
        changed += 1
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return changed


def main():
    files = sorted(f for f in os.listdir(DATA) if f.endswith(".json") and not f.startswith("_"))
    total = 0
    for f in files:
        c = fix_file(os.path.join(DATA, f))
        if c:
            print(f"{f}: fixed {c} question(s)")
            total += c
    print(f"\nTOTAL fixed questions: {total} across {len(files)} files")


if __name__ == "__main__":
    main()
