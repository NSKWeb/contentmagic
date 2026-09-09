"""ContentMagic — FastAPI Backend."""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

from ai_service import generate_blog
from blog_formatter import calculate_reading_time, extract_title, wrap_blog_html
from seo_generator import generate_seo_meta, suggest_image_topic

load_dotenv()

app = FastAPI(title="ContentMagic", version="1.0.0")

# CORS — allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class BlogRequest(BaseModel):
    text: str
    style: str = "professional"  # professional | casual | seo
    language: str = "english"     # english | hindi
    output_format: str = "html"   # html | markdown


class BlogResponse(BaseModel):
    blog_html: str
    title: str
    word_count: int
    reading_time: str
    seo_title: str
    meta_description: str
    keywords: list[str]
    image_suggestion: str
    provider: str


@app.get("/")
def root():
    return {"status": "ok", "app": "ContentMagic", "version": "1.0.0"}


@app.post("/api/generate", response_model=BlogResponse)
async def generate(req: BlogRequest):
    """Convert raw text into a structured blog post."""

    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if len(req.text) > 10000:
        raise HTTPException(status_code=400, detail="Text too long (max 10,000 chars)")

    try:
        # Generate blog via AI
        result = await generate_blog(
            text=req.text,
            style=req.style,
            language=req.language,
        )

        blog_html = result["blog_html"]
        provider = result["provider"]

        # Stats
        title = extract_title(blog_html)
        stats = calculate_reading_time(blog_html)

        # SEO
        seo = generate_seo_meta(blog_html, req.style)
        image_tip = suggest_image_topic(blog_html)

        return BlogResponse(
            blog_html=blog_html,
            title=title,
            word_count=stats["word_count"],
            reading_time=stats["reading_time_text"],
            seo_title=seo["seo_title"],
            meta_description=seo["meta_description"],
            keywords=seo["keywords"],
            image_suggestion=image_tip,
            provider=provider,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
