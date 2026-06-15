import os

repo = 'c:/Users/user/Desktop/DIMONITE/PORTFolio'

# 1. Remove social arrows
for file in os.listdir(repo):
    if file.endswith('.html'):
        path = os.path.join(repo, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if '<span class=\"arrow\">↗</span>' in content:
            content = content.replace(' <span class=\"arrow\">↗</span>', '')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

# 2. Reduce mobile logo size in CSS
css_path = os.path.join(repo, 'css/style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if '/* Mobile Logo Adjustment */' not in css:
    css = css.replace('@media (max-width: 768px) {', '@media (max-width: 768px) {\n  /* Mobile Logo Adjustment */\n  .logo { font-size: 1.1rem !important; }\n')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 3. Create simple project pages based on a template
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Project | Dimonite Designs</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; backdrop-filter: blur(12px); background: rgba(10,10,10,0.85); border-bottom: 1px solid rgba(255,255,255,0.05); padding: 1.25rem 2rem; display: flex; justify-content: space-between; align-items: center; }
        .cs-hero { min-height: 80vh; display: flex; flex-direction: column; justify-content: flex-end; padding-top: 120px; text-align: center; }
        .cs-hero-title { font-family: var(--font-heading); font-size: clamp(3rem, 8vw, 6rem); margin-bottom: 2rem; color: #fff; }
        .cs-hero-image { width: 100%; max-width: 1000px; margin: 0 auto 4rem; border-radius: 12px; }
        .back-link { display: inline-block; margin-top: 120px; margin-left: 2rem; color: var(--accent-color); font-weight: bold; }
    </style>
</head>
<body>
    <nav>
        <div class="logo">dimonitedesigns<span>.</span></div>
        <div class="nav-links">
            <a href="index.html">Work</a>
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
            <a href="contact.html" class="btn btn-primary">Hire me</a>
        </div>
    </nav>
    <a href="index.html" class="back-link">← Back to Work</a>
    <main class="cs-hero container">
        <h1 class="cs-hero-title">{title}</h1>
        <img src="work/{image}" alt="{title}" class="cs-hero-image">
    </main>
</body>
</html>'''

projects = [
    ('Stryx', 'stryx.html', 'stryx social media designs.png'),
    ('Aurawear', 'aurawear.html', 'aurawear.png'),
    ('Paynex', 'paynex.html', 'paynex.png'),
    ('Goway', 'goway.html', 'goway.png')
]

for title, filename, image in projects:
    with open(os.path.join(repo, filename), 'w', encoding='utf-8') as f:
        f.write(template.format(title=title, image=image))

# 4. Update index.html links
index_path = os.path.join(repo, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

idx = idx.replace('<!-- 03 — STRYX -->\n                <a href="#"', '<!-- 03 — STRYX -->\n                <a href="stryx.html"')
idx = idx.replace('<!-- 04 — AURAAWE -->\n                <a href="#"', '<!-- 04 — AURAAWE -->\n                <a href="aurawear.html"')
idx = idx.replace('<!-- 05 — PAYNEX -->\n                <a href="#"', '<!-- 05 — PAYNEX -->\n                <a href="paynex.html"')
idx = idx.replace('<!-- 06 — GOWAY -->\n                <a href="#"', '<!-- 06 — GOWAY -->\n                <a href="goway.html"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print('Script complete!')
