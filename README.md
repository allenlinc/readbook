# A to Z Mysteries · 绘本阅读理解 (Reading Comprehension)

A free, kid-friendly static website to help children learn English by reading the
**A to Z Mysteries** books (by Ron Roy) and taking bilingual (English / 中文) comprehension quizzes.

🌐 Live site: **https://allenlinc.github.io/a-to-z-mysteries/**

## What's inside
- `index.html` — a colorful landing page that lists every book as a card.
- `atozmysteries/*-quiz.html` — one self-contained quiz per book (10 questions each).
  - Tap **🌐 中文** to switch the whole quiz between English and Chinese.
  - Tap **Check My Answers** to see the score plus an English + 中文 explanation for every question.
  - Tap **🏠** to go back to the home page.

## How kids use it
1. Read the book with a grown-up.
2. Open a book card and answer the 10 questions.
3. Check answers to read the bilingual explanation.
4. Try Again and beat the score!

## Add a new book
1. Create `atozmysteries/<book-slug>-quiz.html` following the same self-contained format
   (bilingual `quiz` array + scoring script).
2. Add a matching `<article class="book">` card to `index.html` linking to the new file.
3. Commit and push — GitHub Pages updates automatically.

## Deploy (GitHub Pages)
This is a plain static site. To publish:
```bash
git init
git add -A
git commit -m "Add A to Z Mysteries reading comprehension site"
gh repo create <repo-name> --public --source=. --remote=origin
git push -u origin main
# Then enable Pages in repo Settings → Pages → source: main branch, / (root)
```

Books © Ron Roy / Random House. This project is for educational use only.
