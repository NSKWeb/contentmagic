"""Blog formatting & stats utilities."""

import re


def calculate_reading_time(html_content: str) -> dict:
    """Calculate word count and reading time from HTML content."""
    # Strip HTML tags
    text = re.sub(r"<[^>]+>", " ", html_content)
    text = re.sub(r"\s+", " ", text).strip()

    words = len(text.split())
    # Average reading speed: 200 words/min
    minutes = max(1, round(words / 200))

    return {
        "word_count": words,
        "reading_time_min": minutes,
        "reading_time_text": f"{minutes} min read",
    }


def extract_title(html_content: str) -> str:
    """Extract the first H1 title from HTML."""
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html_content, re.IGNORECASE | re.DOTALL)
    if match:
        return re.sub(r"<[^>]+>", "", match.group(1)).strip()
    return "Untitled Blog Post"


def wrap_blog_html(body_html: str, title: str = "") -> str:
    """Wrap blog body in a clean HTML structure."""
    if not title:
        title = extract_title(body_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: 'Georgia', serif; max-width: 720px; margin: 0 auto; padding: 2rem; line-height: 1.8; color: #1a1a1a; }}
        h1 {{ font-size: 2.2rem; margin-bottom: 0.5rem; }}
        h2 {{ font-size: 1.6rem; margin-top: 2rem; border-bottom: 1px solid #eee; padding-bottom: 0.3rem; }}
        h3 {{ font-size: 1.3rem; }}
        blockquote {{ border-left: 3px solid #7c3aed; padding-left: 1rem; color: #555; font-style: italic; }}
        code {{ background: #f4f4f5; padding: 0.2rem 0.4rem; border-radius: 4px; font-size: 0.9rem; }}
        ul, ol {{ padding-left: 1.5rem; }}
        li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body>
{body_html}
</body>
</html>"""
