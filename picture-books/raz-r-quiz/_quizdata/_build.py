# -*- coding: utf-8 -*-
import json, os

OUT = r"D:\AI\readbook\raz-r-quiz\_quizdata"
os.makedirs(OUT, exist_ok=True)

SKILLS = ["Key Ideas and Details", "Craft and Structure",
          "Integration of Knowledge and Ideas", "Author's Purpose and Perspective"]

books = []

# 1. How the Robin Stole Fire
books.append({
    "slug": "how-the-robin-stole-fire",
    "title": "How the Robin Stole Fire",
    "titleZh": "知更鸟如何偷来火",
    "level": "R",
    "genre": "Folktale",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "What kind of story is 'How the Robin Stole Fire'?",
                  "zh": "《知更鸟如何偷来火》是一篇什么类型的故事？"},
            "options": [
                {"en": "An Australian Aboriginal folktale", "zh": "澳大利亚原住民民间故事"},
                {"en": "A scientific report about weather", "zh": "关于天气的科学报告"},
                {"en": "A news article from a newspaper", "zh": "报纸上的新闻文章"},
                {"en": "A modern science-fiction novel", "zh": "现代科幻小说"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The book's title page says it is 'An Australian Aborigine Folktale' retold by William Harryman.",
                        "zh": "书的扉页标明这是威廉·哈里曼重述的“澳大利亚原住民民间故事”。"}
        },
        {
            "q": {"en": "In the story, what is a 'dilly bag'?",
                  "zh": "在故事中，“dilly bag”是什么？"},
            "options": [
                {"en": "A type of spear", "zh": "一种长矛"},
                {"en": "An empty day pack", "zh": "一个空的日子袋（日用背包）"},
                {"en": "A kind of bird", "zh": "一种鸟"},
                {"en": "A small campfire", "zh": "一小堆营火"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "The old man carried 'a spear and an empty day pack, called a dilly bag.'",
                        "zh": "文中写道，老人随身带着“一支长矛和一个空的日用背包，叫做 dilly bag”。"}
        },
        {
            "q": {"en": "Who kept the fire hidden under his wing?",
                  "zh": "是谁把火藏在翅膀下面？"},
            "options": [
                {"en": "Mar, the Cockatoo", "zh": "凤头鹦鹉马尔"},
                {"en": "Tatkanna, the Robin", "zh": "知更鸟塔特卡纳"},
                {"en": "Prite, the Wren", "zh": "鹪鹩普赖特"},
                {"en": "Quartang, the Kookaburra", "zh": "笑翠鸟昆唐"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The old man saw 'Mar, the Cockatoo, take the fire from under his wing.'",
                        "zh": "老人看到“凤头鹦鹉马尔从翅膀下取出火”。"}
        },
        {
            "q": {"en": "Which bird was chosen by the elders to steal the fire?",
                  "zh": "长老们选了哪只鸟去偷火？"},
            "options": [
                {"en": "Prite the Wren", "zh": "鹪鹩普赖特"},
                {"en": "Quartang the Kookaburra", "zh": "笑翠鸟昆唐"},
                {"en": "Tatkanna the Robin", "zh": "知更鸟塔特卡纳"},
                {"en": "Mar the Cockatoo", "zh": "凤头鹦鹉马尔"}
            ],
            "answer": 2,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The elders decided 'that Tatkanna, the Robin, would make the journey to Mar's camp to steal the fire.'",
                        "zh": "长老们决定“由知更鸟塔特卡纳前往马尔的营地偷火”。"}
        },
        {
            "q": {"en": "Why did Tatkanna become known as 'Robin Redbreast'?",
                  "zh": "塔特卡纳为什么被称为“红胸知更鸟”？"},
            "options": [
                {"en": "He ate red berries every day", "zh": "他每天都吃红色浆果"},
                {"en": "He singed his breast feathers when the fire stick got too close", "zh": "火把离得太近，烧焦了他胸前的羽毛"},
                {"en": "Mar painted his chest red", "zh": "马尔把他的胸涂成了红色"},
                {"en": "He was born with red feathers", "zh": "他生来就有红色羽毛"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "Tatkanna 'got the stick too close to his breast and singed all the feathers. From that day forward he was known as Robin Redbreast.'",
                        "zh": "塔特卡纳“把火把拿得离胸口太近，烧焦了所有羽毛。从那天起他就被称为红胸知更鸟”。"}
        },
        {
            "q": {"en": "At the celebration, what did Mar the Cockatoo accept from the birds?",
                  "zh": "在庆祝会上，凤头鹦鹉马尔从鸟群那里接受了什么？"},
            "options": [
                {"en": "A piece of kangaroo flesh", "zh": "一块袋鼠肉"},
                {"en": "The kangaroo hide", "zh": "袋鼠皮"},
                {"en": "A spear", "zh": "一支长矛"},
                {"en": "The fire stick", "zh": "那根火把"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "They offered Mar kangaroo flesh, which he refused, 'Then they offered Mar the kangaroo hide, which he accepted.'",
                        "zh": "他们先给马尔袋鼠肉（被拒绝），“接着他们把袋鼠皮给了马尔，他收下了”。"}
        },
        {
            "q": {"en": "According to the book, what does this folktale explain?",
                  "zh": "根据书中内容，这个民间故事解释了什么？"},
            "options": [
                {"en": "How to build a corroboree", "zh": "如何举办狂欢聚会"},
                {"en": "The origins of both useful fire and the raging brush fires of the Australian outback", "zh": "有用之火的由来，以及澳洲内陆肆虐的丛林大火的由来"},
                {"en": "Why kangaroos have pouches", "zh": "袋鼠为什么有育儿袋"},
                {"en": "How the Cockatoo learned to fly", "zh": "凤头鹦鹉是如何学会飞的"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "The book says it 'explains both the origins of useful fire and of the raging brush fires that periodically sweep the grasslands of the Australian outback.'",
                        "zh": "书中说它“解释了有用之火的起源，以及周期性席卷澳洲内陆草原的肆虐丛林大火的起源”。"}
        },
        {
            "q": {"en": "What happened to Quartang the Kookaburra after he fought Mar?",
                  "zh": "笑翠鸟昆唐与马尔打斗之后发生了什么？"},
            "options": [
                {"en": "He became the new keeper of the fire", "zh": "他成了火的新守护者"},
                {"en": "He retreated to the trees and has never left them since", "zh": "他退到树上，从此再也没有离开过树"},
                {"en": "He flew away to another country", "zh": "他飞去了另一个国家"},
                {"en": "He stole the fire for himself", "zh": "他自己把火偷走了"}
            ],
            "answer": 1,
            "skill": "Key Ideas and Details",
            "explain": {"en": "Mar defeated Quartang, who 'retreated to the trees to save his own life' and 'has never left the trees since that day.'",
                        "zh": "马尔击败了昆唐，他“退到树上保命”，并且“从那天起就再也没有离开过树”。"}
        },
        {
            "q": {"en": "This story is based on an Australian Aboriginal tale collected in what year?",
                  "zh": "这个故事改编自一则澳大利亚原住民传说，该传说是在哪一年被收集的？"},
            "options": [
                {"en": "1923", "zh": "1923年"},
                {"en": "1862", "zh": "1862年"},
                {"en": "1937", "zh": "1937年"},
                {"en": "2009", "zh": "2009年"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "The book notes the story is 'based on an Australian Aboriginal tale called \"How Fire was Stolen from the Red-Crested Cockatoo,\" collected in 1923.'",
                        "zh": "书中说明这个故事“改编自1923年收集的一则澳大利亚原住民传说《火是如何从红冠凤头鹦鹉那里被偷走的》”。"}
        },
        {
            "q": {"en": "When Quartang says 'The fire is for everyone now,' what idea is the story sharing?",
                  "zh": "当昆唐说“现在火属于每一个人”时，故事在传达什么观点？"},
            "options": [
                {"en": "Fire should belong to only one powerful bird", "zh": "火只应属于一只强大的鸟"},
                {"en": "Fire should be shared by all, not controlled by one", "zh": "火应该由大家共享，而不该被某一方独占"},
                {"en": "Fire is too dangerous to use", "zh": "火太危险，不该使用"},
                {"en": "Only humans may use fire", "zh": "只有人类才能用火"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "Quartang tells Mar, 'The fire is for everyone now. No one should freeze during the cold winters anymore.'",
                        "zh": "昆唐对马尔说：“现在火属于每一个人。寒冷冬天里再也不会有人冻僵了。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Retell the story of how the robin stole fire from the point of view of Prite the Wren, who first spied on Mar.",
                   "zh": "以最先跟踪马尔的鹪鹩普赖特的视角，复述知更鸟偷火的故事。"},
        "guidance": {
            "en": ["Describe what Prite saw when he followed Mar to the camp.",
                   "Explain how Tatkanna got the fire and why he is called Robin Redbreast."],
            "zh": ["描述普赖特跟踪马尔到营地时看到了什么。",
                   "解释塔特卡纳是如何拿到火的，以及他为什么被称为红胸知更鸟。"]
        }
    }
})

# 2. Hillary Clinton
books.append({
    "slug": "hillary-clinton",
    "title": "Hillary Clinton",
    "titleZh": "希拉里·克林顿",
    "level": "R",
    "genre": "Biography",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "In what year was Hillary Clinton born?",
                  "zh": "希拉里·克林顿出生于哪一年？"},
            "options": [
                {"en": "1947", "zh": "1947年"},
                {"en": "1965", "zh": "1965年"},
                {"en": "1975", "zh": "1975年"},
                {"en": "1993", "zh": "1993年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The book states: 'Hillary Rodham was born in 1947 and grew up near Chicago, Illinois.'",
                        "zh": "书中写道：“希拉里·罗达姆1947年出生，在伊利诺伊州芝加哥附近长大。”"}
        },
        {
            "q": {"en": "In the book's glossary, what does 'conservative' mean?",
                  "zh": "在本书词汇表中，“conservative（保守的）”是什么意思？"},
            "options": [
                {"en": "Traditional and reluctant to change", "zh": "传统的、不愿改变的"},
                {"en": "Brave and adventurous", "zh": "勇敢而爱冒险的"},
                {"en": "A kind of lawyer", "zh": "一种律师"},
                {"en": "Elected by the people", "zh": "由人民选举产生的"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines conservative as 'traditional and reluctant to change.'",
                        "zh": "词汇表将 conservative 定义为“传统的、不愿改变的”。"}
        },
        {
            "q": {"en": "Where did Hillary Rodham meet Bill Clinton?",
                  "zh": "希拉里·罗达姆是在哪里遇见比尔·克林顿的？"},
            "options": [
                {"en": "At a campaign rally in Arkansas", "zh": "在阿肯色州的一场竞选集会上"},
                {"en": "In the Yale law library", "zh": "在耶鲁大学法学院图书馆"},
                {"en": "At a NASA office", "zh": "在NASA的办公室"},
                {"en": "In the White House", "zh": "在白宫"}
            ],
            "answer": 1,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The book says: 'In 1971, Rodham met someone special in the Yale law library.'",
                        "zh": "书中说：“1971年，罗达姆在耶鲁大学法学院图书馆遇到了特别的人。”"}
        },
        {
            "q": {"en": "What happened in the year 2000 in Hillary Clinton's life?",
                  "zh": "在希拉里·克林顿的人生中，2000年发生了什么？"},
            "options": [
                {"en": "She became first lady of Arkansas", "zh": "她成为阿肯色州第一夫人"},
                {"en": "She won a seat as a U.S. senator from New York", "zh": "她赢得纽约州联邦参议员席位"},
                {"en": "She was elected president", "zh": "她当选总统"},
                {"en": "She graduated from Yale Law School", "zh": "她从耶鲁法学院毕业"}
            ],
            "answer": 1,
            "skill": "Key Ideas and Details",
            "explain": {"en": "In 2000, 'Hillary Clinton ran to become a U.S. senator for New York. She won easily, becoming the first female senator from that state.'",
                        "zh": "2000年，“希拉里·克林顿竞选纽约州联邦参议员并轻松胜出，成为该州第一位女性参议员”。"}
        },
        {
            "q": {"en": "Compare her travels: as First Lady she visited 79 countries, but as Secretary of State she visited how many?",
                  "zh": "比较她的出访：作为第一夫人她访问了79个国家，而作为国务卿她访问了多少个？"},
            "options": [
                {"en": "112 countries", "zh": "112个国家"},
                {"en": "45 countries", "zh": "45个国家"},
                {"en": "79 countries", "zh": "79个国家"},
                {"en": "200 countries", "zh": "200个国家"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "As First Lady she 'traveled to seventy-nine countries'; as Secretary of State she 'traveled to meet leaders in 112 countries.'",
                        "zh": "作为第一夫人她“出访了79个国家”；作为国务卿她“前往112个国家的领导人处访问”。"}
        },
        {
            "q": {"en": "Why did the author most likely write this book about Hillary Clinton?",
                  "zh": "作者最可能为什么写这本关于希拉里·克林顿的书？"},
            "options": [
                {"en": "To explain how to win a presidential election", "zh": "为了讲解如何赢得总统大选"},
                {"en": "To tell who she is and why she is important", "zh": "为了说明她是谁，以及她为何重要"},
                {"en": "To teach readers about the law", "zh": "为了向读者讲授法律知识"},
                {"en": "To describe life in the White House kitchen", "zh": "为了描写白宫厨房的生活"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "The Focus Question is 'Who is Hillary Clinton, and why is she important?'",
                        "zh": "书中的聚焦问题是：“希拉里·克林顿是谁，她为什么重要？”"}
        },
        {
            "q": {"en": "As Secretary of State, how many countries did Hillary Clinton visit?",
                  "zh": "作为国务卿，希拉里·克林顿访问了多少个国家？"},
            "options": [
                {"en": "112", "zh": "112个"},
                {"en": "79", "zh": "79个"},
                {"en": "50", "zh": "50个"},
                {"en": "33", "zh": "33个"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "She 'traveled to meet leaders in 112 countries—more than any other U.S. secretary of state.'",
                        "zh": "她“前往112个国家的领导人处访问——超过任何其他美国国务卿”。"}
        },
        {
            "q": {"en": "What did NASA tell thirteen-year-old Hillary when she asked how to become an astronaut?",
                  "zh": "当13岁的希拉里询问如何成为宇航员时，NASA告诉了她什么？"},
            "options": [
                {"en": "That she should study political science", "zh": "她应该学习政治科学"},
                {"en": "That there would not be any female astronauts", "zh": "那时不会有任何女性宇航员"},
                {"en": "That she could go to the Moon", "zh": "她可以去月球"},
                {"en": "That she needed to be a lawyer first", "zh": "她得先成为一名律师"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "NASA 'wrote her back and said there would not be any female astronauts.'",
                        "zh": "NASA“回信说那时不会有任何女性宇航员。”"}
        },
        {
            "q": {"en": "In 2016, Hillary Clinton became the first woman to do what?",
                  "zh": "2016年，希拉里·克林顿成为第一位做到什么的女性？"},
            "options": [
                {"en": "Win a U.S. presidential election", "zh": "赢得美国总统大选"},
                {"en": "Run for president on behalf of a major U.S. political party", "zh": "代表美国主要政党竞选总统"},
                {"en": "Serve as Secretary of State", "zh": "担任国务卿"},
                {"en": "Graduate from Wellesley", "zh": "从韦尔斯利学院毕业"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "In 2016 she 'became the first woman to run for president on behalf of a major U.S. political party.'",
                        "zh": "2016年她“成为第一位代表美国主要政党竞选总统的女性”。"}
        },
        {
            "q": {"en": "What main message does the book give about Hillary Clinton's life?",
                  "zh": "本书关于希拉里·克林顿的一生，传达了什么主要信息？"},
            "options": [
                {"en": "That she avoided challenges", "zh": "她回避了各种挑战"},
                {"en": "That she broke through barriers and set an example for girls and women", "zh": "她突破了重重障碍，为女孩和女性树立了榜样"},
                {"en": "That she only cared about winning", "zh": "她只在乎赢"},
                {"en": "That she was born wealthy", "zh": "她生来富有"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "The book says her 'life and work set a strong example for the girls and women who follow.'",
                        "zh": "书中说她“的一生和工作为后来的女孩和女性树立了强有力的榜样”。"}
        }
    ],
    "extended": {
        "prompt": {"en": "Make a timeline of five important events from Hillary Clinton's life in the order they happened.",
                   "zh": "按时间顺序，为希拉里·克林顿人生中的五个重要事件制作一条时间线。"},
        "guidance": {
            "en": ["Start with her birth in 1947 and her education at Wellesley and Yale.",
                   "Include her roles as First Lady, senator, Secretary of State, and 2016 presidential run."],
            "zh": ["从1947年出生以及她在韦尔斯利和耶鲁的求学开始。",
                   "包含她作为第一夫人、参议员、国务卿以及2016年竞选总统的角色。"]
        }
    }
})

# 3. Hansel and Gretel
books.append({
    "slug": "hansel-and-gretel",
    "title": "Hansel and Gretel",
    "titleZh": "汉塞尔与格蕾特",
    "level": "R",
    "genre": "Folktale",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "Why did Hansel and Gretel's family have almost no food?",
                  "zh": "汉塞尔和格蕾特家为什么几乎没有食物？"},
            "options": [
                {"en": "After three years of failed crops, only moldy potatoes were left", "zh": "连续三年庄稼歉收，只剩发霉的土豆"},
                {"en": "A flood washed away their farm", "zh": "洪水冲走了他们的农场"},
                {"en": "They ate too much candy", "zh": "他们吃了太多糖果"},
                {"en": "The stepmother ate it all", "zh": "继母把食物全吃光了"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The book says: 'After three years of failed crops, Hansel and Gretel's family had no food left but some moldy potatoes.'",
                        "zh": "书中说：“连续三年庄稼歉收后，汉塞尔和格蕾特家除了一些发霉的土豆外再无食物。”"}
        },
        {
            "q": {"en": "In the glossary, what does 'wicked' mean?",
                  "zh": "在词汇表中，“wicked”是什么意思？"},
            "options": [
                {"en": "Very mean or bad", "zh": "非常刻薄或坏"},
                {"en": "Very sleepy", "zh": "非常困倦"},
                {"en": "Very small", "zh": "非常小"},
                {"en": "Very happy", "zh": "非常高兴"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines wicked as 'very mean or bad.'",
                        "zh": "词汇表将 wicked 定义为“非常刻薄或坏”。"}
        },
        {
            "q": {"en": "What did Hansel use to mark a path home through the forest?",
                  "zh": "汉塞尔用什么在森林里标记回家的路？"},
            "options": [
                {"en": "Breadcrumbs dropped from a crust of bread", "zh": "从一块面包上掰下的面包屑"},
                {"en": "Stones he carried in his pocket", "zh": "他口袋里装的石头"},
                {"en": "Pieces of the witch's candy", "zh": "女巫的糖果碎块"},
                {"en": "Markings on tree bark", "zh": "树皮上的刻痕"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "Hansel 'decided to tear the bread into crumbs and drop them as he walked. He marked a path.'",
                        "zh": "汉塞尔“决定把面包掰成碎屑，一边走一边撒下。他标记出了一条路。”"}
        },
        {
            "q": {"en": "What ate Hansel's breadcrumbs so the children became lost?",
                  "zh": "是什么吃掉了汉塞尔的面包屑，让孩子们迷了路？"},
            "options": [
                {"en": "A sparrow", "zh": "一只麻雀"},
                {"en": "A hungry bear", "zh": "一只饥饿的熊"},
                {"en": "The stepmother", "zh": "继母"},
                {"en": "A goat", "zh": "一只山羊"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Birds ate your crumbs—we're lost!' Gretel cried, after a sparrow 'grab a crumb, and fly off.'",
                        "zh": "一只麻雀“叼起一块面包屑飞走了”后，格蕾特哭道：“鸟儿吃了你的面包屑——我们迷路了！”"}
        },
        {
            "q": {"en": "How was the cottage in the forest different from a normal house?",
                  "zh": "森林里的小屋与普通房屋有什么不同？"},
            "options": [
                {"en": "It was made entirely of sweets and gingerbread", "zh": "它完全是用糖果和姜饼做成的"},
                {"en": "It was built of stone", "zh": "它是用石头建造的"},
                {"en": "It was floating on water", "zh": "它漂浮在水面上"},
                {"en": "It was made of ice", "zh": "它是用冰做成的"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "'In a meadow was the most remarkable thing—a cottage made entirely of sweets!'",
                        "zh": "“草地上有一件最不寻常的东西——一座完全用糖果做成的小屋！”"}
        },
        {
            "q": {"en": "Why did Gretel give Hansel a chicken bone?",
                  "zh": "格蕾特为什么给汉塞尔一根鸡骨头？"},
            "options": [
                {"en": "To feed him because he was hungry", "zh": "因为他饿了，喂他吃"},
                {"en": "So the witch would pinch the bone instead of his arm, thinking he wasn't getting fat", "zh": "为了让女巫去捏骨头而不是他的胳膊，以为他没长胖"},
                {"en": "To unlock the birdcage", "zh": "用来打开鸟笼"},
                {"en": "To trade it for treasure", "zh": "用来换宝藏"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "Gretel whispered: 'When she tries to grab your arm, give her this instead,' so the witch pinched the bone and wondered 'Why aren't you getting fat?'",
                        "zh": "格蕾特低声说：“她要抓你胳膊时，把这个给她。”于是女巫捏的是骨头，还纳闷“你怎么不长胖？”"}
        },
        {
            "q": {"en": "How did the old woman trap Hansel?",
                  "zh": "老妇人是怎么困住汉塞尔的？"},
            "options": [
                {"en": "She locked him in the cottage door", "zh": "她把他锁在小屋门里"},
                {"en": "She tricked him into a birdcage and the door swung shut", "zh": "她骗他进鸟笼，笼门“咔嗒”一声关上了"},
                {"en": "She tied him with rope", "zh": "她用绳子把他绑起来"},
                {"en": "She fed him too much candy", "zh": "她给他吃太多糖果"}
            ],
            "answer": 1,
            "skill": "Key Ideas and Details",
            "explain": {"en": "Hansel climbed toward a latch 'He heard a click! as the cage door swung shut behind him.'",
                        "zh": "汉塞尔爬向门闩时，“他听到‘咔嗒’一声！笼门在他身后关上了。”"}
        },
        {
            "q": {"en": "What do Hansel and Gretel's actions in the story show about their characters?",
                  "zh": "汉塞尔和格蕾特在故事中的行为体现了他们怎样的性格？"},
            "options": [
                {"en": "They are lazy and give up easily", "zh": "他们懒惰，容易放弃"},
                {"en": "They are brave and clever, using tricks to escape", "zh": "他们勇敢而聪明，用计谋逃了出去"},
                {"en": "They are unkind to animals", "zh": "他们对动物很残忍"},
                {"en": "They are afraid of the dark", "zh": "他们怕黑"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "The Focus Question asks what you learn about their characters 'from what they say and do'; they trick the witch and free themselves.",
                        "zh": "聚焦问题是让你从“他们说的话和做的事”中了解其性格；他们骗过女巫并自救。"}
        },
        {
            "q": {"en": "How did the children finally escape from the witch?",
                  "zh": "孩子们最后是如何从女巫那里逃走的？"},
            "options": [
                {"en": "They ran while she was sleeping", "zh": "趁她睡着时跑掉"},
                {"en": "Gretel knocked the cage down with her broom and they shoved the witch inside it", "zh": "格蕾特用扫帚打落鸟笼，他们把女巫塞进笼里"},
                {"en": "A bird carried them away", "zh": "一只鸟把他们叼走了"},
                {"en": "Their father rescued them", "zh": "他们的父亲救了他们"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "Gretel 'swung her broom at the cage, knocking it from its hook... They shoved her into the cage and slammed the door.'",
                        "zh": "格蕾特“抡起扫帚打向鸟笼，把它从钩子上打落……他们把她塞进笼子，砰地关上门。”"}
        },
        {
            "q": {"en": "What did Hansel grab as the children fled into the forest?",
                  "zh": "孩子们逃进森林时，汉塞尔抓起了什么？"},
            "options": [
                {"en": "The witch's broom", "zh": "女巫的扫帚"},
                {"en": "The treasure chest", "zh": "宝箱"},
                {"en": "A sack of candy", "zh": "一袋糖果"},
                {"en": "The key to the cage", "zh": "笼子的钥匙"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Hansel snatched the treasure chest. Together, the children fled into the forest.' The treasure later buys food for the family.",
                        "zh": "“汉塞尔一把抓起宝箱。孩子们一起逃进了森林。”后来宝箱给家里换来了食物。"}
        }
    ],
    "extended": {
        "prompt": {"en": "Imagine the birds had not eaten Hansel's breadcrumbs. Write a paragraph describing how the story would change.",
                   "zh": "假设鸟儿没有吃掉汉塞尔的面包屑。写一段话，描述故事会有怎样的不同。"},
        "guidance": {
            "en": ["Think about whether the children would have found their way home.",
                   "Consider what might have happened with the witch in the forest."],
            "zh": ["想一想孩子们是否能找到回家的路。",
                   "设想一下森林里的女巫情节可能会怎样发展。"]
        }
    }
})

# 4. Hiking the Appalachian Trail
books.append({
    "slug": "hiking-the-appalachian-trail",
    "title": "Hiking the Appalachian Trail",
    "titleZh": "徒步阿巴拉契亚小径",
    "level": "R",
    "genre": "Narrative Nonfiction",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "When and where did Ben take his first step on the Appalachian Trail?",
                  "zh": "本是在何时何地迈出阿巴拉契亚小径的第一步的？"},
            "options": [
                {"en": "April 4, 2016, from Springer Mountain, Georgia", "zh": "2016年4月4日，从佐治亚州的斯普林格山"},
                {"en": "October 1, 2016, from Mount Katahdin", "zh": "2016年10月1日，从卡塔丁山"},
                {"en": "January 15, 1967, from Maine", "zh": "1967年1月15日，从缅因州"},
                {"en": "Summer 2015, from New Hampshire", "zh": "2015年夏天，从新罕布什尔州"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "Ben 'took my first step on April 4, 2016, from Springer Mountain, Georgia.'",
                        "zh": "本“于2016年4月4日从佐治亚州的斯普林格山迈出第一步”。"}
        },
        {
            "q": {"en": "In the glossary, what is 'thru-hiking'?",
                  "zh": "在词汇表中，“thru-hiking（全程徒步）”是什么？"},
            "options": [
                {"en": "Hiking only on weekends", "zh": "只在周末徒步"},
                {"en": "Hiking a long-distance trail from beginning to end within a single hiking season", "zh": "在单个徒步季节内从头到尾走完一条长途步道"},
                {"en": "Driving along a trail", "zh": "沿步道驾车"},
                {"en": "Climbing one mountain", "zh": "攀登一座山"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines thru-hiking as 'hiking a long-distance trail from beginning to end within a single hiking season.'",
                        "zh": "词汇表将 thru-hiking 定义为“在单个徒步季节内从头到尾走完一条长途步道”。"}
        },
        {
            "q": {"en": "According to the book's fun facts, how long is the Appalachian Trail?",
                  "zh": "根据书中的趣闻，阿巴拉契亚小径有多长？"},
            "options": [
                {"en": "2,190 miles (3,524 km)", "zh": "2,190英里（3,524公里）"},
                {"en": "1,000 miles", "zh": "1,000英里"},
                {"en": "5 million steps", "zh": "500万步"},
                {"en": "14 miles", "zh": "14英里"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The fun-facts box lists 'Length: 2,190 miles (3,524 km).'",
                        "zh": "趣闻框中列出“长度：2,190英里（3,524公里）”。"}
        },
        {
            "q": {"en": "Through how many U.S. states does the Appalachian Trail pass?",
                  "zh": "阿巴拉契亚小径穿过多少个美国州？"},
            "options": [
                {"en": "Fourteen", "zh": "14个"},
                {"en": "Two", "zh": "2个"},
                {"en": "Fifty", "zh": "50个"},
                {"en": "Twenty-five", "zh": "25个"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The trail 'begins in Georgia and travels over 2,000 miles north. It goes through fourteen U.S. states and ends in Maine.'",
                        "zh": "小径“始于佐治亚州，向北延伸两千多英里，穿过14个州，终点在缅因州”。"}
        },
        {
            "q": {"en": "How did Ben's feelings at the end of the hike compare to the beginning?",
                  "zh": "本在徒步结束时的感受与开始时相比如何？"},
            "options": [
                {"en": "He felt the same as at the start", "zh": "他和开始时感觉一样"},
                {"en": "At the end he felt strong and confident, able to call himself an athlete", "zh": "结束时他感到强壮而自信，可以自称运动员了"},
                {"en": "He was more afraid at the end", "zh": "结束时他更害怕了"},
                {"en": "He forgot why he started", "zh": "他忘记了出发的原因"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "Unlike his difficult first days, 'I felt strong and confident... after thru-hiking, I felt proud that I could call myself an athlete.'",
                        "zh": "与艰难的开头不同，“我感到强壮而自信……走完全程后，我自豪地觉得自己可以被称为运动员了”。"}
        },
        {
            "q": {"en": "What is the author's main purpose in writing this book?",
                  "zh": "作者写这本书的主要目的是什么？"},
            "options": [
                {"en": "To teach people to fear the wilderness", "zh": "教导人们畏惧荒野"},
                {"en": "To describe the challenges and rewards of hiking the Appalachian Trail", "zh": "为了描述徒步阿巴拉契亚小径的挑战与回报"},
                {"en": "To sell hiking gear", "zh": "为了售卖徒步装备"},
                {"en": "To compare trails in Europe", "zh": "为了比较欧洲的步道"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "The Focus Question is 'What are the challenges and rewards of hiking the Appalachian Trail?'",
                        "zh": "书中的聚焦问题是：“徒步阿巴拉契亚小径有哪些挑战与回报？”"}
        },
        {
            "q": {"en": "What mountain did Ben summit to finish the trail, and on what date?",
                  "zh": "本是从哪座山登顶完成全程的，具体日期是哪天？"},
            "options": [
                {"en": "Mount Katahdin, on October 1, 2016", "zh": "卡塔丁山，2016年10月1日"},
                {"en": "Clingman's Dome, on April 4, 2016", "zh": "克林曼穹顶，2016年4月4日"},
                {"en": "Springer Mountain, in 2015", "zh": "斯普林格山，2015年"},
                {"en": "Mount Everest, in 1937", "zh": "珠穆朗玛峰，1937年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'After nearly six months of hiking, I completed the A.T.! On October 1, 2016, I summited Mount Katahdin.'",
                        "zh": "“徒步近六个月后，我走完了阿巴拉契亚小径！2016年10月1日，我登上了卡塔丁山山顶。”"}
        },
        {
            "q": {"en": "What did Ben do to prepare for his thru-hike?",
                  "zh": "本为全程徒步做了哪些准备？"},
            "options": [
                {"en": "He practiced with a heavy pack, worked at an outdoor store, and saved money", "zh": "他背着沉重的背包练习、在户外店工作并存钱"},
                {"en": "He took a flight over the trail", "zh": "他乘飞机从空中俯瞰步道"},
                {"en": "He hired a guide", "zh": "他雇了一名向导"},
                {"en": "He waited for winter", "zh": "他一直等到冬天"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "'I practiced hiking while wearing my heavy pack... I got a job at an outdoor store to learn about hiking gear and tried to save money.'",
                        "zh": "“我背着沉重的背包练习徒步……我在一家户外店工作以了解装备，并努力存钱。”"}
        },
        {
            "q": {"en": "The book compares the trail's total elevation gain to climbing Mount Everest how many times?",
                  "zh": "书中把这条步道的总爬升高度比作攀登珠穆朗玛峰多少次？"},
            "options": [
                {"en": "Sixteen times", "zh": "16次"},
                {"en": "One time", "zh": "1次"},
                {"en": "Five times", "zh": "5次"},
                {"en": "One hundred times", "zh": "100次"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "The fun facts state: 'Elevation gain and loss: Equal to hiking Mount Everest from sea level and back—sixteen times!'",
                        "zh": "趣闻写道：“总爬升与下降：相当于从海平面登顶珠峰再返回——十六次！”"}
        },
        {
            "q": {"en": "According to Ben, what kept him going and made him never want to stop?",
                  "zh": "根据本的说法，是什么支撑他坚持下去、让他不想停下？"},
            "options": [
                {"en": "The prize money at the end", "zh": "终点的奖金"},
                {"en": "The love and support from those around him and at home", "zh": "身边人和家人的爱与支持"},
                {"en": "Fear of the bears", "zh": "对熊的恐惧"},
                {"en": "A new pair of shoes", "zh": "一双新鞋"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'The love and support from those around me and at home made me never want to stop.'",
                        "zh": "“身边人和家人的爱与支持，让我从不想停下来。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Write a paragraph about a dream you have achieved or would like to achieve, like Ben achieved his hike.",
                   "zh": "像本实现了徒步梦想一样，写一段话描述你已实现或想要实现的一个梦想。"},
        "guidance": {
            "en": ["State your dream clearly in the first sentence.",
                   "Explain one step you would take, as Ben did 'one step at a time.'"],
            "zh": ["在首句清楚地写出你的梦想。",
                   "像本那样“一步一个脚印”，说明你会采取的一个步骤。"]
        }
    }
})

# 5. Golf
books.append({
    "slug": "golf",
    "title": "Golf",
    "titleZh": "高尔夫",
    "level": "R",
    "genre": "Informational",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "Where is the birthplace of modern golf?",
                  "zh": "现代高尔夫运动的发源地是哪里？"},
            "options": [
                {"en": "Scotland", "zh": "苏格兰"},
                {"en": "The United States", "zh": "美国"},
                {"en": "Japan", "zh": "日本"},
                {"en": "The Moon", "zh": "月球"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Scotland is the birthplace of modern golf.'",
                        "zh": "“苏格兰是现代高尔夫运动的发源地。”"}
        },
        {
            "q": {"en": "In the glossary, what does 'par' mean in golf?",
                  "zh": "在词汇表中，高尔夫里的“par（标准杆）”是什么意思？"},
            "options": [
                {"en": "The number of golf strokes a player should use for a hole or course", "zh": "球员完成一个洞或整场球赛应当使用的击球杆数"},
                {"en": "A type of golf club", "zh": "一种高尔夫球杆"},
                {"en": "The person who carries clubs", "zh": "负责拿球杆的人"},
                {"en": "A water hazard", "zh": "水障"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines par as 'the number of golf strokes a player should use for a hole or course.'",
                        "zh": "词汇表将 par 定义为“球员完成一个洞或整场球赛应当使用的击球杆数”。"}
        },
        {
            "q": {"en": "In golf, what is a 'bunker'?",
                  "zh": "在高尔夫中，“bunker（沙坑）”是什么？"},
            "options": [
                {"en": "A sand-filled hazard", "zh": "填满沙子的障碍区"},
                {"en": "The hole itself", "zh": "球洞本身"},
                {"en": "A type of putter", "zh": "一种推杆"},
                {"en": "The green", "zh": "果岭"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'One type of hazard is a sand-filled area called a bunker.'",
                        "zh": "“有一种障碍区是填满沙子的区域，叫做沙坑（bunker）。”"}
        },
        {
            "q": {"en": "How do professional golfers get around the course differently from casual players?",
                  "zh": "职业高尔夫球员和休闲玩家在球场上移动的方式有何不同？"},
            "options": [
                {"en": "Pros ride golf carts while casual players walk", "zh": "职业选手坐球车，休闲玩家步行"},
                {"en": "Pros walk and have caddies carry their clubs, while casual players often ride carts", "zh": "职业选手步行并有球童背包，休闲玩家常坐球车"},
                {"en": "They both always fly", "zh": "他们都用飞的"},
                {"en": "Casual players use helicopters", "zh": "休闲玩家用直升机"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "'People who golf just for fun often ride the course in golf carts. Professional golfers walk... Helpers called caddies carry their clubs.'",
                        "zh": "“只为乐趣打球的人常坐球车游览球场。职业选手步行……叫做球童的助手替他们背包。”"}
        },
        {
            "q": {"en": "According to the book, which golfer won the most major championships?",
                  "zh": "根据书中内容，哪位高尔夫球员赢得的大满贯冠军最多？"},
            "options": [
                {"en": "Jack Nicklaus (eighteen majors)", "zh": "杰克·尼克劳斯（18个大满贯）"},
                {"en": "Tiger Woods", "zh": "老虎伍兹"},
                {"en": "Patty Berg", "zh": "帕蒂·伯格"},
                {"en": "Alan Shepard", "zh": "艾伦·谢泼德"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Jack Nicklaus is the top golfer in the history of the sport... He won eighteen majors.'",
                        "zh": "“杰克·尼克劳斯是这项运动历史上最顶尖的球员……他赢得过18个大满贯。”"}
        },
        {
            "q": {"en": "According to the book, why do millions of people love to play golf?",
                  "zh": "根据书中内容，为什么数百万人喜欢打高尔夫？"},
            "options": [
                {"en": "Because it is always easy to win", "zh": "因为总是很容易赢"},
                {"en": "It offers fun, relaxation, beautiful places, and a chance to improve", "zh": "它带来乐趣、放松、优美的环境以及提升自我的机会"},
                {"en": "Because it requires no practice", "zh": "因为它无需练习"},
                {"en": "Because it is played indoors", "zh": "因为它在室内进行"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Most of all, golf offers hours of fun and relaxation.' It is also played in 'beautiful places' with a chance 'to learn, practice, and improve.'",
                        "zh": "“最重要的是，高尔夫带来数小时的乐趣与放松。”它还在“优美的地方”进行，并让人有机会“学习、练习、进步”。"}
        },
        {
            "q": {"en": "When did modern golf balls with rubber cores first appear?",
                  "zh": "带橡胶芯的现代高尔夫球最早出现在哪一年？"},
            "options": [
                {"en": "1898", "zh": "1898年"},
                {"en": "1848", "zh": "1848年"},
                {"en": "The 1400s", "zh": "15世纪"},
                {"en": "2001", "zh": "2001年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Modern golf balls with rubber cores first appeared in 1898.'",
                        "zh": "“带橡胶芯的现代高尔夫球最早出现于1898年。”"}
        },
        {
            "q": {"en": "In golf, what are 'irons' used for?",
                  "zh": "在高尔夫中，“irons（铁杆）”是用来做什么的？"},
            "options": [
                {"en": "Shorter shots", "zh": "较短距离的击球"},
                {"en": "Long-distance hits", "zh": "远距离击球"},
                {"en": "Rolling the ball on the green", "zh": "在果岭上滚动球"},
                {"en": "Getting the ball out of water", "zh": "把球从水里弄出来"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "'Irons are used for shorter shots.' Woods/fairway metals are for long distances, putters roll the ball.",
                        "zh": "“铁杆用于较短距离的击球。”木杆用于远距离，推杆用于在果岭上滚球。"}
        },
        {
            "q": {"en": "The book ends by saying golf is 'out of this world.' Where besides Earth was golf once played?",
                  "zh": "本书结尾说高尔夫“超越世界（out of this world）”。除了地球，高尔夫还曾在何处被打过？"},
            "options": [
                {"en": "The Moon", "zh": "月球"},
                {"en": "Mars", "zh": "火星"},
                {"en": "The bottom of the ocean", "zh": "海底"},
                {"en": "A spaceship", "zh": "宇宙飞船里"}
            ],
            "answer": 0,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'The most unusual place golf has been played is ... the Moon! Astronaut Alan Shepard... hit a few golf balls while he was there' in 1971.",
                        "zh": "“高尔夫最不寻常的打球地点是……月球！宇航员艾伦·谢泼德1971年在那里时打了几杆球。”"}
        },
        {
            "q": {"en": "According to the book's list, which country has the most golf courses?",
                  "zh": "根据书中的列表，哪个国家拥有最多的高尔夫球场？"},
            "options": [
                {"en": "United States (17,672)", "zh": "美国（17,672个）"},
                {"en": "Japan (2,442)", "zh": "日本（2,442个）"},
                {"en": "Scotland", "zh": "苏格兰"},
                {"en": "China (500)", "zh": "中国（500个）"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "The Top Ten list ranks '1. United States (17,672)' as having the most golf courses.",
                        "zh": "前十名列表中“1. 美国（17,672）”拥有最多的高尔夫球场。"}
        }
    ],
    "extended": {
        "prompt": {"en": "Write a letter to a friend persuading him or her to start playing golf, using facts from the book.",
                   "zh": "用书中事实，写一封信说服朋友开始打高尔夫。"},
        "guidance": {
            "en": ["Mention that golf builds patience, focus, and offers relaxation.",
                   "Note its history in Scotland and that anyone can play with just a club and ball."],
            "zh": ["提到高尔夫能培养耐心、专注并带来放松。",
                   "指出它起源于苏格兰，而且只要有球杆和球，任何人都能玩。"]
        }
    }
})

# 6. Going to the Super Bowl
books.append({
    "slug": "going-to-the-super-bowl",
    "title": "Going to the Super Bowl",
    "titleZh": "去看超级碗",
    "level": "R",
    "genre": "Informational",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "Which Super Bowl featured the longest touchdown in history (James Harrison's 100-yard return)?",
                  "zh": "哪届超级碗出现了史上最长的达阵（詹姆斯·哈里森的100码回攻达阵）？"},
            "options": [
                {"en": "Super Bowl 43", "zh": "第43届超级碗"},
                {"en": "Super Bowl 1", "zh": "第1届超级碗"},
                {"en": "Super Bowl 5", "zh": "第5届超级碗"},
                {"en": "Super Bowl 24", "zh": "第24届超级碗"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "In Super Bowl 43 (Feb 1, 2009), 'James Harrison snatches the ball... A 100-yard interception return for a touchdown. The longest-ever touchdown in a Super Bowl.'",
                        "zh": "第43届超级碗（2009年2月1日）中，“詹姆斯·哈里森抢断……100码回攻达阵。这是超级碗史上最长的达阵。”"}
        },
        {
            "q": {"en": "In the glossary, what is an 'interception'?",
                  "zh": "在词汇表中，“interception（抄截）”是什么？"},
            "options": [
                {"en": "A pass caught or stolen by a player from the opposing team", "zh": "被对方球员截获或抢断的传球"},
                {"en": "A kind of trophy", "zh": "一种奖杯"},
                {"en": "A field goal", "zh": "一次射门得分"},
                {"en": "A type of helmet", "zh": "一种头盔"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines interception as 'a sports play in which a pass is caught or stolen by a player from the opposing team.'",
                        "zh": "词汇表将 interception 定义为“对方球员截获或抢断传球的比赛行为”。"}
        },
        {
            "q": {"en": "Who performed at the Super Bowl 43 halftime show?",
                  "zh": "第43届超级碗的中场秀由谁表演？"},
            "options": [
                {"en": "Bruce Springsteen", "zh": "布鲁斯·斯普林斯汀"},
                {"en": "Britney Spears", "zh": "布兰妮·斯皮尔斯"},
                {"en": "The Rolling Stones", "zh": "滚石乐队"},
                {"en": "Prince", "zh": "普林斯"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'The celebrity performer at Super Bowl 43 was rock 'n' roll legend Bruce Springsteen.'",
                        "zh": "“第43届超级碗的表演嘉宾是摇滚传奇人物布鲁斯·斯普林斯汀。”"}
        },
        {
            "q": {"en": "When was the first Super Bowl played?",
                  "zh": "第一届超级碗是在何时举行的？"},
            "options": [
                {"en": "January 15, 1967", "zh": "1967年1月15日"},
                {"en": "February 1, 2009", "zh": "2009年2月1日"},
                {"en": "1920", "zh": "1920年"},
                {"en": "1975", "zh": "1975年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'The first Super Bowl was held at the Los Angeles Coliseum on January 15, 1967.'",
                        "zh": "“第一届超级碗于1967年1月15日在洛杉矶纪念体育场举行。”"}
        },
        {
            "q": {"en": "Compare costs: about how much did a 30-second commercial cost in 2009 versus the first Super Bowl in 1967?",
                  "zh": "比较费用：2009年一则30秒广告的费用与1967年第一届超级碗相比大约是多少？"},
            "options": [
                {"en": "Over $3 million in 2009 versus $40,000 in 1967", "zh": "2009年超过300万美元，1967年为4万美元"},
                {"en": "Both cost about $40,000", "zh": "两者都约为4万美元"},
                {"en": "Both cost over $3 million", "zh": "两者都超过300万美元"},
                {"en": "It was free in 2009", "zh": "2009年是免费的"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "'It can cost advertisers over $3 million to air just one 30-second commercial during the Super Bowl' in 2009, while 'Showing a commercial on the first Super Bowl, in 1967, cost just $40,000.'",
                        "zh": "2009年“一则30秒广告花费广告商超过300万美元”，而“1967年第一届超级碗播一则广告只需4万美元”。"}
        },
        {
            "q": {"en": "Why does the book call 'Super Bowl Sunday' an unofficial national holiday?",
                  "zh": "本书为什么把“超级碗星期天”称为非官方的全国性节日？"},
            "options": [
                {"en": "Because the president declares it a holiday", "zh": "因为总统宣布它为节日"},
                {"en": "Because friends and families gather to watch, root for teams, and celebrate", "zh": "因为朋友和家人聚在一起观看、为球队加油并庆祝"},
                {"en": "Because schools close for a week", "zh": "因为学校停课一周"},
                {"en": "Because it is a religious day", "zh": "因为这是一个宗教节日"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Super Bowl Sunday' is 'an unofficial national holiday. Friends and families get together to watch the game, root for their team, and have a good time.'",
                        "zh": "“超级碗星期天”是“非官方的全国性节日。朋友和家人聚在一起看比赛、为球队加油、尽情享受。”"}
        },
        {
            "q": {"en": "The Super Bowl trophy is named after which legendary coach?",
                  "zh": "超级碗奖杯是以哪位传奇教练的名字命名的？"},
            "options": [
                {"en": "Vince Lombardi", "zh": "文斯·隆巴迪"},
                {"en": "Lamar Hunt", "zh": "拉马尔·亨特"},
                {"en": "Pete Rozelle", "zh": "皮特·罗泽尔"},
                {"en": "Joe Namath", "zh": "乔·纳马斯"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The winners get 'the Vince Lombardi Trophy, named after the legendary coach of the Green Bay Packers.'",
                        "zh": "获胜队得到“文斯·隆巴迪奖杯，以绿湾包装工队传奇教练的名字命名”。"}
        },
        {
            "q": {"en": "How did the Super Bowl get its name?",
                  "zh": "“超级碗”这个名字是怎么来的？"},
            "options": [
                {"en": "From a Wham-O SuperBall toy and college 'Bowl' stadiums", "zh": "源自 Wham-O SuperBall 玩具，以及大学'Bowl'（碗形）球场"},
                {"en": "From the shape of a football", "zh": "来自橄榄球的形状"},
                {"en": "From a famous coach", "zh": "来自一位著名教练"},
                {"en": "From the NFL founder", "zh": "来自NFL创始人"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "Lamar Hunt 'came up with the name Super Bowl after he saw his kids playing with a Wham-O SuperBall. The \"Bowl\" part came from... the Rose Bowl' stadiums.",
                        "zh": "拉马尔·亨特“看到孩子们玩 Wham-O SuperBall 玩具后想出了超级碗这个名字。‘Bowl’部分来自……玫瑰碗等体育场。”"}
        },
        {
            "q": {"en": "What does the book say makes the Super Bowl fun?",
                  "zh": "本书说是什么让超级碗充满乐趣？"},
            "options": [
                {"en": "That the winner is always known in advance", "zh": "胜负总是提前确定"},
                {"en": "That you never know what will happen", "zh": "因为你永远不知道会发生什么"},
                {"en": "That it is very short", "zh": "因为它很短"},
                {"en": "That only one team plays", "zh": "因为只有一支球队参赛"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Yet what makes the Super Bowl fun is that you never know what will happen.'",
                        "zh": "“然而，让超级碗充满乐趣的，正是你永远不知道会发生什么。”"}
        },
        {
            "q": {"en": "According to the book, which team set the record for the most Super Bowl wins?",
                  "zh": "根据书中内容，哪支球队创下了超级碗夺冠次数最多的纪录？"},
            "options": [
                {"en": "The Pittsburgh Steelers (six wins)", "zh": "匹兹堡钢人队（6次夺冠）"},
                {"en": "The Green Bay Packers", "zh": "绿湾包装工队"},
                {"en": "The Buffalo Bills", "zh": "布法罗比尔队"},
                {"en": "The New York Giants", "zh": "纽约巨人队"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "The Steelers won Super Bowl 43, 'setting the Super Bowl record for most wins by a team: six.'",
                        "zh": "钢人队赢下第43届超级碗，“创下球队夺冠次数最多纪录：六次”。"}
        }
    ],
    "extended": {
        "prompt": {"en": "Choose two Super Bowl facts from the book and compare how the game has changed since 1967.",
                   "zh": "从书中任选两个关于超级碗的事实，比较这项赛事自1967年以来的变化。"},
        "guidance": {
            "en": ["Compare things like ticket demand, TV viewers, or commercial costs.",
                   "Explain why the game grew into a huge event."],
            "zh": ["可比较门票需求、电视观众数或广告费用等。",
                   "解释这项赛事为何发展成盛大活动。"]
        }
    }
})

# 7. Ghost Towns
books.append({
    "slug": "ghost-towns",
    "title": "Ghost Towns",
    "titleZh": "鬼镇",
    "level": "R",
    "genre": "Informational",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "What is a ghost town?",
                  "zh": "什么是鬼镇？"},
            "options": [
                {"en": "A human settlement where people no longer live", "zh": "人们不再居住的人类聚居地"},
                {"en": "A town full of ghosts", "zh": "到处都是鬼的城镇"},
                {"en": "A very large city", "zh": "一座非常大的城市"},
                {"en": "A town that was never built", "zh": "一座从未建成的城镇"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Ghost towns are human settlements where people no longer live.'",
                        "zh": "“鬼镇是的人们不再居住的人类聚居地。”"}
        },
        {
            "q": {"en": "In the glossary, what does 'remote' mean?",
                  "zh": "在词汇表中，“remote”是什么意思？"},
            "options": [
                {"en": "Distant or isolated", "zh": "遥远或孤立的"},
                {"en": "Crowded", "zh": "拥挤的"},
                {"en": "Underwater", "zh": "在水下的"},
                {"en": "On fire", "zh": "着火的"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines remote as 'distant or isolated.'",
                        "zh": "词汇表将 remote 定义为“遥远的、孤立的”。"}
        },
        {
            "q": {"en": "What caused Bannack, Montana, to become a ghost town?",
                  "zh": "是什么导致蒙大拿州的班纳克变成了鬼镇？"},
            "options": [
                {"en": "A volcano erupted", "zh": "火山喷发"},
                {"en": "Gold became hard to find, so people left", "zh": "金子越来越难找，人们离开了"},
                {"en": "A nuclear accident", "zh": "核事故"},
                {"en": "A tsunami", "zh": "海啸"}
            ],
            "answer": 1,
            "skill": "Key Ideas and Details",
            "explain": {"en": "After John White found gold, 'once gold became hard to find, Bannack turned into a ghost town.'",
                        "zh": "约翰·怀特发现金子后，“金子一旦难找，班纳克就变成了一座鬼镇。”"}
        },
        {
            "q": {"en": "On what date did the volcano on Montserrat erupt, creating a ghost town?",
                  "zh": "蒙特塞拉特岛的火山是在何时喷发、从而形成鬼镇的？"},
            "options": [
                {"en": "July 1995", "zh": "1995年7月"},
                {"en": "March 2011", "zh": "2011年3月"},
                {"en": "May 27, 1962", "zh": "1962年5月27日"},
                {"en": "1986", "zh": "1986年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'In July 1995, the volcano erupted, and it's been erupting ever since.' The capital Plymouth was destroyed.",
                        "zh": "“1995年7月，火山喷发，并且至今仍在喷发。”首府普利茅斯被摧毁。"}
        },
        {
            "q": {"en": "Which town became a ghost town after a 1986 nuclear accident?",
                  "zh": "哪座城镇是在1986年核事故后变成鬼镇的？"},
            "options": [
                {"en": "Pripyat, Ukraine", "zh": "乌克兰的普里皮亚季"},
                {"en": "Centralia, Pennsylvania", "zh": "宾夕法尼亚州的森特利亚"},
                {"en": "Okuma, Japan", "zh": "日本的大熊町"},
                {"en": "Kolmanskop, Namibia", "zh": "纳米比亚的科尔曼斯科普"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "Pripyat, Ukraine, 'was abandoned after a deadly nuclear accident in 1986' at Chernobyl.",
                        "zh": "乌克兰的普里皮亚季“在1986年切尔诺贝利致命核事故后被废弃”。"}
        },
        {
            "q": {"en": "What do all ghost towns have in common, according to the book?",
                  "zh": "根据本书，所有鬼镇有何共同点？"},
            "options": [
                {"en": "They are near the ocean", "zh": "它们都靠近海洋"},
                {"en": "They are lonely places where people left due to a threat or lost work", "zh": "它们都是荒凉之地，人们因受威胁或失去生计而离开"},
                {"en": "They were all founded in 1923", "zh": "它们都建于1923年"},
                {"en": "They all have gold", "zh": "它们都有金子"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Residents often leave a town because of some kind of threat or because their work disappeared.' All are 'lonely places with secrets to share.'",
                        "zh": "“居民常因某种威胁或生计消失而离开。”它们都是“有着秘密可分享的荒凉之地”。"}
        },
        {
            "q": {"en": "What is special about Ordos (Kangbashi), China?",
                  "zh": "中国的鄂尔多斯（康巴什）有什么特别之处？"},
            "options": [
                {"en": "It is the world's largest ghost city that was always empty", "zh": "它是世界上最大的鬼城，且从一开始就空着"},
                {"en": "It was abandoned after a volcano", "zh": "它在火山喷发后被废弃"},
                {"en": "It was a whaling port", "zh": "它曾是一座捕鲸港"},
                {"en": "It was built on a cliff", "zh": "它建在悬崖上"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'the world's largest ghost town—actually a ghost city—has always been empty' because it was poorly planned and too expensive.",
                        "zh": "“世界上最大的鬼镇——其实是一座鬼城——从一开始就是空的”，因为它规划不善、过于昂贵。"}
        },
        {
            "q": {"en": "Why did the underground fire start in Centralia, Pennsylvania?",
                  "zh": "宾夕法尼亚州森特利亚的地下火是如何燃起的？"},
            "options": [
                {"en": "Lightning struck the town", "zh": "闪电击中了小镇"},
                {"en": "Firefighters set fire to a trash dump in 1962 and it spread to old mines", "zh": "1962年消防员焚烧垃圾场，火势蔓延到旧矿井"},
                {"en": "A volcano erupted", "zh": "火山喷发"},
                {"en": "A nuclear plant exploded", "zh": "核电站爆炸"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "'On May 27, 1962, Firefighters set fire to the town's trash dump... The fire was not put out properly, and it spread into the abandoned mines.'",
                        "zh": "“1962年5月27日，消防员焚烧镇上的垃圾场……火没有被妥善扑灭，蔓延进了废弃矿井。”"}
        },
        {
            "q": {"en": "Which ghost town was abandoned because it was too remote with too few resources?",
                  "zh": "哪座鬼镇是因为过于偏远、资源太少而被废弃的？"},
            "options": [
                {"en": "St. Kilda, Scotland", "zh": "苏格兰的圣基尔达"},
                {"en": "Bannack, Montana", "zh": "蒙大拿州的班纳克"},
                {"en": "Villa Epecuen, Argentina", "zh": "阿根廷的维拉埃佩库恩"},
                {"en": "Grytviken, South Georgia", "zh": "南乔治亚岛的格里特维肯"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "St. Kilda is 'a group of small islands 110 miles off the west coast... The islands had too few resources for residents... Life in such a remote place simply became too difficult.'",
                        "zh": "圣基尔达是“西海岸外110英里处的一组小岛……岛上资源太少……在如此偏远的地方生活实在太艰难了。”"}
        },
        {
            "q": {"en": "What is the author's purpose in writing about ghost towns?",
                  "zh": "作者写鬼镇的目的是什么？"},
            "options": [
                {"en": "To scare readers with ghost stories", "zh": "用鬼故事吓唬读者"},
                {"en": "To share the stories and reasons behind why these places were abandoned", "zh": "为了讲述这些地方被废弃的故事与原因"},
                {"en": "To sell real estate", "zh": "为了卖房"},
                {"en": "To teach about volcanoes only", "zh": "只为了讲授火山知识"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Learning their stories brings life to places where only shadows and memories may remain.'",
                        "zh": "“了解它们的故事，为那些只剩阴影与记忆的地方注入生机。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Create an imaginary ghost town: give it a name and location, and write how it became a ghost town.",
                   "zh": "创造一个虚构的鬼镇：给它起名并设定地点，再写写它是如何变成鬼镇的。"},
        "guidance": {
            "en": ["Choose a reason from the book (lost resource, disaster, remote location, etc.).",
                   "Describe what the empty buildings look like now."],
            "zh": ["从书中选一个原因（资源枯竭、灾难、位置偏远等）。",
                   "描述如今那些空建筑的样子。"]
        }
    }
})

# 8. Glow-in-the-Dark Animals
books.append({
    "slug": "glow-in-the-dark-animals",
    "title": "Glow-in-the-Dark Animals",
    "titleZh": "夜间发光的动物",
    "level": "R",
    "genre": "Informational",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "What does 'bioluminescent' mean?",
                  "zh": "“bioluminescent（生物发光）”是什么意思？"},
            "options": [
                {"en": "Glowing with light made by living things", "zh": "由生物自身化学反应发出光"},
                {"en": "Able to fly", "zh": "能够飞行"},
                {"en": "Living in the desert", "zh": "生活在沙漠里"},
                {"en": "Very large", "zh": "体型非常大"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The book explains bioluminescent means 'life glowing'—animals that 'make their own light.'",
                        "zh": "书中解释 bioluminescent 意为“生命发光”——动物“自己制造光”。"}
        },
        {
            "q": {"en": "In the word 'bioluminescent,' what does 'bio' come from?",
                  "zh": "在“bioluminescent”一词中，“bio”来自哪里？"},
            "options": [
                {"en": "A Greek word meaning 'life'", "zh": "一个意为‘生命’的希腊词"},
                {"en": "A Latin word meaning 'light'", "zh": "一个意为‘光’的拉丁词"},
                {"en": "A Spanish word meaning 'water'", "zh": "一个意为‘水’的西班牙语词"},
                {"en": "An English word meaning 'big'", "zh": "一个意为‘大’的英语词"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "'The first part, bio, comes from a Greek word that means \"life.\" The second part... comes from a Latin word that means \"glowing.\"'",
                        "zh": "“前半部分 bio 来自一个意为‘生命’的希腊词。后半部分……来自一个意为‘发光’的拉丁词。”"}
        },
        {
            "q": {"en": "Which land animal glows in its abdomen (hind part of its body)?",
                  "zh": "哪种陆地动物在腹部（身体后部）发光？"},
            "options": [
                {"en": "The firefly", "zh": "萤火虫"},
                {"en": "The kangaroo", "zh": "袋鼠"},
                {"en": "The eagle", "zh": "鹰"},
                {"en": "The penguin", "zh": "企鹅"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Fireflies produce the glow in their abdomen, the hind part of their bodies.'",
                        "zh": "“萤火虫在腹部——身体的后部——产生光。”"}
        },
        {
            "q": {"en": "How does the anglerfish use its glow?",
                  "zh": "鮟鱇鱼是如何利用它的光的？"},
            "options": [
                {"en": "It lights up its whole body to scare enemies", "zh": "它让全身发光来吓退敌人"},
                {"en": "A glowing tip on a stalk lures small fish, then it swallows them", "zh": "柄端的发光 tip 吸引小鱼，然后把它吞掉"},
                {"en": "It uses the glow to cook food", "zh": "它用光来烹饪食物"},
                {"en": "It signals other anglerfish to mate", "zh": "它发光向同类求偶"}
            ],
            "answer": 1,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'The tip of the stalk has a glowing white light that attracts small ocean fish... Then the anglerfish swallows them whole.'",
                        "zh": "“柄端有发光的白光，吸引小型海洋鱼类……然后鮟鱇鱼把它们整个吞下。”"}
        },
        {
            "q": {"en": "How do a squid and a cookie-cutter shark each use glow to hide?",
                  "zh": "鱿鱼和雪茄鲨分别是如何利用光来隐藏自己的？"},
            "options": [
                {"en": "Both squirt glowing clouds", "zh": "两者都喷出发光云"},
                {"en": "Squid makes a glowing cloud; the shark's belly glows to blend with the bright surface", "zh": "鱿鱼制造发光云；雪茄鲨的腹部发光以融入明亮的水面"},
                {"en": "Both glow their whole bodies", "zh": "两者都让全身发光"},
                {"en": "Neither uses glow to hide", "zh": "两者都不用光来隐藏"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "Squid 'squirt chemicals... to make a glowing cloud' to hide. The cookie-cutter shark's belly 'glows with a pale blue-green color' to camouflage against the surface.",
                        "zh": "鱿鱼“喷出化学物质……制造发光云”来隐藏。雪茄鲨的腹部“发出淡淡的蓝绿色光”以融入水面伪装。"}
        },
        {
            "q": {"en": "Why do animals flash and glow, according to the book?",
                  "zh": "根据本书，动物为什么会闪烁和发光？"},
            "options": [
                {"en": "Just for decoration", "zh": "仅仅为了装饰"},
                {"en": "To help them survive: signal, hunt, hide, call for help, fool enemies", "zh": "为了生存：发信号、捕猎、隐藏、求救、迷惑敌人"},
                {"en": "Because they are cold", "zh": "因为它们冷"},
                {"en": "To attract humans", "zh": "为了吸引人类"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'They use their lights to signal, hunt, and hide. They also use them to call for help and to fool their enemies. Glowing helps them survive.'",
                        "zh": "“它们用光来发信号、捕猎、隐藏，也用来求救和迷惑敌人。发光帮助它们生存。”"}
        },
        {
            "q": {"en": "What three things mix together inside an animal to produce light?",
                  "zh": "动物体内是哪三种物质混合在一起产生光的？"},
            "options": [
                {"en": "Luciferin + luciferase + oxygen", "zh": "荧光素 + 荧光素酶 + 氧气"},
                {"en": "Water + salt + sugar", "zh": "水 + 盐 + 糖"},
                {"en": "Sunlight + blood + skin", "zh": "阳光 + 血液 + 皮肤"},
                {"en": "Bones + muscle + fat", "zh": "骨头 + 肌肉 + 脂肪"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "The chemical equation given is 'Luciferin + Luciferase + Oxygen = Light.'",
                        "zh": "书中给出的化学方程式是“荧光素 + 荧光素酶 + 氧气 = 光”。"}
        },
        {
            "q": {"en": "How does the flashlight fish produce its glow?",
                  "zh": "闪光鱼是如何发出光的？"},
            "options": [
                {"en": "It makes light inside its own cells", "zh": "它在自身细胞内制造光"},
                {"en": "It stores glowing bacteria in a pouch beneath each eye", "zh": "它在每只眼睛下方的囊袋中储存发光细菌"},
                {"en": "It reflects moonlight", "zh": "它反射月光"},
                {"en": "It eats fireflies", "zh": "它吃萤火虫"}
            ],
            "answer": 1,
            "skill": "Craft and Structure",
            "explain": {"en": "'The flashlight fish stores about a billion glowing bacteria inside a pouch beneath each eye.'",
                        "zh": "“闪光鱼在每只眼睛下方的囊袋中储存约十亿个发光细菌。”"}
        },
        {
            "q": {"en": "In what ocean zone do most glowing animals live (about 200–1,000 m deep)?",
                  "zh": "大多数发光动物生活在哪个海洋区域（约水深200–1000米）？"},
            "options": [
                {"en": "The twilight zone", "zh": "微光带"},
                {"en": "The surface only", "zh": "仅在水面"},
                {"en": "The deepest trench", "zh": "最深的海沟"},
                {"en": "Rivers and lakes", "zh": "河流和湖泊"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "Scientists call the area 'from about 200 meters... to about 1,000 meters' the twilight zone, where most glowing animals produce matching blue-green light.",
                        "zh": "科学家把“约200米……到约1000米”的区域称为微光带，大多数发光动物在那里发出相应的蓝绿色光。"}
        },
        {
            "q": {"en": "How is an animal's glow different from a lightbulb's light?",
                  "zh": "动物的光与灯泡的光有何不同？"},
            "options": [
                {"en": "It gives off very little heat (a cool glow)", "zh": "它几乎不发热（是冷光）"},
                {"en": "It is much hotter", "zh": "它热得多"},
                {"en": "It only works underwater", "zh": "它只能在水下起作用"},
                {"en": "It changes color with sound", "zh": "它随声音变色"}
            ],
            "answer": 0,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'A glowing animal gives off very little heat.' Unlike a lightbulb, 'This chemically created light... is a cool glow.'",
                        "zh": "“发光动物几乎不散发热量。”与灯泡不同，“这种化学反应产生的光……是冷光。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Imagine you discovered a new glow-in-the-dark animal. Describe what it looks like and how it uses its glow to survive.",
                   "zh": "假设你会发现一种新的夜间发光动物。描述它的样子，以及它如何利用光来生存。"},
        "guidance": {
            "en": ["Name one reason it glows (signal, hunt, hide, fool enemies).",
                   "Decide whether it lives on land or in the sea."],
            "zh": ["说出它发光的一个原因（发信号、捕猎、隐藏、迷惑敌人）。",
                   "判断它生活在陆地还是海洋。"]
        }
    }
})

# 9. Foods Around the World
books.append({
    "slug": "foods-around-the-world",
    "title": "Foods Around the World",
    "titleZh": "世界各地的食物",
    "level": "R",
    "genre": "Informational",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "In which African region are many dishes made with peanuts?",
                  "zh": "在非洲的哪个地区，许多菜肴是用花生制作的？"},
            "options": [
                {"en": "West Africa", "zh": "西非"},
                {"en": "North Africa", "zh": "北非"},
                {"en": "Southern Africa", "zh": "南部非洲"},
                {"en": "Central Africa", "zh": "中部非洲"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'In West Africa, you can find lots of dishes made with peanuts. Peanuts flavor everything from... chicken-peanut stew to peanut ice cream.'",
                        "zh": "“在西非，你能找到许多用花生做的菜。花生为从……鸡肉花生炖菜到花生冰淇淋的一切增添风味。”"}
        },
        {
            "q": {"en": "In the glossary, what is 'sushi'?",
                  "zh": "在词汇表中，“sushi（寿司）”是什么？"},
            "options": [
                {"en": "Small pieces of fish or vegetables wrapped in rice or seaweed", "zh": "用米饭或海苔包裹的小块鱼或蔬菜"},
                {"en": "A Russian beet soup", "zh": "一种俄罗斯甜菜汤"},
                {"en": "A French pastry", "zh": "一种法式糕点"},
                {"en": "A type of barbecue", "zh": "一种烧烤"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines sushi as 'Japanese delicacy; small pieces of fish or vegetables wrapped in rice or seaweed.'",
                        "zh": "词汇表将 sushi 定义为“日本佳肴；用米饭或海苔包裹的小块鱼或蔬菜”。"}
        },
        {
            "q": {"en": "What is borscht?",
                  "zh": "“borscht（罗宋汤）”是什么？"},
            "options": [
                {"en": "A Russian cold beet soup served with sour cream", "zh": "一种俄罗斯冷甜菜汤，配酸奶油食用"},
                {"en": "A Japanese fish dish", "zh": "一种日本鱼肴"},
                {"en": "A Mexican chocolate drink", "zh": "一种墨西哥巧克力饮品"},
                {"en": "An Italian pastry", "zh": "一种意大利糕点"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "Russia 'is also home to a famous cold beet soup called borscht,' often served 'with a drop of sour cream on top.'",
                        "zh": "俄罗斯“还有一种著名的冷甜菜汤叫罗宋汤”，通常“顶上点一滴酸奶油”食用。"}
        },
        {
            "q": {"en": "Where did chocolate originally come from, according to the book?",
                  "zh": "根据本书，巧克力最初来自哪里？"},
            "options": [
                {"en": "From the cacao tree; the Aztecs in Mexico made a bitter chocolate drink", "zh": "来自可可树；墨西哥的阿兹特克人制作了苦巧克力饮品"},
                {"en": "From France", "zh": "来自法国"},
                {"en": "From China", "zh": "来自中国"},
                {"en": "From Australia", "zh": "来自澳大利亚"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Chocolate comes from the beans of the cacao tree. The Aztecs... crushed cacao beans to make a rich, bitter chocolate drink.'",
                        "zh": "“巧克力来自可可树的豆子。阿兹特克人……碾碎可可豆，制成浓郁苦涩的巧克力饮品。”"}
        },
        {
            "q": {"en": "How are foods in North Africa and Southern Africa different?",
                  "zh": "北非和南部非洲的食物有何不同？"},
            "options": [
                {"en": "North Africa cooks in a tagine pot; Southern Africa grills fish and wild game", "zh": "北非用塔吉锅烹煮；南部非洲烧烤鱼和野味"},
                {"en": "They are exactly the same", "zh": "它们完全一样"},
                {"en": "Both only eat peanuts", "zh": "两者都只吃花生"},
                {"en": "Both are known for sushi", "zh": "两者都以寿司闻名"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "North Africa: 'many family meals are cooked in a special clay pot called a tagine pot.' Southern Africa: 'people near the coast eat a variety of fresh fish... wild game.'",
                        "zh": "北非：“许多家庭餐用一种叫塔吉锅的特制陶锅烹煮。”南部非洲：“沿海居民吃各种鲜鱼……以及野味。”"}
        },
        {
            "q": {"en": "According to the book, why is learning about foods from other places valuable?",
                  "zh": "根据本书，了解其他地方的食物为什么有价值？"},
            "options": [
                {"en": "Because it helps you cook faster", "zh": "因为它让你做饭更快"},
                {"en": "Because learning a country's foods is part of learning its culture", "zh": "因为了解一个国家的食物，就是了解其文化的一部分"},
                {"en": "Because it replaces school", "zh": "因为它能替代上学"},
                {"en": "Because it is required by law", "zh": "因为这是法律要求的"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Learning about the country's foods is part of learning about its culture.'",
                        "zh": "“了解一个国家的食物，就是了解其文化的一部分。”"}
        },
        {
            "q": {"en": "In Latino cooking, what is a 'tortilla' used for?",
                  "zh": "在拉美烹饪中，“tortilla（玉米饼）”是用来做什么的？"},
            "options": [
                {"en": "Wrapping up quick meals", "zh": "包裹速食"},
                {"en": "Making soup", "zh": "做汤"},
                {"en": "Baking bread", "zh": "烤面包"},
                {"en": "Brewing tea", "zh": "泡茶"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Quick meals can be wrapped up in a tortilla, a thin, flat, fried bread made with flour or ground cornmeal.'",
                        "zh": "“速食可以用玉米饼包裹，那是一种用面粉或玉米粉做的薄而平的油炸面饼。”"}
        },
        {
            "q": {"en": "What is 'dim sum'?",
                  "zh": "“dim sum（点心）”是什么？"},
            "options": [
                {"en": "A light meal of filled dumplings and bite-sized foods in bamboo steamers", "zh": "用竹蒸笼蒸的、包馅小饺子与一口大小食物组成的轻食"},
                {"en": "A kind of tea", "zh": "一种茶"},
                {"en": "A spicy sauce", "zh": "一种辣酱"},
                {"en": "A sweet dessert", "zh": "一种甜点"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "'Filled dumplings and bite-sized portions of food are stacked in small bamboo steamers for a light meal called dim sum.'",
                        "zh": "“包馅的小饺子和小份食物叠在小竹蒸笼里，做成一种叫点心的轻食。”"}
        },
        {
            "q": {"en": "Which South Pacific animal was once eaten but is now protected because it became endangered?",
                  "zh": "南太平洋的哪种动物曾被食用，但因濒临灭绝如今受到保护？"},
            "options": [
                {"en": "Flying foxes (large fruit bats)", "zh": "飞狐（大型果蝠）"},
                {"en": "Giant clams", "zh": "巨蛤"},
                {"en": "Sea cucumbers", "zh": "海参"},
                {"en": "Pineapples", "zh": "菠萝"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "'Some tropical islanders ate large bats called flying foxes... the tasty bats became endangered, so people have stopped eating them.'",
                        "zh": "“一些热带岛民吃叫飞狐的大型蝙蝠……这些美味的蝙蝠变得濒危，所以人们已停止食用它们。”"}
        },
        {
            "q": {"en": "What does the book encourage readers to do after learning about world foods?",
                  "zh": "本书鼓励读者在了解世界各地食物后去做什么？"},
            "options": [
                {"en": "Avoid unfamiliar foods", "zh": "避开不熟悉的食物"},
                {"en": "Try new restaurants or foods with family and explore", "zh": "和家人尝试新餐馆或新食物，并去探索"},
                {"en": "Only eat peanut butter", "zh": "只吃花生酱"},
                {"en": "Stop eating vegetables", "zh": "停止吃蔬菜"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "'Try new restaurants or foods with your family. Learning about new foods and flavors... can be fun.'",
                        "zh": "“和家人尝试新餐馆或新食物。了解新的食物和风味……会很有趣。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Choose a country from the book and write about one traditional food eaten there, including what it is made of.",
                   "zh": "从书中选一个国家，写一种当地的传统食物，包括它是由什么做成的。"},
        "guidance": {
            "en": ["Name the country and the food (e.g., borscht in Russia, sushi in Japan).",
                   "Describe its main ingredients."],
            "zh": ["说出国家和食物（如俄罗斯的罗宋汤、日本的寿司）。",
                   "描述它的主要食材。"]
        }
    }
})

# 10. George Washington Carver
books.append({
    "slug": "george-washington-carver",
    "title": "George Washington Carver",
    "titleZh": "乔治·华盛顿·卡弗",
    "level": "R",
    "genre": "Biography",
    "mainSkill": "Key Ideas and Details",
    "questions": [
        {
            "q": {"en": "In what year was George Washington Carver born?",
                  "zh": "乔治·华盛顿·卡弗出生于哪一年？"},
            "options": [
                {"en": "1864", "zh": "1864年"},
                {"en": "1896", "zh": "1896年"},
                {"en": "1848", "zh": "1848年"},
                {"en": "1921", "zh": "1921年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'George was born in Missouri in 1864, during the Civil War.'",
                        "zh": "“乔治1864年生于密苏里州，正值内战期间。”"}
        },
        {
            "q": {"en": "In the glossary, what does 'segregated' mean?",
                  "zh": "在词汇表中，“segregated（隔离的）”是什么意思？"},
            "options": [
                {"en": "Kept apart based on group differences such as race", "zh": "基于种族等群体差异而被分开"},
                {"en": "Mixed together", "zh": "混合在一起"},
                {"en": "Very rich", "zh": "非常富有"},
                {"en": "Good at farming", "zh": "擅长农耕"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "The glossary defines segregated as 'kept apart based on group differences, such as race.'",
                        "zh": "词汇表将 segregated 定义为“基于种族等群体差异而被分开”。"}
        },
        {
            "q": {"en": "What crop had worn out the soil on Alabama farms?",
                  "zh": "是什么作物耗尽了阿拉巴马州农场的地力？"},
            "options": [
                {"en": "Cotton", "zh": "棉花"},
                {"en": "Peanuts", "zh": "花生"},
                {"en": "Wheat", "zh": "小麦"},
                {"en": "Corn", "zh": "玉米"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'Years of growing only cotton had worn out the soil.' Carver taught that 'too much cotton' was ruining the farms.",
                        "zh": "“连年只种棉花耗尽了地力。”卡弗认为“太多的棉花”正在毁掉农场。"}
        },
        {
            "q": {"en": "At which college did Carver become the first Black graduate and first Black professor?",
                  "zh": "卡弗在哪所学院成为第一位黑人毕业生和第一位黑人教授？"},
            "options": [
                {"en": "Iowa State Agricultural College", "zh": "爱荷华州立农学院"},
                {"en": "Simpson College", "zh": "辛普森学院"},
                {"en": "Yale Law School", "zh": "耶鲁法学院"},
                {"en": "Tuskegee Institute", "zh": "塔斯基吉学院"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "He moved to Iowa State Agricultural College and 'became the first black graduate there as well as the first black professor.'",
                        "zh": "他进入爱荷华州立农学院，“成为该校第一位黑人毕业生，也是第一位黑人教授”。"}
        },
        {
            "q": {"en": "Did Carver invent peanut butter? What does the book say?",
                  "zh": "卡弗发明了花生酱吗？书中是怎么说的？"},
            "options": [
                {"en": "Yes, he invented it", "zh": "是的，他发明的"},
                {"en": "No; he invented 300+ uses for peanuts but not peanut butter (the Aztecs ate it first)", "zh": "没有；他发明了300多种花生用途，但没发明花生酱（阿兹特克人最早食用）"},
                {"en": "He invented the peanut plant", "zh": "他发明了花生这种植物"},
                {"en": "He invented the jar", "zh": "他发明了装花生酱的罐子"}
            ],
            "answer": 1,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "'Contrary to popular belief, however, he did not create peanut butter. The Aztecs are known to have eaten a paste made from peanuts.'",
                        "zh": "“然而与普遍看法相反，他并没有发明花生酱。已知阿兹特克人曾食用花生制成的糊。”"}
        },
        {
            "q": {"en": "Why did Carver teach farmers to plant peanuts and sweet potatoes?",
                  "zh": "卡弗为什么教农民种花生和红薯？"},
            "options": [
                {"en": "To make the soil poor", "zh": "为了让土地更贫瘠"},
                {"en": "They put nitrogen back in the soil and were foods the farmers could eat", "zh": "它们把氮还给土壤，而且是农民能吃的食物"},
                {"en": "Because they were easy to sell only", "zh": "因为只容易卖钱"},
                {"en": "To feed the cattle", "zh": "为了喂养牛群"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "These crops 'put nitrogen, an important nutrient that the cotton crop used up, back in the soil' and 'were foods that farmers could eat.'",
                        "zh": "这些作物“把棉花消耗掉的重要养分氮重新还给土壤”，而且“是农民能吃的食物”。"}
        },
        {
            "q": {"en": "In what year did Carver speak before members of the U.S. Congress about peanuts?",
                  "zh": "卡弗是在哪一年到美国国会就花生问题发表演讲的？"},
            "options": [
                {"en": "1921", "zh": "1921年"},
                {"en": "1896", "zh": "1896年"},
                {"en": "1864", "zh": "1864年"},
                {"en": "1936", "zh": "1936年"}
            ],
            "answer": 0,
            "skill": "Key Ideas and Details",
            "explain": {"en": "'By 1921, people were listening to Carver's ideas. He was asked to speak before members of the U.S. Congress.'",
                        "zh": "“到1921年，人们开始倾听卡弗的想法。他受邀到美国国会发表演讲。”"}
        },
        {
            "q": {"en": "Why did Carver add 'Washington' to his name?",
                  "zh": "卡弗为什么在名字里加上“Washington（华盛顿）”？"},
            "options": [
                {"en": "There was another George Carver in town, so he added the initial W", "zh": "镇上有另一个乔治·卡弗，所以他加了个首字母W"},
                {"en": "He was related to the president", "zh": "他与总统有亲戚关系"},
                {"en": "A teacher gave it to him", "zh": "是一位老师给他的"},
                {"en": "He won it in a contest", "zh": "他在一场比赛中赢来的"}
            ],
            "answer": 0,
            "skill": "Craft and Structure",
            "explain": {"en": "'because there was another George Carver in town, he added the initial W... he said \"Washington.\"'",
                        "zh": "“因为镇上还有另一个乔治·卡弗，他加上了首字母W……他说那是‘Washington（华盛顿）’。”"}
        },
        {
            "q": {"en": "Which famous inventor offered Carver a high-paying job that he turned down?",
                  "zh": "哪位著名发明家曾向卡弗提供高薪工作，却被他拒绝？"},
            "options": [
                {"en": "Thomas Edison", "zh": "托马斯·爱迪生"},
                {"en": "Alexander Graham Bell", "zh": "亚历山大·格雷厄姆·贝尔"},
                {"en": "Henry Ford", "zh": "亨利·福特"},
                {"en": "Albert Einstein", "zh": "阿尔伯特·爱因斯坦"}
            ],
            "answer": 0,
            "skill": "Integration of Knowledge and Ideas",
            "explain": {"en": "'The inventor Thomas Edison offered him a high-paying job in his lab, but Carver didn't want it.'",
                        "zh": "“发明家托马斯·爱迪生给他实验室的高薪职位，但卡弗不想要。”"}
        },
        {
            "q": {"en": "What did Carver believe about ideas?",
                  "zh": "卡弗对“想法/点子”抱着怎样的信念？"},
            "options": [
                {"en": "Ideas should be sold for money", "zh": "想法应该卖钱"},
                {"en": "Ideas are free and should be freely given", "zh": "想法是自由的，应当免费分享"},
                {"en": "Ideas are worthless", "zh": "想法毫无价值"},
                {"en": "Only scientists have ideas", "zh": "只有科学家才有想法"}
            ],
            "answer": 1,
            "skill": "Author's Purpose and Perspective",
            "explain": {"en": "He 'believed that ideas were free, so they should be freely given.'",
                        "zh": "他“相信想法是自由的，所以应当免费分享给他人。”"}
        }
    ],
    "extended": {
        "prompt": {"en": "Write a short paragraph about how George Washington Carver helped poor farmers and why his ideas were 'free.'",
                   "zh": "写一小段话，说明乔治·华盛顿·卡弗如何帮助贫苦农民，以及为什么他的想法是“自由/免费”的。"},
        "guidance": {
            "en": ["Mention crop rotation and natural fertilizers.",
                   "Explain his belief that ideas should help people, not just make money."],
            "zh": ["提及作物轮作和天然肥料。",
                   "解释他“想法应助人而非只为赚钱”的信念。"]
        }
    }
})

# Write files
for b in books:
    path = os.path.join(OUT, b["slug"] + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
    print("wrote", path)
print("DONE", len(books))
