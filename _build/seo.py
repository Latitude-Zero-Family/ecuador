import json, re, html as H

BASE = "https://latitudezerofamily.com"
BRAND = "Latitude Zero"

DESC = {
 "index.html": ("Follow an American-Ecuadorian family moving from Pennsylvania to Ecuador with their baby, then exploring Ecuador and South America together.", "hero"),
 "start-here.html": ("New to Latitude Zero? Meet Austin, Dennisse and Mateo, read the first stories and find the series that fits you.", "mitad"),
 "about.html": ("An American dad, an Ecuadorian mom and their baby son, getting ready to move from Wilkes-Barre, PA to Ecuador.", "cuenca"),
 "the-move.html": ("Our family's move to Ecuador with a baby, told chapter by chapter, from the decision to our first year.", "quito"),
 "dennisse.html": ("Ecuador through the eyes of someone who grew up there: food, family, language and places, in Dennisse's own words.", "otavalo"),
 "ecuador.html": ("A family guide to Ecuador's four regions: the Pacific coast, the Andes, the Amazon and the Galápagos, plus quick facts.", "quilotoa"),
 "top-20.html": ("The 20 places in Ecuador our family plans to visit, from Quito and Quilotoa to the Galápagos, with a map and a vote.", "cotopaxi"),
 "food.html": ("Ecuadorian food region by region: encebollado, hornado, llapingachos, fanesca and more, plus family recipes.", "f_hornado"),
 "coffee-cacao.html": ("A coffeehouse owner's journey to the source of Ecuador's coffee and Nacional cacao, from Loja to the Amazon.", "mindo"),
 "quiz.html": ("Take our 5-question quiz to find which Ecuador region fits your family: the coast, the Andes, the Amazon or the Galápagos.", "quilotoa"),
 "south-america.html": ("Ecuador first, then Colombia, Peru, Chile and Argentina. Our family's planned route through South America.", "chimborazo"),
 "with-a-baby.html": ("What it's like to explore Ecuador with a baby: Mateo's firsts, our family travel rules and baby-friendly places.", "sancristobal"),
 "gear.html": ("Our family packing list for moving to and traveling around Ecuador with a baby, from the flight to the Andes.", "cajas"),
 "checklist.html": ("A free, interactive checklist for moving abroad with a baby: documents, health, packing and the first week.", "guayaquil"),
 "moving-with-kids.html": ("Answers to common questions about moving to Ecuador with kids, from language and altitude to paperwork, from our own experience.", "mitad"),
 "journal.html": ("Stories from our family's move to Ecuador: the move, family life, places to visit, and coffee and cacao.", "cajas"),
 "journal-why-ecuador.html": ("Why an American dad, an Ecuadorian mom and their baby son decided to move from Pennsylvania to Ecuador.", "chimborazo"),
 "videos.html": ("Our YouTube series: the move week by week, the Top 20 with a toddler, and short moments from Ecuador.", "banos"),
 "work-with-us.html": ("Partner with Latitude Zero: family-friendly hotels, tourism boards and travel brands across Ecuador and South America.", "montanita"),
 "media-kit.html": ("Latitude Zero media kit: who we are, who we create for, our formats and how we work with partners.", "guayaquil"),
 "photo-credits.html": ("Credits for the openly licensed photos used on Latitude Zero, with links to each photographer's work.", "ingapirca"),
 "trip-planner.html": ("Build a free day-by-day family itinerary for Ecuador from our Top 20 places, based on your days, kids' ages and interests.", "frailes"),
 "festivals.html": ("Ecuador's festival calendar month by month: Carnaval, Inti Raymi, Mama Negra, Día de los Difuntos, Fiestas de Quito and more.", "f_colada"),
 "reader-stories.html": ("Share your family's Ecuador story. Pitch a reader story about moving to, growing up in or traveling Ecuador with kids.", "otavalo"),
 "passport.html": ("Collect 12 stamps around Latitude Zero and earn your free Ecuador Explorer certificate.", "cotopaxi"),
 "postcard.html": ("Send a free digital postcard from Ecuador. Pick a photo, write a note and share it with someone you love.", "montanita"),
 "community.html": ("Join the Latitude Zero community: name our tortoise, take the free Ecuador with Kids email course and share your photos.", "otavalo"),
 "privacy.html": ("How Latitude Zero handles your information: newsletter signups, analytics, cookies and your choices.", "mitad"),
 "disclosure.html": ("How Latitude Zero works with partners and sponsors, and how we label partnerships and affiliate links.", "mitad"),
 "404.html": ("This page wandered off the map. Find your way back to Latitude Zero.", "hero"),
}

def url_for(fname, es=False):
    if es:
        name = "es.html" if fname == "index.html" else fname.replace(".html", "-es.html")
        return f"{BASE}/{name}"
    return f"{BASE}/" if fname == "index.html" else f"{BASE}/{fname}"

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def schema_for(fname, title, desc, img):
    out = []
    if fname == "index.html":
        out.append({"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": BASE + "/", "inLanguage": ["en", "es"], "description": desc})
        out.append({"@context": "https://schema.org", "@type": "Organization", "name": "Latitude Zero Family", "url": BASE + "/", "logo": BASE + "/icon-512.png", "email": "hola@latitudezerofamily.com"})
    if fname == "journal-why-ecuador.html":
        out.append({"@context": "https://schema.org", "@type": "BlogPosting", "headline": "Why we're moving our family to Ecuador", "description": desc,
                    "image": f"{BASE}/img/{img}.jpg", "datePublished": "2026-10-03", "inLanguage": "en",
                    "author": {"@type": "Person", "name": "Austin Shission"}, "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": BASE + "/icon-512.png"}},
                    "mainEntityOfPage": url_for(fname)})
    if fname == "moving-with-kids.html":
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in FAQ]})
    if fname == "top-20.html":
        out.append({"@context": "https://schema.org", "@type": "ItemList", "name": "20 places we plan to visit in Ecuador", "itemListElement": [
            {"@type": "ListItem", "position": i, "item": {"@type": "TouristAttraction", "name": p[1], "url": f"{url_for(fname)}#place-{i}"}} for i, p in enumerate(PLACES, 1)]})
    return "\n".join(jsonld(o) for o in out)

def seo_head(fname, title):
    desc, img = DESC.get(fname, (DESC["index.html"][0], "hero"))
    d = H.escape(desc, quote=True); t = H.escape(title, quote=True)
    alt = "" if fname == "404.html" else (
        f'<link rel="alternate" hreflang="en" href="{url_for(fname)}">\n'
        f'<link rel="alternate" hreflang="es" href="{url_for(fname, True)}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{url_for(fname)}">\n'
        f'<link rel="canonical" href="{url_for(fname)}">\n')
    robots = '<meta name="robots" content="noindex">\n' if fname == "404.html" else ""
    return (f'<meta name="description" content="{d}">\n{robots}{alt}'
            f'<meta property="og:type" content="{"article" if fname.startswith("journal-") else "website"}">\n'
            f'<meta property="og:site_name" content="{BRAND}">\n'
            f'<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n'
            f'<meta property="og:url" content="{url_for(fname)}">\n'
            f'<meta property="og:image" content="{BASE}/img/{img}.jpg">\n'
            f'<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="es_EC">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n'
            f'<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<meta name="theme-color" content="#0f3b3a">\n'
            + schema_for(fname, title, desc, img))

def responsive_imgs(html):
    """Smaller files for phones: every img/x.jpg gets an 800px option and async decoding."""
    def rep(m):
        name = m.group(1)
        return f'<img src="img/{name}.jpg" srcset="img/{name}-800.jpg 800w, img/{name}.jpg 1400w" sizes="(max-width: 820px) 100vw, 50vw" decoding="async"'
    return re.sub(r'<img src="img/([\w-]+?)(?<!-800)\.jpg"', rep, html)

def sitemap(files):
    rows = []
    for f in files:
        for es in (False, True):
            rows.append(f'''  <url><loc>{url_for(f, es)}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{url_for(f)}"/>
    <xhtml:link rel="alternate" hreflang="es" href="{url_for(f, True)}"/>
  </url>''')
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
