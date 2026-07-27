import json, sys, re

TAILS = [
 (" according to some versions of the story", "（按书中另一种说法）"),
 (" in an early draft of the book", "（在书的早期草稿中）"),
 (" as mentioned in a later chapter", "（正如后文某一章提到的）"),
 (" before the main events begin", "（在主要事件发生之前）"),
 (" as the author once noted", "（正如作者曾提到的）"),
 (" in a different account of the same event", "（对同一事件的另一种记述中）"),
 (" which a minor character also says", "（某个次要角色也说过）"),
 (" during an earlier part of the story", "（在故事更早的片段里）"),
 (" as recalled by someone who was there", "（据当时在场的人的回忆）"),
 (" in a scene that was later cut", "（在那个后来被删掉的段落里）"),
 (" if you read between the lines", "（如果你仔细推敲字里行间的意思）"),
 (" as the illustrator imagined it", "（正如绘者所想象的那样）"),
 (" though the book does not say so outright", "（尽管书里没有明说）"),
 (" in a moment the reader might have missed", "（在读者可能忽略的一瞬间）"),
 (" as the narrator quietly hints", "（正如讲述者悄悄暗示的那样）"),
 (" when looked at from another angle", "（换个角度看的话）"),
 (" (this is what the story tells us)", "（故事就是这样告诉我们的）"),
 (" (we see this in the book)", "（我们在书里看到这个）"),
 (" (the text says so)", "（书里是这么写的）"),
 (" (it happens in the tale)", "（故事里就是这么发生的）"),
 (" (the characters experience this)", "（角色们经历了这个）"),
 (" (this is in the book)", "（这书写在书里）"),
 (" (readers learn this in the story)", "（读者在故事里会知道这个）"),
 (" (the book describes it this way)", "（书是这样描写的）"),
 (" (you can find this on the page)", "（在书页上能找到这个）"),
 (" (this is part of the plot)", "（这是情节的一部分）"),
 (" (the story shows it clearly)", "（故事清楚地写出了这一点）"),
 (" (it is written in the book)", "（书里写明了这一点）"),
 (" (the reader discovers this)", "（读者会发现这个）"),
 (" (this is how the book puts it)", "（书是这么说的）"),
 (" (the events unfold like this)", "（事情就是这样发生的）"),
 (" (the book confirms this)", "（书里确认了这一点）"),
]

def strip_tails(s):
    changed = True
    while changed:
        changed = False
        for en, zh in TAILS:
            if en in s:
                s = s.replace(en, ""); changed = True
            if zh in s:
                s = s.replace(zh, ""); changed = True
    return re.sub(r"\s{2,}", " ", s).strip()

paths = sys.argv[1:]
for p in paths:
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        print(f"SKIP (load error) {p}: {e}")
        continue
    if not isinstance(d, dict) or "questions" not in d:
        print(f"SKIP (no questions) {p}")
        continue
    fc = False
    def walk(o):
        global fc
        if isinstance(o, dict):
            for k in list(o.keys()):
                o[k] = walk(o[k])
            return o
        elif isinstance(o, list):
            return [walk(v) for v in o]
        elif isinstance(o, str):
            n = strip_tails(o)
            if n != o:
                fc = True
            return n
        return o
    d = walk(d)
    if fc:
        json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"STRIPPED {p}")
    else:
        print(f"clean (no tails) {p}")
