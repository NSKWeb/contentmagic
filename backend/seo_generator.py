"""SEO meta generation from blog content."""

import re


def generate_seo_meta(html_content: str, style: str = "professional") -> dict:
    """Generate SEO title, meta description, and keywords from blog HTML."""

    # Extract text
    text = re.sub(r"<[^>]+>", " ", html_content)
    text = re.sub(r"\s+", " ", text).strip()

    # Extract title
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html_content, re.IGNORECASE | re.DOTALL)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() if title_match else ""

    # Generate meta description (first 155 chars of body text, skip title)
    body_text = text[len(title):].strip() if title else text
    sentences = re.split(r'[.!?]+', body_text)
    description = ""
    for s in sentences:
        s = s.strip()
        if s and len(description) + len(s) < 155:
            description += s + ". "
    description = description.strip()
    if len(description) > 155:
        description = description[:152] + "..."

    # Extract potential keywords from headings
    headings = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", html_content, re.IGNORECASE)
    keywords = [re.sub(r"<[^>]+>", "", h).strip().lower() for h in headings]
    keywords = [k for k in keywords if len(k) > 2][:5]

    return {
        "seo_title": title[:60] if title else "",
        "meta_description": description,
        "keywords": keywords,
        "og_title": title[:95] if title else "",
        "og_description": description,
    }


def suggest_image_topic(html_content: str) -> str:
    """Suggest a featured image topic based on blog content."""
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html_content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip()
        return f"Suggested image: A visual representation of '{title}'. Search on Unsplash/Pexels for relevant free images."
    return "Suggested image: A generic blog header image related to the topic."
