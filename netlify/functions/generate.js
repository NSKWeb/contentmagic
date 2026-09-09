// Netlify Function — ContentMagic API

const https = require("https");
const http = require("http");

const SYSTEM_PROMPT = `You are ContentMagic — an expert blog writer.

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
Use tags: h1, h2, h3, p, ul, ol, li, strong, em, blockquote, code`;

function extractTitle(html) {
  const match = html.match(/<h1[^>]*>(.*?)<\/h1>/is);
  if (match) return match[1].replace(/<[^>]+>/g, "").trim();
  return "Untitled Blog Post";
}

function calcReadingTime(html) {
  const text = html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
  const words = text.split(/\s+/).length;
  const minutes = Math.max(1, Math.round(words / 200));
  return { word_count: words, reading_time_min: minutes, reading_time_text: `${minutes} min read` };
}

function generateSeo(html) {
  const titleMatch = html.match(/<h1[^>]*>(.*?)<\/h1>/is);
  const title = titleMatch ? titleMatch[1].replace(/<[^>]+>/g, "").trim() : "";
  const text = html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
  const bodyText = title ? text.slice(title.length).trim() : text;
  const sentences = bodyText.split(/[.!?]+/).filter(s => s.trim());

  let desc = "";
  for (const s of sentences) {
    if (desc.length + s.trim().length < 155) desc += s.trim() + ". ";
  }
  desc = desc.trim().slice(0, 155);

  const headings = [...html.matchAll(/<h[23][^>]*>(.*?)<\/h[23]>/gis)];
  const keywords = headings
    .map(h => h[1].replace(/<[^>]+>/g, "").trim().toLowerCase())
    .filter(k => k.length > 2)
    .slice(0, 5);

  return { seo_title: title.slice(0, 60), meta_description: desc, keywords };
}

function suggestImage(html) {
  const match = html.match(/<h1[^>]*>(.*?)<\/h1>/is);
  if (match) {
    const title = match[1].replace(/<[^>]+>/g, "").trim();
    return `Suggested image: A visual representation of '${title}'. Search on Unsplash/Pexels.`;
  }
  return "Suggested image: A generic blog header image.";
}

async function callAI(text, style, language) {
  const system = SYSTEM_PROMPT.replace("{style}", style).replace("{language}", language);
  const url = process.env.NARA_ROUTER_URL || "https://router.bynara.id/v1/chat/completions";
  const apiKey = process.env.NARA_ROUTER_API_KEY || "";

  const body = JSON.stringify({
    model: "google/gemini-2.0-flash-001",
    messages: [
      { role: "system", content: system },
      { role: "user", content: text },
    ],
    temperature: 0.7,
    max_tokens: 4000,
  });

  return new Promise((resolve, reject) => {
    const parsedUrl = new URL(url);
    const options = {
      hostname: parsedUrl.hostname,
      port: parsedUrl.port || 443,
      path: parsedUrl.pathname,
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(body),
      },
    };

    const reqModule = parsedUrl.protocol === "https:" ? https : http;
    const req = reqModule.request(options, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => {
        try {
          const json = JSON.parse(data);
          if (json.choices && json.choices[0]) {
            resolve(json.choices[0].message.content);
          } else {
            reject(new Error("Invalid AI response"));
          }
        } catch (e) {
          reject(e);
        }
      });
    });

    req.on("error", reject);
    req.setTimeout(60000, () => {
      req.destroy();
      reject(new Error("AI request timeout"));
    });
    req.write(body);
    req.end();
  });
}

exports.handler = async (event) => {
  // CORS headers
  const headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
  };

  // Handle OPTIONS (preflight)
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 200, headers, body: "" };
  }

  // Handle GET
  if (event.httpMethod === "GET") {
    return {
      statusCode: 200,
      headers: { ...headers, "Content-Type": "application/json" },
      body: JSON.stringify({ status: "ok", app: "ContentMagic", version: "1.0.0" }),
    };
  }

  // Handle POST
  if (event.httpMethod === "POST") {
    try {
      const data = JSON.parse(event.body);
      const text = (data.text || "").trim();
      const style = data.style || "professional";
      const language = data.language || "english";

      if (!text) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: "Text cannot be empty" }) };
      }
      if (text.length > 10000) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: "Text too long (max 10,000 chars)" }) };
      }

      const blogHtml = await callAI(text, style, language);
      const title = extractTitle(blogHtml);
      const stats = calcReadingTime(blogHtml);
      const seo = generateSeo(blogHtml);
      const imageSuggestion = suggestImage(blogHtml);

      const response = {
        blog_html: blogHtml,
        title,
        word_count: stats.word_count,
        reading_time: stats.reading_time_text,
        seo_title: seo.seo_title,
        meta_description: seo.meta_description,
        keywords: seo.keywords,
        image_suggestion: imageSuggestion,
        provider: "nara-router",
      };

      return {
        statusCode: 200,
        headers: { ...headers, "Content-Type": "application/json" },
        body: JSON.stringify(response),
      };
    } catch (e) {
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ error: e.message }),
      };
    }
  }

  return { statusCode: 405, headers, body: JSON.stringify({ error: "Method not allowed" }) };
};
