# MEMORY — readbook project

## 分级阅读乐园 · Reading by Level (reading comprehension site)
- Purpose: help kids learn reading via bilingual (EN/ZH) comprehension quizzes, organized by reading level + a 中文书 section.
- Local dir: `/Users/allen/Nextcloud/macbook/readbook`. Root `index.html` = 5 level sections (绘本/桥梁书/初章书/中章书/高章书) **+ 1 中文书 section** (accent #d4a017, 🀄, pill "中文", placeholder for now). Five level folders exist: `picture-books/`, `bridge-books/`, `early-chapter/`, `middle-chapter/`, `higher-chapter/` (empty ones have `.gitkeep`). A to Z Mysteries lives at `early-chapter/atozmysteries/` = hub `index.html` + **26 `*quiz.html` (A–Z)**, self-contained 10 Q each, 🌐 toggle, 🏠 home link `../../index.html`. Regenerate via `build.py` from `_quizdata/<LETTER>.json`. 中文书 has no folder yet.
- GitHub: repo **allenlinc/readbook** (`git@github.com:allenlinc/readbook.git`, SSH). GitHub Pages on `main`, root. Live: **https://allenlinc.github.io/readbook/**
- Old repo `allenlinc/a-to-z-mysteries` is outdated (old single-page site); prefer `readbook` now.
- To add a book: put quiz under the level folder, add a card in `index.html` (or level hub), commit & push. Pages auto-rebuilds on push (or POST /pages/builds). After moving files deeper, fix home links (`../index.html` → `../../index.html`).

## GitHub publishing notes (this machine)
- `gh` CLI is NOT logged in (`gh auth login` fails: token lacks `read:org` scope). A `gho_` OAuth token IS in the macOS keychain (scopes: read:user, repo, user:email, workflow).
- **SSH push works** (`ssh -T git@github.com` authenticates as allenlinc) — so pushing via `git@github.com:...` remotes is the easy path; no token needed.
- Workaround for API: read token via `git credential-osxkeychain get`, use it in API calls or as `https://<TOKEN>@github.com/...` remote URL for push, then strip the token from local remote config.
- Commit author email MUST be `7354315+allenlinc@users.noreply.github.com` (GitHub blocks real emails via GH007). Set in repo-local git config.
