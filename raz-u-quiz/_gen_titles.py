# -*- coding: utf-8 -*-
"""
Reproducible generator for RAZ-U title -> IMA media_id mapping.

Re-creates  raz-u-quiz/_quizdata/_titles.json  from the embedded
(title, media_id) tuples using the slugify rule described in the task.

Usage:
    python _gen_titles.py

No network calls are made; the tuples below were captured from the
IMA knowledge base "RAZ-U" (knowledge_base_id=7485015877236829).
"""

import json
import os
import re

# --- Embedded source data: (title_without_pdf, media_id) ---------------
# media_id values are passed EXACTLY as returned by the IMA API.
BOOKS = [
    ("The Jr. Iditarod", "pdf_c64dc37104cd00a5901ab8059b66f8df_556108074e3bbecce1da12e79d7d33e57485015877236829"),
    ("The Inuit Northern Living", "pdf_c64dc37104cd00a5901ab8059b66f8df_cf3f7b436dc7543054c3735cf604a5c27485015877236829"),
    ("The History of Halloween", "pdf_c64dc37104cd00a5901ab8059b66f8df_ad4372533dd623ee67e49380651975ac7485015877236829"),
    ("The History of Anime", "pdf_c64dc37104cd00a5901ab8059b66f8df_83c6b771832c174071933bc49d32aad27485015877236829"),
    ("The Hard Stuff! All About Bones", "pdf_c64dc37104cd00a5901ab8059b66f8df_9ecb7eb2769710e6be24818c132293dd7485015877236829"),
    ("The Great Gallardo's Books", "pdf_c64dc37104cd00a5901ab8059b66f8df_866ed622dfe0505907ce471830f184777485015877236829"),
    ("The Genius of Tesla", "pdf_c64dc37104cd00a5901ab8059b66f8df_81a3f47bef5c6e137418ed1752771c497485015877236829"),
    ("The Amazing Amazon", "pdf_c64dc37104cd00a5901ab8059b66f8df_d7c66a2de208892ca44e9d689818d9a17485015877236829"),
    ("The Bill of Rights", "pdf_c64dc37104cd00a5901ab8059b66f8df_b0994a5050d522bb4ac968a275c8dd707485015877236829"),
    ("Tanya's Money Problem", "pdf_c64dc37104cd00a5901ab8059b66f8df_f347b4a78062090c680017e34d49a2c57485015877236829"),
    ("Teotihuacan", "pdf_c64dc37104cd00a5901ab8059b66f8df_47d00d7a268a1c9bf7c95ffdfe938e1f7485015877236829"),
    ("Samson A Horse Story", "pdf_c64dc37104cd00a5901ab8059b66f8df_ba105057b4a8d36db0bb70771901742a7485015877236829"),
    ("Seven Wonders You Can Visit", "pdf_c64dc37104cd00a5901ab8059b66f8df_633fd79da9d1ad54be0c3a70b6ad3f177485015877236829"),
    ("Polar Regions of the Earth", "pdf_c64dc37104cd00a5901ab8059b66f8df_fcddb4a003915018b8de20af6cefbb2f7485015877236829"),
    ("Robin Hood Wins the Sheriff's Golden Arrow", "pdf_c64dc37104cd00a5901ab8059b66f8df_149a39c756876afc2a8a96e0b511826a7485015877236829"),
    ("Pirate Ships and Flags", "pdf_c64dc37104cd00a5901ab8059b66f8df_3038964e3deff8fdeb3c736d88fc549e7485015877236829"),
    ("Page's School Report", "pdf_c64dc37104cd00a5901ab8059b66f8df_e4c08578ae32c67c4a7aaa20831bd0d47485015877236829"),
    ("Noni's Newspaper", "pdf_c64dc37104cd00a5901ab8059b66f8df_abe3b29e07a5e472ffc27a10d9cd09f87485015877236829"),
    ("Mystery in the Moonlight", "pdf_c64dc37104cd00a5901ab8059b66f8df_954ccfe1fbcb43140bdae414a5f2747b7485015877236829"),
    ("Morocco", "pdf_c64dc37104cd00a5901ab8059b66f8df_98df4e383bbd2275081aa1d18d50ff377485015877236829"),
    ("More Valuable Than Gold", "pdf_c64dc37104cd00a5901ab8059b66f8df_ce023b46588d4c816d43b3512daf609e7485015877236829"),
    ("Meteors and Meteorites", "pdf_c64dc37104cd00a5901ab8059b66f8df_2846eed907075ed8d86ea7d1d1195c777485015877236829"),
    ("Microbes Friend or Foe", "pdf_c64dc37104cd00a5901ab8059b66f8df_81e309b047a0c79c75650a19f08794147485015877236829"),
    ("Magnificent Meatball Maker", "pdf_c64dc37104cd00a5901ab8059b66f8df_fd6ee6277952a74c5c3361afa30fd1c97485015877236829"),
    ("Maria Tallchief Prima Ballerina", "pdf_c64dc37104cd00a5901ab8059b66f8df_948a2309579c9d6e0b33ea40d4c32b007485015877236829"),
    ("Kenya", "pdf_c64dc37104cd00a5901ab8059b66f8df_ce07a918a5f0e51ea3c7df1ad9247d8c7485015877236829"),
    ("Life Cycles", "pdf_c64dc37104cd00a5901ab8059b66f8df_61f36c4cf88a7ad8c7e84279546f37ce7485015877236829"),
    ("Jupiter's Secrets Revealed", "pdf_c64dc37104cd00a5901ab8059b66f8df_b761a3db1c04f4d02bc84875b46c00c67485015877236829"),
    ("Hubble An Out-of-This-World Telescope", "pdf_c64dc37104cd00a5901ab8059b66f8df_632979f505a2371a4de9842be88b59727485015877236829"),
    ("How to Build a Greenhouse", "pdf_c64dc37104cd00a5901ab8059b66f8df_375d5123cc32d398ee7d7076f67ca3677485015877236829"),
    ("How Sound Works", "pdf_c64dc37104cd00a5901ab8059b66f8df_8f6c8e116b8f474d5f868eaf05a7aece7485015877236829"),
    ("Hillary Clinton", "pdf_c64dc37104cd00a5901ab8059b66f8df_e7722a74bcb961a8c82279c22439d1377485015877236829"),
    ("Hiking the Appalachian Trail", "pdf_c64dc37104cd00a5901ab8059b66f8df_f2ff0018ca9b524b9df50472a96438967485015877236829"),
    ("Hansel and Gretel", "pdf_c64dc37104cd00a5901ab8059b66f8df_3f4acc162f48d1a7b121c15fdfd0010f7485015877236829"),
    ("Growing Up Green", "pdf_c64dc37104cd00a5901ab8059b66f8df_82e5b97f78dbd8ba016b891ed3dc30f67485015877236829"),
    ("Get Moving! All About Muscles", "pdf_c64dc37104cd00a5901ab8059b66f8df_a26adbb68b65f1200d36c07f53877e4e7485015877236829"),
    ("Great Zimbabwe", "pdf_c64dc37104cd00a5901ab8059b66f8df_e928073914db93957aa6e8257ef435997485015877236829"),
    ("Galapagos Wonder", "pdf_c64dc37104cd00a5901ab8059b66f8df_aa5a22952d6e4889b88224467e5ae1577485015877236829"),
    ("Gandhi", "pdf_c64dc37104cd00a5901ab8059b66f8df_49cb02f6a3f994e3b89ccc8126f45b137485015877236829"),
    ("Fabulous Faberg\u00e9 Eggs", "pdf_c64dc37104cd00a5901ab8059b66f8df_3cc32b39c0817ca2c897b901e86021397485015877236829"),
    ("Eiffel Tower", "pdf_c64dc37104cd00a5901ab8059b66f8df_daae3fc248866c540d45da3dfe7e908f7485015877236829"),
    ("Don't Wake the Mummy", "pdf_c64dc37104cd00a5901ab8059b66f8df_18c88c9ba2b6a9e9726d3cb6ffe356027485015877236829"),
    ("Egypt", "pdf_c64dc37104cd00a5901ab8059b66f8df_5845f38fbb0f6de24e30f388baa24a107485015877236829"),
    ("Deep Trouble The Gulf Coast Oil Spill", "pdf_c64dc37104cd00a5901ab8059b66f8df_4c6c57cea60ea576c7733eadfd9c243c7485015877236829"),
    ("Dawn of the Doughnut", "pdf_c64dc37104cd00a5901ab8059b66f8df_524f0af5280a84fed36c02a4914fd23a7485015877236829"),
    ("Coral Reefs", "pdf_c64dc37104cd00a5901ab8059b66f8df_475295c1acc9908fd19d4dc4654def847485015877236829"),
    ("China", "pdf_c64dc37104cd00a5901ab8059b66f8df_8821a6ccd687e8030ef9f748ac171b4c7485015877236829"),
    ("Chick-a-Dude", "pdf_c64dc37104cd00a5901ab8059b66f8df_0580885aa4a6f9b0dd0525031de099137485015877236829"),
    ("Big Ben and Westminster Palace", "pdf_c64dc37104cd00a5901ab8059b66f8df_70d4bfe58c0f18e80c2c0ba6721944e97485015877236829"),
    ("Chich\u00e9n Itz\u00e1", "pdf_c64dc37104cd00a5901ab8059b66f8df_8821a6ccd687e8030ef9f748ac171b4c7485015877236829"),
    ("Beowulf", "pdf_c64dc37104cd00a5901ab8059b66f8df_de200eabfa3c8e33f24b35e0ea22a1787485015877236829"),
    ("Australia", "pdf_c64dc37104cd00a5901ab8059b66f8df_0d5b00a48413330531b058d0f07292847485015877236829"),
    ("Arrows", "pdf_c64dc37104cd00a5901ab8059b66f8df_d573c99cec52441095fbeab691be2b537485015877236829"),
    ("Animal Discoveries", "pdf_c64dc37104cd00a5901ab8059b66f8df_b6cdb54dbb983c5ca202ba89ef4703cd7485015877236829"),
    ("All About Chocolate", "pdf_c64dc37104cd00a5901ab8059b66f8df_8df4061ba1ebb8f777e1928c683336547485015877236829"),
    ("1849 The California Gold Rush", "pdf_c64dc37104cd00a5901ab8059b66f8df_7b233ff511bb7ed790b8c48f5603c1987485015877236829"),
    ("Wildlife Rescue", "pdf_c64dc37104cd00a5901ab8059b66f8df_258870443604b5903f38be80556fb5ad7485015877236829"),
    ("Yellow Brick Roadies", "pdf_c64dc37104cd00a5901ab8059b66f8df_17e2cbaadab8aa3cf2e1d36f3251f9737485015877236829"),
    ("Weaving Around the World", "pdf_c64dc37104cd00a5901ab8059b66f8df_984de30dbbf806f7f0642620aada97027485015877236829"),
    ("What Happens When You Flush", "pdf_c64dc37104cd00a5901ab8059b66f8df_ce169f35cde9c8e8d0c1d96658c22b567485015877236829"),
    ("Veterans Day", "pdf_c64dc37104cd00a5901ab8059b66f8df_1987672b43a39970df09fb20d3b0f24a7485015877236829"),
    ("Water Cities", "pdf_c64dc37104cd00a5901ab8059b66f8df_b0d391434e1902122f4d55af20a89b157485015877236829"),
    ("Underground Cities", "pdf_c64dc37104cd00a5901ab8059b66f8df_2e4f39d6c7e67f38f5a90719515695517485015877236829"),
    ("United Arab Emirates", "pdf_c64dc37104cd00a5901ab8059b66f8df_60fef703840d21a7973593efd8573a347485015877236829"),
    ("The Treasure of El Dorado", "pdf_c64dc37104cd00a5901ab8059b66f8df_f1d2e9bf54c76492e78e2c2277545d607485015877236829"),
    ("Thomas Edison", "pdf_c64dc37104cd00a5901ab8059b66f8df_d71a0e40be2e07b81ca44329824be6a27485015877236829"),
    ("The Village", "pdf_c64dc37104cd00a5901ab8059b66f8df_a46fc5b4d944ae2732dfb3b6ee1de8ef7485015877236829"),
    ("The Thing in the Forest", "pdf_c64dc37104cd00a5901ab8059b66f8df_1c90326b2800f4ad4cece132787132a07485015877236829"),
    ("The Super School Bus System", "pdf_c64dc37104cd00a5901ab8059b66f8df_dc12c5c2e101d788476e76dfed71ca917485015877236829"),
    ("The Sun, Earth, and Moon", "pdf_c64dc37104cd00a5901ab8059b66f8df_007eae7bb63f69afd442dba658bd25137485015877236829"),
    ("The Stanley Cup Hockey's Greatest Prize", "pdf_c64dc37104cd00a5901ab8059b66f8df_6a7e8664362711b97220bcb1dd28ed5d7485015877236829"),
    ("The Recess Revolt", "pdf_c64dc37104cd00a5901ab8059b66f8df_a7466d2c568e119b932e9ddca29c18237485015877236829"),
    ("The Secret Service", "pdf_c64dc37104cd00a5901ab8059b66f8df_6b7d04f01c1ab4f6a8487b66d5cd83717485015877236829"),
    ("The Mighty Saguaro Cactus", "pdf_c64dc37104cd00a5901ab8059b66f8df_c4283c5b49cbdc70dbc4cb345b1c8c4a7485015877236829"),
    ("The Outburst", "pdf_c64dc37104cd00a5901ab8059b66f8df_52c8fd6aeb18dbd767a39f04b860d7947485015877236829"),
]


def slugify(title: str) -> str:
    """URL-safe slug per task rules.

    - lowercase
    - keep only [a-z0-9]
    - accented/non-ASCII letters are dropped entirely (e.g. Chichén Itzá -> chichn-itz)
    - every run of other characters (spaces, punctuation, apostrophes) becomes a single hyphen
    - leading/trailing hyphens stripped
    """
    s = title.strip().lower()
    # Drop apostrophes AND any non-ASCII (accented) characters entirely
    # (they are removed, NOT turned into a hyphen). e.g. Gallardo's -> gallardos,
    # Chichen Itza accents -> chichn itz.
    s = "".join(ch for ch in s if ch != "'" and ord(ch) < 128)
    # Replace any run of remaining non [a-z0-9] characters with a single hyphen.
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def build_records():
    records = []
    for title, media_id in BOOKS:
        records.append({
            "slug": slugify(title),
            "title": title,
            "media_id": media_id,
        })
    return records


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_quizdata")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "_titles.json")

    records = build_records()
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=1)

    print(f"Wrote {len(records)} records to {out_path}")


if __name__ == "__main__":
    main()
