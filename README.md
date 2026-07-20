# 英语分级阅读乐园 · Reading by Level

A free, kid-friendly static website to help children learn English by reading books
organized by reading level, then taking bilingual (English / 中文) comprehension quizzes.

🌐 Live site: **https://allenlinc.github.io/readbook/**

## Reading levels (分类)
Books are grouped into five levels — pick the right one for the child:

| Level | 分类 | English | Status |
|------|------|---------|--------|
| 1 | 绘本 | Picture Books | 🚧 reserved |
| 2 | 桥梁书 | Bridge Books | 🚧 reserved |
| 3 | 初章书 | Early Chapter Books | ✅ **A to Z Mysteries** (by Ron Roy) |
| 4 | 中章书 | Middle Chapter Books | 🚧 reserved |
| 5 | 高章书 | Higher Chapter Books | 🚧 reserved |

Other levels are placeholders for now and will be filled in over time.

## What's inside
- `index.html` — landing page with the five reading-level sections.
- `atozmysteries/index.html` — the **A to Z Mysteries** book hub (under 初章书), listing 6 quizzes.
- `atozmysteries/*-quiz.html` — one self-contained quiz per book (10 questions each).
  - Tap **🌐 中文** to switch the whole quiz between English and Chinese.
  - Tap **Check My Answers** to see the score plus an English + 中文 explanation for every question.
  - Tap **🏠** to go back to the home page.

## How kids use it
1. Choose a reading level, then a book.
2. Read the book with a grown-up.
3. Open a book and answer the 10 questions.
4. Check answers to read the bilingual explanation, then Try Again!

## Add a new book
1. Put the quiz file under the matching level folder (e.g. `atozmysteries/<slug>-quiz.html`).
2. Add a matching `<article class="book">` card — either on the level's hub page or in `index.html`.
3. Commit and push — GitHub Pages updates automatically.

## Deploy (GitHub Pages)
This is a plain static site hosted on GitHub Pages from the `main` branch, root path.
```bash
git add -A
git commit -m "Add a new book"
git push -u origin main
```
Repo: `git@github.com:allenlinc/readbook.git`. Pages is enabled in repo Settings → Pages
(source: `main` branch, `/` root).

Books © their respective authors / publishers. This project is for educational use only.
