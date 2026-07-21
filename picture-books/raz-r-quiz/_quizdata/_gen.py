# -*- coding: utf-8 -*-
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

KID = "Key Ideas and Details"
CRA = "Craft and Structure"
INT = "Integration of Knowledge and Ideas"
AUT = "Author's Purpose and Perspective"

books = []

# ---------------------------------------------------------------------------
# 1. Charlene's Sea of Cortez Journal
# ---------------------------------------------------------------------------
books.append({
    "slug": "charlene-s-sea-of-cortez-journal",
    "title": "Charlene's Sea of Cortez Journal",
    "titleZh": "查伦的科尔特斯海日记",
    "level": "R",
    "genre": "Narrative Nonfiction",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "How old was Charlene when she wrote her Sea of Cortez journal?",
                  "zh": "查伦写科尔特斯海日记时几岁？"},
            "options": [
                {"en": "Eight years old", "zh": "八岁"},
                {"en": "Ten years old", "zh": "十岁"},
                {"en": "Twelve years old", "zh": "十二岁"},
                {"en": "Six years old", "zh": "六岁"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "The journal states: \"My name is Charlene, and I am eight years old.\"",
                        "zh": "日记中写道：“我叫查伦，今年八岁。”"}
        },
        {
            "q": {"en": "At which place did Charlene and her family board the ship Sea Bird?",
                  "zh": "查伦一家是在哪个地方登上“海鸟号”船的？"},
            "options": [
                {"en": "La Paz", "zh": "拉巴斯"},
                {"en": "Guaymas", "zh": "瓜伊马斯"},
                {"en": "Catalina Island", "zh": "卡塔利娜岛"},
                {"en": "Bahia de Los Angeles", "zh": "洛杉矶湾"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "The book says: \"Last night, we boarded the ship Sea Bird at La Paz.\"",
                        "zh": "书中写道：“昨晚，我们在拉巴斯登上了‘海鸟号’船。”"}
        },
        {
            "q": {"en": "In the book, what is a \"boojum\"?",
                  "zh": "在书中，“boojum”是什么？"},
            "options": [
                {"en": "A tree that looks like an upside-down carrot", "zh": "一种看起来像倒立胡萝卜的树"},
                {"en": "A kind of sea lion", "zh": "一种海狮"},
                {"en": "A type of whale", "zh": "一种鲸鱼"},
                {"en": "A small desert bird", "zh": "一种小沙漠鸟"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary says a boojum is \"a tree that looks like an upside-down carrot and only grows on the Baja California peninsula.\"",
                        "zh": "词汇表说明 boojum 是“一种看起来像倒立胡萝卜、只生长在加利福尼亚半岛的树”。"}
        },
        {
            "q": {"en": "What activity did Charlene do at Los Islotes on Monday?",
                  "zh": "星期一在洛斯伊斯洛特斯岛，查伦做了什么活动？"},
            "options": [
                {"en": "Snorkel and swim with the sea lions", "zh": "和海狮一起浮潜、游泳"},
                {"en": "Kayak in a two-seater", "zh": "划双人皮划艇"},
                {"en": "Hike to find fossils", "zh": "徒步去寻找化石"},
                {"en": "Watch dolphins with binoculars", "zh": "用望远镜看海豚"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "On Monday at Los Islotes, \"We were allowed to snorkel and swim with the sea lions.\"",
                        "zh": "星期一在洛斯伊斯洛特斯岛，“我们被允许和海狮一起浮潜、游泳。”"}
        },
        {
            "q": {"en": "According to the journal, which whale is described as the biggest creature on Earth?",
                  "zh": "根据日记，哪种鲸鱼被描述为“地球上最大的生物”？"},
            "options": [
                {"en": "The blue whale", "zh": "蓝鲸"},
                {"en": "The fin whale", "zh": "长须鲸"},
                {"en": "The pilot whale", "zh": "领航鲸"},
                {"en": "The bottle-nosed dolphin", "zh": "宽吻海豚"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "On Friday Charlene writes they were next to \"the biggest creature on Earth—a blue whale.\"",
                        "zh": "星期五查伦写道，他们身旁是“地球上最大的生物——一头蓝鲸”。"}
        },
        {
            "q": {"en": "How are the blue whale and the fin whale different in size?",
                  "zh": "蓝鲸和长须鲸在体型上有什么不同？"},
            "options": [
                {"en": "The blue whale is the biggest on Earth, while the fin whale is the second largest",
                 "zh": "蓝鲸是地球上最大的，长须鲸是第二大"},
                {"en": "They are exactly the same size", "zh": "它们体型完全一样"},
                {"en": "The fin whale is bigger than the blue whale", "zh": "长须鲸比蓝鲸更大"},
                {"en": "Both are smaller than dolphins", "zh": "两者都比海豚小"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "The book calls the blue whale \"the biggest creature on Earth\" and says fin whales \"are the second largest whales in the ocean.\"",
                        "zh": "书中称蓝鲸为“地球上最大的生物”，并说长须鲸“是海洋中第二大的鲸鱼”。"}
        },
        {
            "q": {"en": "On which day did Charlene see hundreds of dolphins surrounding the ship?",
                  "zh": "查伦是在星期几看到数百只海豚包围了船？"},
            "options": [
                {"en": "Thursday", "zh": "星期四"},
                {"en": "Monday", "zh": "星期一"},
                {"en": "Friday", "zh": "星期五"},
                {"en": "Sunday", "zh": "星期日"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The Thursday entry begins: \"Breakfast this morning was interrupted by the captain letting us know that there were dolphins close by,\" and soon \"hundreds of dolphins surrounding the ship.\"",
                        "zh": "星期四的日记开头写道：“今天早餐时被船长打断，他告诉我们附近有海豚”，不久就出现了“数百只海豚包围了船”。"}
        },
        {
            "q": {"en": "Why did Charlene and the others have to walk very carefully on Isla Rasa?",
                  "zh": "为什么查伦等人在拉萨岛必须非常小心地走路？"},
            "options": [
                {"en": "To avoid stepping on any bird nests or eggs", "zh": "为了不踩到鸟巢或鸟蛋"},
                {"en": "Because the ground was slippery from rain", "zh": "因为地面被雨淋得很滑"},
                {"en": "Because it was very dark", "zh": "因为天非常黑"},
                {"en": "To stay quiet so the whales wouldn't hear them", "zh": "为了安静不让鲸鱼听见"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "On Isla Rasa, \"The noise they make is deafening. We had to walk very carefully to make sure we didn't step on any nests or eggs.\"",
                        "zh": "在拉萨岛，“它们的叫声震耳欲聋。我们不得不非常小心地走，确保不踩到任何鸟巢或鸟蛋。”"}
        },
        {
            "q": {"en": "What is the main purpose of Charlene's writing in this book?",
                  "zh": "查伦写这本书的主要目的是什么？"},
            "options": [
                {"en": "To record her daily experiences on a cruise", "zh": "记录她乘船游览时的每日经历"},
                {"en": "To teach readers how to fly a plane", "zh": "教读者如何开飞机"},
                {"en": "To explain how chocolate is made", "zh": "解释巧克力是如何制作的"},
                {"en": "To tell a scary ghost story", "zh": "讲一个恐怖鬼故事"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The book is Charlene's personal journal: \"This is my journal. I am going to write in it every day while I am on a cruise.\"",
                        "zh": "这本书是查伦的私人日记：“这是我的日记。我要在乘船游览期间每天都写。”"}
        },
        {
            "q": {"en": "How did Charlene feel about her cruise vacation?",
                  "zh": "查伦对她的乘船度假有什么感受？"},
            "options": [
                {"en": "She loved it and called it a wonderful vacation", "zh": "她很喜爱，称它是一次美妙的度假"},
                {"en": "She was bored and wanted to go home", "zh": "她很无聊，想回家"},
                {"en": "She was frightened the whole time", "zh": "她一直很害怕"},
                {"en": "She did not like the food", "zh": "她不喜欢那里的食物"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "At the end she writes: \"I will always remember this wonderful vacation and the new friends that I have made.\"",
                        "zh": "在结尾她写道：“我将永远记得这次美妙的度假，以及我交到的新朋友。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Imagine you are Charlene writing one more journal page about your favorite animal from the trip. Which animal would you choose and why?",
                   "zh": "想象你是查伦，再写一篇日记，写写旅途中你最喜欢的动物。你会选哪种动物？为什么？"},
        "guidance": {
            "en": ["Name the animal and the day you saw it (e.g., sea lions on Monday, dolphins on Thursday, blue whales on Friday).",
                   "Describe what it looked like or did, and explain why it was your favorite using details from the book."],
            "zh": ["说出动物名称以及你看到它的星期（如星期一的海狮、星期四的海豚、星期五的蓝鲸）。",
                   "描述它的样子或行为，并结合书中的细节说明为什么它是你的最爱。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 2. Bessie Coleman
# ---------------------------------------------------------------------------
books.append({
    "slug": "bessie-coleman",
    "title": "Bessie Coleman",
    "titleZh": "贝西·科尔曼",
    "level": "R",
    "genre": "Biography",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "When and where was Bessie Coleman born?",
                  "zh": "贝西·科尔曼何时何地出生？"},
            "options": [
                {"en": "In 1892 in Atlanta, Texas", "zh": "1892年生于得克萨斯州亚特兰大"},
                {"en": "In 1921 in Chicago, Illinois", "zh": "1921年生于伊利诺伊州芝加哥"},
                {"en": "In 1892 in Waxahachie, Texas", "zh": "1892年生于得克萨斯州瓦克萨哈奇"},
                {"en": "In 1900 in Oklahoma", "zh": "1900年生于俄克拉荷马"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Bessie Coleman was born in Atlanta, Texas, in 1892.\"",
                        "zh": "“贝西·科尔曼于1892年出生在得克萨斯州亚特兰大。”"}
        },
        {
            "q": {"en": "Why did Bessie have to travel to France to learn to fly?",
                  "zh": "贝西为什么要去法国学习飞行？"},
            "options": [
                {"en": "No one in the United States would teach a black woman to fly", "zh": "美国没有人愿意教一名黑人女性飞行"},
                {"en": "Flying schools in the U.S. were too expensive", "zh": "美国的飞行学校太贵"},
                {"en": "She wanted to visit the Eiffel Tower", "zh": "她想去参观埃菲尔铁塔"},
                {"en": "Her brothers lived there", "zh": "她的兄弟住在那里"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"But who would teach her? No one she asked would teach a black woman to fly.\" Her friend Robert Abbott told her to go to France.",
                        "zh": "“可是谁来教她呢？她问过的人都不愿教一名黑人女性飞行。”她的朋友罗伯特·阿博特建议她去法国。"}
        },
        {
            "q": {"en": "In the book, what is a \"barnstormer\"?",
                  "zh": "在书中，“barnstormer”（巡回飞行表演者）是什么意思？"},
            "options": [
                {"en": "A pilot who traveled around performing shows, often in farmers' fields", "zh": "四处巡回表演飞行、常在农场田野上表演的飞行员"},
                {"en": "A person who builds airplanes", "zh": "制造飞机的人"},
                {"en": "A type of airplane with two wings", "zh": "一种双翼飞机"},
                {"en": "A teacher of flying lessons", "zh": "飞行课老师"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines barnstormer as \"a person who travels the country performing shows in rural areas, often on farms.\"",
                        "zh": "词汇表将 barnstormer 定义为“在全国各地、常在农场等农村地区巡回表演的人”。"}
        },
        {
            "q": {"en": "In what year, and at what age, did Bessie earn her pilot's license?",
                  "zh": "贝西是在哪一年、几岁时获得飞行执照的？"},
            "options": [
                {"en": "In 1921, at age 29", "zh": "1921年，29岁"},
                {"en": "In 1920, at age 28", "zh": "1920年，28岁"},
                {"en": "In 1922, at age 30", "zh": "1922年，30岁"},
                {"en": "In 1919, at age 27", "zh": "1919年，27岁"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"In 1921, at the age of 29, Bessie became the first African-American female pilot… the first African-American to earn an international pilot's license.\"",
                        "zh": "“1921年，29岁的贝西成为第一位非裔美国女性飞行员……也是第一位获得国际飞行执照的非裔美国人。”"}
        },
        {
            "q": {"en": "How was Eugene Bullard connected to Bessie's dream?",
                  "zh": "尤金·巴拉德与贝西的梦想有什么联系？"},
            "options": [
                {"en": "He was an African-American who flew for France and inspired her", "zh": "他是一名为非国飞行的非裔美国人，激励了她"},
                {"en": "He was her flying instructor in France", "zh": "他是她在法国的飞行教练"},
                {"en": "He owned the barbershop where she worked", "zh": "他拥有她工作的理发店"},
                {"en": "He was the captain of her ship", "zh": "他是她那艘船的船长"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "Bessie \"was especially inspired by one, Eugene Bullard, an African-American who flew for the French.\"",
                        "zh": "贝西“尤其受到其中一人尤金·巴拉德的鼓舞，他是一名为非国飞行的非裔美国人。”"}
        },
        {
            "q": {"en": "Why did Bessie perform at air shows?",
                  "zh": "贝西为什么参加飞行表演？"},
            "options": [
                {"en": "To make money so she could start a flying school", "zh": "为了赚钱，以便开办一所飞行学校"},
                {"en": "Because she did not like flying alone", "zh": "因为她不喜欢独自飞行"},
                {"en": "To travel to France again", "zh": "为了再次去法国"},
                {"en": "Because the law required it", "zh": "因为法律有此要求"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"She wanted to start a flying school for others… the best way for a pilot to make money was to perform at air shows.\"",
                        "zh": "“她想为别人开办一所飞行学校……飞行员赚钱的最好方式就是参加飞行表演。”"}
        },
        {
            "q": {"en": "What happened right after Bessie earned her pilot's license?",
                  "zh": "贝西获得飞行执照后紧接着发生了什么？"},
            "options": [
                {"en": "She returned to America and later performed in air shows", "zh": "她回到美国，后来参加了飞行表演"},
                {"en": "She moved to Chicago to be a manicurist", "zh": "她搬到芝加哥做美甲师"},
                {"en": "She married her mechanic William Wills", "zh": "她嫁给了机械师威廉·威尔斯"},
                {"en": "She opened a flying school immediately", "zh": "她立刻开办了飞行学校"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "\"In the fall of 1921, Bessie returned to America… Robert Abbott helped her organize an air show near New York City on September 3, 1922.\"",
                        "zh": "“1921年秋，贝西回到美国……罗伯特·阿博特帮她在1922年9月3日于纽约附近组织了一场飞行表演。”"}
        },
        {
            "q": {"en": "Why does the book mention Mae Jemison, the first African-American woman in space?",
                  "zh": "书中为什么提到首位进入太空的非裔美国女性梅·杰米森？"},
            "options": [
                {"en": "To show that Bessie paved the way for later African-American achievers", "zh": "为了表明贝西为后来的非裔美国杰出人物铺平了道路"},
                {"en": "To explain how airplanes are built", "zh": "为了解释飞机是如何制造的"},
                {"en": "To compare their heights", "zh": "为了比较她们的身高"},
                {"en": "To describe a parachute jump", "zh": "为了描述一次跳伞"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The book says Bessie \"paved the way for women like Mae Jemison,\" who admires Bessie's courage.",
                        "zh": "书中说贝西“为梅·杰米森这样的女性铺平了道路”，杰米森钦佩贝西的勇气。"}
        },
        {
            "q": {"en": "What personal trait does the book most highlight about Bessie?",
                  "zh": "这本书最突出地强调了贝西的哪种品质？"},
            "options": [
                {"en": "Determination to fight discrimination and follow her dream", "zh": "反抗歧视、追寻梦想的坚定决心"},
                {"en": "A fear of airplanes", "zh": "对飞机的恐惧"},
                {"en": "A love of cotton picking", "zh": "对摘棉花的喜爱"},
                {"en": "A dislike of math", "zh": "对数学的讨厌"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"Her determination opened doors for other African-Americans and women who came after her.\"",
                        "zh": "“她的决心为后来其他非裔美国人和女性打开了大门。”"}
        },
        {
            "q": {"en": "How did Bessie Coleman die?",
                  "zh": "贝西·科尔曼是如何去世的？"},
            "options": [
                {"en": "The plane spun, she fell out (without a seat belt), and was killed", "zh": "飞机旋转，她没系安全带摔出机外身亡"},
                {"en": "She crashed into the ocean", "zh": "她坠入海中"},
                {"en": "She died of old age in Chicago", "zh": "她在芝加哥安老去世"},
                {"en": "She was struck by lightning", "zh": "她被闪电击中"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"Bessie didn't wear her seat belt… The plane suddenly went into a spin. Bessie fell out of the plane and was killed.\"",
                        "zh": "“贝西没有系安全带……飞机突然旋转起来。贝西摔出机外，不幸身亡。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Bessie Coleman opened doors for others. Name one person or group she inspired, and write a sentence about why her story matters today.",
                   "zh": "贝西·科尔曼为他人打开了大门。说出她激励的一个人或群体，并写一句话说明她的故事为何今天仍然重要。"},
        "guidance": {
            "en": ["Use details from the book, such as Mae Jemison or the Bessie Coleman Aero Club.",
                   "Explain how her courage against discrimination is still meaningful."],
            "zh": ["运用书中的细节，例如梅·杰米森或贝西·科尔曼飞行俱乐部。",
                   "说明她反抗歧视的勇气为何至今仍有意义。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 3. Basketball
# ---------------------------------------------------------------------------
books.append({
    "slug": "basketball",
    "title": "Basketball",
    "titleZh": "篮球",
    "level": "R",
    "genre": "Informational",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "Who invented basketball, and in what year?",
                  "zh": "谁发明了篮球？在哪一年？"},
            "options": [
                {"en": "Dr. James Naismith, in 1891", "zh": "詹姆斯·奈史密斯博士，1891年"},
                {"en": "Michael Jordan, in 1984", "zh": "迈克尔·乔丹，1984年"},
                {"en": "George Mikan, in 1950", "zh": "乔治·迈肯，1950年"},
                {"en": "A coach in France, in 1900", "zh": "一位法国教练，1900年"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Although basketball is now a global sport, it started small in 1891. Dr. James Naismith… hit gold by nailing a peach basket up on the wall.\"",
                        "zh": "“虽然篮球如今是一项全球性运动，它于1891年从小处起步。詹姆斯·奈史密斯博士……把一只桃篮钉在墙上，从而大获成功。”"}
        },
        {
            "q": {"en": "How many players are on each team during a basketball game?",
                  "zh": "一场篮球比赛每队有多少名球员？"},
            "options": [
                {"en": "Five players", "zh": "五名球员"},
                {"en": "Six players", "zh": "六名球员"},
                {"en": "Seven players", "zh": "七名球员"},
                {"en": "Two players", "zh": "两名球员"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Two teams of five players play a game of basketball.\"",
                        "zh": "“篮球比赛由两支各五人的队伍进行。”"}
        },
        {
            "q": {"en": "In the book, what is a \"foul shot\"?",
                  "zh": "在书中，“foul shot”（罚球）是什么？"},
            "options": [
                {"en": "A free throw from the foul line given after a rule is broken", "zh": "犯规后从罚球线进行的自由投篮"},
                {"en": "A shot worth three points", "zh": "值三分的投篮"},
                {"en": "A shot from half-court", "zh": "中场投篮"},
                {"en": "A type of basketball hoop", "zh": "一种篮球筐"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary says a foul shot is \"a free throw from the foul line… given to a player after another player has broken a rule.\"",
                        "zh": "词汇表说明 foul shot 是“在对方犯规后，从罚球线进行的自由投篮”。"}
        },
        {
            "q": {"en": "In what year did the National Basketball Association (NBA) begin?",
                  "zh": "美国职业篮球联赛（NBA）始于哪一年？"},
            "options": [
                {"en": "1949", "zh": "1949年"},
                {"en": "1891", "zh": "1891年"},
                {"en": "1992", "zh": "1992年"},
                {"en": "1920", "zh": "1920年"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Basketball remained mostly an American pastime until 1949, when the National Basketball Association (NBA) began.\"",
                        "zh": "“篮球在1949年美国职业篮球联赛（NBA）成立之前，基本只是一项美国人的消遣。”"}
        },
        {
            "q": {"en": "How do the tallest and shortest NBA players compare in height?",
                  "zh": "NBA最高和最矮的球员身高相差多少？"},
            "options": [
                {"en": "The tallest were 7'7\" (Manute Bol and Gheorghe Muresan) and the shortest was 5'3\" (Muggsy Bogues)",
                 "zh": "最高为7英尺7英寸（马努特·波尔和格奥尔基·穆雷桑），最矮为5英尺3英寸（穆格斯·博格斯）"},
                {"en": "Both were exactly 6'10\"", "zh": "两人都正好6英尺10英寸"},
                {"en": "The tallest was 6'10\" and the shortest was 5'0\"", "zh": "最高6英尺10英寸，最矮5英尺"},
                {"en": "There is no record of player heights", "zh": "没有球员身高的记录"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"The tallest players ever in the NBA were Manute Bol and Gheorghe Muresan, who were both 7 feet 7 inches… Muggsy Bogues was the shortest NBA player in history, at 5 feet 3 inches.\"",
                        "zh": "“NBA史上最高的球员是马努特·波尔和格奥尔基·穆雷桑，均为7英尺7英寸……穆格斯·博格斯是NBA史上最矮的球员，身高5英尺3英寸。”"}
        },
        {
            "q": {"en": "Why was the backboard invented?",
                  "zh": "篮板是被发明出来的原因是什么？"},
            "options": [
                {"en": "To stop spectators in the balcony from knocking away shots", "zh": "为了阻止楼座上的观众把球拍掉"},
                {"en": "To make the hoop smaller", "zh": "为了让篮筐更小"},
                {"en": "To help players dribble", "zh": "为了帮助球员运球"},
                {"en": "To measure the score", "zh": "为了记分"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "A \"Do You Know?\" note says: \"The backboard was invented to stop spectators in the balcony from knocking away shots!\"",
                        "zh": "“你知道吗？”中写道：“篮板被发明出来，是为了阻止楼座上的观众把球拍掉！”"}
        },
        {
            "q": {"en": "What does \"amateur\" mean in this book?",
                  "zh": "在本书中，“amateur”（业余的）是什么意思？"},
            "options": [
                {"en": "Not professional; done as a hobby", "zh": "非职业的；作为爱好来做"},
                {"en": "A paid professional player", "zh": "领薪的职业球员"},
                {"en": "A type of basketball position", "zh": "一种篮球位置"},
                {"en": "A referee's whistle", "zh": "裁判的哨子"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines amateur as \"not professional; done as a hobby.\"",
                        "zh": "词汇表将 amateur 定义为“非职业的；作为爱好来做”。"}
        },
        {
            "q": {"en": "How many points does a team earn for a shot made from behind the three-point line?",
                  "zh": "球队在三分线外投中一球得几分？"},
            "options": [
                {"en": "Three points", "zh": "三分"},
                {"en": "Two points", "zh": "两分"},
                {"en": "One point", "zh": "一分"},
                {"en": "Four points", "zh": "四分"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"A team earns two points for making a shot, three points for making a shot from behind the three-point line, and one point for each foul shot.\"",
                        "zh": "“投中得两分，三分线外投中得三分，每次罚球得一分。”"}
        },
        {
            "q": {"en": "What is the book's focus question?",
                  "zh": "这本书的核心问题是什么？"},
            "options": [
                {"en": "\"How has basketball changed over time?\"", "zh": "“篮球是如何随着时间改变的？”"},
                {"en": "\"Who is the tallest player?\"", "zh": "“谁是最高的球员？”"},
                {"en": "\"Why do people love golf?\"", "zh": "“人们为什么喜欢高尔夫？”"},
                {"en": "\"How do you bake brownies?\"", "zh": "“怎么做布朗尼？”"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The focus question on the title page reads: \"How has basketball changed over time?\"",
                        "zh": "标题页上的核心问题是：“篮球是如何随着时间改变的？”"}
        },
        {
            "q": {"en": "Why does the book mention George Mikan?",
                  "zh": "书中为什么提到乔治·迈肯？"},
            "options": [
                {"en": "He was the first 'big man' who changed basketball into a game of giants", "zh": "他是第一位“大个子”，把篮球变成了巨人的运动"},
                {"en": "He invented the peach basket", "zh": "他发明了桃篮"},
                {"en": "He was the shortest player", "zh": "他是最矮的球员"},
                {"en": "He started the NBA", "zh": "他创办了NBA"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"He was the first of the 'big men' who changed basketball from being a sport of small and quick players into that of giants.\"",
                        "zh": "“他是‘大个子’中的第一人，把篮球从一项由矮小敏捷球员主导的运动，变成了巨人的运动。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "The book asks 'How has basketball changed over time?' List two changes from the book and one way the game is still the same.",
                   "zh": "书中问“篮球是如何随着时间改变的？”列出书中的两个变化，以及这项运动至今仍相同的一点。"},
        "guidance": {
            "en": ["Changes could include: started with a peach basket in 1891, NBA began in 1949, became global after the 1992 Dream Team.",
                   "Same: still two teams of five trying to shoot into the opponent's hoop."],
            "zh": ["变化可包括：1891年始于桃篮；1949年NBA成立；1992年“梦之队”后走向全球。",
                   "相同：仍是两队各五人，力争把球投进对方篮筐。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 4. April Fool's
# ---------------------------------------------------------------------------
books.append({
    "slug": "april-fool-s",
    "title": "April Fool's",
    "titleZh": "四月愚人节",
    "level": "R",
    "genre": "Fiction",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "Who is the narrator sent to see at the beginning of the story?",
                  "zh": "故事开头，叙述者被带去见谁？"},
            "options": [
                {"en": "Principal Taylor", "zh": "泰勒校长"},
                {"en": "Mrs. Shoemaker", "zh": "舒梅克老师"},
                {"en": "Mr. Kendall", "zh": "肯德尔先生"},
                {"en": "Rob Turtle", "zh": "罗布·特特尔"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"As I walk into Principal Taylor's office, I wonder who glued Mrs. Shoemaker to her chair.\"",
                        "zh": "“当我走进泰勒校长的办公室时，我想知道是谁把舒梅克老师粘在了椅子上。”"}
        },
        {
            "q": {"en": "What had someone done to Mrs. Shoemaker?",
                  "zh": "有人对舒梅克老师做了什么？"},
            "options": [
                {"en": "Glued her to her chair", "zh": "把她粘在了椅子上"},
                {"en": "Covered her with leaves", "zh": "用树叶盖住她"},
                {"en": "Put oil on the floor near her", "zh": "在她附近地板上泼油"},
                {"en": "Hid her tuba", "zh": "藏起了她的低音号"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"I wonder who glued Mrs. Shoemaker to her chair. It would have been a hilarious April Fool's prank if the old, faded glue bottle hadn't been hidden in my desk.\"",
                        "zh": "“我想知道是谁把舒梅克老师粘在了椅子上。如果那瓶旧而褪色胶水没藏在我桌里，这本是个滑稽的愚人节恶作剧。”"}
        },
        {
            "q": {"en": "In the book, what is a \"prank\"?",
                  "zh": "在书中，“prank”是什么？"},
            "options": [
                {"en": "A trick or practical joke", "zh": "一个恶作剧或玩笑"},
                {"en": "A school subject", "zh": "一门学校课程"},
                {"en": "A type of sandwich", "zh": "一种三明治"},
                {"en": "A kind of bird", "zh": "一种鸟"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines prank as \"a trick or practical joke.\"",
                        "zh": "词汇表将 prank 定义为“恶作剧或玩笑”。"}
        },
        {
            "q": {"en": "What was the students' punishment for the pranks?",
                  "zh": "学生们因这些恶作剧受到了什么惩罚？"},
            "options": [
                {"en": "Stay after school until all the pranks were cleaned up", "zh": "放学后留下，直到所有恶作剧被清理干净"},
                {"en": "They were sent home immediately", "zh": "他们被立刻送回家"},
                {"en": "They had to write a letter", "zh": "他们必须写一封信"},
                {"en": "They were given candy", "zh": "他们得到了糖果"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"As punishment, you will stay after school until all these pranks are cleaned up.\"",
                        "zh": "“作为惩罚，你们放学后必须留下，直到所有这些恶作剧被清理干净。”"}
        },
        {
            "q": {"en": "What did the narrator and Sarah find in the basement?",
                  "zh": "叙述者和萨拉在地下室发现了什么？"},
            "options": [
                {"en": "Rob Turtle's duffel bag with cooking-oil cans, a bologna wrapper, and scissors", "zh": "罗布·特特尔的旅行袋，里面有食用油罐、 Bologna 香肠包装纸和剪刀"},
                {"en": "A hidden treasure chest", "zh": "一个藏起来的宝箱"},
                {"en": "Mrs. Shoemaker's chair", "zh": "舒梅克老师的椅子"},
                {"en": "A box of old books only", "zh": "只发现一箱旧书"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"This is Rob Turtle's duffel bag; his initials RT are on the straps,\" … Inside are old cans that say 'cooking oil' … a paper wrapper … and an ancient-looking pair of scissors.",
                        "zh": "“这是罗布·特特尔的旅行袋；背带上有他的缩写RT”……里面有写着“食用油”的旧罐子……一张包装纸……以及一把看起来很古老的剪刀。"}
        },
        {
            "q": {"en": "Who does the evidence in the basement suggest really planned the pranks?",
                  "zh": "地下室的证据暗示，究竟是谁真正策划了这些恶作剧？"},
            "options": [
                {"en": "Rob Turtle, whose bag held the prank supplies", "zh": "罗布·特特尔，因为包里装着恶作剧用品"},
                {"en": "Principal Taylor", "zh": "泰勒校长"},
                {"en": "The narrator's little brother Jake", "zh": "叙述者的小弟弟杰克"},
                {"en": "A janitor", "zh": "一名看门人"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"This doesn't tell us who the laughing kids are, but it looks as if Rob Turtle framed us all.\" Rob had said he lost his gym bag in the Hollow.",
                        "zh": "“这没告诉我们那些笑的孩子是谁，但看起来像是罗布·特特尔栽赃我们所有人。”罗布曾说他在“洼地”丢了他的运动包。"}
        },
        {
            "q": {"en": "What did the narrator and Sarah do with the bag after finding it?",
                  "zh": "发现包后，叙述者和萨拉怎么处理它？"},
            "options": [
                {"en": "Left it in the cafeteria so someone would turn it in to lost and found", "zh": "把它留在食堂，让别人交到失物招领处"},
                {"en": "Gave it directly to Principal Taylor", "zh": "直接交给了泰勒校长"},
                {"en": "Threw it in the river", "zh": "把它扔进了河里"},
                {"en": "Kept it for themselves", "zh": "自己留着了"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "\"Let's leave it in the cafeteria,\" I suggest. \"Someone will turn it in to the lost and found.\"",
                        "zh": "“我们把它留在食堂吧，”我提议，“会有人把它交到失物招领处的。”"}
        },
        {
            "q": {"en": "Where may the tradition of April Fool's Day come from, according to the book?",
                  "zh": "根据书中说法，愚人节传统可能源自哪里？"},
            "options": [
                {"en": "A 16th-century French calendar change moving New Year's Day from April 1 to January", "zh": "16世纪法国更改历法，把新年从4月1日改到1月"},
                {"en": "An old American school rule", "zh": "一条古老的美国校规"},
                {"en": "A Chinese festival", "zh": "一个中国节日"},
                {"en": "A birthday of Principal Taylor", "zh": "泰勒校长的生日"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"It may stem from a calendar change in 16th century France -- the moving of New Year's Day from April 1 to January.\"",
                        "zh": "“它可能源自16世纪法国的一次历法更改——把新年从4月1日改到1月。”"}
        },
        {
            "q": {"en": "What kind of story is 'April Fool's'?",
                  "zh": "《四月愚人节》是一个什么样的故事？"},
            "options": [
                {"en": "A mystery story with suspense", "zh": "一个带有悬念的神秘故事"},
                {"en": "A science textbook", "zh": "一本科普教科书"},
                {"en": "A biography", "zh": "一本传记"},
                {"en": "A recipe book", "zh": "一本食谱书"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The book is a fictional story where the narrator and Sarah sneak into a basement to solve a mystery about who framed them.",
                        "zh": "这本书是一个虚构故事，叙述者和萨拉潜入地下室，去解开是谁栽赃他们的谜团。"}
        },
        {
            "q": {"en": "What had someone used to block the toilets in the bathrooms?",
                  "zh": "有人用什么堵住了洗手间的马桶？"},
            "options": [
                {"en": "Handfuls of dead leaves", "zh": "一把把枯树叶"},
                {"en": "Cooking oil", "zh": "食用油"},
                {"en": "Bologna", "zh": "Bologna 香肠"},
                {"en": "Old books", "zh": "旧书"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Someone also stuck old bologna under the cafeteria tables… Someone covered the gym floor with vegetable oil and blocked the toilets in the bathrooms with handfuls of dead leaves.\"",
                        "zh": "“还有人把旧 Bologna 香肠塞在食堂桌子底下……有人用植物油盖住体育馆地板，并用一把把枯树叶堵住洗手间的马桶。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "The narrator thinks Rob Turtle framed them. Do you agree? Use clues from the basement to support your opinion.",
                   "zh": "叙述者认为是罗布·特特尔栽赃了他们。你同意吗？用地下室里的线索来支持你的看法。"},
        "guidance": {
            "en": ["Mention the duffel bag with RT initials, the cooking-oil cans, and the bologna wrapper.",
                   "Note Rob said he lost his bag in the Hollow, which connects him to the supplies."],
            "zh": ["提到带RT缩写的旅行袋、食用油罐和 Bologna 香肠包装纸。",
                   "注意罗布说他在“洼地”丢了包，这把他和那些物品联系了起来。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 5. Arrows
# ---------------------------------------------------------------------------
books.append({
    "slug": "arrows",
    "title": "Arrows",
    "titleZh": "箭头",
    "level": "R",
    "genre": "Historical Fiction",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "Who discovers the first arrow carved in the rock?",
                  "zh": "是谁发现了刻在岩石上的第一个箭头？"},
            "options": [
                {"en": "Poloma", "zh": "波洛玛"},
                {"en": "Papa (her grandfather)", "zh": "爸爸（她爷爷）"},
                {"en": "A Choctaw soldier", "zh": "一名乔克托士兵"},
                {"en": "A spy from the Civil War", "zh": "一名内战时期的间谍"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "Poloma \"was digging the ball out from the heavy undergrowth when she noticed the arrow. It was carved into the lower part of the massive rock.\"",
                        "zh": "波洛玛“在茂密灌木下挖球时，注意到了那个箭头。它是刻在那块巨石下半部分的。”"}
        },
        {
            "q": {"en": "What was Poloma's grandfather (Papa) in real history?",
                  "zh": "波洛玛的爷爷（爸爸）在真实历史中是什么身份？"},
            "options": [
                {"en": "A Choctaw Code Talker who sent secret messages in World War II", "zh": "一名在二战中用土著语言发送密信的乔克托密码通讯兵"},
                {"en": "A pilot in the French air force", "zh": "法国空军的一名飞行员"},
                {"en": "A teacher of Greek history", "zh": "一名希腊历史老师"},
                {"en": "A sailor on the Sea Bird", "zh": "“海鸟号”上的一名水手"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Papa and other Native American Code Talkers had helped the United States… win the war by sending secret messages.\" He was a Choctaw Code Talker.",
                        "zh": "“爸爸和其他美洲原住民密码通讯兵通过发送密信帮助美国……赢得战争。”他是一名乔克托密码通讯兵。"}
        },
        {
            "q": {"en": "In the book, what is a \"cipher\"?",
                  "zh": "在书中，“cipher”（密码）是什么？"},
            "options": [
                {"en": "A code that substitutes letters or numbers for the real letters in a message",
                 "zh": "一种用字母或数字替换信息中真实字母的密码"},
                {"en": "A kind of arrow carved in rock", "zh": "刻在石头上的一种箭头"},
                {"en": "A type of tree", "zh": "一种树"},
                {"en": "A group of seven stars", "zh": "一组七颗星"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "Poloma \"knew what a cipher was. It was a code that substituted letters or numbers for the real letters in a message.\"",
                        "zh": "波洛玛“知道什么是密码。它是一种用字母或数字替换信息中真实字母的代码。”"}
        },
        {
            "q": {"en": "In the advance cipher used in the story, what does the word \"uif\" stand for?",
                  "zh": "在故事使用的递进密码中，“uif”代表哪个词？"},
            "options": [
                {"en": "\"the\" (each letter is moved back one in the alphabet)", "zh": "“the”（每个字母在字母表中往前移一位）"},
                {"en": "\"and\"", "zh": "“and”"},
                {"en": "\"sky\"", "zh": "“sky”"},
                {"en": "\"bird\"", "zh": "“bird”"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"The letter h comes before i, and the letter e comes before f. This is a substitute-letter cipher!\" So u→t, i→h, f→e, making \"uif\" = \"the\".",
                        "zh": "“h在i前面，e在f前面。这是一个字母替换密码！”所以u→t，i→h，f→e，使“uif”=“the”。"}
        },
        {
            "q": {"en": "How many arrows in all did Poloma and Papa follow?",
                  "zh": "波洛玛和爸爸一共跟随了多少个箭头？"},
            "options": [
                {"en": "Six arrows", "zh": "六个箭头"},
                {"en": "Two arrows", "zh": "两个箭头"},
                {"en": "Ten arrows", "zh": "十个箭头"},
                {"en": "One arrow", "zh": "一个箭头"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"There were six arrows in all.\" They led from boulder to boulder toward a stream.",
                        "zh": "“一共有六个箭头。”它们从一块巨石引向另一块巨石，通向一条小溪。"}
        },
        {
            "q": {"en": "Why did escaping slaves follow the Drinking Gourd?",
                  "zh": "逃跑的奴隶为什么要跟随“饮酒勺”（北斗七星）？"},
            "options": [
                {"en": "It is the Big Dipper in the northern sky that led them north to freedom", "zh": "它是北方天空中的北斗七星，引导他们向北走向自由"},
                {"en": "It pointed south to a safe river", "zh": "它指向南方一条安全的河"},
                {"en": "It was a kind of map made of arrows", "zh": "它是一种由箭头组成的地图"},
                {"en": "It was the name of their captain", "zh": "那是他们船长的名字"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"The Drinking Gourd is the group of seven stars now called the Big Dipper, which can always be found in the northern sky. Escaping slaves followed the Drinking Gourd… until they reached their freedom.\"",
                        "zh": "“饮酒勺是如今被称为北斗七星的那组七颗星，总能在北方天空找到。逃跑的奴隶跟随饮酒勺……直到获得自由。”"}
        },
        {
            "q": {"en": "After following the arrows, what did the boulder across the stream contain?",
                  "zh": "跟随箭头之后，小溪对岸的巨石上有什么？"},
            "options": [
                {"en": "A group of letters carved into the bottom (the secret message)", "zh": "底部刻着一组字母（秘密信息）"},
                {"en": "Another arrow pointing north", "zh": "另一个指向北方的箭头"},
                {"en": "A picture of a bird", "zh": "一只鸟的图案"},
                {"en": "A Choctaw flag", "zh": "一面乔克托旗"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "\"It's not an arrow at all. A bunch of letters are carved into the bottom of the boulder!\" They read gpmmpx uif esjoljoh hpvse.",
                        "zh": "“它根本不是箭头。巨石底部刻着一组字母！”他们读出 gpmmpx uif esjoljoh hpvse。"}
        },
        {
            "q": {"en": "What historical war does Papa connect the carved code to?",
                  "zh": "爸爸把刻着的密码与哪场历史战争联系起来？"},
            "options": [
                {"en": "The Civil War, when Northern spies used the advance cipher", "zh": "内战，当时北方间谍使用递进密码"},
                {"en": "World War II", "zh": "第二次世界大战"},
                {"en": "The Revolutionary War", "zh": "独立战争"},
                {"en": "The Vietnam War", "zh": "越南战争"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"About 150 years ago, the Civil War was fought… the soldiers and spies in the North used a special code… the advance cipher.\"",
                        "zh": "“大约150年前爆发了内战……北方的士兵和间谍使用了一种特殊密码……递进密码。”"}
        },
        {
            "q": {"en": "What real history is woven into this fictional story?",
                  "zh": "这个虚构故事中融入了哪些真实历史？"},
            "options": [
                {"en": "Choctaw Code Talkers of the World Wars and the Underground Railroad's Drinking Gourd", "zh": "两次世界大战中的乔克托密码通讯兵，以及地下铁路的“饮酒勺”"},
                {"en": "The invention of basketball", "zh": "篮球的发明"},
                {"en": "The first Moon landing", "zh": "首次登月"},
                {"en": "The California Gold Rush", "zh": "加利福尼亚淘金热"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "Papa is a Choctaw Code Talker, and the decoded message \"Follow the Drinking Gourd\" refers to the route escaping slaves used.",
                        "zh": "爸爸是乔克托密码通讯兵，而破译出的信息“跟随饮酒勺”指的是逃跑奴隶使用的路线。"}
        },
        {
            "q": {"en": "At the end, which direction did Poloma and Papa go?",
                  "zh": "结尾时，波洛玛和爸爸朝哪个方向走？"},
            "options": [
                {"en": "South, toward home", "zh": "向南，朝家的方向"},
                {"en": "North, following the Drinking Gourd", "zh": "向北，跟随饮酒勺"},
                {"en": "East, to the stream", "zh": "向东，去小溪"},
                {"en": "West, to the ocean", "zh": "向西，去海边"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"We need to go south, Papa. That's where we live.\" They turned and went home.",
                        "zh": "“我们得往南走，爸爸。我们家在那边。”他们转身回家了。"}
        }
    ],
    "extended": {
        "prompt": {"en": "The message 'Follow the Drinking Gourd' helped escaping slaves. In your own words, explain what the Drinking Gourd is and how it guided people.",
                   "zh": "“跟随饮酒勺”这句话帮助了逃跑的奴隶。用自己的话解释“饮酒勺”是什么，以及它如何为人们指引方向。"},
        "guidance": {
            "en": ["Say that the Drinking Gourd is the Big Dipper, a group of seven stars in the northern sky.",
                   "Explain that it always points north, so escaping slaves followed it to freedom."],
            "zh": ["说明饮酒勺就是北斗七星，是北方天空中的一组七颗星。",
                   "解释它总是指向北方，所以逃跑的奴隶跟随它走向自由。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 6. Animal Discoveries
# ---------------------------------------------------------------------------
books.append({
    "slug": "animal-discoveries",
    "title": "Animal Discoveries",
    "titleZh": "动物大发现",
    "level": "R",
    "genre": "Informational",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "About how many new animal species do scientists discover each year?",
                  "zh": "科学家每年大约发现多少种新动物？"},
            "options": [
                {"en": "More than 15,000 species", "zh": "超过15,000种"},
                {"en": "Fewer than 100 species", "zh": "不到100种"},
                {"en": "Exactly 1,000 species", "zh": "正好1,000种"},
                {"en": "Over one million species", "zh": "超过一百万种"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Scientists discover more than 15,000 animal species each year.\"",
                        "zh": "“科学家每年发现超过15,000种动物。”"}
        },
        {
            "q": {"en": "Where and when was the lesula monkey found?",
                  "zh": "lesula 猴是在哪里、何时被发现的？"},
            "options": [
                {"en": "In the forests of the Democratic Republic of Congo in 2007", "zh": "2007年在刚果民主共和国的森林中"},
                {"en": "In Borneo in 2010", "zh": "2010年在婆罗洲"},
                {"en": "In Madagascar in 2005", "zh": "2005年在马达加斯加"},
                {"en": "In New Guinea in 2013", "zh": "2013年在新几内亚"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"In 2007, a new species of monkey was found in the forests of the Democratic Republic of the Congo. The lesula has large eyes and is shy and quiet.\"",
                        "zh": "“2007年，在刚果民主共和国的森林中发现了一个猴子新种。lesula 有大大眼睛，害羞而安静。”"}
        },
        {
            "q": {"en": "In the book, what is a \"herpetologist\"?",
                  "zh": "在书中，“herpetologist”（爬虫学家）是什么？"},
            "options": [
                {"en": "A scientist who studies reptiles and amphibians", "zh": "研究爬行动物和两栖动物的科学家"},
                {"en": "A scientist who studies stars", "zh": "研究星星的科学家"},
                {"en": "A person who trains bats", "zh": "训练蝙蝠的人"},
                {"en": "A type of frog", "zh": "一种青蛙"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines herpetologist as \"a scientist who studies reptiles and amphibians.\"",
                        "zh": "词汇表将 herpetologist 定义为“研究爬行动物和两栖动物的科学家”。"}
        },
        {
            "q": {"en": "How is the Caquetá titi monkey different from other titi monkeys?",
                  "zh": "卡克塔卷尾猴与其他卷尾猴有什么不同？"},
            "options": [
                {"en": "It has a bushy red beard and no white bar on its forehead", "zh": "它有浓密的红胡子，额头上没有白色条纹"},
                {"en": "It is the tallest monkey in the world", "zh": "它是世界上最高的猴子"},
                {"en": "It can fly", "zh": "它会飞"},
                {"en": "It lives only in water", "zh": "它只生活在水中"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"The Caquetá is known for its bushy red beard. It doesn't have a white bar on its forehead as other titi monkeys do.\"",
                        "zh": "“卡克塔猴以浓密的红胡子闻名。它不像其他卷尾猴那样额头上有一条白色条纹。”"}
        },
        {
            "q": {"en": "Which frog is also called the Pinocchio frog because of its long nose?",
                  "zh": "哪种青蛙因为长鼻子又被称为“匹诺曹蛙”？"},
            "options": [
                {"en": "The long-nosed tree frog", "zh": "长鼻树蛙"},
                {"en": "The Matang narrow-mouthed frog", "zh": "马当小口蛙"},
                {"en": "The Gorgon's head starfish", "zh": "蛇发女妖海星"},
                {"en": "The blossom bat", "zh": "花蝠"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "The long-nosed tree frog \"is known for its long, unique nose… This tree frog is known for its long, unique nose… The frog has another name: the Pinocchio frog.\"",
                        "zh": "长鼻树蛙“以它独特的长鼻子闻名……这只树蛙还有一个名字：匹诺曹蛙。”"}
        },
        {
            "q": {"en": "How are 'cryptic species' finally identified as distinct?",
                  "zh": "“隐存种”最终是如何被确认为不同物种的？"},
            "options": [
                {"en": "By studying their genetic code (DNA)", "zh": "通过研究它们的基因密码（DNA）"},
                {"en": "By their different colors only", "zh": "仅凭不同颜色"},
                {"en": "By where they live", "zh": "凭它们住在哪里"},
                {"en": "By counting their legs", "zh": "数它们的腿"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"These are called cryptic species. They are only found to be distinct when scientists study their genetic code.\"",
                        "zh": "“这些被称为隐存种。只有在科学家研究它们的基因密码时，才被发现是不同的物种。”"}
        },
        {
            "q": {"en": "Where was the olinguito discovered, and why was it important?",
                  "zh": "olinguito（小熊浣熊）是在哪里发现的？为何重要？"},
            "options": [
                {"en": "In Ecuador and Colombia in 2013; the first such species found in the Americas in 35 years", "zh": "2013年在厄瓜多尔和哥伦比亚；35年来美洲发现的第一个此类物种"},
                {"en": "In Borneo in 2010; the smallest frog", "zh": "2010年在婆罗洲；最小的青蛙"},
                {"en": "In the Atlantic Ocean in 2010; a starfish", "zh": "2010年在大西洋；一种海星"},
                {"en": "In Madagascar; a lemur", "zh": "在马达加斯加；一种狐猴"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"In 2013, researchers discovered that… olinguitos… can be found in Ecuador and Colombia. It is the first species of this type to be discovered in the Americas in thirty-five years.\"",
                        "zh": "“2013年，研究者发现……olinguito 分布在厄瓜多尔和哥伦比亚。它是35年来美洲发现的第一个此类物种。”"}
        },
        {
            "q": {"en": "In the book, what is a \"species\"?",
                  "zh": "在书中，“species”（物种）是什么？"},
            "options": [
                {"en": "A group of living things that are physically similar and can reproduce", "zh": "一群外形相似、能够繁殖后代的生物"},
                {"en": "A type of weather", "zh": "一种天气"},
                {"en": "A kind of kite", "zh": "一种风筝"},
                {"en": "A number of calories", "zh": "一定数量的卡路里"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines species as \"a group of living things that are physically similar and can reproduce.\"",
                        "zh": "词汇表将 species 定义为“一群外形相似、能够繁殖后代的生物”。"}
        },
        {
            "q": {"en": "Why does the book say most animal species have yet to be discovered?",
                  "zh": "为什么书中说大多数动物物种尚未被发现？"},
            "options": [
                {"en": "Earth's oceans and remote areas are still largely unexplored", "zh": "地球的海洋和偏远地区大多仍未被探索"},
                {"en": "Scientists have stopped looking", "zh": "科学家已停止寻找"},
                {"en": "All animals are already known", "zh": "所有动物都已被认知"},
                {"en": "DNA cannot be studied", "zh": "DNA无法被研究"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"Experts agree that most have yet to be discovered,\" because large parts of the oceans and remote places are unexplored.",
                        "zh": "“专家们一致认为大多数尚未被发现”，因为海洋的大片区域和偏远之地仍未被探索。"}
        },
        {
            "q": {"en": "What main message does the book give about new discoveries?",
                  "zh": "关于新发现，这本书传达的主要信息是什么？"},
            "options": [
                {"en": "Each discovery brings hope and a reason to save habitats", "zh": "每一次发现都带来希望，也提醒我们要保护栖息地"},
                {"en": "New animals are not important", "zh": "新动物不重要"},
                {"en": "Only birds are worth finding", "zh": "只有鸟类值得去寻找"},
                {"en": "Discoveries should be ignored", "zh": "发现应被忽视"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"Yet each new discovery is also cause for hope. It can bring a renewed effort to save and even restore a habitat.\"",
                        "zh": "“然而每一次新发现也是希望的理由。它能带来新的努力，去保护甚至恢复栖息地。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Choose one animal from the book and write two facts about it, including where it was found.",
                   "zh": "从书中选一种动物，写出关于它的两个事实，包括它是在哪里被发现的。"},
        "guidance": {
            "en": ["Pick any animal (e.g., lesula monkey in Congo, olinguito in Ecuador/Colombia, walking bamboo shark in Indonesia).",
                   "Include the year and place, and one special feature from the book."],
            "zh": ["任选一种动物（如刚果的 lesula 猴、厄瓜多尔/哥伦比亚的 olinguito、印尼的步行竹鲨）。",
                   "包括发现年份和地点，以及书中的一个特别特征。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 7. An Apple a Day
# ---------------------------------------------------------------------------
books.append({
    "slug": "an-apple-a-day",
    "title": "An Apple a Day",
    "titleZh": "每天一个苹果",
    "level": "R",
    "genre": "Informational",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "What do proteins do for your body?",
                  "zh": "蛋白质对身体有什么作用？"},
            "options": [
                {"en": "They build and repair cells and help make strong muscles", "zh": "它们构建和修复细胞，帮助长出强壮的肌肉"},
                {"en": "They are only found in candy", "zh": "它们只存在于糖果中"},
                {"en": "They make you sleepy", "zh": "它们让你犯困"},
                {"en": "They are a type of vitamin", "zh": "它们是一种维生素"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Proteins make up the building blocks of your body, helping build and repair cells. Proteins are especially important for strong muscles.\"",
                        "zh": "“蛋白质构成身体的基本材料，帮助构建和修复细胞。蛋白质对强壮的肌肉尤其重要。”"}
        },
        {
            "q": {"en": "How many glasses of water should you drink each day, according to the book?",
                  "zh": "根据本书，你每天应喝几杯水？"},
            "options": [
                {"en": "Six to eight glasses", "zh": "六到八杯"},
                {"en": "One glass", "zh": "一杯"},
                {"en": "Twenty glasses", "zh": "二十杯"},
                {"en": "None", "zh": "不喝"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"But you should also drink six to eight glasses of water each day.\"",
                        "zh": "“但你每天还应喝六到八杯水。”"}
        },
        {
            "q": {"en": "In the book, what is a \"calorie\"?",
                  "zh": "在书中，“calorie”（卡路里）是什么？"},
            "options": [
                {"en": "A bit of energy that you get from food", "zh": "你从食物中获得的少量能量"},
                {"en": "A type of fruit", "zh": "一种水果"},
                {"en": "A kind of exercise", "zh": "一种运动"},
                {"en": "A vitamin supplement", "zh": "一种维生素补充剂"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines calorie as \"a unit that measures how much energy is in food.\"",
                        "zh": "词汇表将 calorie 定义为“衡量食物中能量多少的单位”。"}
        },
        {
            "q": {"en": "Why can eating too many sweets raise your health risk?",
                  "zh": "为什么吃太多甜食会增加健康风险？"},
            "options": [
                {"en": "It can increase the risk of type 2 diabetes", "zh": "会增加患2型糖尿病的风险"},
                {"en": "It makes you grow taller", "zh": "它会让你长高"},
                {"en": "It gives you more vitamins", "zh": "它会给你更多维生素"},
                {"en": "It cleans your teeth", "zh": "它会清洁牙齿"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"Type 2 diabetes is a disease caused by too much sugar in the blood… Poor eating habits, including eating too many sweets, can increase your risk of diabetes.\"",
                        "zh": "“2型糖尿病是一种由血液中糖分过多引起的疾病……不良的饮食习惯，包括吃太多甜食，会增加患糖尿病的风险。”"}
        },
        {
            "q": {"en": "In the book, what is a \"nutrient\"?",
                  "zh": "在书中，“nutrient”（营养素）是什么？"},
            "options": [
                {"en": "Any substance your body needs to live, stay healthy, and grow", "zh": "身体生存、保持健康、生长所需的任何物质"},
                {"en": "A type of candy", "zh": "一种糖果"},
                {"en": "A sport", "zh": "一项运动"},
                {"en": "A kitchen tool", "zh": "一种厨房工具"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines nutrient as \"any substance your body needs to live, stay healthy, and grow.\"",
                        "zh": "词汇表将 nutrient 定义为“身体生存、保持健康、生长所需的任何物质”。"}
        },
        {
            "q": {"en": "Which kind of carbohydrate gives your body energy over a long period of time?",
                  "zh": "哪种碳水化合物能为身体提供较长时间的能量？"},
            "options": [
                {"en": "Vegetables, fruits, oatmeal, and whole grains", "zh": "蔬菜、水果、燕麦和全谷物"},
                {"en": "Candy and white cakes", "zh": "糖果和白蛋糕"},
                {"en": "Only soda", "zh": "只有汽水"},
                {"en": "Plain sugar", "zh": "纯糖"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"Some carbohydrates are especially good for you because they give you energy over a long period of time. These are found in foods such as vegetables, many fruits, oatmeal, whole grains, and whole-grain bread.\"",
                        "zh": "“有些碳水化合物特别有益，因为它们能在较长时间内提供能量。这些存在于蔬菜、许多水果、燕麦、全谷物和全麦面包等食物中。”"}
        },
        {
            "q": {"en": "Which activity in the book burns the most calories per hour?",
                  "zh": "书中哪项活动每小时消耗的卡路里最多？"},
            "options": [
                {"en": "Swimming (300 calories per hour)", "zh": "游泳（每小时300卡路里）"},
                {"en": "Watching TV (43 calories per hour)", "zh": "看电视（每小时43卡路里）"},
                {"en": "Cleaning your room (115 calories per hour)", "zh": "打扫房间（每小时115卡路里）"},
                {"en": "Playing ping-pong (171 calories per hour)", "zh": "打乒乓球（每小时171卡路里）"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "The chart lists Watching TV 43, Cleaning 115, Ping-pong 171, Washing car 193, and Swimming 300 calories per hour.",
                        "zh": "图表列出：看电视43、打扫115、乒乓球171、洗车193、游泳300卡路里/小时。"}
        },
        {
            "q": {"en": "What does the old saying 'an apple a day' suggest about staying healthy?",
                  "zh": "老话“每天一个苹果”对保持健康有什么暗示？"},
            "options": [
                {"en": "Eating healthy foods like fruit is a good way to stay healthy", "zh": "吃水果等健康食物是保持健康的好方法"},
                {"en": "You should only eat apples", "zh": "你只应该吃苹果"},
                {"en": "Candy is the best food", "zh": "糖果是最好的食物"},
                {"en": "Exercise is useless", "zh": "运动没用"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"As the old saying goes, an 'apple a day' is a good way to stay healthy.\"",
                        "zh": "“正如老话所说，‘每天一个苹果’是保持健康的好方法。”"}
        },
        {
            "q": {"en": "What is the main goal of this book?",
                  "zh": "这本书的主要目的是什么？"},
            "options": [
                {"en": "To teach readers about nutrients and smart eating", "zh": "教读者了解营养素和智慧饮食"},
                {"en": "To tell a pirate story", "zh": "讲一个海盗故事"},
                {"en": "To explain how to fly a kite", "zh": "解释如何放风筝"},
                {"en": "To describe a sea voyage", "zh": "描述一次海上航行"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The book explains proteins, carbohydrates, fats, vitamins, water, and calories, then gives \"Smart Eating\" advice.",
                        "zh": "这本书讲解蛋白质、碳水化合物、脂肪、维生素、水和卡路里，随后给出“智慧饮食”建议。"}
        },
        {
            "q": {"en": "Where do trans fats come from, and why are they unhealthy?",
                  "zh": "反式脂肪来自哪里？为什么它们不健康？"},
            "options": [
                {"en": "They come from processed foods and are not good for the body", "zh": "它们来自加工食品，对身体无益"},
                {"en": "They come from fresh fruit", "zh": "它们来自新鲜水果"},
                {"en": "They come from drinking water", "zh": "它们来自饮水"},
                {"en": "They are the same as vegetable fats", "zh": "它们和植物脂肪一样"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Fats called trans fats are processed fats in pre-made foods… Studies have shown that these fats are not good for the body.\"",
                        "zh": "“被称为反式脂肪的脂肪，是预制食品中的加工脂肪……研究表明这些脂肪对身体无益。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Plan one healthy meal using the book's 'Smart Eating' advice. Name foods from at least two nutrient groups.",
                   "zh": "运用书中“智慧饮食”的建议规划一顿健康餐。说出至少来自两个营养素组的食物。"},
        "guidance": {
            "en": ["Include a protein (e.g., fish, chicken, eggs) and colorful vegetables or fruit.",
                   "Remember to drink water and limit trans fats and sweets."],
            "zh": ["包含一种蛋白质（如鱼、鸡肉、蛋）以及色彩丰富的蔬菜或水果。",
                   "记得多喝水，并限制反式脂肪和甜食。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 8. All About Kites
# ---------------------------------------------------------------------------
books.append({
    "slug": "all-about-kites",
    "title": "All About Kites",
    "titleZh": "关于风筝的一切",
    "level": "R",
    "genre": "Informational",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "What were the first toy kites named after?",
                  "zh": "最早的玩具风筝是以什么命名的？"},
            "options": [
                {"en": "The kite bird, a large graceful bird with a wide wingspan", "zh": "鸢鸟，一种翅展很宽、优雅的大鸟"},
                {"en": "A famous king", "zh": "一位著名的国王"},
                {"en": "The moon", "zh": "月亮"},
                {"en": "A type of fish", "zh": "一种鱼"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Thousands of years ago, the first toy kites were named after the kite bird, a large, graceful bird with a very wide wingspan.\"",
                        "zh": "“数千年前，最早的玩具风筝以鸢鸟命名，那是一种翅展很宽、优雅的大鸟。”"}
        },
        {
            "q": {"en": "What did Ben Franklin prove using a kite?",
                  "zh": "本·富兰克林用风筝证明了什么？"},
            "options": [
                {"en": "That lightning is made of electric current", "zh": "闪电是由电流构成的"},
                {"en": "That the Earth is round", "zh": "地球是圆的"},
                {"en": "That wind can lift a person", "zh": "风可以把人托起"},
                {"en": "That birds can talk", "zh": "鸟会说话"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"He used a kite to prove his idea that lightning was made of electric current.\"",
                        "zh": "“他用风筝证明了自己的想法：闪电是由电流构成的。”"}
        },
        {
            "q": {"en": "In the book, what is a \"bridle\"?",
                  "zh": "在书中，“bridle”（骨架绳）是什么？"},
            "options": [
                {"en": "A kind of harness that guides movement with ropes or strings", "zh": "一种用绳索引导运动的装置"},
                {"en": "The tail of a kite", "zh": "风筝的尾巴"},
                {"en": "A type of weather instrument", "zh": "一种气象仪器"},
                {"en": "A sharp metal hook", "zh": "一个尖锐的金属钩"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines bridle as \"a kind of harness that guides movement with ropes or strings.\"",
                        "zh": "词汇表将 bridle 定义为“一种用绳索引导运动的装置”。"}
        },
        {
            "q": {"en": "Why do some cargo ships use large kites?",
                  "zh": "为什么一些货船使用大风筝？"},
            "options": [
                {"en": "To help pull the ship so it burns less fuel and makes less pollution", "zh": "帮助拉船，从而少烧燃料、减少污染"},
                {"en": "To catch fish", "zh": "为了捕鱼"},
                {"en": "To take photographs", "zh": "为了拍照"},
                {"en": "To keep birds away", "zh": "为了赶走鸟"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"One German shipping company is experimenting with special kites to help reduce both problems. The big kite helps to pull the ship so the ship's engines will burn less fuel every day… the amount of air pollution… will also be reduced.\"",
                        "zh": "“一家德国航运公司正试验用特制风筝来缓解这两个问题。大风筝帮助拉船，使船的发动机每天少烧燃料……空气污染量也会减少。”"}
        },
        {
            "q": {"en": "In a famous Chinese legend, how did a man use a kite to attack a fort?",
                  "zh": "在一个著名的中国传说中，一个人如何用风筝攻击堡垒？"},
            "options": [
                {"en": "He tied himself to a huge kite, flew over the walls, and frightened the soldiers away", "zh": "他把自己绑在一只大风筝上，飞过城墙，把士兵吓跑"},
                {"en": "He shot arrows from the kite", "zh": "他从风筝上射箭"},
                {"en": "He used it to start a fire", "zh": "他用它来生火"},
                {"en": "He sailed it like a boat", "zh": "他像划船一样驾驭它"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"One famous Chinese legend tells a story about a man who used a kite to attack a fort. Unable to penetrate the walls, he tied himself to a huge kite, flew over the fort's high walls, and frightened the soldiers away.\"",
                        "zh": "“一个著名的中国传说讲了一个人用风筝攻击堡垒的故事。他无法突破城墙，便把自己绑在一只大风筝上，飞过堡垒的高墙，把士兵吓跑。”"}
        },
        {
            "q": {"en": "In the book, what is a \"legend\"?",
                  "zh": "在书中，“legend”（传说）是什么？"},
            "options": [
                {"en": "An old story that is well known but cannot be proved", "zh": "一个广为人知但无法被证实的古老故事"},
                {"en": "A science fact", "zh": "一个科学事实"},
                {"en": "A kind of kite string", "zh": "一种风筝线"},
                {"en": "A weather report", "zh": "一份天气报告"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines legend as \"an old story that is well known but cannot be proved.\"",
                        "zh": "词汇表将 legend 定义为“一个广为人知但无法被证实的古老故事”。"}
        },
        {
            "q": {"en": "To make your own kite, how long are the two sticks the book says to use?",
                  "zh": "自己做风筝时，书中说要用多长的两根棍子？"},
            "options": [
                {"en": "One 3 feet (90 cm) long and one 2 feet (60 cm) long", "zh": "一根3英尺（90厘米），一根2英尺（60厘米）"},
                {"en": "Both 5 feet long", "zh": "两根都5英尺长"},
                {"en": "One 1 foot and one 10 feet", "zh": "一根1英尺，一根10英尺"},
                {"en": "Three sticks of equal length", "zh": "三根等长的棍子"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"You'll need: two lightweight, smooth sticks, one 3 feet (90 cm) long, the other 2 feet (60 cm).\"",
                        "zh": "“你需要：两根轻质光滑的棍子，一根3英尺（90厘米）长，另一根2英尺（60厘米）长。”"}
        },
        {
            "q": {"en": "What do the unusual uses of kites (fishing, weather charts, cargo ships) have in common?",
                  "zh": "风筝的各种特殊用途（捕鱼、气象图、货船）有什么共同点？"},
            "options": [
                {"en": "They all use the kite to do a useful job up in the air", "zh": "它们都用风筝在空中完成一项有用的任务"},
                {"en": "They are all only for decoration", "zh": "它们都只用于装饰"},
                {"en": "They all require electricity", "zh": "它们都需要电"},
                {"en": "They are all dangerous", "zh": "它们都很危险"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "Whether skipping bait over water, carrying weather instruments aloft, or pulling a ship, the kite performs work in the air.",
                        "zh": "无论是让诱饵掠过水面、把气象仪器带上高空，还是拉船，风筝都在空中完成工作。"}
        },
        {
            "q": {"en": "Why does the book include a 'Make Your Own Kite' section?",
                  "zh": "书中为什么包含“自己做风筝”一节？"},
            "options": [
                {"en": "To let readers try making and flying a kite themselves", "zh": "让读者自己动手制作并尝试放风筝"},
                {"en": "To teach a history lesson", "zh": "为了上一堂历史课"},
                {"en": "To sell kite supplies", "zh": "为了卖风筝材料"},
                {"en": "To explain weather", "zh": "为了解释天气"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"With a little practice, almost anyone can assemble a kite and learn to fly it,\" so the book gives step-by-step making instructions.",
                        "zh": "“稍加练习，几乎任何人都能组装风筝并学会放它”，所以书中给出了逐步的制作说明。"}
        },
        {
            "q": {"en": "What is the book's overall purpose?",
                  "zh": "这本书的总体目的是什么？"},
            "options": [
                {"en": "To inform readers about kites' history, unusual uses, and how to make one", "zh": "向读者介绍风筝的历史、特殊用途以及如何制作"},
                {"en": "To argue that kites are dangerous", "zh": "论证风筝很危险"},
                {"en": "To tell a fairy tale", "zh": "讲一个童话"},
                {"en": "To teach math", "zh": "教数学"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The book covers the history of kites, unusual uses (fishing, weather, cargo, spies), and a make-your-own guide.",
                        "zh": "本书涵盖风筝的历史、特殊用途（捕鱼、气象、货船、间谍）以及自制指南。"}
        }
    ],
    "extended": {
        "prompt": {"en": "The book says kites have unusual uses. Invent one new helpful use for a kite and explain how it would work.",
                   "zh": "书中说风筝有特殊的用途。请你发明一种风筝的新用途，并说明它如何运作。"},
        "guidance": {
            "en": ["Think about jobs done up in the air, like the book's examples (fishing, weather, pulling ships).",
                   "Explain what the kite would carry or do."],
            "zh": ["想想在空中完成的任务，就像书中例子（捕鱼、气象、拉船）。",
                   "说明风筝会携带什么或做什么。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 9. All About Chocolate
# ---------------------------------------------------------------------------
books.append({
    "slug": "all-about-chocolate",
    "title": "All About Chocolate",
    "titleZh": "关于巧克力的一切",
    "level": "R",
    "genre": "Informational",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "Which tree gives us chocolate, and where does it grow?",
                  "zh": "哪种树产出巧克力？它生长在哪里？"},
            "options": [
                {"en": "The cacao tree, which grows near the equator where it is hot and wet", "zh": "可可树，生长在炎热潮湿的赤道附近"},
                {"en": "The apple tree, in cold climates", "zh": "苹果树，在寒冷气候中"},
                {"en": "The pine tree, in mountains", "zh": "松树，在山中"},
                {"en": "The oak tree, in deserts", "zh": "橡树，在沙漠中"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"The tree that gives us chocolate is the cacao tree. Cacao trees grow near the equator, where it is hot and wet.\"",
                        "zh": "“给我们巧克力的是可可树。可可树生长在炎热潮湿的赤道附近。”"}
        },
        {
            "q": {"en": "What tool is used to cut open the cacao pods?",
                  "zh": "用什么工具切开可可果荚？"},
            "options": [
                {"en": "A large blade called a machete", "zh": "一种叫砍刀（machete）的大刀片"},
                {"en": "A spoon", "zh": "一把勺子"},
                {"en": "A pair of scissors", "zh": "一把剪刀"},
                {"en": "A hammer", "zh": "一把锤子"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Then, someone using a large blade called a machete cuts the pods open.\"",
                        "zh": "“然后，有人用一种叫砍刀的大刀片把果荚切开。”"}
        },
        {
            "q": {"en": "In the book, what is \"conching\"?",
                  "zh": "在书中，“conching”（精磨）是什么？"},
            "options": [
                {"en": "The final step where sugar, cocoa powder, and cocoa butter are rolled smooth", "zh": "最后一步，将糖、可可粉和可可脂碾磨均匀"},
                {"en": "The first step of cutting pods", "zh": "切开果荚的第一步"},
                {"en": "A type of cocoa bean", "zh": "一种可可豆"},
                {"en": "Drying the beans in the sun", "zh": "把豆子晒干"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "\"The chocolate we eat is made in the final step, called conching. Conching takes place in machines with big rollers. Sugar, cocoa powder, cocoa butter, and other ingredients are rolled and mixed until smooth.\"",
                        "zh": "“我们吃的巧克力在最后一步制成，称为精磨。精磨在带大滚筒的机器中进行，糖、可可粉、可可脂和其他配料被碾磨混合至顺滑。”"}
        },
        {
            "q": {"en": "How did the Aztecs value cacao beans?",
                  "zh": "阿兹特克人如何看重可可豆？"},
            "options": [
                {"en": "They used the beans as a form of money", "zh": "他们把可可豆当作一种货币"},
                {"en": "They used them only to build houses", "zh": "他们只用它来盖房子"},
                {"en": "They threw them away", "zh": "他们把它们扔掉"},
                {"en": "They fed them to horses", "zh": "他们拿去喂马"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"They placed so much value on cacao beans that they used the beans as a form of money.\"",
                        "zh": "“他们如此看重可可豆，以至于把它当作一种货币来使用。”"}
        },
        {
            "q": {"en": "What yellow liquid is removed when the chocolate bars are pressed?",
                  "zh": "压紧巧克力块时会分离出什么黄色液体？"},
            "options": [
                {"en": "Cocoa butter", "zh": "可可脂"},
                {"en": "Apple juice", "zh": "苹果汁"},
                {"en": "Lemonade", "zh": "柠檬水"},
                {"en": "Olive oil", "zh": "橄榄油"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"The bars are then pressed until the most important part of the chocolate, a yellow liquid called cocoa butter, is removed.\"",
                        "zh": "“然后把块状物压榨，直到巧克力中最重要的部分——一种叫可可脂的黄色液体——被分离出来。”"}
        },
        {
            "q": {"en": "Which type of chocolate has medical benefits, according to the book?",
                  "zh": "根据书中说法，哪种巧克力有医疗益处？"},
            "options": [
                {"en": "Dark chocolate (not milk chocolate)", "zh": "黑巧克力（而非牛奶巧克力）"},
                {"en": "White chocolate only", "zh": "只有白巧克力"},
                {"en": "All chocolate is unhealthy", "zh": "所有巧克力都不健康"},
                {"en": "Milk chocolate", "zh": "牛奶巧克力"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"The benefits are linked to dark chocolate, rather than milk chocolate. Some of the medical benefits include a reduction in heart disease and blood pressure.\"",
                        "zh": "“这些益处与黑巧克力有关，而非牛奶巧克力。部分医疗益处包括降低心脏病和血压。”"}
        },
        {
            "q": {"en": "In the steps from bean to chocolate, what happens right after roasting?",
                  "zh": "从豆子到巧克力的步骤中，烘烤之后紧接着做什么？"},
            "options": [
                {"en": "Shelling (the shells are cracked and blown away)", "zh": "去壳（敲裂外壳并吹走）"},
                {"en": "Wrapping the chocolate", "zh": "包装巧克力"},
                {"en": "Eating it", "zh": "吃掉它"},
                {"en": "Planting the beans", "zh": "种下豆子"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The book's picture steps show: 1. Roasting, 2. Shelling, 3. Grinding, 4. Mixing, 5. Conching, 6. Pouring, 7. Cooling, 8. Wrapping.",
                        "zh": "书中的步骤图显示：1.烘烤，2.去壳，3.研磨，4.混合，5.精磨，6.浇注，7.冷却，8.包装。"}
        },
        {
            "q": {"en": "Which country eats the most chocolate per person each year?",
                  "zh": "哪个国家每人每年吃的巧克力最多？"},
            "options": [
                {"en": "Switzerland (22.4 lbs / 10.1 kg)", "zh": "瑞士（22.4磅 / 10.1公斤）"},
                {"en": "The United States", "zh": "美国"},
                {"en": "Mexico", "zh": "墨西哥"},
                {"en": "China", "zh": "中国"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"The people of Switzerland consume more chocolate per person than anyone else in the world… 1 Switzerland … 22.4 lbs … 10.1 kg.\"",
                        "zh": "“瑞士人人均消费的巧克力比世界上任何国家都多……1 瑞士……22.4磅……10.1公斤。”"}
        },
        {
            "q": {"en": "Why does the book include a recipe for chocolate brownies?",
                  "zh": "书中为什么包含巧克力布朗尼的食谱？"},
            "options": [
                {"en": "To let readers try making a chocolate treat themselves", "zh": "让读者自己动手做一份巧克力点心"},
                {"en": "To explain how to grow cacao", "zh": "为了解释如何种植可可"},
                {"en": "To teach a history lesson", "zh": "为了上一堂历史课"},
                {"en": "To describe the weather", "zh": "为了描述天气"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The \"Try This!\" section gives a brownie recipe so readers can \"think about how it was made\" after eating chocolate.",
                        "zh": "“试试看！”一节给出布朗尼食谱，让读者在吃巧克力后“想想它是怎么做出来的”。"}
        },
        {
            "q": {"en": "What is the book's main purpose?",
                  "zh": "这本书的主要目的是什么？"},
            "options": [
                {"en": "To explain where chocolate comes from and how it is made", "zh": "解释巧克力的来源以及它是如何制作的"},
                {"en": "To tell a ghost story", "zh": "讲一个鬼故事"},
                {"en": "To teach about kites", "zh": "教关于风筝的知识"},
                {"en": "To describe a basketball game", "zh": "描述一场篮球比赛"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The book covers where cacao grows, preparing beans, making chocolate, its history, and chocolate today.",
                        "zh": "本书涵盖可可的生长地、豆子的处理、巧克力的制作、历史以及当今的巧克力。"}
        }
    ],
    "extended": {
        "prompt": {"en": "Using the book's steps, explain in order how cacao beans become a chocolate bar. Name at least four steps.",
                   "zh": "运用书中的步骤，按顺序说明可可豆如何变成巧克力块。至少说出四个步骤。"},
        "guidance": {
            "en": ["Steps include: fermenting/drying, roasting, shelling, grinding, conching, pouring, cooling, wrapping.",
                   "Mention that cocoa butter is pressed out and sugar is added during conching."],
            "zh": ["步骤包括：发酵/干燥、烘烤、去壳、研磨、精磨、浇注、冷却、包装。",
                   "提到在精磨时会压榨出可可脂并加入糖。"]
        }
    }
})

# ---------------------------------------------------------------------------
# 10. Alexander the Great
# ---------------------------------------------------------------------------
books.append({
    "slug": "alexander-the-great",
    "title": "Alexander the Great",
    "titleZh": "亚历山大大帝",
    "level": "R",
    "genre": "Biography",
    "mainSkill": KID,
    "questions": [
        {
            "q": {"en": "When and where was Alexander the Great born?",
                  "zh": "亚历山大大帝何时何地出生？"},
            "options": [
                {"en": "In 356 BC, in Macedonia (part of ancient Greece)", "zh": "公元前356年，生于马其顿（古希腊的一部分）"},
                {"en": "In 323 BC, in Egypt", "zh": "公元前323年，生于埃及"},
                {"en": "In 359 BC, in Persia", "zh": "公元前359年，生于波斯"},
                {"en": "In 300 BC, in Rome", "zh": "公元前300年，生于罗马"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Alexander was born in 356 BC. Alexander's father, Philip II, was king of Macedonia… part of ancient Greece.\"",
                        "zh": "“亚历山大生于公元前356年。他的父亲腓力二世是马其顿国王……马其顿是古希腊的一部分。”"}
        },
        {
            "q": {"en": "Who taught Alexander science and history when he was growing up?",
                  "zh": "亚历山大成长过程中，谁教他科学和历史？"},
            "options": [
                {"en": "Aristotle, a very wise man", "zh": "亚里士多德，一位非常睿智的人"},
                {"en": "His father Philip II", "zh": "他的父亲腓力二世"},
                {"en": "The king of Persia, Darius III", "zh": "波斯国王大流士三世"},
                {"en": "A soldier named Bucephalus", "zh": "一个叫布西发拉斯的士兵"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Philip asked Aristotle—a very wise man—to teach Alexander science, history, and other subjects.\"",
                        "zh": "“腓力请亚里士多德——一位非常睿智的人——教亚历山大科学、历史和其他科目。”"}
        },
        {
            "q": {"en": "In the book, what is an \"empire\"?",
                  "zh": "在书中，“empire”（帝国）是什么？"},
            "options": [
                {"en": "A collection of nations or people ruled by one person or government", "zh": "由一人或一个政府统治的多个民族或国家的集合"},
                {"en": "A type of sword", "zh": "一种剑"},
                {"en": "A kind of horse", "zh": "一种马"},
                {"en": "A small village", "zh": "一个小村庄"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "The glossary defines empire as \"a collection of nations or people ruled by one person or government.\"",
                        "zh": "词汇表将 empire 定义为“由一人或一个政府统治的多个民族或国家的集合”。"}
        },
        {
            "q": {"en": "How did Alexander become king of Macedonia?",
                  "zh": "亚历山大是如何成为马其顿国王的？"},
            "options": [
                {"en": "His father Philip was killed in 336 BC and the baby was too young to rule", "zh": "他的父亲腓力于公元前336年被杀，婴儿太小无法执政"},
                {"en": "He won an election", "zh": "他赢得了选举"},
                {"en": "He built the biggest army by himself", "zh": "他独自组建了最庞大的军队"},
                {"en": "The Persians chose him", "zh": "波斯人选中了他"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"In 336 BC, Philip's new wife had a baby girl. In the same year, a man killed Philip. The new baby was too young to take the throne, and after Philip's death, Alexander became king.\"",
                        "zh": "“公元前336年，腓力的新妻子生下一个女婴。同年，有人杀死了腓力。女婴太小不能即位，腓力死后，亚历山大成为国王。”"}
        },
        {
            "q": {"en": "At what age did Alexander become king?",
                  "zh": "亚历山大几岁成为国王？"},
            "options": [
                {"en": "Twenty years old", "zh": "二十岁"},
                {"en": "Twelve years old", "zh": "十二岁"},
                {"en": "Thirty-three years old", "zh": "三十三岁"},
                {"en": "Forty years old", "zh": "四十岁"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"Alexander became king of Macedonia when he was twenty years old.\"",
                        "zh": "“亚历山大二十岁时成为马其顿国王。”"}
        },
        {
            "q": {"en": "What made Alexander's army strong in battle?",
                  "zh": "亚历山大的军队在战斗中强大靠的是什么？"},
            "options": [
                {"en": "Fighting in a tight rectangular formation (phalanx) with very long spears", "zh": "以紧密的矩形方阵（马其顿方阵）作战，使用很长的长矛"},
                {"en": "Riding horses only, with no foot soldiers", "zh": "只骑马，没有步兵"},
                {"en": "Using airplanes", "zh": "使用飞机"},
                {"en": "Having the smallest army", "zh": "拥有最小的军队"}],
            "answer": 0, "skill": INT,
            "explain": {"en": "\"The army's strength in battle came in part from fighting in a tight rectangular formation… Foot soldiers in tight formations carried spears that were sometimes 6 meters (20 ft.) long.\"",
                        "zh": "“军队在战斗中的力量部分来自紧密的矩形方阵……紧密队形的步兵手持有时长达6米（20英尺）的长矛。”"}
        },
        {
            "q": {"en": "After defeating Darius at Issus, where did Alexander march in 332 BC?",
                  "zh": "在伊苏斯击败大流士后，亚历山大于公元前332年向哪里进军？"},
            "options": [
                {"en": "South into Egypt, where the Persians gave him control", "zh": "向南进入埃及，波斯人把控制权交给了他"},
                {"en": "Back to Macedonia", "zh": "返回马其顿"},
                {"en": "Across the Atlantic", "zh": "跨越大西洋"},
                {"en": "To Rome", "zh": "前往罗马"}],
            "answer": 0, "skill": CRA,
            "explain": {"en": "\"In 332 BC, Alexander marched south into Egypt. The Persian leader there gave Alexander control. The Egyptians welcomed him.\"",
                        "zh": "“公元前332年，亚历山大向南进军埃及。那里的波斯首领把控制权交给亚历山大。埃及人欢迎他。”"}
        },
        {
            "q": {"en": "When and where did Alexander the Great die?",
                  "zh": "亚历山大大帝何时何地去世？"},
            "options": [
                {"en": "In 323 BC at Babylon, of a fever, just before turning 33", "zh": "公元前323年在巴比伦，死于发烧，就在33岁生日前"},
                {"en": "In 356 BC in Macedonia", "zh": "公元前356年在马其顿"},
                {"en": "In battle in India in 326 BC", "zh": "公元前326年在印度战死"},
                {"en": "In Egypt of old age", "zh": "在埃及安老去世"}],
            "answer": 0, "skill": KID,
            "explain": {"en": "\"They made it to Babylon in 323 BC. However, Alexander came down with a fever, and in June of that year, Alexander the Great died, just before he turned thirty-three.\"",
                        "zh": "“他们于公元前323年抵达巴比伦。然而亚历山大染上热病，同年6月去世，就在他三十三岁生日前。”"}
        },
        {
            "q": {"en": "Why does the book mention that Aristotle taught Alexander?",
                  "zh": "书中为什么提到亚里士多德教导过亚历山大？"},
            "options": [
                {"en": "To show his education shaped him and helped spread Greek culture", "zh": "为了说明他的教育塑造了他，并帮助传播希腊文化"},
                {"en": "To explain how to ride a horse", "zh": "为了解释如何骑马"},
                {"en": "To describe a battle plan", "zh": "为了描述一个战斗计划"},
                {"en": "To list the empire's size", "zh": "为了列出帝国的版图"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "\"Perhaps because of his early education, he learned the traditions of his new empire, and in turn, he and the Macedonians spread Greek culture in new lands.\"",
                        "zh": "“或许由于早年的教育，他学习了新帝国的传统，并进而和马其顿人把希腊文化传播到新的土地。”"}
        },
        {
            "q": {"en": "What is the book's focus question?",
                  "zh": "这本书的核心问题是什么？"},
            "options": [
                {"en": "\"How did Alexander the Great create his large empire?\"", "zh": "“亚历山大大帝是如何建立他庞大的帝国的？”"},
                {"en": "\"Why do kites fly?\"", "zh": "“风筝为什么会飞？”"},
                {"en": "\"How is chocolate made?\"", "zh": "“巧克力是如何制作的？”"},
                {"en": "\"Who invented basketball?\"", "zh": "“谁发明了篮球？”"}],
            "answer": 0, "skill": AUT,
            "explain": {"en": "The focus question at the start reads: \"How did Alexander the Great create his large empire?\"",
                        "zh": "开头的核心问题是：“亚历山大大帝是如何建立他庞大的帝国的？”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Alexander built a huge empire by age 32. Name two lands/regions he conquered and one way his early life prepared him.",
                   "zh": "亚历山大在32岁前建立了庞大帝国。说出他征服的两个地区，以及早年生活为他做了哪项准备。"},
        "guidance": {
            "en": ["Regions include Asia Minor, Egypt, Persia, and parts of India.",
                   "Preparation: Aristotle taught him, he learned to ride Bucephalus and fight, and he led soldiers from a young age."],
            "zh": ["地区包括小亚细亚、埃及、波斯和印度部分地区。",
                   "准备：亚里士多德教导他；他学会骑布西发拉斯、作战，并从小就领军。"]
        }
    }
})

# ---------------------------------------------------------------------------
# Write all files
# ---------------------------------------------------------------------------
for b in books:
    path = os.path.join(OUT, b["slug"] + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
    print("wrote", path)

print("\nTotal books written:", len(books))
