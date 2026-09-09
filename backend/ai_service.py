"""AI Service — OpenRouter & Gemini integration."""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("AI_PROVIDER", "openrouter")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "")
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")
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
    """Convert raw text into a structured blog post."""

    system = SYSTEM_PROMPT.format(style=style, language=language)

    if PROVIDER == "openrouter":
        return await _call_openrouter(system, text)
    elif PROVIDER == "gemini":
        return await _call_gemini(system, text)
    else:
        raise ValueError(f"Unknown provider: {PROVIDER}")


async def _call_openrouter(system: str, user_text: str) -> dict:
    """Call Nara Router API (OpenRouter compatible)."""
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
                    {"role": "user", "content": user_text},
                ],
                "temperature": 0.7,
                "max_tokens": 4000,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return {"blog_html": content, "provider": "openrouter"}


async def _call_gemini(system: str, user_text: str) -> dict:
    """Call Google Gemini API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"
    prompt = f"{system}\n\n---\n\nConvert this text into a blog:\n\n{user_text}"

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            url,
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 4000,
                },
            },
        )
        resp.raise_for_status()
        data = resp.json()
        content = data["candidates"][0]["content"]["parts"][0]["text"]
        # Clean up markdown code fences if present
        if content.startswith("```"):
            content = content.split("\n", 1)[1]
            if content.endswith("```"):
                content = content[:-3]
        return {"blog_html": content.strip(), "provider": "gemini"}
