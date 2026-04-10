import os
import re

def stabilize_paths():
    # 1. Update Markdown files in categories
    md_pattern = re.compile(r'\(/article\.html\?')
    cat_dirs = ['ai', 'dev', 'finance', 'infra', 'lpo', 'other', 'glossary']
    
    for cat in cat_dirs:
        if not os.path.exists(cat):
            continue
        for file in os.listdir(cat):
            if file.endswith('.md'):
                filepath = os.path.join(cat, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = md_pattern.sub(r'(article.html?', content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated MD: {filepath}")

    # 2. Update index.html
    index_path = 'index.html'
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # In index.html, /article.html should just be article.html
        new_content = content.replace('"/article.html?', '"article.html?')
        
        if new_content != content:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated HTML: {index_path}")

if __name__ == "__main__":
    stabilize_paths()
