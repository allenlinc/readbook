# -*- coding: utf-8 -*-
import json, os

OUT = r"D:\AI\readbook\picture-books\_quizdata"

# ---------------- A Golden Tragedy ----------------
a_golden_tragedy = {
  "slug": "a-golden-tragedy",
  "title": "A Golden Tragedy",
  "titleZh": "金色的悲剧",
  "level": "P",
  "genre": "Myth",
  "mainSkill": "Key Ideas and Details",
  "questions": [
    {
      "q": {"en":"Who was King Midas at the beginning of the story?",
            "zh":"故事开头，迈达斯国王是怎样的人？"},
      "options": [
        {"en":"A wealthy and kind king who loved his daughter Penelope","zh":"一位富有而善良的国王，深爱女儿佩内洛普"},
        {"en":"A poor farmer who owned many birds","zh":"一位养了许多鸟的穷苦农夫"},
        {"en":"A wise wizard who granted wishes","zh":"一位能实现愿望的睿智巫师"},
        {"en":"A talking parakeet in the palace","zh":"宫殿里一只会说话的鹦鹉"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The book states: King Midas had everything anyone could hope for, immense wealth, a peaceful kingdom, and a beautiful daughter he loved dearly.","zh":"书中写道：迈达斯国王拥有人们所期望的一切——巨大的财富、和平的王国，以及他深爱着的美丽女儿。"}
    },
    {
      "q": {"en":"What did King Midas ask the wizard to give him?",
            "zh":"迈达斯国王请求巫师赐予他什么？"},
      "options": [
        {"en":"The power to turn anything he touched into gold","zh":"把任何他触碰到的东西都变成金子的能力"},
        {"en":"A basket of golden eggs for his daughter","zh":"给女儿的一篮金蛋"},
        {"en":"A much longer life","zh":"更长的寿命"},
        {"en":"A bigger and taller palace","zh":"更大更高的宫殿"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Midas said: I would like the power to turn anything I touch into gold.","zh":"迈达斯说：「我希望拥有把任何我触碰到的东西都变成金子的能力。」"}
    },
    {
      "q": {"en":"A Golden Tragedy is best described as what kind of story?","zh":"《金色的悲剧》最能被描述成怎样的故事？"},
      "options": [
        {"en":"An ancient Greek myth retold by Robin King","zh":"由罗宾·金重述的古希腊神话"},
        {"en":"A news report about a modern king","zh":"关于一位现代国王的新闻报道"},
        {"en":"A science textbook chapter","zh":"一本科学课本章节"},
        {"en":"A recipe book for cooking","zh":"一本烹饪食谱书"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The title page reads: An ancient Greek myth retold by Robin King.","zh":"书名页写着：由罗宾·金重述的古希腊神话。"}
    },
    {
      "q": {"en":"Why does the story call Midas's wish a tragic mistake?",
            "zh":"为什么故事称迈达斯的愿望是一个「悲剧性的错误」？"},
      "options": [
        {"en":"Because when Penelope hugged him, she turned into a gold statue","zh":"因为佩内洛普拥抱他时，变成了金像"},
        {"en":"Because the wizard refused to grant it","zh":"因为巫师拒绝实现它"},
        {"en":"Because he lost all of his birds","zh":"因为他失去了所有的鸟"},
        {"en":"Because the kingdom became too crowded","zh":"因为王国变得过于拥挤"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"The book says a tragedy occurred when Penelope froze in her loving embrace, stiff as a statue, after hugging her golden father.","zh":"书中说，当佩内洛普拥抱变成金人的父亲后，她在拥抱中僵住，像雕像一样——一场悲剧发生了。"}
    },
    {
      "q": {"en":"What happened to King Midas on his way back to the palace?",
            "zh":"迈达斯国王在返回宫殿的路上发生了什么？"},
      "options": [
        {"en":"Rocks, flowers, and trees turned to gold and the kingdom grew stiff","zh":"岩石、花朵和树木变成了金子，王国变得僵硬"},
        {"en":"He met a friendly dragon","zh":"他遇到了一只友善的龙"},
        {"en":"He lost his way in the forest","zh":"他在森林里迷了路"},
        {"en":"It began to rain gold coins","zh":"开始下起金币雨"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The text says his path became littered with golden rocks and glistening flowers and trees with leaves of gold, and his kingdom turned stiff and still.","zh":"文中说，他的路上散落着金色的岩石，闪烁的花朵和金叶树木，而他的王国变得僵硬静止。"}
    },
    {
      "q": {"en":"What lesson does King Midas learn by the end of the story?",
            "zh":"在故事结尾，迈达斯国王明白了什么道理？"},
      "options": [
        {"en":"There is much more to life than glitter and gold","zh":"生命中比闪光与黄金更重要的东西还有很多"},
        {"en":"Gold is the only thing worth having","zh":"黄金是唯一值得拥有的东西"},
        {"en":"Wizards should never be trusted","zh":"永远不该信任巫师"},
        {"en":"Birds should lay golden eggs","zh":"鸟应该下金蛋"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The author concludes: He learned that there was much more to life than glitter and gold.","zh":"作者总结道：他明白了，生命中比闪光与黄金更重要的东西还有很多。"}
    },
    {
      "q": {"en":"How was the golden spell finally reversed?",
            "zh":"金子的魔咒最终是怎样被解除的？"},
      "options": [
        {"en":"The wizard took away ALL the gold, even what Midas had before","zh":"巫师取走了所有的金子，包括他之前拥有的"},
        {"en":"Midas simply wished it away","zh":"迈达斯只需许个愿就解除了"},
        {"en":"Penelope said a magic word","zh":"佩内洛普说了一句咒语"},
        {"en":"The birds pecked the gold away","zh":"鸟儿把金子啄掉了"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The wizard warned the only way was to take away ALL the gold and glitter, even that which Midas had before the touch overtook him.","zh":"巫师警告，唯一的办法是取走所有的金子与闪光，甚至连他获得点金术之前拥有的那些也要拿走。"}
    },
    {
      "q": {"en":"What happened to Midas after the spell was removed?",
            "zh":"魔咒解除后，迈达斯变成了什么样子？"},
      "options": [
        {"en":"His clothes became plain and his palace shrank to a humble house","zh":"他的衣服变得朴素，宫殿缩成简陋的房子"},
        {"en":"He became richer than ever","zh":"他变得比以往更富有"},
        {"en":"He turned into a golden statue","zh":"他变成了一座金像"},
        {"en":"He grew wings and flew away","zh":"他长出翅膀飞走了"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The book says his clothes became drab and common and his palace shrank into a humble house.","zh":"书中说，他的衣服变得单调普通，宫殿缩成一座简陋的房子。"}
    },
    {
      "q": {"en":"What did Midas gain even though he lost his wealth?",
            "zh":"虽然失去了财富，迈达斯得到了什么？"},
      "options": [
        {"en":"His daughter, something far more precious than gold","zh":"他的女儿，比黄金珍贵得多的东西"},
        {"en":"A larger kingdom","zh":"一个更大的王国"},
        {"en":"A flock of golden birds","zh":"一群金鸟"},
        {"en":"A magical sword","zh":"一把魔法剑"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"The text says he lost all that made him wealthy, but gained something far more precious, his daughter.","zh":"文中说，他失去了使他富有的一切，却得到了珍贵得多的东西——他的女儿。"}
    },
    {
      "q": {"en":"What does the title 'A Golden Tragedy' most likely refer to?",
            "zh":"标题《金色的悲剧》最可能指的是什么？"},
      "options": [
        {"en":"The golden touch that caused a sad ending","zh":"造成悲惨结局的点金术"},
        {"en":"A golden trophy at a race","zh":"比赛中的一座金质奖杯"},
        {"en":"A sunny beach in Rio","zh":"里约阳光明媚的海滩"},
        {"en":"A yellow school bus","zh":"一辆黄色的校车"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The title combines gold, from his wish, with tragedy, from losing his daughter to the golden touch.","zh":"标题把「金」（来自他的愿望）与「悲剧」（女儿因点金术而失去）结合在一起。"}
    }
  ],
  "extended": {
    "prompt": {"en":"Imagine you are King Midas after the spell is reversed. Write a short diary entry about what you learned and how you will treat your daughter Penelope from now on.",
               "zh":"想象你是法力被解除后的迈达斯国王。写一段简短的日记，讲述你学到了什么，以及今后你会怎样对待女儿佩内洛普。"},
    "guidance": {
      "en":["Describe one thing Midas lost and one thing he gained.","Explain the lesson about what is truly precious in life."],
      "zh":["描述迈达斯失去的一样东西和他得到的一样东西。","解释故事中关于什么才是真正珍贵之物的道理。"]
    }
  }
}

# ---------------- A Late Night Chat with a Parakeet ----------------
a_late_night_chat_with_a_parakeet = {
  "slug": "a-late-night-chat-with-a-parakeet",
  "title": "A Late Night Chat with a Parakeet",
  "titleZh": "深夜与鹦鹉的聊天",
  "level": "P",
  "genre": "Fiction",
  "mainSkill": "Key Ideas and Details",
  "questions": [
    {
      "q": {"en":"Who is the narrator of this story?",
            "zh":"这个故事的叙述者是谁？"},
      "options": [
        {"en":"Hattie MacGruder, a third-grade girl","zh":"哈蒂·麦克格劳德，一名三年级女生"},
        {"en":"A wise old wizard","zh":"一位睿智的老巫师"},
        {"en":"King Midas","zh":"迈达斯国王"},
        {"en":"The parakeet Fred","zh":"鹦鹉弗雷德"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The diary begins: My name is Hattie MacGruder. I am queen and absolute leader of my third grade class.","zh":"日记开头写道：我叫哈蒂·麦克格劳德。我是三年级班的女王和绝对领袖。"}
    },
    {
      "q": {"en":"What surprise did Hattie's mother give her?",
            "zh":"哈蒂的妈妈给了她什么惊喜？"},
      "options": [
        {"en":"A parakeet that had belonged to her great-aunt","zh":"一只曾经属于她姑祖母的鹦鹉"},
        {"en":"A new Britney Spears CD","zh":"一张新的布兰妮·斯皮尔斯唱片"},
        {"en":"A kitten","zh":"一只小猫"},
        {"en":"A trip to the movies","zh":"一次看电影的机会"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The surprise was a parakeet, her great-aunt's parakeet, given to her mother by her great-uncle.","zh":"惊喜是一只鹦鹉——她姑祖母的鹦鹉，由姑祖父送给了她的妈妈。"}
    },
    {
      "q": {"en":"How is this story mainly told?",
            "zh":"这个故事主要以什么形式讲述？"},
      "options": [
        {"en":"As entries from Hattie's diary","zh":"以哈蒂日记中的篇章形式"},
        {"en":"As a newspaper article","zh":"以一篇新闻报道形式"},
        {"en":"As a science report","zh":"以一份科学报告形式"},
        {"en":"As a recipe list","zh":"以一张食谱清单形式"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"Hattie says the proof is in my diary and lets the reader read it exactly as she wrote it.","zh":"哈蒂说证据就在她的日记里，并让读者按她写下的原样阅读。"}
    },
    {
      "q": {"en":"Why does Hattie call Sybil and Sarah liars?",
            "zh":"哈蒂为什么称西比尔和莎拉是「骗子」？"},
      "options": [
        {"en":"Because they said the parakeet never really talked","zh":"因为她们说那只鹦鹉根本没有真的说过话"},
        {"en":"Because they stole her diary","zh":"因为她们偷了她的日记"},
        {"en":"Because they ate all the chili cheese fries","zh":"因为她们吃光了辣味芝士薯条"},
        {"en":"Because they loved Britney Spears","zh":"因为她们喜欢布兰妮·斯皮尔斯"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"Hattie writes that Sybil and Sarah said there never was a talking parakeet and that parakeets don't talk.","zh":"哈蒂写道，西比尔和莎拉说从来没有会说话的鹦鹉，还说鹦鹉不会说话。"}
    },
    {
      "q": {"en":"What name did the parakeet say he preferred?",
            "zh":"鹦鹉说他自己更喜欢被叫做什么名字？"},
      "options": [
        {"en":"Fred, though his great-aunt called him Freddie","zh":"弗雷德，尽管姑祖母叫他弗雷迪"},
        {"en":"Hattie","zh":"哈蒂"},
        {"en":"Davey","zh":"戴维"},
        {"en":"Britney","zh":"布兰妮"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Fred said: my great-aunt called him Freddie, but he much preferred Fred.","zh":"弗雷德说：姑祖母叫他弗雷迪，但他更喜欢弗雷德。"}
    },
    {
      "q": {"en":"Why does Hattie keep a diary about the parakeet?",
            "zh":"哈蒂为什么要写关于鹦鹉的日记？"},
      "options": [
        {"en":"To prove the truth about the talking parakeet","zh":"为了证明会说话的鹦鹉确有其事"},
        {"en":"To practice her spelling","zh":"为了练习拼写"},
        {"en":"To write a school essay","zh":"为了写学校作文"},
        {"en":"To list her favorite songs","zh":"为了列出她最爱的歌曲"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"Hattie says My diary proves it! because others did not believe her.","zh":"哈蒂说「我的日记证明了这一切！」，因为别人都不相信她。"}
    },
    {
      "q": {"en":"What happened to Fred the next morning?",
            "zh":"第二天早上，弗雷德怎么了？"},
      "options": [
        {"en":"He was gone; the cage was empty","zh":"他不见了；笼子是空的"},
        {"en":"He learned to read","zh":"他学会了阅读"},
        {"en":"He turned into gold","zh":"他变成了金子"},
        {"en":"He ate the whole pillow","zh":"他把整只枕头吃了"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Hattie writes: When I woke up, he was gone! The cage was still there, but it was empty.","zh":"哈蒂写道：我醒来时，他不见了！笼子还在，但空了。"}
    },
    {
      "q": {"en":"What kind of story is 'A Late Night Chat with a Parakeet'?",
            "zh":"《深夜与鹦鹉的聊天》是一个怎样的故事？"},
      "options": [
        {"en":"A humorous fiction told through a diary","zh":"以日记形式讲述的幽默小说"},
        {"en":"A book of real science facts","zh":"一本真实的科学事实书"},
        {"en":"A history of Brazil","zh":"一部巴西历史"},
        {"en":"A myth about King Midas","zh":"关于迈达斯国王的神话"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The cover shows it is a Level P Leveled Book written by Stephen Cosgrove, a work of fiction.","zh":"封面显示这是斯蒂芬·科斯格罗夫所写的 P 级分级读物，属于虚构作品。"}
    },
    {
      "q": {"en":"According to Hattie, what did Fred the parakeet like to eat?",
            "zh":"据哈蒂说，鹦鹉弗雷德喜欢吃什么？"},
      "options": [
        {"en":"Jelly or chili cheese fries, not just seeds","zh":"果冻或辣味芝士薯条，而不只是种子"},
        {"en":"Only dry bird seeds","zh":"只有干鸟食"},
        {"en":"Fresh fish","zh":"新鲜的鱼"},
        {"en":"Green leaves","zh":"绿叶"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"Hattie says he would rather eat jelly or chili cheese fries and loves Britney Spears.","zh":"哈蒂说，它更想吃果冻或辣味芝士薯条，而且喜欢布兰妮·斯皮尔斯。"}
    },
    {
      "q": {"en":"How does the story end regarding Fred?",
            "zh":"关于弗雷德，故事是如何结尾的？"},
      "options": [
        {"en":"He may have flown south with the wild ducks","zh":"他可能已经和野鸭一起飞往南方"},
        {"en":"He became the class pet","zh":"他成了班级的宠物"},
        {"en":"He turned into a statue","zh":"他变成了一座雕像"},
        {"en":"He learned to drive a car","zh":"他学会了开车"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"Hattie guesses Fred talked about traveling with the ducks and probably headed south with them.","zh":"哈蒂猜测，弗雷德曾说起要和鸭子一起旅行，大概是跟着一群野鸭往南飞走了。"}
    }
  ],
  "extended": {
    "prompt": {"en":"Hattie believes her parakeet really talked. Write a few sentences telling whether you think Fred was real or imagined, and give one reason from the story.",
               "zh":"哈蒂相信她的鹦鹉真的说过话。写几句话，说明你认为弗雷德是真实的还是想象出来的，并从故事中给出一个理由。"},
    "guidance": {
      "en":["State your opinion clearly.","Use a detail from Hattie's diary to support it."],
      "zh":["清楚地表明你的看法。","用哈蒂日记中的一个细节来支持它。"]
    }
  }
}

# ---------------- A Nation on Wheels ----------------
a_nation_on_wheels = {
  "slug": "a-nation-on-wheels",
  "title": "A Nation on Wheels",
  "titleZh": "车轮上的国家",
  "level": "P",
  "genre": "Informational",
  "mainSkill": "Key Ideas and Details",
  "questions": [
    {
      "q": {"en":"About how many cars and trucks are in the United States?",
            "zh":"美国大约有多少辆小汽车和卡车？"},
      "options": [
        {"en":"Over 200 million","zh":"超过两亿辆"},
        {"en":"About 1 million","zh":"大约一百万辆"},
        {"en":"Exactly 50 thousand","zh":"正好五万辆"},
        {"en":"Fewer than 100","zh":"不到一百辆"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The book says there are over 200 million cars and trucks just in the United States.","zh":"书中说，仅美国就有超过两亿辆小汽车和卡车。"}
    },
    {
      "q": {"en":"What kind of engine worked well enough to power the first real cars?",
            "zh":"哪种发动机足够好，为最早真正的汽车提供动力？"},
      "options": [
        {"en":"Gasoline engines, developed in the late 1880s","zh":"19世纪80年代末开发的汽油发动机"},
        {"en":"Steam engines only","zh":"只有蒸汽发动机"},
        {"en":"Electric engines only","zh":"只有电动发动机"},
        {"en":"Wind-powered engines","zh":"风力发动机"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"In the late 1880s, people made engines that could run on gasoline, and today most cars use gas engines.","zh":"19世纪80年代末，人们制造出可用汽油驱动的发动机，如今大多数汽车使用汽油发动机。"}
    },
    {
      "q": {"en":"The word 'car' was first used in 1301 to describe a what?",
            "zh":"「car」一词在1301年首次被用来描述什么？"},
      "options": [
        {"en":"A Celtic war chariot","zh":"凯尔特人的战车"},
        {"en":"A gasoline automobile","zh":"汽油汽车"},
        {"en":"A bicycle","zh":"自行车"},
        {"en":"A train","zh":"火车"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"A Do You Know note says Car was first used in 1301 to describe a Celtic war chariot.","zh":"「你知道吗」小注说，car 在1301年首次被用来描述凯尔特人的战车。"}
    },
    {
      "q": {"en":"What did Henry Ford introduce in 1913 to build cars faster and cheaper?",
            "zh":"亨利·福特在1913年引入了什么，使汽车造得更快更便宜？"},
      "options": [
        {"en":"The assembly line","zh":"装配线"},
        {"en":"The gasoline engine","zh":"汽油发动机"},
        {"en":"The steering wheel","zh":"方向盘"},
        {"en":"The electronic computer","zh":"电子计算机"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"The book states: In 1913, he invented the assembly line, a faster and cheaper way to make a car.","zh":"书中说：1913年，他发明了装配线，一种更快更便宜的造车方式。"}
    },
    {
      "q": {"en":"Which three big companies have long made cars in the United States?",
            "zh":"哪三家大公司长期以来都在美国制造汽车？"},
      "options": [
        {"en":"General Motors, Chrysler, and Ford","zh":"通用汽车、克莱斯勒和福特"},
        {"en":"Toyota, Honda, and Nissan","zh":"丰田、本田和日产"},
        {"en":"BMW, Volvo, and Saab","zh":"宝马、沃尔沃和萨博"},
        {"en":"Apple, Google, and Microsoft","zh":"苹果、谷歌和微软"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Three big companies have been making cars in the United States for a long time: General Motors, Chrysler, and Ford.","zh":"长期以来，有三家大公司一直在美国制造汽车：通用汽车、克莱斯勒和福特。"}
    },
    {
      "q": {"en":"Why does the author mention exhaust and traffic jams?",
            "zh":"作者为什么提到尾气排放和交通堵塞？"},
      "options": [
        {"en":"To show that cars also cause serious problems","zh":"为了说明汽车也会造成严重问题"},
        {"en":"To praise how fast cars are","zh":"为了称赞汽车有多快"},
        {"en":"To sell more gasoline","zh":"为了多卖汽油"},
        {"en":"To describe a new car color","zh":"为了描述一种新的汽车颜色"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The section titled Problems Caused by the Automobile explains exhaust and traffic jams as downsides.","zh":"题为「汽车造成的问题」的章节，把尾气与交通堵塞作为汽车的负面后果来说明。"}
    },
    {
      "q": {"en":"In 2007, which company sold more cars and trucks than any other in the world?",
            "zh":"2007年，哪家公司卖出的汽车和卡车比世界上任何一家都多？"},
      "options": [
        {"en":"Toyota, a Japanese company","zh":"日本公司丰田"},
        {"en":"Ford, an American company","zh":"美国公司福特"},
        {"en":"Volkswagen of Germany","zh":"德国大众"},
        {"en":"General Motors","zh":"通用汽车"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"In 2007, Toyota, the first foreign company to do so, sold more cars and trucks than any other company in the world.","zh":"2007年，丰田作为第一家做到这一点的外国公司，卖出的汽车和卡车超过了世界上任何一家公司。"}
    },
    {
      "q": {"en":"What is a hybrid car?",
            "zh":"什么是混合动力汽车？"},
      "options": [
        {"en":"A car that uses both a gas engine and an electric motor","zh":"同时使用汽油发动机和电动机的汽车"},
        {"en":"A car made only of wood","zh":"只用木头制造的车"},
        {"en":"A car that flies","zh":"会飞的车"},
        {"en":"A car pulled by horses","zh":"由马匹拉的车"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The book says a hybrid uses both a gas engine and an electric motor and uses less gas.","zh":"书中说，混合动力车同时使用汽油发动机和电动机，耗油更少。"}
    },
    {
      "q": {"en":"Where did Henry Ford start the Ford Motor Company in 1903?",
            "zh":"1903年，亨利·福特在哪里创办了福特汽车公司？"},
      "options": [
        {"en":"Detroit, Michigan","zh":"密歇根州的底特律"},
        {"en":"New York City","zh":"纽约市"},
        {"en":"Los Angeles, California","zh":"加利福尼亚州的洛杉矶"},
        {"en":"London, England","zh":"英国伦敦"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"In 1903, Henry Ford started the Ford Motor Company in Detroit, Michigan, which became the center of car making.","zh":"1903年，亨利·福特在密歇根州的底特律创办了福特汽车公司，那里很快成为汽车制造中心。"}
    },
    {
      "q": {"en":"What is the author's main purpose in writing this book?",
            "zh":"作者写这本书的主要目的是什么？"},
      "options": [
        {"en":"To inform readers about how cars shaped America","zh":"向读者介绍汽车如何塑造了美国"},
        {"en":"To teach readers how to drive","zh":"教读者如何开车"},
        {"en":"To sell a specific car brand","zh":"推销某个特定汽车品牌"},
        {"en":"To tell a fairy tale","zh":"讲述一个童话故事"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"As an informational leveled book, its aim is to teach facts about cars, their history, and their impact.","zh":"作为一本科普分级读物，它的目的是讲授有关汽车、其历史及其影响的事实。"}
    }
  ],
  "extended": {
    "prompt": {"en":"The book says we are a nation moving on wheels. Write a short paragraph about one way cars help people and one problem they can cause.",
               "zh":"书中说，我们是一个在车轮上移动的国家。写一段简短的文字，说明汽车帮助人们的一种方式，以及它们可能造成的一个问题。"},
               "guidance": {
      "en":["Name one benefit of cars from the book.","Name one problem, such as exhaust or traffic jams."],
      "zh":["从书中举出汽车的一个好处。","举出一个问题，例如尾气或交通堵塞。"]
    }
  }
}

# ---------------- A Trip to Rio ----------------
a_trip_to_rio = {
  "slug": "a-trip-to-rio",
  "title": "A Trip to Rio",
  "titleZh": "里约之旅",
  "level": "P",
  "genre": "Fiction",
  "mainSkill": "Key Ideas and Details",
  "questions": [
    {
      "q": {"en":"Where does Julia travel in this story?",
            "zh":"在这个故事里，朱莉娅去了哪里旅行？"},
      "options": [
        {"en":"Rio de Janeiro, Brazil","zh":"巴西的里约热内卢"},
        {"en":"New York City, USA","zh":"美国纽约市"},
        {"en":"London, England","zh":"英国伦敦"},
        {"en":"Tokyo, Japan","zh":"日本东京"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The book is titled A Trip to Rio and Julia visits Rio de Janeiro, Brazil, for the Olympics.","zh":"这本书名为《里约之旅》，朱莉娅为了奥运会前往巴西的里约热内卢。"}
    },
    {
      "q": {"en":"Why did Julia feel nervous at the Olympic opening ceremonies?",
            "zh":"为什么朱莉娅在奥运会开幕式上感到紧张？"},
      "options": [
        {"en":"Crowds, many languages, and fast Portuguese made her feel alone","zh":"拥挤的人群、多种语言和快速的葡萄牙语让她感到孤单"},
        {"en":"She was afraid of the beach","zh":"她害怕海滩"},
        {"en":"She lost her suitcase","zh":"她丢失了行李箱"},
        {"en":"She could not find her cat","zh":"她找不到自己的猫"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"She heard different languages and her parents spoke Portuguese rapidly; she felt nervous and alone.","zh":"她听到不同的语言，父母飞快地说着葡萄牙语，她感到紧张而孤单。"}
    },
    {
      "q": {"en":"What kind of book is 'A Trip to Rio'?",
            "zh":"《里约之旅》是一本怎样的书？"},
      "options": [
        {"en":"A fiction story about a girl visiting family during the Olympics","zh":"一个关于女孩在奥运会期间探访家人的虚构故事"},
        {"en":"A math textbook","zh":"一本数学课本"},
        {"en":"A book about car engines","zh":"一本关于汽车发动机的书"},
        {"en":"A Greek myth","zh":"一个希腊神话"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"It is a Level P Leveled Book by Katherine Follett, a realistic fiction narrative.","zh":"它是凯瑟琳·福莱特所写的 P 级分级读物，属于现实类虚构叙事。"}
    },
    {
      "q": {"en":"How does Julia's attitude change during the trip?",
            "zh":"在旅行中，朱莉娅的态度发生了怎样的变化？"},
      "options": [
        {"en":"From nervous and lonely to excited and happy","zh":"从紧张孤单变得兴奋开心"},
        {"en":"From happy to angry","zh":"从开心变得生气"},
        {"en":"From sleepy to hungry","zh":"从困倦变得饥饿"},
        {"en":"From brave to scared of birds","zh":"从勇敢变得怕鸟"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"She starts wanting to go home with a headache, but later cheers at a football game and never wants to forget it.","zh":"她起初头痛想回家，但后来在足球赛中欢呼，再也不想忘记那一刻。"}
    },
    {
      "q": {"en":"What is feijoada?",
            "zh":"什么是 feijoada（巴西炖菜）？"},
      "options": [
        {"en":"A traditional bean stew with pork and spicy sausages, Brazil's national dish","zh":"一种用猪肉和辣香肠做的传统豆炖菜，是巴西的国菜"},
        {"en":"A kind of sweet mango","zh":"一种甜芒果"},
        {"en":"A type of dance","zh":"一种舞蹈"},
        {"en":"A soccer team","zh":"一支足球队"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The book says feijoada is a traditional bean stew with pork and spicy sausages, the national dish of Brazil.","zh":"书中说，feijoada 是一种用猪肉和辣香肠做的传统豆炖菜，是巴西的国菜。"}
    },
    {
      "q": {"en":"Why does the author describe the golden beach and Sugarloaf Mountain?",
            "zh":"作者为什么要描写金色的海滩和面包山？"},
      "options": [
        {"en":"To show Rio's wild beauty and change how Julia sees the city","zh":"为了展现里约野性的美，并改变朱莉娅对这座城市的看法"},
        {"en":"To teach a math lesson","zh":"为了上一堂数学课"},
        {"en":"To list car brands","zh":"为了列举汽车品牌"},
        {"en":"To explain how to cook","zh":"为了讲解如何烹饪"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The description helps Julia realize the city can look wild and beautiful, lifting her headache.","zh":"这段描写让朱莉娅意识到这座城市可以如此野性而美丽，令她的头痛消失。"}
    },
    {
      "q": {"en":"What did Grandpa teach Julia when she visited at age five?",
            "zh":"朱莉娅五岁来访时，外公教了她什么？"},
      "options": [
        {"en":"To samba by standing on his feet","zh":"让他踩在自己的脚上，教她跳桑巴"},
        {"en":"To swim in the ocean","zh":"在海里游泳"},
        {"en":"To speak English","zh":"说英语"},
        {"en":"To drive a cable car","zh":"开缆车"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"Grandpa taught her to samba by letting her stand on his feet, and they laughed and laughed.","zh":"外公让她踩在自己的脚上教她跳桑巴，两人笑个不停。"}
    },
    {
      "q": {"en":"What does the chant 'Eu sou brasileiro!' mean?",
            "zh":"口号「Eu sou brasileiro!」是什么意思？"},
      "options": [
        {"en":"I am Brazilian!","zh":"我是巴西人！"},
        {"en":"Go Brazil!","zh":"加油，巴西！"},
        {"en":"Thank you!","zh":"谢谢！"},
        {"en":"Goodbye!","zh":"再见！"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The book translates the chant: Eu sou brasileiro! means I am Brazilian!","zh":"书中把这句口号翻译为：Eu sou brasileiro! 意思是「我是巴西人！」"}
    },
    {
      "q": {"en":"How did Julia and Gabriela go up Sugarloaf Mountain?",
            "zh":"朱莉娅和加布里埃拉是怎样登上面包山的？"},
      "options": [
        {"en":"They rode a cable car high above the city","zh":"他们乘坐高悬于城市上空的缆车"},
        {"en":"They swam there","zh":"他们游过去的"},
        {"en":"They rode elephants","zh":"他们骑大象"},
        {"en":"They walked up the stairs","zh":"他们走楼梯上去"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"They rode a cable car that hung high above the city to go up Sugarloaf Mountain.","zh":"他们乘坐高悬于城市上空的缆车登上面包山。"}
    },
    {
      "q": {"en":"What is the main message of Julia's trip?",
            "zh":"朱莉娅这趟旅行主要传达了什么？"},
      "options": [
        {"en":"New experiences can change how we feel about a place","zh":"新的经历能改变我们对一个地方的感受"},
        {"en":"Never leave home","zh":"永远不要离开家"},
        {"en":"Cars are the best way to travel","zh":"汽车是最好的旅行方式"},
        {"en":"Always avoid crowds","zh":"永远避开人群"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"Julia moves from dreading Rio to loving it, showing how new experiences change feelings.","zh":"朱莉娅从害怕里约变成爱上它，展现出新的经历如何改变人的感受。"}
    }
  ],
  "extended": {
    "prompt": {"en":"Pretend you are Julia writing a postcard to your teacher from Rio. Tell about one thing you saw and one thing you did there.",
               "zh":"假设你是朱莉娅，从里约给老师写一张明信片。讲述你在那里看到的一件事和你做的一件事。"},
    "guidance": {
      "en":["Mention a real place from the book, like the beach or Sugarloaf.","Describe an activity such as the football game or the cable car."],
      "zh":["提到书中一个真实的地点，例如海滩或面包山。","描述一项活动，例如足球赛或缆车。"]
    }
  }
}

# ---------------- April Fools' Day ----------------
april_fools_day = {
  "slug": "april-fools-day",
  "title": "April Fools' Day",
  "titleZh": "愚人节",
  "level": "P",
  "genre": "Informational",
  "mainSkill": "Key Ideas and Details",
  "questions": [
    {
      "q": {"en":"When is April Fools' Day celebrated?",
            "zh":"愚人节是在什么时候庆祝的？"},
      "options": [
        {"en":"On or around the first day of April","zh":"在四月一日或前后"},
        {"en":"On December 25","zh":"在十二月二十五日"},
        {"en":"On the first day of January","zh":"在一月一日"},
        {"en":"On Halloween","zh":"在万圣节"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The book says April Fools' Day is celebrated on or around the first day of April every year.","zh":"书中说，愚人节每年在四月一日或前后庆祝。"}
    },
    {
      "q": {"en":"Which of these is a popular April Fools' prank from the book?",
            "zh":"以下哪一个是书中提到的常见愚人节恶作剧？"},
      "options": [
        {"en":"Swapping the sugar for salt","zh":"把糖换成盐"},
        {"en":"Painting the house red","zh":"把房子漆成红色"},
        {"en":"Planting a tree","zh":"种一棵树"},
        {"en":"Fixing a car","zh":"修理汽车"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Popular pranks include putting grease on a doorknob or swapping the sugar for salt.","zh":"常见的恶作剧包括在门把手上涂油，或把糖换成盐。"}
    },
    {
      "q": {"en":"In France, April 1 is often known as what?",
            "zh":"在法国，四月一日通常被称为什么？"},
      "options": [
        {"en":"April Fish","zh":"四月鱼（April Fish）"},
        {"en":"Lie Day","zh":"谎言日"},
        {"en":"The Spaghetti Day","zh":"意大利面日"},
        {"en":"Washing the Lions","zh":"洗狮子日"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"In France, April 1 is often known as April Fish, and a paper fish is taped to the victim's back.","zh":"在法国，四月一日常被称为「四月鱼」，人们会把纸鱼贴在被捉弄者的背上。"}
    },
    {
      "q": {"en":"What is Sizdah Bedar, and why is it special?",
            "zh":"什么是 Sizdah Bedar，它有什么特别之处？"},
      "options": [
        {"en":"An Iranian celebration around April 1, practiced since 536 BC, maybe the oldest joke day","zh":"伊朗在四月一日前后的庆祝活动，自公元前536年延续至今，可能是最古老的玩笑日"},
        {"en":"A French fish festival","zh":"一个法国的鱼节"},
        {"en":"A Brazilian dance","zh":"一种巴西舞蹈"},
        {"en":"An American sports day","zh":"一个美国的运动日"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"Sizdah Bedar is the thirteenth day of the Iranian new year, around April 1, practiced since 536 BC and possibly the oldest joke day.","zh":"Sizdah Bedar 是伊朗新年的第十三天，约在四月一日前后，自公元前536年延续，可能是最古老的玩笑日。"}
    },
    {
      "q": {"en":"What fake event was staged at the Tower of London in 1857?",
            "zh":"1857年，伦敦塔上演了什么假事件？"},
      "options": [
        {"en":"Washing the Lions","zh":"「清洗狮子」"},
        {"en":"A spaghetti harvest","zh":"意大利面丰收"},
        {"en":"A left-handed burger sale","zh":"左撇子汉堡售卖"},
        {"en":"A spaceship landing","zh":"外星飞船降落"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Washing the Lions was a fake event staged at the Tower of London in England, with no actual lions present.","zh":"「清洗狮子」是英国伦敦塔上演的一场假事件，现场并没有真正的狮子。"}
    },
    {
      "q": {"en":"Why does the author include 'Tips to Avoid Being the April Fool!'?",
            "zh":"作者为什么加入「避免成为愚人的小贴士」？"},
      "options": [
        {"en":"To help readers notice and avoid tricks","zh":"为了帮助读者察觉并避开恶作剧"},
        {"en":"To teach how to cook fish","zh":"为了教人烹饪鱼"},
        {"en":"To sell newspapers","zh":"为了卖报纸"},
        {"en":"To describe car parts","zh":"为了描述汽车零件"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The tips warn readers to read carefully and be on guard against fake stories.","zh":"这些提示提醒读者仔细阅读并保持警惕，以防被假消息欺骗。"}
    },
    {
      "q": {"en":"In 1996, which company joked that it bought the Liberty Bell?",
            "zh":"1996年，哪家公司开玩笑说它买下了自由钟？"},
      "options": [
        {"en":"Taco Bell, calling it the Taco Liberty Bell","zh":"塔可钟，称之为「塔可自由钟」"},
        {"en":"Burger King","zh":"汉堡王"},
        {"en":"Google","zh":"谷歌"},
        {"en":"BBC TV","zh":"英国广播公司电视台"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"In 1996, Taco Bell announced it had bought the Liberty Bell and would call it the Taco Liberty Bell.","zh":"1996年，塔可钟宣布买下了自由钟，并要把它称为「塔可自由钟」。"}
    },
    {
      "q": {"en":"How is this book mainly organized?",
            "zh":"这本书主要以什么方式组织内容？"},
      "options": [
        {"en":"As informational text with sections about the world","zh":"以介绍世界各地情况的说明性章节组织"},
        {"en":"As a single long poem","zh":"作为一首长篇诗歌"},
        {"en":"As a cookbook","zh":"作为一本烹饪书"},
        {"en":"As a car manual","zh":"作为一本汽车手册"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The table of contents lists Pranking Fun, Around the World, Famous Foolery, and more informational sections.","zh":"目录列出了「恶作剧乐趣」「世界各地」「著名的愚弄」等多个说明性章节。"}
    },
    {
      "q": {"en":"In Scotland, how long can April Fools' fun last?",
            "zh":"在苏格兰，愚人节的乐趣可以持续多久？"},
      "options": [
        {"en":"Two days","zh":"两天"},
        {"en":"One minute","zh":"一分钟"},
        {"en":"A whole week","zh":"整整一周"},
        {"en":"Only one hour","zh":"只有一个小时"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"In Scotland, April Fools' can go on for two days, with foolish errands on April 1 and more jokes the next day.","zh":"在苏格兰，愚人节可以持续两天：四月一日让人去做傻事，第二天再来更多玩笑。"}
    },
    {
      "q": {"en":"What rule does the author say April Fools' jokes should follow?",
            "zh":"作者说愚人节的玩笑应该遵守什么原则？"},
      "options": [
        {"en":"Be fun but harmless, and not mean","zh":"有趣但无害，不能刻薄"},
        {"en":"Scare as many people as possible","zh":"尽可能吓唬更多人"},
        {"en":"Always cost a lot of money","zh":"一定要花很多钱"},
        {"en":"Only happen at night","zh":"只在夜间发生"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The conclusion says the best pranks are fun but harmless, and jokes are supposed to be fun, not mean.","zh":"结语说，最好的恶作剧有趣但无害，玩笑本应好玩，而不是刻薄。"}
    }
  ],
  "extended": {
    "prompt": {"en":"The book says the best April Fools' pranks are fun but harmless. Write about a safe joke you would play on a friend, and explain why it is harmless.",
               "zh":"书中说，最好的愚人节恶作剧要有趣但无害。写一个有关于你对朋友会开的、安全的玩笑，并解释它为什么无害。"},
    "guidance": {
      "en":["Describe the joke clearly.","Explain why it would not hurt anyone."],
      "zh":["清楚地描述这个玩笑。","解释它为什么不会伤害任何人。"]
    }
  }
}

# ---------------- Art Around Us ----------------
art_around_us = {
  "slug": "art-around-us",
  "title": "Art Around Us",
  "titleZh": "我们身边的艺术",
  "level": "P",
  "genre": "Informational",
  "mainSkill": "Key Ideas and Details",
  "questions": [
    {
      "q": {"en":"What are murals?",
            "zh":"什么是壁画（murals）？"},
      "options": [
        {"en":"Large paintings painted onto a wall or the side of a building","zh":"画在墙面上或建筑侧面的大型绘画"},
        {"en":"Small paintings on paper","zh":"画在纸上的小画"},
        {"en":"Songs sung in a choir","zh":"合唱团演唱的歌曲"},
        {"en":"A kind of car","zh":"一种汽车"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The book says murals are large paintings painted onto a wall or the side of a building.","zh":"书中说，壁画是画在墙面或建筑侧面的大型绘画。"}
    },
    {
      "q": {"en":"How do potters shape wet clay?",
            "zh":"陶艺师如何塑造湿润的黏土？"},
      "options": [
        {"en":"On a pottery wheel that spins very fast","zh":"在快速旋转的陶轮上"},
        {"en":"By freezing it","zh":"把它冻起来"},
        {"en":"By blowing air through a tube","zh":"用管子吹气"},
        {"en":"By weaving fabric","zh":"通过编织布料"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"Potters put a lump of wet clay on a pottery wheel that spins very fast and shape it with their hands.","zh":"陶艺师把一团湿黏土放在快速旋转的陶轮上，用手塑形。"}
    },
    {
      "q": {"en":"In sculpture, what does the word 'cast' mean?",
            "zh":"在雕塑中，「cast」这个词是什么意思？"},
      "options": [
        {"en":"To pour hot metal into a mold","zh":"把熔融的金属倒入模具"},
        {"en":"To paint a picture","zh":"画一幅画"},
        {"en":"To weave yarn","zh":"编织毛线"},
        {"en":"To blow glass","zh":"吹制玻璃"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"The glossary defines cast as to pour hot metal into a mold.","zh":"词汇表把 cast 定义为把熔融的金属倒入模具。"}
    },
    {
      "q": {"en":"How do glassblowers make a glass bubble?",
            "zh":"玻璃吹制师如何制造出玻璃泡？"},
      "options": [
        {"en":"By blowing air through a long, hollow tube called a blowpipe","zh":"通过一根叫吹管的空心长管吹气"},
        {"en":"By hammering cold glass","zh":"敲打冷玻璃"},
        {"en":"By weaving threads","zh":"编织线"},
        {"en":"By baking clay","zh":"烧制黏土"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"Glassblowers scoop hot glass on a blowpipe and blow air through the tube to make a glass bubble.","zh":"玻璃吹制师用吹管舀起热玻璃，并通过管子吹气，制造出玻璃泡。"}
    },
    {
      "q": {"en":"What is an installation in art?",
            "zh":"艺术中的「装置（installation）」是什么？"},
      "options": [
        {"en":"Entire rooms or buildings made into works of art","zh":"把整个房间或建筑变成艺术作品"},
        {"en":"A small painting","zh":"一幅小画"},
        {"en":"A type of clay","zh":"一种黏土"},
        {"en":"A kind of bird","zh":"一种鸟"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The glossary says installations are entire rooms or buildings made into art.","zh":"词汇表说，装置是把整个房间或建筑变成的艺术。"}
    },
    {
      "q": {"en":"Why does the author repeat 'Art is all around us'?",
            "zh":"作者为什么反复说「艺术就在我们身边」？"},
      "options": [
        {"en":"To encourage readers to notice art everywhere","zh":"为了鼓励读者留意处处皆有的艺术"},
        {"en":"To sell more paint","zh":"为了卖出更多颜料"},
        {"en":"To teach math","zh":"为了教数学"},
        {"en":"To describe a car","zh":"为了描述一辆汽车"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The author wants readers to look and find art all around them, in museums, parks, and daily life.","zh":"作者希望读者去观察并在身边、博物馆、公园和日常生活中发现艺术。"}
    },
    {
      "q": {"en":"What do fiber artists use to make their art?",
            "zh":"纤维艺术家使用什么来创作？"},
      "options": [
        {"en":"Thread, yarns, and fabric pieces, often on a loom","zh":"线、纱线和布片，常用织布机编织"},
        {"en":"Only metal and stone","zh":"只用金属和石头"},
        {"en":"Only computers","zh":"只用电脑"},
        {"en":"Only water","zh":"只有水"}
      ],
      "answer": 0,
      "skill": "Integration of Knowledge and Ideas",
      "explain": {"en":"Fiber artists use thread, yarns, and fabric pieces; weavers loop yarns on a loom to make designs.","zh":"纤维艺术家使用线、纱线和布片；织工在织布机上环绕纱线，织出图案。"}
    },
    {
      "q": {"en":"What is found object art made from?",
            "zh":"「现成物艺术（found object art）」是用什么做的？"},
      "options": [
        {"en":"Junk, car parts, old toys, wire, and other scrap materials","zh":"垃圾、汽车零件、旧玩具、铁丝和其他废料"},
        {"en":"Fresh fruit","zh":"新鲜水果"},
        {"en":"Pure gold","zh":"纯金"},
        {"en":"Live animals","zh":"活体动物"}
      ],
      "answer": 0,
      "skill": "Craft and Structure",
      "explain": {"en":"Some artists make found object art out of junk, car parts, old toys, wire, and other scrap materials.","zh":"一些艺术家用垃圾、汽车零件、旧玩具、铁丝和其他废料创作现成物艺术。"}
    },
    {
      "q": {"en":"Where is some of the oldest art found?",
            "zh":"一些最古老的艺术是在哪里发现的？"},
      "options": [
        {"en":"Painted in caves or scratched into rocks","zh":"画在洞穴中或刻在岩石上"},
        {"en":"Printed in newspapers","zh":"印在报纸上"},
        {"en":"Stored on computers","zh":"储存在电脑里"},
        {"en":"Floating in the ocean","zh":"漂浮在海洋里"}
      ],
      "answer": 0,
      "skill": "Key Ideas and Details",
      "explain": {"en":"The oldest art was painted in caves or scratched into rocks, telling stories of long ago.","zh":"最古老的艺术画在洞穴中或刻在岩石上，讲述久远的往事。"}
    },
    {
      "q": {"en":"What is the author's main message about art?",
            "zh":"作者关于艺术的主要观点是什么？"},
      "options": [
        {"en":"Art can be fun and is everywhere around you","zh":"艺术可以很有趣，而且就在你身边无处不在"},
        {"en":"Art is only in museums","zh":"艺术只存在于博物馆"},
        {"en":"Art must be expensive","zh":"艺术必须很昂贵"},
        {"en":"Art is only for experts","zh":"艺术只属于专家"}
      ],
      "answer": 0,
      "skill": "Author's Purpose and Perspective",
      "explain": {"en":"The book ends: Art doesn't have to be serious or hard; look, and you will find art all around you.","zh":"书的结尾说：艺术不必严肃或困难；只要你去观察，就会发现艺术无处不在。"}
    }
  ],
  "extended": {
    "prompt": {"en":"The book says you can make your own art with chalk, clay, or shells. Describe one piece of art you could make from things around you.",
               "zh":"书中说，你可以用粉笔、黏土或贝壳创作自己的艺术。描述一件你可以用身边材料创作的艺术品。"},
    "guidance": {
      "en":["Name the materials you would use.","Describe what your art would look like."],
      "zh":["说出你会用到的材料。","描述你的艺术作品会是什么样子。"]
    }
  }
}

quizzes = [
  a_golden_tragedy,
  a_late_night_chat_with_a_parakeet,
  a_nation_on_wheels,
  a_trip_to_rio,
  april_fools_day,
  art_around_us,
]

for q in quizzes:
    path = os.path.join(OUT, q["slug"] + ".json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(q, f, ensure_ascii=False, indent=2)
    # validate
    with open(path, encoding="utf-8") as f:
        json.load(f)
    print("OK", q["slug"])
print("ALL DONE")
