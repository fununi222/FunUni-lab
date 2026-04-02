# Blog Brush-up Changelog (2026-04-03)

## Overview
Based on the guidelines in `SKILL.md`, the FunUni-lab blog has been updated to a premium, monochrome, VS Code-inspired dark theme.

## Modifications

### [MODIFY] [style.css](file:///c:/Users/fumiy/.openclaw/workspace/FunUni-lab/style.css)
- **Theme Shift**: Transitioned from a colorful gradient theme to a strict "Dark Modern" monochrome palette (`#0d0f14` background).
- **Editor Aesthetics**:
    - Added a subtle grid background pattern.
    - Implemented "Syntax Highlighting" utility classes (`.syntax-keyword`, `.syntax-string`, `.syntax-comment`, etc.).
    - Added decorative "Editor Tabs" to cards using pseudo-elements.
    - Added a mock "Line Number" sidebar to article content blocks.
- **Glassmorphism**: Enhanced `backdrop-filter: blur(20px)` and semi-transparent borders for all containers.
- **Typography**: switched headers to `JetBrains Mono` for a coding environment feel.

### [MODIFY] [index.html](file:///c:/Users/fumiy/.openclaw/workspace/FunUni-lab/index.html)
- Updated titles to use "coding" notation (e.g., `FunUni-lab.js`).
- Applied monochrome styling and removed legacy inline gradients.
- Updated the featured post to the latest article.

### [FIX] [2026-04-03-operation-automation.html](file:///c:/Users/fumiy/.openclaw/workspace/FunUni-lab/2026-04-03-operation-automation.html)
- **Syntax Fix**: Added missing `<head>`, `<meta>`, and `<link>` tags.
- **Styling**: Wrapped content in `.article-content` and added syntax highlighting spans to technical terms (`vSphere`, `philosophy`, etc.).
- **Consistency**: Applied the same fixes to the version inside the `it/` directory.

## Re-use Guidelines
- When adding new articles, wrap the main content in `<main class="article-content animate-in">`.
- Use `<span class="syntax-keyword">`, `<span class="syntax-string">`, etc. to highlight technical terms in prose.
- Ensure the character set and viewport meta tags are present for proper rendering.
