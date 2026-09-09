"""Vercel Serverless Function — ContentMagic API."""

import os
import json
import httpx
import re
from http.server import BaseHTTPRequestHandler


# ─── AI Service ───

PROVIDER = os.getenv("AI_PROVIDER", "openrouter")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "")
NARA_ROUTER_URL = os.getenv("NARA_ROUTER_URL", "https://router.bynara.id/v1/chat/completions")

SYSTEM_PROMPT = """You are ContentMagic — an expert blog writer.

Your job: Convert the user's raw text into a well-structured, engaging blog post.

Rules:
1. Add a catchy title (H1)
2. Write an engaging introduction paragraph
3. Break content into sections with proper headings (H2, H3)
4. Add bullet points or numbered lists where appropriate
5. Write a conclusion with a takeaway
6. Keep the original meaning — don't add fake info
7. Match the requested style: {style}
8. Match the requested language: {language}

Output format: Return ONLY valid HTML (no markdown, no code fences).
Use tags: h1, h2, h3, p, ul, ol, li, strong, em, blockquote, code
"""


async def generate_blog(text, style="professional", language="english"):
    system = SYSTEM_PROMPT.format(style=style, language=language)

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            NARA_ROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "google/gemini-2.0-flash-001",
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": text},
                ],
                "temperature": 0.7,
                "max_tokens": 4000,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return {"blog_html": content, "provider": "nara-router"}


# ─── Blog Utils ───

def calculate_reading_time(html_content):
    text = re.sub(r"<[^>]+>", " ", html_content)
    words = len(text.split())
    minutes = max(1, round(words / 200))
    return {"word_count": words, "reading_time_min": minutes, "reading_time_text": f"{minutes} min read"}


def extract_title(html_content):
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html_content, re.IGNORECASE | re.DOTALL)
    if match:
        return re.sub(r"<[^>]+>", "", match.group(1)).strip()
    return "Untitled Blog Post"


def generate_seo_meta(html_content, style="professional"):
    text = re.sub(r"<[^>]+>", " ", html_content)
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html_content, re.IGNORECASE | re.DOTALL)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() if title_match else ""

    body_text = text[len(title):].strip() if title else text
    sentences = re.split(r'[.!?]+', body_text)
    description = ""
    for s in sentences:
        s = s.strip()
        if s and len(description) + len(s) < 155:
            description += s + ". "
    description = description.strip()[:155]

    headings = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", html_content, re.IGNORECASE)
    keywords = [re.sub(r"<[^>]+>", "", h).strip().lower() for h in headings if len(h.strip()) > 2][:5]

    return {
        "seo_title": title[:60] if title else "",
        "meta_description": description,
        "keywords": keywords,
    }


def suggest_image_topic(html_content):
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html_content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip()
        return f"Suggested image: A visual representation of '{title}'. Search on Unsplash/Pexels."
    return "Suggested image: A generic blog header image."


# ─── Vercel Handler ───

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        text = data.get("text", "").strip()
        style = data.get("style", "professional")
        language = data.get("language", "english")

        if not text:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Text cannot be empty"}).encode())
            return

        if len(text) > 10000:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Text too long (max 10,000 chars)"}).encode())
            return

        try:
            import asyncio
            result = asyncio.run(generate_blog(text, style, language))
            blog_html = result["blog_html"]
            title = extract_title(blog_html)
            stats = calculate_reading_time(blog_html)
            seo = generate_seo_meta(blog_html, style)
            image_tip = suggest_image_topic(blog_html)

            response = {
                "blog_html": blog_html,
                "title": title,
                "word_count": stats["word_count"],
                "reading_time": stats["reading_time_text"],
                "seo_title": seo["seo_title"],
                "meta_description": seo["meta_description"],
                "keywords": seo["keywords"],
                "image_suggestion": image_tip,
                "provider": result["provider"],
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok", "app": "ContentMagic", "version": "1.0.0"}).encode())
