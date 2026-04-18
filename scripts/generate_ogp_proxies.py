import os
import re
import sys

# Configuration
CONTENT_DIRS = ['infra', 'dev', 'ai', 'finance', 'lpo', 'other']
ROOT_DIR = '.'
TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO & OGP -->
    <title>{title} | FunUni-lab</title>
    <meta name="description" content="{description}" />
    <meta property="og:title" content="{title} | FunUni-lab" />
    <meta property="og:description" content="{description}" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://fununi222.github.io/website/article.html?md={md_path}" />
    <meta property="og:site_name" content="FunUni-lab" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="{title} | FunUni-lab" />
    <meta name="twitter:description" content="{description}" />

    <!-- Redirect to the dynamic viewer -->
    <script>
        window.location.href = 'article.html?md={md_path}';
    </script>
    
    <style>
        body {{ background: #0f172a; color: #a3aac4; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
        .loading {{ text-align: center; }}
        .spinner {{ border: 2px solid rgba(255,255,255,0.1); border-left-color: #aaa4ff; border-radius: 50%; width: 20px; height: 20px; animation: spin 1s linear infinite; margin: 0 auto 10px; }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>
    <div class="loading">
        <div class="spinner"></div>
        <p>Redirecting to Research Log...</p>
    </div>
</body>
</html>
"""

def parse_frontmatter(content):
    match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not match:
        return {}
    
    data = {}
    fm_text = match.group(1)
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip().strip('"').strip("'")
    return data

def main():
    print("Generating OGP Proxy Files...")
    count = 0
    
    for category in CONTENT_DIRS:
        cat_path = os.path.join(ROOT_DIR, category)
        if not os.path.exists(cat_path):
            continue
            
        for filename in os.listdir(cat_path):
            if filename.endswith('.md'):
                md_rel_path = f"{category}/{filename}"
                with open(os.path.join(cat_path, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                metadata = parse_frontmatter(content)
                title = metadata.get('title', 'Technical Archive')
                description = metadata.get('description', 'FunUni-lab Research Log')
                
                # HTML filename (matching the MD basename)
                html_name = filename.replace('.md', '.html')
                html_path = os.path.join(ROOT_DIR, html_name)
                
                # Render template
                output = TEMPLATE.format(
                    title=title,
                    description=description,
                    md_path=md_rel_path
                )
                
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(output)
                
                print(f"  [CREATED] {html_name}")
                count += 1

    print(f"\nDone! Generated {count} proxy files.")

if __name__ == "__main__":
    main()
