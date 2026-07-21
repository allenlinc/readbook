#!/usr/bin/env python3
# Generate _quizdata/_titles.json : master map of all RSZ-S books
# slug <- title (lowercase, non-alphanumeric -> '-', collapse, strip)
import json, re, os

KB = "7485004015746189"  # RSZ-S knowledge base id (already suffix of each media_id)

RAW = [
("Woolly and Fang","pdf_c64dc37104cd00a5901ab8059b66f8df_a14ed41525d8fa2f3001e426b72aeb117485004015746189"),
("Wild and Wacky World of Wigs","pdf_c64dc37104cd00a5901ab8059b66f8df_4bd295d43ab690834f7df4f00eb94d4e7485004015746189"),
("Wheeling the Snake","pdf_c64dc37104cd00a5901ab8059b66f8df_a7085079aa62bc1ac52a12f2eaa34c027485004015746189"),
("Why We Sleep","pdf_c64dc37104cd00a5901ab8059b66f8df_8f75b20c692a8668046c9413189e677b7485004015746189"),
("What the Boys Found","pdf_c64dc37104cd00a5901ab8059b66f8df_98c3211821e675152078d1073b3093957485004015746189"),
("What's in a Name","pdf_c64dc37104cd00a5901ab8059b66f8df_bd0424d7fb659511eadfd3ad525069dc7485004015746189"),
("Volcanoes","pdf_c64dc37104cd00a5901ab8059b66f8df_20c4be89ec220b1cd4f26d20d2f69abf7485004015746189"),
("Voyagers in Space","pdf_c64dc37104cd00a5901ab8059b66f8df_c9e71823c3f75b6a8668fd8d6e84264a7485004015746189"),
("Two Kettles","pdf_c64dc37104cd00a5901ab8059b66f8df_56b7f6f86ddac83a1679d17554ccd0c97485004015746189"),
("Tsunamis","pdf_c64dc37104cd00a5901ab8059b66f8df_872e52da1c6756e5954c8fc806ce2a4d7485004015746189"),
("The Wall","pdf_c64dc37104cd00a5901ab8059b66f8df_6b8c7a770485db68febe592f4204aba47485004015746189"),
("The Trouble with English","pdf_c64dc37104cd00a5901ab8059b66f8df_dfdad9b0e52d9dd32f8c045924cef5937485004015746189"),
("The Titanic Lost and Found","pdf_c64dc37104cd00a5901ab8059b66f8df_7ed53bc474a27dd06a804c27edb2d3707485004015746189"),
("The International T-Shirt Challenge","pdf_c64dc37104cd00a5901ab8059b66f8df_0ca9a0b4d1cc221ecee49ae8c4209f897485004015746189"),
("The Moon Bowl","pdf_c64dc37104cd00a5901ab8059b66f8df_9217fdcf681333f401e98e54ddf8e54b7485004015746189"),
("The Hidden Room","pdf_c64dc37104cd00a5901ab8059b66f8df_a33372568e6fc0eb05a0cc5cc1603f037485004015746189"),
("Stories from Asgard Norse Myths","pdf_c64dc37104cd00a5901ab8059b66f8df_e02c1dfdd10cab92aa226109880921427485004015746189"),
("Space Camp","pdf_c64dc37104cd00a5901ab8059b66f8df_23a654358163ae9ad8e59df8929823257485004015746189"),
("Snakebite!","pdf_c64dc37104cd00a5901ab8059b66f8df_1a817ecf9310343533d2ed5aa1fff2387485004015746189"),
("Seven Wonders of the Modern World","pdf_c64dc37104cd00a5901ab8059b66f8df_dafed0cfd6f8b9e25970e25d4400b88b7485004015746189"),
("Searching for the Loch Ness Monster","pdf_c64dc37104cd00a5901ab8059b66f8df_58af4ab75330949d85ac07f10f343c067485004015746189"),
("Penguins","pdf_c64dc37104cd00a5901ab8059b66f8df_596c95fa181b82c8eb8b0ee4cd0cfed07485004015746189"),
("Morty the Meany","pdf_c64dc37104cd00a5901ab8059b66f8df_1c8d9b072426fdf2eb5b7311b962f4377485004015746189"),
("Part 5 Let a Smiley Face Be Your Umbrella","pdf_c64dc37104cd00a5901ab8059b66f8df_d19c8bd2305dd1c0989deb326361d36c7485004015746189"),
("Our Solar System","pdf_c64dc37104cd00a5901ab8059b66f8df_e58b39658498fe3818f45146d26f2a5a7485004015746189"),
("Ostriches Giant Birds","pdf_c64dc37104cd00a5901ab8059b66f8df_963df0ad1b4ecc450e366555eb9b5e857485004015746189"),
("Noni and the Book Ban","pdf_c64dc37104cd00a5901ab8059b66f8df_d884d7307e94760c4c559fc9c9bd57b17485004015746189"),
("National Parks","pdf_c64dc37104cd00a5901ab8059b66f8df_bbcbcf30f48b487a568aa6c48258569d7485004015746189"),
("Mortyangelo and the Mystery Art","pdf_c64dc37104cd00a5901ab8059b66f8df_0f6d379bbea2e379ce38afe3126f9fbb7485004015746189"),
("Morty and the Mousetown Talent Show","pdf_c64dc37104cd00a5901ab8059b66f8df_34ccd62054e0dbf88cf5d693e0efd94c7485004015746189"),
("Monkey Business","pdf_c64dc37104cd00a5901ab8059b66f8df_ef7faa869278de50fd57f49a439ba2267485004015746189"),
("Morty and the Fancy-Pants Wedding","pdf_c64dc37104cd00a5901ab8059b66f8df_387d9b8e2666b73c89a7dd86c758d4417485004015746189"),
("Martin Luther King, Jr.","pdf_c64dc37104cd00a5901ab8059b66f8df_8c00ef9e2638cd272fa70fcae3935c617485004015746189"),
("Losing Grandpa","pdf_c64dc37104cd00a5901ab8059b66f8df_2146377d742ee34669891402431a58987485004015746189"),
("Making Mosaics","pdf_c64dc37104cd00a5901ab8059b66f8df_adb8d2b96a528a35cd6bb95838d761877485004015746189"),
("Life in Space","pdf_c64dc37104cd00a5901ab8059b66f8df_4bac78b8b7d32d09572c82d570a4005a7485004015746189"),
("Let's Make Vegetable Soup","pdf_c64dc37104cd00a5901ab8059b66f8df_abb144f30c60c872b567482768bb85c67485004015746189"),
("Laura Ingalls Wilder A Pioneer's Life","pdf_c64dc37104cd00a5901ab8059b66f8df_ccb74d2284d63e81a26f2a2e4cb341137485004015746189"),
("Lacrosse","pdf_c64dc37104cd00a5901ab8059b66f8df_161c1b27cfa18779b1d3bdc66c552a3c7485004015746189"),
("Labor Day","pdf_c64dc37104cd00a5901ab8059b66f8df_642a7fb1094170134e55ed84ee2774a07485004015746189"),
("Julius Caesar","pdf_c64dc37104cd00a5901ab8059b66f8df_9ad0409e40fa805d9db801657d3ab0207485004015746189"),
("India","pdf_c64dc37104cd00a5901ab8059b66f8df_13ebfc7e9cc4af7289056dfbea7832837485004015746189"),
("How Little John Joined Robin Hood","pdf_c64dc37104cd00a5901ab8059b66f8df_f080b6d7b4ee1bfb53ca797d4077ae7f7485004015746189"),
("Guy Fawkes Day","pdf_c64dc37104cd00a5901ab8059b66f8df_697d2e58553b25f9e421194cb030e5a37485004015746189"),
("Harriet Tubman and the Underground Railroad","pdf_c64dc37104cd00a5901ab8059b66f8df_4926f540b47bebb7580061aa58487da57485004015746189"),
("Harold the Dummy","pdf_c64dc37104cd00a5901ab8059b66f8df_8be56b6f20c277ae2a9fe046f05f62647485004015746189"),
("Goliath Beetles Giant Insects","pdf_c64dc37104cd00a5901ab8059b66f8df_53ad241fb6769d00755c6631ab99ce927485004015746189"),
("Groundwater","pdf_c64dc37104cd00a5901ab8059b66f8df_f8debd480c5c7335e255f34bbd2b1b097485004015746189"),
("Ghosts in the House","pdf_c64dc37104cd00a5901ab8059b66f8df_18e76d99b4f837279874ed32503acc437485004015746189"),
("Gems Treasures from the Earth","pdf_c64dc37104cd00a5901ab8059b66f8df_90aba77c6288e13da0b62d82a88d24e77485004015746189"),
("George Washington","pdf_c64dc37104cd00a5901ab8059b66f8df_7cec45fcff54b9edd2f186f429e0dc757485004015746189"),
("Galileo","pdf_c64dc37104cd00a5901ab8059b66f8df_8d08d554fc75ebf75b813488f1a25b8e7485004015746189"),
("Frederick Douglass Forever Free","pdf_c64dc37104cd00a5901ab8059b66f8df_bd041c73d0ebcce8df6ab817628752337485004015746189"),
("France","pdf_c64dc37104cd00a5901ab8059b66f8df_5e77cf7d1f6683a90570ca64d12219817485004015746189"),
("Finding the Tome","pdf_c64dc37104cd00a5901ab8059b66f8df_f7df9fb39cf75419518666240ccffd7c7485004015746189"),
("Condors Giant Birds","pdf_c64dc37104cd00a5901ab8059b66f8df_7f9802c4c8c85f2b8f99ee4f580d52f27485004015746189"),
("Cricket","pdf_c64dc37104cd00a5901ab8059b66f8df_e4b7dde4d9bcd92f92fdbf1cb78011607485004015746189"),
("Code Talkers","pdf_c64dc37104cd00a5901ab8059b66f8df_e8769b93fe9a503fa0f83208313af57d7485004015746189"),
("Chef Morty's Party Surprise","pdf_c64dc37104cd00a5901ab8059b66f8df_aa3ca7a472f2df0e60a75cd9cf2c1fa07485004015746189"),
("Canada","pdf_c64dc37104cd00a5901ab8059b66f8df_73cc871526bf6f2c0875d61cbdb0b7c97485004015746189"),
("Butterflies and Moths","pdf_c64dc37104cd00a5901ab8059b66f8df_932af36d7d20ca060cd3e1cbe967ae877485004015746189"),
("Building Big Dreams","pdf_c64dc37104cd00a5901ab8059b66f8df_f0c41144ad8b6e564e06d37e2f1a09be7485004015746189"),
("Bites and Stings","pdf_c64dc37104cd00a5901ab8059b66f8df_7cd19daa6cb2eaa9a27047ee124a3a487485004015746189"),
("Bears","pdf_c64dc37104cd00a5901ab8059b66f8df_1fc44eb5dbbefa019a362892aced44437485004015746189"),
("Baseball","pdf_c64dc37104cd00a5901ab8059b66f8df_31ed5684deb0be4ee37f9c1744f524277485004015746189"),
("Argentina","pdf_c64dc37104cd00a5901ab8059b66f8df_8cb7746009936205c9120221a5bfc4fb7485004015746189"),
("Barack Obama","pdf_c64dc37104cd00a5901ab8059b66f8df_28d0bca7df488d2b36a3bc8603494d2d7485004015746189"),
("April Fools' Day","pdf_c64dc37104cd00a5901ab8059b66f8df_cd4d1fb129541b1279c1a42bc23a94b27485004015746189"),
("Animals Feel Emotions","pdf_c64dc37104cd00a5901ab8059b66f8df_523bbb7a888352d8078c8f70e65a5c9b7485004015746189"),
("Aesop's Fables","pdf_c64dc37104cd00a5901ab8059b66f8df_fb61507c6843a87182d6eb1ede71711a7485004015746189"),
("A Selection From Alice in Wonderland","pdf_c64dc37104cd00a5901ab8059b66f8df_770a69c4da8c5a2d77d8e1877095887d7485004015746189"),
("A Big League for Little Players","pdf_c64dc37104cd00a5901ab8059b66f8df_6889f2f895877987197695493f390c067485004015746189"),
("World Traveler Ibn Battuta","pdf_c64dc37104cd00a5901ab8059b66f8df_59ffd6e7cdf5c6888352f7efe47831267485004015746189"),
]

def slugify(t):
    s = t.lower().replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

out = []
for title, mid in RAW:
    out.append({"slug": slugify(title), "title": title, "media_id": mid})

assert len(out) == 73, len(out)
slugs = [o["slug"] for o in out]
assert len(set(slugs)) == 73, "duplicate slugs: " + str([s for s in slugs if slugs.count(s)>1])

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "_quizdata", "_titles.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Wrote %d books to _quizdata/_titles.json" % len(out))
print("sample:", out[0])
print("last:", out[-1])
