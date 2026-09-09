"""AI Service — Nara Router integration."""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

NARA_ROUTER_KEY = os.getenv("NARA_ROUTER_API_KEY", "")
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


async def generate_blog(
    text: str,
    style: str = "professional",
    language: str = "english",
) -> dict:
    """Convert raw text into a structured blog post via Nara Router."""

    system = SYSTEM_PROMPT.format(style=style, language=language)

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            NARA_ROUTER_URL,
            headers={
                "Authorization": f"Bearer {NARA_ROUTER_KEY}",
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
