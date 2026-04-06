const fs = require('fs');
const marked = require('marked');
const DOMPurify = require('dompurify');
const { JSDOM } = require('jsdom');
const window = new JSDOM('').window;
const purify = DOMPurify(window);

async function test() {
    const mdText = fs.readFileSync('ai/2026-04-06-antigravity-n8n-pipeline.md', 'utf8').replace(/^---\s*([\s\S]*?)\s*---\n?/, '');
    
    marked.setOptions({
        gfm: true,
        breaks: true,
        headerIds: true,
        mangle: false
    });

    const rawHtml = marked.parse(mdText);
    
    const cleanHtml = purify.sanitize(rawHtml, { 
        ADD_TAGS: ['canvas', 'button', 'iframe'], 
        ADD_ATTR: ['target', 'data-dataset', 'data-metric', 'id', 'class', 'style', 'width', 'height', 'onclick'] 
    });

    console.log("CONTAINS CANVAS IN RAW?", rawHtml.includes('<canvas'));
    console.log("CONTAINS CANVAS IN CLEAN?", cleanHtml.includes('<canvas'));
    
    // Extracted
    const match = cleanHtml.match(/<canvas[^>]*><\/canvas>/g);
    console.log("CANVAS TAGS AFTER PURIFY:", match);
}

test();
