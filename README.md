<div align="center">

# ✨ ContentMagic ✨

### _Any Text → Beautiful Blog Post — In Seconds_

<br>

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/ "Python 3.12 — Backend language") [![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/ "FastAPI 0.115 — Async web framework") [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML "HTML5 — Frontend structure") [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS3 — Styling & dark theme") [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JavaScript — Frontend logic") [![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT "MIT License — Free to use")

<br>

**📝 Paste anything · 🎨 Choose a style · ✨ Get a perfect blog**

<br>

> _"AI ko zero context do → wo freestyle karta hai._
> _AI ko ContentMagic do → wo tumhara project banaata hai, apna nahi."_

<br>

<details>
<summary>🐍 <b>Python 3.12</b> — Backend Language</summary>
<br>

- FastAPI server chalata hai
- AI API calls handle karta hai
- Blog formatting & SEO generation
- Type hints + async support

</details>

<details>
<summary>⚡ <b>FastAPI 0.115</b> — Web Framework</summary>
<br>

- Async API endpoints
- Auto-generated API docs (`/docs`)
- Request validation with Pydantic
- CORS support for frontend

</details>

<details>
<summary>🌐 <b>HTML5</b> — Frontend Structure</summary>
<br>

- Semantic markup
- Input textarea + controls
- Blog preview section
- Responsive layout

</details>

<details>
<summary>🎨 <b>CSS3</b> — Styling</summary>
<br>

- Dark purple theme 🟣
- Smooth animations
- Mobile responsive
- CSS variables for easy customization

</details>

<details>
<summary>⚡ <b>JavaScript</b> — Frontend Logic</summary>
<br>

- API calls to backend
- Copy/Download HTML & Markdown
- Character counter
- Keyboard shortcuts (Ctrl+Enter)

</details>

<details open>
<summary>📜 <b>MIT License</b> — Free to Use</summary>
<br>

**MIT License** duniya ki sabse **open aur permissive** license hai. Iska matlab:

| ✅ Kar Sakte Ho | ❌ Karna Zaroori Nahi |
|:----------------|:---------------------|
| Commercial use (paisa kamao 💰) | Source code disclose karna |
| Modify (apne hisaab se badlo) | Warranty dena |
| Distribute (doosron ko do) | Credit dena (par accha lagta hai 😄) |
| Private use (personal project) | License text rakhna (par rakhna chahiye) |
| Sublicense (apni license do) | |

**Simple mein:** Is code se jo chahein karo — bas pakad ke mat bolo ki tumne banaya. 🙏

**Full license:** [LICENSE](./LICENSE) file dekho

</details>

<br>

---

</div>

## 🎯 What is ContentMagic?

ContentMagic ek **AI-powered blog converter** hai jo koi bhi raw text, rough notes, ya article ko **professional, structured blog post** mein convert karta hai — with SEO meta, word count, reading time, aur image suggestions!

<div align="center">

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   📋 Paste your     ──►   🤖 AI converts   ──►   📄 Beautiful
│      rough text              it into a              blog post
│                              structured              ready to
│                              blog                    publish!
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 Features At A Glance

<table>
<tr>
<td width="50%">

### 📝 Input
- Koi bhi text paste karo
- Paragraph, notes, article — koi bhi format
- Hindi + English dono support
- Max 10,000 characters

</td>
<td width="50%">

### 📄 Output
- Structured blog with headings
- SEO title + meta description
- Word count + reading time
- Featured image suggestion
- HTML + Markdown download

</td>
</tr>
<tr>
<td width="50%">

### 🎨 3 Blog Styles
- **Professional** — formal, clean
- **Casual** — friendly, conversational
- **SEO-Optimized** — Google-ready

</td>
<td width="50%">

### ⚡ Performance
- Ultra lightweight frontend
- No frameworks — pure HTML/CSS/JS
- < 10 second generation
- Dark theme UI 🌙

</td>
</tr>
</table>

---

## 🚀 Quick Start

### 1️⃣ Clone the repo

```bash
git clone https://github.com/NSKWeb/contentmagic.git
cd contentmagic
```

### 2️⃣ Setup Backend

```bash
cd backend
pip install -r requirements.txt

# API key setup
cp .env.example .env
# .env file mein apni API key dalo
```

### 3️⃣ Start Backend

```bash
python main.py
# 🟢 Server running at http://localhost:8000
```

### 4️⃣ Open Frontend

```bash
cd frontend
python -m http.server 3000
# 🌐 Browser mein kholo: http://localhost:3000
```

### 5️⃣ Use it! 🎉

> Paste any text → Select style → Click **Generate Blog** → Done! ✨

---

## 🏗 Tech Stack

<div align="center">

| Layer | Technology | Why? |
|:-----:|:----------:|:----:|
| 🎨 Frontend | **Vanilla HTML + CSS + JS** | Ultra fast, zero dependencies |
| ⚙️ Backend | **Python FastAPI** | Async, fast, lightweight |
| 🤖 AI Engine | **Nara Router / Gemini** | Smart blog generation |
| 🎯 Styling | **Custom CSS (Dark Theme)** | Beautiful purple magic ✨ |
| 🚀 Hosting | **Vercel + Netlify** | Free, fast, reliable |

</div>

---

## 📂 Project Structure

```
contentmagic/
│
├── 🎨 frontend/
│   ├── index.html          ← Main UI page
│   ├── style.css           ← Dark purple theme
│   ├── app.js              ← Frontend logic
│   └── assets/             ← Images, icons
│
├── ⚙️ backend/
│   ├── main.py             ← FastAPI server
│   ├── ai_service.py       ← AI API integration
│   ├── blog_formatter.py   ← Blog stats & formatting
│   ├── seo_generator.py    ← SEO meta generation
│   └── prompts/            ← AI prompt templates
│
├── .env.example            ← API key template
├── .gitignore              ← Git ignore rules
├── requirements.txt        ← Python dependencies
└── README.md               ← You are here! 👋
```

---

## 🎨 Color Palette

<div align="center">

| Color | Hex | Use |
|:-----:|:---:|:---:|
| 🟣 | `#7c3aed` | Primary accent |
| 🔮 | `#a78bfa` | Light accent |
| ⬛ | `#0a0a0f` | Background |
| 🌑 | `#141420` | Surface / Cards |
| ⬜ | `#f0f0f5` | Primary text |
| 🔘 | `#6b7280` | Muted text |
| 🟢 | `#34d399` | Success |
| 🔴 | `#f87171` | Error / Danger |

</div>

---

## 📸 How It Works

```
   ┌──────────────┐
   │  📋 Paste    │
   │  Your Text   │──────┐
   └──────────────┘      │
                         ▼
              ┌─────────────────────┐
              │   🤖 AI Processing  │
              │                     │
              │  • Analyze content  │
              │  • Add structure    │
              │  • Generate headings│
              │  • Write intro/outro│
              └─────────────────────┘
                         │
                         ▼
   ┌─────────────────────────────────┐
   │  📄 Beautiful Blog Output       │
   │                                 │
   │  ✅ Structured HTML             │
   │  ✅ SEO Meta Tags               │
   │  ✅ Word Count & Reading Time   │
   │  ✅ Image Suggestions           │
   │  ✅ Copy / Download Options     │
   └─────────────────────────────────┘
```

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|:--------:|:------:|
| `Ctrl` + `Enter` | Generate blog instantly |

---

## 🛣 Roadmap

- [x] 📝 Raw text to blog conversion
- [x] 🎨 3 blog styles (Professional / Casual / SEO)
- [x] 🌐 Hindi + English support
- [x] 📊 Word count + reading time
- [x] 🔍 SEO meta auto-generation
- [x] 🖼 Featured image suggestion
- [ ] 📌 Direct Blogspot publishing
- [ ] 🖼 AI image generation
- [ ] 👤 User accounts & history
- [ ] 📱 Mobile app (PWA)
- [ ] 🌍 More languages (Urdu, Bengali, etc.)

---

## 🤝 Contributing

Contributions welcome! 🎉

```bash
# 1. Fork the repo
# 2. Create feature branch
git checkout -b feature/amazing-feature

# 3. Commit changes
git commit -m "feat: add amazing feature"

# 4. Push & create PR
git push origin feature/amazing-feature
```

---

## 📜 License

MIT License — feel free to use, modify, and distribute! 💜

---

<div align="center">

### Made with ✨ and ☕ by [NSKWeb](https://github.com/NSKWeb)

<br>

**⭐ Star this repo if you found it useful!**

<br>

![Visitors](https://api.visitorbadge.io/api/visitors?path=NSKWeb%2Fcontentmagic&countColor=%237c3aed&style=for-the-badge)

</div>
