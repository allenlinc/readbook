#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Factuality spot-check: for each question, verify the CORRECT option's EN text
has support in the book's extracted text. Flags questions whose correct option
cannot be found in the text (candidate invented answers) for manual review.
Heuristic only — a MISS does not prove wrong, but warrants a look."""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "_quizdata")
TXT = os.path.join(BASE, "_pdftext")

def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()

def keywords(en):
    # drop trailing tail we may have appended, take meaningful words
    base = en.split(", though")[0].split(", as someone")[0].split(", from long")[0].split(", in a place")[0]
    words = [w for w in norm(base).split() if len(w) >= 4]
    # also try the full normalized base as a phrase
    return words, norm(base)

def support(text, en):
    words, phrase = keywords(en)
    low = text.lower()
    # phrase search (allow small gaps)
    p = re.sub(r"\s+", ".*?", re.escape(phrase))
    if phrase and re.search(p, low):
        return True
    # keyword search: at least the 2 longest distinct keywords present
    if len(words) >= 2:
        uniq = list(dict.fromkeys(words))
        hit = sum(1 for w in uniq[:4] if w in low)
        if hit >= min(2, len(uniq[:4])):
            return True
    if words and words[0] in low:
        return True
    return False

def main():
    files = sorted(f for f in os.listdir(DATA) if f.endswith(".json") and not f.startswith("_"))
    flagged = 0
    for f in files:
        num = f.replace(".json", "")
        d = json.load(open(os.path.join(DATA, f), encoding="utf-8"))
        txt_path = os.path.join(TXT, f"{num}.txt")
        text = open(txt_path, encoding="utf-8").read() if os.path.exists(txt_path) else ""
        for i, q in enumerate(d["questions"]):
            correct = q["options"][q["answer"]]["en"]
            if not support(text, correct):
                print(f"{f} Q{i+1}: MAYBE-INVENTED correct -> {correct}")
                flagged += 1
    print(f"\nFlagged (review): {flagged}")

if __name__ == "__main__":
    main()
