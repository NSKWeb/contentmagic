// ContentMagic — Frontend Logic

const API_URL = "http://localhost:8000/api/generate";

// DOM elements
const inputText = document.getElementById("inputText");
const charCount = document.getElementById("charCount");
const styleSelect = document.getElementById("styleSelect");
const langSelect = document.getElementById("langSelect");
const generateBtn = document.getElementById("generateBtn");
const loader = document.getElementById("loader");
const outputSection = document.getElementById("outputSection");
const blogPreview = document.getElementById("blogPreview");

// State
let currentBlogHTML = "";

// Char counter
inputText.addEventListener("input", () => {
    const len = inputText.value.length;
    charCount.textContent = len.toLocaleString();
    charCount.style.color = len > 10000 ? "#f87171" : "#6b7280";
});

// Generate blog
async function generateBlog() {
    const text = inputText.value.trim();
    if (!text) {
        alert("Please paste some text first!");
        return;
    }
    if (text.length > 10000) {
        alert("Text too long! Max 10,000 characters.");
        return;
    }

    // UI states
    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";
    loader.classList.remove("hidden");
    outputSection.classList.add("hidden");

    try {
        const resp = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text: text,
                style: styleSelect.value,
                language: langSelect.value,
            }),
        });

        if (!resp.ok) {
            const err = await resp.json();
            throw new Error(err.detail || "Generation failed");
        }

        const data = await resp.json();
        currentBlogHTML = data.blog_html;

        // Update stats
        document.getElementById("statWords").textContent = `📊 ${data.word_count} words`;
        document.getElementById("statTime").textContent = `⏱ ${data.reading_time}`;
        document.getElementById("statProvider").textContent = `🤖 ${data.provider}`;

        // Update SEO
        document.getElementById("seoTitle").textContent = data.seo_title || "—";
        document.getElementById("seoDesc").textContent = data.meta_description || "—";
        document.getElementById("seoKeywords").textContent = data.keywords.length ? data.keywords.join(", ") : "—";
        document.getElementById("seoImage").textContent = data.image_suggestion || "—";

        // Show blog preview
        blogPreview.innerHTML = data.blog_html;

        // Show output
        outputSection.classList.remove("hidden");
        outputSection.scrollIntoView({ behavior: "smooth" });

    } catch (err) {
        alert("Error: " + err.message);
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = "✨ Generate Blog";
        loader.classList.add("hidden");
    }
}

// Copy HTML
function copyHTML() {
    if (!currentBlogHTML) return;
    navigator.clipboard.writeText(currentBlogHTML).then(() => {
        alert("HTML copied to clipboard! 📋");
    });
}

// Download HTML
function downloadHTML() {
    if (!currentBlogHTML) return;
    const blob = new Blob([currentBlogHTML], { type: "text/html" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "blog.html";
    a.click();
    URL.revokeObjectURL(url);
}

// Download Markdown
function downloadMarkdown() {
    if (!currentBlogHTML) return;
    // Simple HTML to Markdown conversion
    let md = currentBlogHTML;
    md = md.replace(/<h1[^>]*>(.*?)<\/h1>/gi, "# $1\n\n");
    md = md.replace(/<h2[^>]*>(.*?)<\/h2>/gi, "## $1\n\n");
    md = md.replace(/<h3[^>]*>(.*?)<\/h3>/gi, "### $1\n\n");
    md = md.replace(/<p[^>]*>(.*?)<\/p>/gi, "$1\n\n");
    md = md.replace(/<li[^>]*>(.*?)<\/li>/gi, "- $1\n");
    md = md.replace(/<strong>(.*?)<\/strong>/gi, "**$1**");
    md = md.replace(/<em>(.*?)<\/em>/gi, "*$1*");
    md = md.replace(/<blockquote[^>]*>(.*?)<\/blockquote>/gi, "> $1\n\n");
    md = md.replace(/<code>(.*?)<\/code>/gi, "`$1`");
    md = md.replace(/<[^>]+>/g, "");
    md = md.replace(/\n{3,}/g, "\n\n").trim();

    const blob = new Blob([md], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "blog.md";
    a.click();
    URL.revokeObjectURL(url);
}

// Keyboard shortcut: Ctrl+Enter to generate
inputText.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        generateBlog();
    }
});
