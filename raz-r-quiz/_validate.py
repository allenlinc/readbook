import os, json, re, glob

QDATA = "raz-r-quiz/_quizdata"
titles = [
"What Happens When You Flush","Whale Sharks Giant Fish","We're in Business","Weird Bird Beaks","Water Cities",
"Two Artists Vermeer's Forger","Trick or Treat","Turtle Tom","Treasure Found","Thomas Edison",
"The Thesaurus","The Super School Bus System","The Stanley Cup Hockey's Greatest Prize","The Recess Revolt","The Olympics Past and Present",
"The Nor'easter","The Hunting Trip","The History of Halloween","The Hard Stuff! All About Bones","The Genius of Tesla",
"Storm Chasers","Speed","Skydiving","Ships and Boats","September 11 Always Remember",
"Seeds and Sunflowers","Sea Turtles","Scaredy Camp","Rattlers","Robin Hood Wins the Sheriff's Golden Arrow",
"Pi Day","Part 4 Raining Cats, Dogs, and Other Animals","Part 3 Charly Dances 'til It Drops","Part 2 Charly's New Year's Revolution","Part 1 Charly Did It",
"Only One Aunt Maggie","New Year Celebrations","Neighborhood Mystery","Nature Reuses and Recycles","Murdoch's Path",
"Mozart","Morty's Roadside Refreshments","Morty Takes a Wooden Nickel","Morty and the Monster Truck Madness","Morty and the Twice-Fit Mice",
"Maria Tallchief Prima Ballerina","Morty and Charming Theo","King George III","Inventions","Hockey",
"How the Robin Stole Fire","Hillary Clinton","Hansel and Gretel","Hiking the Appalachian Trail","Golf",
"Going to the Super Bowl","Ghost Towns","Glow-in-the-Dark Animals","Foods Around the World","George Washington Carver",
"Fishing in Simplicity","Exploring Tide Pools","Explorer's Guide to World Weather","Expedition Zero","Expedition 60 The Subarctic",
"Expedition 25 The Subtropics","Expedition 40 The Secret of the Seasons","Elephants Giant Mammals","Deep in the Ocean","Blue Whales Giant Mammals",
"Charlene's Sea of Cortez Journal","Bessie Coleman","Basketball","April Fool's","Arrows",
"Animal Discoveries","An Apple a Day","All About Kites","All About Chocolate","Alexander the Great",
"Alaska The Last Frontier","Woods of Wonder","1849 The California Gold Rush","Wonders of Nature","Wildlife Rescue",
]
def slugify(t):
    s = t.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

expected = {slugify(t): t for t in titles}
files = sorted(f[:-5] for f in os.listdir(QDATA) if f.endswith('.json'))
print("total json files:", len(files))
print("expected slugs:", len(expected))

broken, invalid, valid = [], [], []
for s in files:
    fp = os.path.join(QDATA, s+".json")
    try:
        d = json.load(open(fp, encoding='utf-8'))
    except Exception as e:
        broken.append((s, str(e)[:90])); continue
    errs = []
    qs = d.get('questions', [])
    if len(qs) != 10: errs.append('q!=10(%d)' % len(qs))
    for i, q in enumerate(qs):
        if not isinstance(q.get('options'), list) or len(q['options']) != 4:
            errs.append('q%d opt!=4' % i); continue
        a = q.get('answer')
        if not isinstance(a, int) or not (0 <= a <= 3): errs.append('q%d ans' % i)
        for k in ('q', 'explain'):
            if not (q.get(k) or {}).get('en'): errs.append('q%d %s.en' % (i, k))
        for oi, o in enumerate(q['options']):
            if not o.get('en'): errs.append('q%d o%d.en' % (i, oi))
    if errs: invalid.append((s, '; '.join(errs)))
    else: valid.append(s)

print("VALID:", len(valid))
print("BROKEN:", len(broken))
for b in broken: print("  BROKEN", b)
print("INVALID:", len(invalid))
for b in invalid: print("  INVALID", b[0], '->', b[1])
missing = [s for s in expected if s not in files]
print("MISSING (expected not present):", len(missing))
for m in missing: print("  MISSING", m)
unexpected = [s for s in files if s not in expected]
print("UNEXPECTED (present but not in 85):", len(unexpected))
for u in unexpected: print("  UNEXPECTED", u)
