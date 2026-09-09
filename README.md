# ✨ ContentMagic

Any raw text/article ko proper structured blog post mein convert karo — seconds mein!

## Features

- 📝 Koi bhi text paste karo — paragraph, notes, article
- 🎨 3 Blog Styles: Professional / Casual / SEO-optimized
- 🌐 Hindi + English dono support
- 📊 Word count + reading time
- 🔍 Auto SEO title + meta description
- 🖼 Featured image suggestion
- 📋 HTML + Markdown download
- 🚀 Ultra lightweight frontend (vanilla HTML/CSS/JS)

## Quick Start

### 1. Clone
```bash
git clone https://github.com/NSKWeb/contentmagic.git
cd contentmagic
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# .env mein apni API key dalo
python main.py
```

### 3. Frontend
```bash
cd frontend
# Simple HTTP server se kholo
python -m http.server 3000
```

Browser mein: `http://localhost:3000`

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | Vanilla HTML + CSS + JS |
| Backend | Python FastAPI |
| AI | OpenRouter / Gemini API |
| Hosting | Vercel + Netlify |

## License

MIT
