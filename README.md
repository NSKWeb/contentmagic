<div align="center">

<br>

◆ &nbsp; VOL. I &nbsp; · &nbsp; NO. 1 &nbsp; · &nbsp; EST. 2026 &nbsp; ◆

<br><br>

# ContentMagic

### _The Art of Transforming Words_

<br>

A single tool — born of necessity, shaped by craft — that takes your rough,
unformed text and weaves it into something worth reading.

<br>

---

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-c44b2b?style=flat-square)](https://opensource.org/licenses/MIT)

<br>

</div>

---

## On the Purpose of This Thing

> *"AI ko zero context do → wo freestyle karta hai.*
> *AI ko ContentMagic do → wo tumhara project banaata hai, apna nahi."*

You have words. Scattered notes. Half-formed paragraphs. Maybe in English, maybe in Hindi, maybe in something in between. They make sense to you — but would they make sense to a reader?

**ContentMagic** takes that raw material and gives it shape. Structure. A beginning, a middle, an end. Headings where headings belong. An introduction that draws the reader in. A conclusion that sends them away satisfied.

In seconds. Not hours.

---

## What It Does

<table>
<tr>
<td width="50%" valign="top">

**You provide:**
- Any text, any format
- Rough notes, articles, paragraphs
- Hindi or English
- Chaos, disorder, fragments

</td>
<td width="50%" valign="top">

**You receive:**
- A structured blog post
- Headings, subheadings, flow
- SEO title & meta description
- Word count & reading time
- Featured image suggestions
- HTML & Markdown downloads

</td>
</tr>
</table>

---

## Three Voices, One Tool

| Voice | Character |
|:------|:----------|
| **Professional** | The Boardroom. Clean. Authoritative. Measured. |
| **Casual** | The Fireside. Warm. Conversational. Human. |
| **SEO-Optimized** | The Searchlight. Precise. Discoverable. Strategic. |

---

## Getting Started

### I. Clone

```bash
git clone https://github.com/NSKWeb/contentmagic.git
cd contentmagic
```

### II. Install

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env
```

### III. Run

```bash
# Backend
python main.py

# Frontend (new terminal)
cd frontend
python -m http.server 3000
```

### IV. Use

Open `http://localhost:3000` — paste your text — choose a voice — transform.

---

## The Craft Behind It

| Layer | Choice | Reason |
|:-----:|:------:|:-------|
| **Frontend** | [Vanilla HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) · [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) · [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | No frameworks. No bloat. Just speed. |
| **Backend** | [Python](https://www.python.org/) · [FastAPI](https://fastapi.tiangolo.com/) | Async. Fast. Gets out of the way. |
| **AI** | [Nara Router](https://router.bynara.id/) · [Gemini](https://ai.google.dev/) | The brain. The wordsmith. |
| **Design** | Editorial · Neo-Brutalist | Warm ink on cream parchment. |
| **Hosting** | [Vercel](https://vercel.com/) · [Netlify](https://netlify.com/) | Free. Fast. Everywhere. |

---

## Project Anatomy

```
contentmagic/
│
├── frontend/                  ← Static files (browser mein dikhta hai)
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── api/                       ← ▲ Vercel backend (Python serverless function)
│   └── generate.py
│
├── netlify/                   ← ◆ Netlify backend (JS serverless function)
│   └── functions/
│       └── generate.js
│
├── backend/                   ← Local development ke liye
│   ├── main.py
│   ├── ai_service.py
│   ├── blog_formatter.py
│   └── seo_generator.py
│
├── vercel.json                ← ▲ Vercel config
├── netlify.toml               ← ◆ Netlify config
├── .env.example
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## The Palette

<div align="center">

| | Name | Hex | Role |
|:-:|:-----|:---:|:-----|
| 🟫 | Venetian Red | `#c44b2b` | Accent — warmth, action, emphasis |
| 🟡 | Antique Gold | `#b8963e` | Secondary — ornament, detail |
| ⬛ | Printer's Ink | `#1a1614` | Text — primary reading color |
| 🟤 | Sepia | `#7a6f66` | Muted — secondary text |
| 🟫 | Parchment | `#f5f0e8` | Background — the page itself |
| 🟫 | Vellum | `#faf6ef` | Surface — cards, inputs |

</div>

---

## 🚀 Deploy Guide — Full Stack (Frontend + Backend)

---

### ❓ Sabse Pehle: Backend Kahan Deploy Karna Hai?

**Jawab: Backend ALAG se deploy nahi karna.**

Vercel ya Netlify pe jab tum repo import karo ge, toh wo **khud** tumhare backend code ko detect karke deploy kar denge. Tumhe kuch extra nahi karna.

| Platform | Backend File | Kya Hota Hai |
|----------|-------------|-------------|
| ▲ **Vercel** | `api/generate.py` | Vercel ise uthata hai aur **serverless function** bana deta hai |
| ◆ **Netlify** | `netlify/functions/generate.js` | Netlify ise uthata hai aur **serverless function** bana deta hai |

> **Matlab:** Frontend + Backend dono ek hi repo mein hain. Ek hi platform pe deploy hote hain. Alag server ki zaroorat **NAHI**. Alag se backend deploy karne ki zaroorat **NAHI**.

---

### 🔑 Yeh Kaise Possible Hai?

Vercel/Netlify ka feature hai: **Serverless Functions**

```
TUMHARA REPO                      VERCEL / NETLIFY
─────────────                      ────────────────

frontend/          ──────────►     CDN pe serve hota hai
  index.html                       (frontend dikhta hai)
  style.css
  app.js

api/generate.py    ──────────►     Serverless Function
  (backend code)                   ban jaata hai
                                   (jab API call aaye
                                    tabhi chalta hai,
                                    baaki time band)
```

> **Simple mein:** Backend code repo mein hai. Vercel/Netlify use le ke automatically function bana deta hai. Jab user API call kare → function chalta hai → AI se blog banta hai → response aata hai. Bas. Koi alag server nahi. Koi extra paisa nahi.

```
┌──────────────────────────────────────────────────────┐
│                    VERCEL / NETLIFY                  │
│                                                      │
│   ┌──────────────┐        ┌──────────────────────┐  │
│   │   FRONTEND   │  API   │  BACKEND             │  │
│   │   (Static)   │──────► │  (Serverless Fn)     │  │
│   │              │ call   │                      │  │
│   │  index.html  │        │  generate.py / .js   │  │
│   │  style.css   │        │  AI call karta hai   │  │
│   │  app.js      │        │  Response deta hai   │  │
│   └──────────────┘        └──────────────────────┘  │
│                                                      │
│   Sab ek hi repo mein hai. Ek hi deploy.             │
│   Alag server ki zaroorat NAHI.                      │
└──────────────────────────────────────────────────────┘
```

> **Matlab:** Tumhe alag se backend server nahi chalana. Vercel/Netlify khud backend code ko **serverless function** mein chalata hai — jab API call aaye, tabhi execute hota hai. Free hai. Fast hai.

---

## ▲ VERCEL — Full Stack Deploy (Step by Step)

> **Frontend:** Static files CDN se serve hote hain (fast)
> **Backend:** `api/generate.py` — Vercel automatically Python serverless function banata hai

### Step 1: Vercel pe jaao

🔗 [https://vercel.com](https://vercel.com) → **"Continue with GitHub"** → Login karo

### Step 2: New Project Import karo

1. Dashboard mein **"Add New..."** → **"Project"** dabao
2. **"Import Git Repository"** section mein `NSKWeb/contentmagic` search karo
3. **"Import"** dabao

### Step 3: Project Settings

| Setting | Kya Daalein |
|---------|-------------|
| **Framework Preset** | `Other` select karo |
| **Root Directory** | `.` (khali chhodo — default hai) |
| **Build Command** | khali chhodo |
| **Output Directory** | khali chhodo |

### Step 4: Environment Variables (Zaroori!) ⚠️

**"Environment Variables"** section expand karo aur yeh 2 variables add karo:

| Key | Value |
|-----|-------|
| `NARA_ROUTER_API_KEY` | `apni-nara-router-key-yahan-daal` |
| `NARA_ROUTER_URL` | `https://router.bynara.id/v1/chat/completions` |

> ⚠️ **Bina environment variables ke backend kaam nahi karega!** API key yahin set hoti hai — `.env` file deploy mein nahi jaati.

### Step 5: Deploy!

1. **"Deploy"** button dabao ✅
2. 1-2 minute wait karo (build ho raha hoga)
3. **"Congratulations!"** dikhega — tera live URL milega
4. URL milega: `https://contentmagic-xxx.vercel.app`

### Step 6: Test Karo

1. URL kholo browser mein
2. Koi bhi text paste karo
3. Style select karo (Professional / Casual / SEO)
4. **"✦ Transform My Words ✦"** dabao
5. Blog generate hona chahiye! 🎉

### Kaise Kaam Karta Hai Vercel Pe:

```
User visits https://contentmagic-xxx.vercel.app
        │
        ▼
┌─ Vercel CDN ─────────────────────────┐
│  Frontend files serve hote hain      │
│  (index.html, style.css, app.js)     │
└──────────────────────────────────────┘
        │
        │  User clicks "Generate"
        ▼
┌─ Vercel Serverless Function ─────────┐
│  /api/generate.py execute hota hai   │
│  → AI API call karta hai             │
│  → Blog generate karta hai           │
│  → Response bhejta hai               │
│  (Free hai — sirf call pe chalta hai)│
└──────────────────────────────────────┘
        │
        ▼
Blog preview frontend pe dikh jata hai
```

---

## ◆ NETLIFY — Full Stack Deploy (Step by Step)

> **Frontend:** Static files Netlify CDN se serve hote hain
> **Backend:** `netlify/functions/generate.js` — Netlify automatically JavaScript serverless function banata hai

### Step 1: Netlify pe jaao

🔗 [https://netlify.com](https://netlify.com) → **"Sign up with GitHub"** → Login karo

### Step 2: New Site Create karo

1. Dashboard mein **"Add new site"** dabao
2. **"Import an existing project"** select karo
3. **"GitHub"** select karo (authorize karo agar puche)
4. `NSKWeb/contentmagic` search karo → select karo

### Step 3: Site Settings

| Setting | Kya Daalein |
|---------|-------------|
| **Branch to deploy** | `main` |
| **Base directory** | khali chhodo |
| **Build command** | `echo 'Static site'` |
| **Publish directory** | `frontend` |

> ⚠️ **Publish directory** mein `frontend` zaroor daalo — warna files nahi milengi.

### Step 4: Environment Variables (Zaroori!) ⚠️

1. **"Deploy site"** se pehle **"Site settings"** pe jaao
2. **"Environment variables"** → **"Add a variable"** dabao
3. Yeh 3 variables add karo:

| Key | Value |
|-----|-------|
| `NARA_ROUTER_API_KEY` | `apni-nara-router-key-yahan-daal` |
| `NARA_ROUTER_URL` | `https://router.bynara.id/v1/chat/completions` |

> ⚠️ **Environment variables bina backend kaam nahi karega!**

### Step 5: Deploy!

1. **"Deploy site"** button dabao ✅
2. 1-2 minute wait karo
3. **"Published"** dikhega — tera live URL milega
4. URL milega: `https://xxx-xxx.netlify.app`

### Step 6: Test Karo

1. URL kholo browser mein
2. Koi bhi text paste karo
3. Style select karo
4. **"✦ Transform My Words ✦"** dabao
5. Blog generate hona chahiye! 🎉

### Kaise Kaam Karta Hai Netlify Pe:

```
User visits https://xxx-xxx.netlify.app
        │
        ▼
┌─ Netlify CDN ────────────────────────┐
│  Frontend files serve hote hain      │
│  (index.html, style.css, app.js)     │
└──────────────────────────────────────┘
        │
        │  User clicks "Generate"
        ▼
┌─ Netlify Function ───────────────────┐
│  /.netlify/functions/generate        │
│  → AI API call karta hai             │
│  → Blog generate karta hai           │
│  → Response bhejta hai               │
│  (Free hai — sirf call pe chalta hai)│
└──────────────────────────────────────┘
        │
        ▼
Blog preview frontend pe dikh jata hai
```

---

## 📊 Vercel vs Netlify — Kaunsa Choose Karein?

| Feature | ▲ Vercel | ◆ Netlify |
|---------|----------|----------|
| **Frontend** | ✅ Static (CDN) | ✅ Static (CDN) |
| **Backend** | ✅ Python serverless | ✅ JavaScript serverless |
| **Free Tier** | ✅ 100GB bandwidth | ✅ 100GB bandwidth |
| **Custom Domain** | ✅ Free | ✅ Free |
| **SSL (HTTPS)** | ✅ Auto | ✅ Auto |
| **GitHub Auto-deploy** | ✅ Push → Auto deploy | ✅ Push → Auto deploy |
| **Deploy Speed** | ⚡ 1-2 min | ⚡ 1-2 min |
| **Python Support** | ✅ Native | ⚠️ JS function (included) |
| **Difficulty** | ⭐ Easy | ⭐ Easy |

> **Dono free hain. Dono full stack support karte hain. Dono mein backend alag server pe nahi — serverless function hai.**

> 💡 **Meri recommendation:** Vercel use karo — Python native support hai, thoda fast hai.

---

## 🖥 VPS / Local — Full Stack Deploy (Gemini API)

Agar VPS pe deploy karna hai ya local chalana hai, toh **Gemini API** use karo (Nara Router nahi).

### .env file setup:

```bash
# VPS/Local ke liye yeh .env mein daalo:
AI_PROVIDER=gemini
GEMINI_API_KEY=apni-gemini-key-yahan-daal
```

### Steps:

```bash
# 1. VPS pe SSH karo
ssh root@your-vps-ip

# 2. Clone karo
git clone https://github.com/NSKWeb/contentmagic.git
cd contentmagic

# 3. Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt

# 4. .env setup (Gemini key daalo)
cp ../.env.example .env
nano .env
# AI_PROVIDER=gemini
# GEMINI_API_KEY=apni-gemini-key

# 5. Backend chalao
python main.py
# 🟢 http://localhost:8000

# 6. Frontend (naye terminal mein)
cd ../frontend
python3 -m http.server 3000
# 🌐 http://localhost:3000
```

### 🤖 Available Providers (6 Options!)

| Provider | Key | Free? | Best For |
|----------|-----|-------|----------|
| `nara` | `NARA_ROUTER_API_KEY` | ✅ | Vercel/Netlify (default) |
| `gemini` | `GEMINI_API_KEY` | ✅ | VPS/Local |
| `openrouter` | `OPENROUTER_API_KEY` | ✅ free models | Sab kuch |
| `groq` | `GROQ_API_KEY` | ✅ free tier | Fastest inference ⚡ |
| `together` | `TOGETHER_API_KEY` | ✅ free tier | Llama models |
| `huggingface` | `HUGGINGFACE_API_KEY` | ✅ free | Open source models |

### Kaunsa Provider Kab Use Karein?

| Deploy Kar Rahe Ho? | Recommended Provider |
|---------------------|---------------------|
| ▲ **Vercel** | `nara` (default) |
| ◆ **Netlify** | `nara` (default) |
| 🖥 **VPS** | `nara` ya `gemini` ya `groq` |
| 💻 **Local** | `nara` ya `gemini` ya `groq` |

> **Koi bhi provider kahin bhi use kar sakte ho — VPS pe bhi Nara Router chalega!**

### Provider Kaise Switch Karein?

`.env` file mein bas `AI_PROVIDER` change karo:

```bash
# Example: Groq use karna hai (fastest)
AI_PROVIDER=groq
GROQ_API_KEY=apni-g…daal
```

```bash
# Example: Nara Router use karna hai
AI_PROVIDER=nara
NARA_ROUTER_API_KEY=apni-n…daal
```

---

## Roadmap

- [x] Raw text → structured blog
- [x] Three editorial voices
- [x] Hindi & English
- [x] Word count & reading time
- [x] SEO metadata generation
- [x] Image suggestions
- [ ] Direct Blogspot publishing
- [ ] AI image generation
- [ ] Reader accounts & history
- [ ] Progressive Web App
- [ ] More languages (Urdu, Bengali, Marathi)

---

## Contributing

Fork it. Branch it. Commit with intention. Pull request with care.

```bash
git checkout -b feature/your-idea
git commit -m "feat: describe what you did"
git push origin feature/your-idea
```

---

## The License

<div align="center">

**◆ &nbsp; THE &nbsp; MIT &nbsp; LICENSE &nbsp; ◆**

</div>

### In Plain Words

| You May | You Need Not |
|:--------|:-------------|
| ✅ Use it for anything — personal or commercial | Disclose your source code |
| ✅ Modify it to suit your needs | Provide any warranty |
| ✅ Share it with others | Give credit (though it's kind to do so) |
| ✅ Sell products built with it | Include the license (though you should) |
| ✅ Sublicense under your own terms | Ask permission first |

> **In short:** Do whatever you wish with this code. Just don't hold us liable if something goes wrong, and don't claim you wrote it from scratch.

### The Full Text

```
MIT License

Copyright (c) 2026 NSKWeb — ContentMagic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

→ See [LICENSE](./LICENSE) for the official file.

---

<div align="center">

<br>

◆

<br>

_ContentMagic · Vol. I · A tool for writers, bloggers, & makers of all kinds_

<br>

[![Visitors](https://api.visitorbadge.io/api/visitors?path=NSKWeb%2Fcontentmagic&countColor=%23c44b2b&style=flat-square)](https://github.com/NSKWeb/contentmagic)

</div>
