#!/usr/bin/env python3
# Generate _quizdata/_titles.json (slug/title map) for RAZ-W from IMA titles.
import json, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_quizdata")

TITLES = [
    "The Nobel Prize",
    "The Kingdom of Happiness",
    "The Mystery of Granville Library",
    "The Hero Maui",
    "The Creature and the Queen",
    "The Buffalo Soldiers",
    "The Black Stones",
    "Taj Mahal",
    "Stonehenge",
    "Ships of Discovery",
    "Scratching a Good Story",
    "Route 66",
    "Robin Hood and the King",
    "Puffins",
    "Pirates and Privateers",
    "Petra",
    "Otzi The Iceman",
    "Nelson Mandela",
    "Ocean Quiz",
    "Mummies",
    "Miguel in the Secret Garden",
    "Microbes Friend or Foe",
    "March Madness",
    "Mapping the Woods Maps and Cartography",
    "Joe Kittinger An Unsung Hero",
    "InFLUenza",
    "Hurricanes",
    "Hoofed Animals",
    "High-Tech Treasure Hunt",
    "Great Mosque of Djenné",
    "Fearless Felix",
    "Earthquakes Volcanoes and Tsunamis",
    "Electric Cars History and Future",
    "Discovery in the Americas",
    "Desert People",
    "Curiosity on Mars",
    "Color Blindness",
    "Climbing Mountains An Interview with Erik Weihenmayer",
    "Catching Air",
    "Atlantic Crossing",
    "Ben Franklin",
    "Ancient Mesopotamia",
    "American Sports Legends",
    "Ancient Greek and Roman Gods",
    "Amelia Earhart A Legend in Flight",
    "Alberto Salazar An American Runner",
    "Albert Einstein",
    "Adventure in Bear Valley",
    "Acropolis Adventure",
    "A Place for Wild Things",
    "A New Skyline",
    "Yo-Yo Ma",
    "What Is Water Worth",
    "Vikings",
    "Valley of the Kings",
    "To Drill or Not to Drill",
    "Threats to Our Atmosphere",
    "The World of NASCAR",
    "The Yanomami Deep in the Amazon",
    "The Smithsonian Institution",
    "The University of Arizona College of Science Biosphere 2",
    "The Plague!",
    "The Red Baron",
    "The Other Side of the Glass",
    "The Olympics Past and Present",
]

def slugify(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("'", "")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", "-", s.strip()).strip("-")

out = []
seen = {}
for t in TITLES:
    slug = slugify(t)
    if slug in seen:
        raise SystemExit("DUPLICATE SLUG: %s -> %s and %s" % (slug, seen[slug], t))
    seen[slug] = t
    out.append({"title": t, "slug": slug})

with open(os.path.join(DATA, "_titles.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Wrote %d entries to _titles.json" % len(out))
for e in out:
    print(e["slug"])
