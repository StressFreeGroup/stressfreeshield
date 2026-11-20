import os, sys, html, json
sys.path.insert(0, os.path.dirname(__file__))
from items import ITEMS, INDUSTRY_BASE

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'coverage')
os.makedirs(os.path.join(OUT, 'photos'), exist_ok=True)
E = html.escape
SITE = 'https://www.stressfreeshield.com'

SHIELD_SM = '<svg width="24" height="24" viewBox="0 0 48 54" fill="none" aria-hidden="true"><path d="M24 2L4 10V24C4 36.5 12.5 47.2 24 51C35.5 47.2 44 36.5 44 24V10L24 2Z" fill="rgba(55,138,221,.25)" stroke="rgba(55,138,221,.9)" stroke-width="2"/><path d="M15 25.5L21 32L33 20" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def svg(item, cls='ill'):
    return (f'<svg class="{cls}" viewBox="0 0 320 220" role="img" aria-label="Illustration: {E(item["name"])}">'
            f'<rect x="0" y="0" width="320" height="220" rx="14" class="bg"/>{item["ill"]}</svg>')

def head(title, desc, path):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#042C53">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Stress Free Shield">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/coverage/coverage.css">
</head>
<body>
<nav>
  <a class="nav-brand" href="/">{SHIELD_SM}<div><div class="nav-logo">Stress Free Shield</div><span class="nav-sub">Damage Waiver Program</span></div></a>
  <div class="nav-links" id="nav-links">
    <a class="nav-link" href="/#home">Overview</a>
    <a class="nav-link active" href="/#coverage">Coverage</a>
    <a class="nav-link" href="/#claim">File a Claim</a>
    <a class="nav-link" href="/#vendors">Service Network</a>
    <a class="nav-link" href="/#tos">Terms</a>
  </div>
  <div class="nav-right">
    <a class="nav-cta" href="/#claim">File a Claim</a>
    <button class="nav-burger" id="nav-burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="nav-spacer" aria-hidden="true"></div>
'''

FOOT = '''<footer class="site-foot">
  <div>Website built by <a href="https://www.StressFreeGroup.com" target="_blank" rel="noopener">STRESS FREE GROUP</a> (<a href="https://www.StressFreeGroup.com" target="_blank" rel="noopener">www.StressFreeGroup.com</a>)</div>
  <div class="sf-note">Offered with <a href="https://stressfreervs.com/">Stress Free RVs: RV and travel trailer rentals in San Diego</a>.</div>
  <div class="sf-note">Stress Free Shield is not an insurance product.</div>
</footer>
<script>
(function(){var b=document.getElementById('nav-burger'),l=document.getElementById('nav-links');
b.addEventListener('click',function(){var o=!l.classList.contains('open');l.classList.toggle('open',o);b.setAttribute('aria-expanded',String(o));});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){l.classList.remove('open');b.setAttribute('aria-expanded','false');}});
var g=document.getElementById('photos');if(!g)return;var slug=g.getAttribute('data-slug');
fetch('/coverage/photos/manifest.json',{cache:'no-cache'}).then(function(r){return r.ok?r.json():{}}).then(function(m){
 var list=(m&&m[slug])||[];if(!list.length)return;
 g.querySelector('.ph-grid').innerHTML=list.map(function(p){var f=typeof p==='string'?{file:p}:p;
  return '<figure class="ph"><img src="/coverage/photos/'+encodeURIComponent(f.file)+'" alt="'+(f.alt||'Example photo').replace(/"/g,'&quot;')+'" loading="lazy">'+(f.caption?'<figcaption>'+f.caption.replace(/</g,'&lt;')+'</figcaption>':'')+'</figure>';}).join('');
 g.hidden=false;}).catch(function(){});
})();
</script>
</body>
</html>
'''

def li(items):
    return ''.join(f'<li>{E(x)}</li>' for x in items)

pages = []
for i, it in enumerate(ITEMS):
    prev_it = ITEMS[i - 1] if i > 0 else None
    next_it = ITEMS[i + 1] if i < len(ITEMS) - 1 else None
    path = f'/coverage/{it["slug"]}'
    title = f'{it["name"]} — What Stress Free Shield Covers'
    desc = f'{it["short"]} What it is, what the Stress Free Shield damage waiver covers, and how RV and trailer rentals usually handle it.'
    new = '<span class="new-b">NEW</span>' if it.get('new') else ''
    cost = (f'<div class="cost"><div class="cost-lbl">Typical parts cost</div><p>{E(it["cost"])}</p></div>' if it['cost'] else '')
    pn = '<nav class="pn" aria-label="More covered items">'
    pn += (f'<a class="pn-a" href="/coverage/{prev_it["slug"]}"><span class="pn-k">← Previous item</span><span class="pn-n">{E(prev_it["name"])}</span></a>' if prev_it else '<span></span>')
    pn += (f'<a class="pn-a r" href="/coverage/{next_it["slug"]}"><span class="pn-k">Next item →</span><span class="pn-n">{E(next_it["name"])}</span></a>' if next_it else '<span></span>')
    pn += '</nav>'
    body = f'''<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/coverage">Covered items</a><span>/</span><span aria-current="page">{E(it["name"])}</span></nav>
  <div class="eyebrow"><div class="ey-line"></div>Covered item · {E(it["group"])}</div>
  <h1 class="h1">{E(it["name"])}{new}</h1>
  <p class="lead">{E(it["short"])}</p>
  <div class="facts"><span>$250 deductible per occurrence</span><span>Up to $2,500 per coverage duration</span><span>Parked (stationary) only</span></div>

  <section class="intro">
    <figure class="fig">{svg(it)}<figcaption>Diagram: the covered part is shown in blue.</figcaption></figure>
    <div>
      <h2 class="h2">What it is</h2>
      <p class="p">{E(it["what"])}</p>
      {cost}
    </div>
  </section>

  <section class="photos" id="photos" data-slug="{it["slug"]}" hidden>
    <h2 class="h2">Photo examples</h2>
    <div class="ph-grid"></div>
  </section>

  <section class="cov2">
    <div class="box yes"><h2 class="h3">What the Shield covers</h2><ul>{li(it["covered"])}</ul></div>
    <div class="box no"><h2 class="h3">Not covered</h2><ul>{li(it["notcov"])}</ul></div>
  </section>

  <section class="ind">
    <h2 class="h2">How RV and trailer rentals usually handle this</h2>
    <p class="p">{E(INDUSTRY_BASE)}</p>
    <p class="p">{E(it["industry"])}</p>
  </section>

  <div class="tip"><strong>Avoid it:</strong> {E(it["tip"])}</div>

  <div class="actions">
    <a class="btn-pri" href="/#claim">File a Claim</a>
    <a class="btn-sec" href="/coverage">All covered items</a>
    <a class="btn-sec" href="/#coverage">Coverage &amp; exclusions</a>
  </div>
  <p class="fine">Every claim is reviewed against the Stress Free Shield <a href="/#tos">Terms &amp; Conditions</a>, which control if anything on this page differs. Items not expressly listed as covered are excluded. Cost ranges are general estimates, not quotes. Stress Free Shield is not an insurance product.</p>
  {pn}
</main>
'''
    with open(os.path.join(OUT, f'{it["slug"]}.html'), 'w') as f:
        f.write(head(title, desc, path) + body + FOOT)
    pages.append(path)

# Index
cards = ''.join(f'''<a class="card" href="/coverage/{it["slug"]}">{svg(it, 'ill sm')}<div class="card-b"><div class="card-g">{E(it["group"])}</div><div class="card-n">{E(it["name"])}{'<span class="new-b">NEW</span>' if it.get('new') else ''}</div><p class="card-s">{E(it["short"])}</p><span class="card-go">See details →</span></div></a>''' for it in ITEMS)
idx = f'''<main class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><span aria-current="page">Covered items</span></nav>
  <div class="eyebrow"><div class="ey-line"></div>Coverage guide</div>
  <h1 class="h1">What the Stress Free Shield covers</h1>
  <p class="lead">The Shield is an interior accidental damage waiver for RV and trailer rentals: $25 per rental day, capped at $250 per reservation, with a $250 deductible per occurrence and up to $2,500 per coverage duration. Select an item to see exactly which part is meant, what is and is not included, and how rentals usually handle it.</p>
  <div class="grid">{cards}</div>
  <div class="actions" style="margin-top:36px">
    <a class="btn-pri" href="/#claim">File a Claim</a>
    <a class="btn-sec" href="/#coverage">Full coverage &amp; exclusions list</a>
  </div>
  <p class="fine">Items not expressly listed as covered are excluded. The Stress Free Shield <a href="/#tos">Terms &amp; Conditions</a> control. Stress Free Shield is not an insurance product.</p>
</main>
'''
with open(os.path.join(OUT, 'index.html'), 'w') as f:
    f.write(head('Covered Items Guide — Stress Free Shield', 'Every item the Stress Free Shield RV and trailer rental damage waiver covers, with diagrams, definitions, and how rentals usually handle each one.', '/coverage') + idx + FOOT)
pages.append('/coverage')

man = os.path.join(OUT, 'photos', 'manifest.json')
if not os.path.exists(man):
    with open(man, 'w') as f:
        json.dump({it['slug']: [] for it in ITEMS}, f, indent=2)

# sitemap
with open(os.path.join(ROOT, 'sitemap.xml'), 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in ['/'] + pages:
        f.write(f'  <url><loc>{SITE}{p}</loc></url>\n')
    f.write('</urlset>\n')
print(len(pages), 'pages')
