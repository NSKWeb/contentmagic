"""AI Service — Multi-Provider Support.

Supported Providers:
- nara        → Nara Router (router.bynara.id)
- gemini      → Google Gemini (generativelanguage.googleapis.com)
- openrouter  → OpenRouter (openrouter.ai)
- groq        → Groq (groq.com) — fast & free tier
- together    → Together AI (together.ai) — free tier
- huggingface → Hugging Face (huggingface.co) — free tier
"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

# ─── Provider select karo (.env mein AI_PROVIDER set karo) ───
PROVIDER = os.getenv("AI_PROVIDER", "nara")

# ─── Nara Router ───
NARA_ROUTER_KEY = ***"NARA_ROUTER_API_KEY", "")
NARA_ROUTER_URL = os.getenv("NARA_ROUTER_URL", "https://router.bynara.id/v1/chat/completions")

# ─── Google Gemini ───
GEMINI_KEY = ***"GEMINI_API_KEY", "")

# ─── OpenRouter ───
OPENROUTER_KEY = ***"OPENROUTER_API_KEY", "")

# ─── Groq ───
GROQ_KEY = ***"GROQ_API_KEY", "")

# ─── Together AI ───
TOGETHER_KEY = ***"TOGETHER_API_KEY", "")

# ─── Hugging Face ───
HF_KEY = ***"HUGGINGFACE_API_KEY", "")


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

    providers = {
        "nara": _call_nara,
        "gemini": _call_gemini,
        "openrouter": _call_openrouter,
        "groq": _call_groq,
        "together": _call_together,
        "huggingface": _call_huggingface,
    }

    if PROVIDER not in providers:
        raise ValueError(
            f"Unknown provider: '{PROVIDER}'. "
            f"Use one of: {', '.join(providers.keys())}"
        )

    return await providers[PROVIDER](system, text)


# ═══════════════════════════════════════
# Provider Functions
# ═══════════════════════════════════════

async def _call_nara(system: str, user_text: str) -> dict:
    """Nara Router — router.bynara.id (OpenRouter compatible)."""
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
                    {"role": "user", "content": user_text},
                ],
                "temperature": 0.7,
                "max_tokens": 4000,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return {"blog_html": content, "provider": "nara-router"}


async def _call_gemini(system: str, user_text: str) -> dict:
    """Google Gemini — generativelanguage.googleapis.com."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"
    prompt = f"{system}\n\n---\n\nConvert this text into a blog:\n\n{user_text}"

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            url,
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 4000},
            },
        )
        resp.raise_for_status()
        data = resp.json()
        content = data["candidates"][0]["content"]["parts"][0]["text"]
        if content.startswith("```"):
            content = content.split("\n", 1)[1]
            if content.endswith("```"):
                content = content[:-3]
        return {"blog_html": content.strip(), "provider": "gemini"}


async def _call_openrouter(system: str, user_text: str) -> dict:
    """OpenRouter — openrouter.ai (free models available)."""
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "google/gemini-2.0-flash-001:free",
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


async def _call_groq(system: str, user_text: str) -> dict:
    """Groq — groq.com (fast inference, free tier)."""
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "llama-3.3-70b-versatile",
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
        return {"blog_html": content, "provider": "groq"}


async def _call_together(system: str, user_text: str) -> dict:
    """Together AI — together.ai (free tier)."""
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {TOGETHER_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
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
        return {"blog_html": content, "provider": "together"}


async def _call_huggingface(system: str, user_text: str) -> dict:
    """Hugging Face — huggingface.co (free inference API)."""
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            "https://api-inference.huggingface.co/models/meta-llama/Llama-3.3-70B-Instruct",
            headers={
                "Authorization": f"Bearer {HF_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "inputs": f"{system}\n\n---\n\nConvert this text into a blog:\n\n{user_text}",
                "parameters": {"temperature": 0.7, "max_new_tokens": 4000},
            },
        )
        resp.raise_for_status()
        data = resp.json()
        content = data[0]["generated_text"] if isinstance(data, list) else data.get("generated_text", "")
        # Clean up if it repeats the prompt
        if "---" in content:
            content = content.split("---", 1)[-1].strip()
        return {"blog_html": content, "provider": "huggingface"}
