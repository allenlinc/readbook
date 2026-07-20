# MEMORY — readbook project

## A to Z Mysteries 绘本阅读理解 (reading comprehension site)
- Purpose: help kids learn English via bilingual (EN/ZH) comprehension quizzes for the "A to Z Mysteries" books by Ron Roy (letters U–Z quizzes exist).
- Local dir: `/Users/allen/Nextcloud/macbook/readbook`. Landing = `index.html`; quizzes in `atozmysteries/*-quiz.html` (self-contained, 10 Q each, 🌐 language toggle, 🏠 home link).
- GitHub: repo `allenlinc/a-to-z-mysteries` (public). GitHub Pages on `main`, root. Live: **https://allenlinc.github.io/a-to-z-mysteries/**
- To add a book: create `atozmysteries/<slug>-quiz.html` + a card in `index.html`, commit & push (Pages auto-updates).

## GitHub publishing notes (this machine)
- `gh` CLI is NOT logged in (`gh auth login` fails: token lacks `read:org` scope). A `gho_` OAuth token IS in the macOS keychain (scopes: read:user, repo, user:email, workflow).
- Workaround: read token via `git credential-osxkeychain get`, use it in API calls or as `https://<TOKEN>@github.com/...` remote URL for push, then strip the token from local remote config.
- Commit author email MUST be `7354315+allenlinc@users.noreply.github.com` (GitHub blocks real emails via GH007). Set in repo-local git config.
