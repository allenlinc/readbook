#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anti-cheat fix for Captain Underpants quizzes (mirrors quiz-anti-cheat-fix skill).
- Rebalance answer positions so each of 0..3 appears at most 3 times per 10-q book.
- Guarantee >=1 distractor is strictly longer than the correct option (append neutral
  filler to the longest distractor until it exceeds the correct option's length).
Correct option wording, question text and explanation are NEVER changed.
"""
import json, glob, os, random

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")

TAILS = [
    {"en": " (Some fans of the series might pick this one.)",
     "zh": "（这个系列的一些小粉丝可能会选这个。）"},
    {"en": " (You can find a clue about this in the book.)",
     "zh": "（你能在书里找到关于这个的线索。）"},
    {"en": " (This is one of the trickier choices.)",
     "zh": "（这是比较有迷惑性的一个选项。）"},
    {"en": " (The story mentions something like this too.)",
     "zh": "（故事里也提到过类似的内容。）"},
]

def fix_file(path):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    base = os.path.splitext(os.path.basename(path))[0]
    try:
        seed = int(base)
    except ValueError:
        seed = abs(hash(base)) % (10**9)
    rnd = random.Random(seed)
    qs = d["questions"]

    target = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
    rnd.shuffle(target)

    for i, q in enumerate(qs):
        opts = q["options"]
        cidx = q["answer"]
        correct = opts[cidx]
        others = [o for k, o in enumerate(opts) if k != cidx]
        rnd.shuffle(others)
        p = target[i]
        new = [None] * 4
        new[p] = correct
        oi = 0
        for s in range(4):
            if s != p:
                new[s] = others[oi]
                oi += 1
        # guarantee >=1 distractor strictly longer than correct
        corr_len = len(correct["en"]) + len(correct["zh"])
        ti = 0
        while True:
            ds = [s for s in range(4) if s != p]
            lens = [len(new[s]["en"]) + len(new[s]["zh"]) for s in ds]
            if max(lens) > corr_len:
                break
            s = ds[lens.index(max(lens))]
            t = TAILS[ti % len(TAILS)]
            ti += 1
            new[s]["en"] = new[s]["en"].rstrip() + t["en"]
            new[s]["zh"] = new[s]["zh"].rstrip() + t["zh"]
        q["options"] = new
        q["answer"] = p

    with open(path, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    return len(qs)

def verify(path):
    d = json.load(open(path, encoding="utf-8"))
    longest = 0
    pos = [0, 0, 0, 0]
    for q in d["questions"]:
        lens = [len(o["en"]) + len(o["zh"]) for o in q["options"]]
        if lens[q["answer"]] == max(lens):
            longest += 1
        pos[q["answer"]] += 1
    return longest, max(pos)

if __name__ == "__main__":
    files = sorted(f for f in glob.glob(os.path.join(DATA, "*.json"))
                   if not os.path.basename(f).startswith("_"))
    tot_long = 0
    posbad = 0
    for f in files:
        n = fix_file(f)
        long, mx = verify(f)
        tot_long += long
        if mx > 4:
            posbad += 1
        print(f"{os.path.basename(f)}: fixed ({n} qs), correct-longest={long}, maxpos={mx}")
    print(f"\nTOTAL correct-longest = {tot_long} (want 0); posbad(files>4)={posbad} (want 0)")
