import json

files = ["14.json", "15.json", "16.json", "17.json"]
required_keys = {"number", "title", "titleZh", "year", "author", "emoji", "desc", "source", "questions"}
ok = True

for f in files:
    try:
        with open(f, encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"{f}: INVALID JSON -> {e}")
        ok = False
        continue
    errs = []
    if set(data.keys()) != required_keys:
        errs.append(f"keys mismatch: {set(data.keys()) ^ required_keys}")
    qs = data.get("questions", [])
    if len(qs) != 10:
        errs.append(f"expected 10 questions, got {len(qs)}")
    for i, q in enumerate(qs):
        if not isinstance(q.get("q"), dict) or "en" not in q["q"] or "zh" not in q["q"]:
            errs.append(f"Q{i}: bad q")
        opts = q.get("options", [])
        if not isinstance(opts, list) or len(opts) != 4:
            errs.append(f"Q{i}: options not exactly 4")
        else:
            for o in opts:
                if not isinstance(o, dict) or "en" not in o or "zh" not in o:
                    errs.append(f"Q{i}: option missing en/zh")
        a = q.get("answer")
        if not (isinstance(a, int) and 0 <= a <= 3):
            errs.append(f"Q{i}: answer not int 0-3 ({a})")
        if not isinstance(q.get("explain"), dict) or "en" not in q["explain"] or "zh" not in q["explain"]:
            errs.append(f"Q{i}: bad explain")
    desc = data.get("desc", "")
    emoji = data.get("emoji", "")
    if not (desc.endswith(emoji) and len(desc) < 200):
        errs.append(f"desc issue (len={len(desc)}, ends_with_emoji={desc.endswith(emoji)})")
    if errs:
        ok = False
        print(f"{f}: FAIL")
        for e in errs:
            print("   -", e)
    else:
        print(f"{f}: OK (10 questions, source={data.get('source')}, year={data.get('year')}, emoji={emoji})")

print("ALL VALID" if ok else "SOME FAILED")
