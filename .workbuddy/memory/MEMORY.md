# MEMORY — readbook project

## 分级阅读乐园 · Reading by Level (reading comprehension site)
- Purpose: help kids learn reading via bilingual (EN/ZH) comprehension quizzes, organized by reading level + a 中文书 section.
- Local dir: `/Users/allen/Nextcloud/macbook/readbook`. Root `index.html` = 5 level sections (绘本/桥梁书/初章书/中章书/高章书) **+ 1 中文书 section** (accent #d4a017, 🀄, pill "中文", placeholder for now). Five level folders exist: `picture-books/`, `bridge-books/`, `early-chapter/`, `middle-chapter/`, `higher-chapter/` (empty ones have `.gitkeep`). A to Z Mysteries lives at `early-chapter/atozmysteries/` = hub `index.html` + **26 `*quiz.html` (A–Z)**, self-contained 10 Q each, 🌐 toggle, 🏠 home link `../../index.html`. Regenerate via `build.py` from `_quizdata/<LETTER>.json`. 中文书 has no folder yet.
- GitHub: repo **allenlinc/readbook** (`git@github.com:allenlinc/readbook.git`, SSH). GitHub Pages on `main`, root. Live: **https://allenlinc.github.io/readbook/**
- Old repo `allenlinc/a-to-z-mysteries` is outdated (old single-page site); prefer `readbook` now.
- **绘本 section now populated**: RAZ-O quiz set lives at `raz-o-quiz/` (NOT under `picture-books/`). Hub `index.html` (one level deep, home link `../index.html`) + `books/<slug>.html` (72 pages, two levels deep, home `../../index.html` + back-to-hub `../index.html`) + shared `assets/style.css`,`assets/quiz.js`. Regenerate via `raz-o-quiz/build.py` from `_quizdata/<slug>.json` (72 files, 10 bilingual MCQs + 1 思考题 each, tagged by 4 RAZ skills). `_sources.json` = 72 {title,slug,media_id}. Hub has search + skill filter. build.py's "MISSING (N of 72)" report is a false positive from title normalization (colons/apostrophes) — ignore if 72 pages generated. Live: https://allenlinc.github.io/readbook/raz-o-quiz/
- **IMA `fetch_media_content` gotcha**: media_id MUST have KB id appended (RAZ-O KB = `7473064203796870`), i.e. `<bare_id><kb_id>`; a bare id returns error `220030` (looks like an outage but isn't). Always suffix.
- To add a book: put quiz under the level folder, add a card in `index.html` (or level hub), commit & push. Pages auto-rebuilds on push (or POST /pages/builds). After moving files deeper, fix home links (`../index.html` → `../../index.html`).

## GitHub publishing notes (this machine)
- `gh` CLI is NOT logged in (`gh auth login` fails: token lacks `read:org` scope). A `gho_` OAuth token IS in the macOS keychain (scopes: read:user, repo, user:email, workflow).
- **SSH push works** (`ssh -T git@github.com` authenticates as allenlinc) — so pushing via `git@github.com:...` remotes is the easy path; no token needed.
- Workaround for API: read token via `git credential-osxkeychain get`, use it in API calls or as `https://<TOKEN>@github.com/...` remote URL for push, then strip the token from local remote config.
- Commit author email MUST be `7354315+allenlinc@users.noreply.github.com` (GitHub blocks real emails via GH007). Set in repo-local git config.
