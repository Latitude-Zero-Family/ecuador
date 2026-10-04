import re

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Figtree:wght@400;500;600;700&family=DM+Mono:wght@400;500&family=Caveat:wght@600;700&display=swap">
<link rel="stylesheet" href="styles.css">'''

LOGO = '''<svg class="logo" viewBox="0 0 48 48" aria-hidden="true" focusable="false">
  <circle cx="24" cy="24" r="21" fill="none" stroke="currentColor" stroke-width="2.2"/>
  <circle cx="15" cy="16" r="3" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M10 30 Q10 21.5 15 21.5 Q20 21.5 20 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <circle cx="32.5" cy="17.5" r="2.7" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M28 30 Q28 22.5 32.5 22.5 Q37 22.5 37 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <circle cx="24" cy="23.4" r="1.8" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <path d="M21.6 30 Q21.6 26.6 24 26.6 Q26.4 26.6 26.4 30" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="0.5" y1="30.5" x2="47.5" y2="30.5" stroke="var(--sun)" stroke-width="2.4" stroke-linecap="round"/>
</svg>'''

MENU = [
  ("Our story", [("start-here.html","Start here","New here? Begin with this","start"),("about.html","About us","Austin, Dennisse and Mateo","about"),("the-move.html","The move","Our relocation, chapter by chapter","move"),("dennisse.html","Dennisse's Ecuador","Her column, in her words","dennisse")]),
  ("Ecuador", [("ecuador.html","Ecuador guide","The four regions and quick facts","ecuador"),("top-20.html","Top 20 places","Our Ecuador bucket list","top20"),("food.html","Food & recipes","What to eat, region by region","food"),("coffee-cacao.html","Coffee & cacao","From farm to cup","coffee"),("quiz.html","Region quiz","Which region fits your family?","quiz"),("festivals.html","Festival calendar","Celebrations, month by month","festivals"),("south-america.html","Beyond Ecuador","Our South America route","sa")]),
  ("Family travel", [("trip-planner.html","Trip planner","Build a day-by-day family plan","planner"),("with-a-baby.html","Traveling with a baby","Exploring Ecuador with Mateo","baby"),("gear.html","What we're packing","Our family packing list","gear"),("checklist.html","Moving checklist","Free: moving abroad with a baby","checklist"),("moving-with-kids.html","Moving with kids FAQ","Your questions, our answers","faq")]),
  ("Stories", [("journal.html","Journal","Every story we publish","journal"),("videos.html","Videos","Our YouTube series","videos"),("reader-stories.html","Reader stories","Share your family's story","stories"),("community.html","Community","Contests, photos and more","community"),("postcard.html","Send a postcard","Free postcards from the equator","postcard")]),
  ("Work with us", [("work-with-us.html","Partnerships","Ways to collaborate","work"),("media-kit.html","Media kit","For brands and media","kit")]),
]

POSTS = [
  ("journal-why-ecuador.html", "art-1", "PA → EC", "The move", "Why we're moving our family to Ecuador", "The decision, the doubts and what finally made us say yes.", "move"),
  ("the-move.html", "art-5", "CHECKLIST", "The move", "Moving abroad with a baby: what we packed and what we left behind", "Car seats, documents, favorite toys and the things that didn't make the cut.", "move"),
  ("the-move.html", "art-7", "0° 00′", "The move", "Our first week in Ecuador", "Jet lag, altitude, abuela's kitchen and Mateo's first look at the Andes.", "move"),
  ("dennisse.html", "art-3", "OTAVALO", "Family", "Marrying into an Ecuadorian family", "Sunday almuerzos, abuela's rules and learning the difference between ají and salsa.", "family"),
  ("with-a-baby.html", "art-6", "HOLA · HI", "Family", "Raising Mateo bilingual", "His first words in two languages, and how we're making Spanish part of every day.", "family"),
  ("dennisse.html", "art-8", "HER ECUADOR", "Family", "Dennisse's Ecuador: the places she grew up loving", "The streets, foods and views that made her who she is, seen through her eyes.", "family"),
  ("top-20.html", "art-2", "MINDO", "Places", "Cloud forest weekends near Quito", "Hummingbirds, waterfalls and stroller-friendly trails.", "places"),
  ("top-20.html", "art-4", "GALÁPAGOS", "Places", "Planning the Galápagos with a toddler", "Islands, boats and naps. How we're making it work.", "places"),
  ("coffee-cacao.html", "art-9", "CAFÉ · CACAO", "Coffee & cacao", "From farm to cup: Ecuador's coffee and cacao", "A coffeehouse owner goes to the source, from highland coffee farms to Amazon cacao.", "coffee"),
]

ART_IMG = {"art-7":("mitad","The Mitad del Mundo monument on the equator"),"art-8":("quilotoa","The Quilotoa crater lake"),"art-9":("tena","The Napo River near Tena, in cacao country"),"art-1":("quito","Plaza Grande in Quito's historic center"),"art-5":("guayaquil","The Malecón 2000 boardwalk in Guayaquil"),
  "art-3":("otavalo","The Saturday market in Otavalo"),"art-6":("cuenca","Rooftops and cathedral domes in Cuenca"),
  "art-2":("mindo","An orchid in the Mindo cloud forest"),"art-4":("sancristobal","A sea lion on San Cristóbal, Galápagos")}

def post_card(p, live=False):
    href, art, stamp, cat, title, desc, group = p
    status = "Read now" if href.startswith("journal-") else "Coming soon"
    return f'''<a class="post" href="{href}" data-group="{group}">
  <div class="post-art"><img src="img/{ART_IMG[art][0]}.jpg" alt="{ART_IMG[art][1]}" loading="lazy"><span class="stamp">{stamp}</span></div>
  <div class="post-body"><div class="meta"><span class="pill">{cat}</span><span>{status}</span></div><h3>{title}</h3><p>{desc}</p></div>
</a>'''

ICON = {
 "home":'<path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v9.5h13V10"/><path d="M10 19.5v-5h4v5"/>',
 "start":'<path d="M6 21V4"/><path d="M6 4h11l-2.5 4L17 12H6"/>',
 "about":'<circle cx="7" cy="7.5" r="2.3"/><circle cx="17" cy="7.5" r="2.3"/><circle cx="12" cy="11" r="1.7"/><path d="M3 19c0-3.3 1.8-6 4-6s4 2.7 4 6"/><path d="M13 19c0-3.3 1.8-6 4-6s4 2.7 4 6"/>',
 "move":'<path d="M2.5 13.5 21 6.5l-4.5 13-3.6-5.4z"/><path d="M12.9 14.1 21 6.5"/>',
 "dennisse":'<path d="M12 20s-7.5-4.6-8.8-9.3C2.4 7.6 4.4 5 7.2 5c2 0 3.4 1.2 4.8 3 1.4-1.8 2.8-3 4.8-3 2.8 0 4.8 2.6 4 5.7C19.5 15.4 12 20 12 20z"/>',
 "ecuador":'<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
 "top20":'<path d="m12 3 2.7 5.6 6.1.8-4.5 4.3 1.1 6.1L12 17l-5.4 2.8 1.1-6.1-4.5-4.3 6.1-.8z"/>',
 "food":'<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M8 7c0-1.5 1-1.5 1-3M12 7c0-1.5 1-1.5 1-3M16 7c0-1.5 1-1.5 1-3"/>',
 "coffee":'<path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M17 10.5h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3.5c0 1.5 1 1.5 1 3M12 3.5c0 1.5 1 1.5 1 3"/>',
 "quiz":'<circle cx="12" cy="12" r="9"/><path d="M9.6 9.3a2.5 2.5 0 1 1 3.4 2.4c-.7.3-1 .8-1 1.5v.6"/><circle cx="12" cy="17" r=".6" fill="currentColor"/>',
 "festivals":'<path d="M4 20 9 7l8 8z"/><path d="M14 4.5c.5 1 1.5 1.3 2.5 1M18.5 9c1-.3 2 .2 2.5 1M15.5 2.5l.5.5M20 5.5l.6-.4"/>',
 "sa":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.8 2.6 4 5.6 4 9s-1.2 6.4-4 9c-2.8-2.6-4-5.6-4-9s1.2-6.4 4-9z"/>',
 "planner":'<path d="m3 6.5 6-2.5 6 2.5 6-2.5v13.5l-6 2.5-6-2.5-6 2.5z"/><path d="M9 4v13.5M15 6.5V20"/>',
 "baby":'<path d="M4 6h3l2 8h9.5a5 5 0 0 0-5-5H9"/><circle cx="9.5" cy="18.5" r="1.8"/><circle cx="17" cy="18.5" r="1.8"/>',
 "gear":'<rect x="3.5" y="7" width="17" height="12.5" rx="2.5"/><path d="M9 7V5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5v2M3.5 12.5h17"/>',
 "checklist":'<rect x="4" y="3.5" width="16" height="17" rx="2.5"/><path d="m8 9 1.5 1.5L12 8M8 15l1.5 1.5L12 14M14.5 9.5H17M14.5 15.5H17"/>',
 "faq":'<path d="M4 5h11v8H9l-3.5 3v-3H4z"/><path d="M15 9h5v8h-1.5v3L15 17h-5v-1.5"/>',
 "journal":'<path d="M12 6.5C10 5 7 4.5 3.5 5v13.5c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5z"/><path d="M12 6.5V20"/>',
 "videos":'<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m10 9 5 3-5 3z"/>',
 "stories":'<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
 "community":'<circle cx="12" cy="8" r="3"/><path d="M6 20c0-3.5 2.7-6 6-6s6 2.5 6 6"/><circle cx="4.8" cy="10" r="1.8"/><circle cx="19.2" cy="10" r="1.8"/>',
 "postcard":'<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
 "passport":'<rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="10.5" r="3"/><path d="M9 16.5h6"/>',
 "work":'<path d="m3 12 4-4 3 2 4-3 7 5-3 3"/><path d="m7 8 7 7c.6.6 1.6.6 2.1 0s.6-1.5 0-2.1M10.5 14.5l2 2c.6.6 1.6.6 2.1 0M8.5 16.5l1 1c.6.6 1.5.6 2 0"/>',
 "kit":'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
}
def icon(k):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICON.get(k, ICON["start"])}</svg>'

MEGA = {
 "Our story": ("Meet the family", "An American dad, an Ecuadorian mom and a baby boy, packing up for the equator.", "cuenca", "Our first story", "Why we're moving our family to Ecuador", "journal-why-ecuador.html", "Read it"),
 "Ecuador": ("Four worlds, one country", "Volcanoes, beaches, rainforest and the Galápagos. Plus all the food.", "quilotoa", "Two-minute quiz", "Which Ecuador region fits your family?", "quiz.html", "Take the quiz"),
 "Family travel": ("Little legs, big trips", "Plans, packing lists and honest notes on exploring with a baby.", "frailes", "Free planner", "Build a day-by-day family trip", "trip-planner.html", "Start planning"),
 "Stories": ("Pull up a chair", "Our journal, our videos and plenty of fun ways to join in.", "montanita", "Free, from 0°", "Send a postcard from the equator", "postcard.html", "Make a postcard"),
 "Work with us": ("Let's make something", "For hotels, tourism boards and family brands that travel like we do.", "guayaquil", "For partners", "See who we create for", "media-kit.html", "Open the media kit"),
}
TINTS = ["sun", "moss", "sky", "coral"]

def nav(active):
    groups = [f'<li class="home-li"><a class="home-link" href="./"{" aria-current=\"page\"" if active == "home" else ""}>{icon("home")}<span>Home</span></a></li>']
    for gi, (label, links) in enumerate(MENU):
        cur = any(k == active for *_, k in links)
        subs = "".join(f'<li style="--i:{i}"><a href="{h}"{" aria-current=\"page\"" if k == active else ""}><i class="mm-ic t-{TINTS[(i + gi) % 4]}">{icon(k)}</i><b>{t}<span>{d}</span></b></a></li>' for i, (h, t, d, k) in enumerate(links))
        it, idesc, img, ftag, ftitle, fhref, fcta = MEGA[label]
        groups.append(f'''<li class="grp{" current" if cur else ""}"><button class="grp-btn" type="button" aria-expanded="false" aria-controls="sub-{gi}">{label}</button><div class="sub mega" id="sub-{gi}"><div class="mega-in">
<div class="mega-intro" aria-hidden="true"><span class="mega-num">0{gi + 1} / 0{len(MENU)}</span><b class="mega-title">{it}</b><p>{idesc}</p><span class="mega-doodle d{gi}"></span></div>
<ul class="mega-links{" two" if len(links) > 4 else ""}">{subs}</ul>
<a class="mega-feat" href="{fhref}"><span class="mega-ph"><img src="img/{img}-800.jpg" alt="" loading="lazy"></span><span class="mega-tag">{ftag}</span><b>{ftitle}</b><span class="mega-cta">{fcta} →</span></a>
</div></div></li>''')
    return f'''<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="brand" href="./">{LOGO}<span>Latitude Zero</span></a>
    <ul class="menu" id="site-menu">{"".join(groups)}</ul>
    <div class="lang" role="group" aria-label="Language"><a href="#" aria-current="true" lang="en">EN</a><a href="__ES__" lang="es" hreflang="es">ES</a></div>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-menu"><span class="bars" aria-hidden="true"></span><span class="menu-label">Menu</span></button>
  </div>
</nav>'''

FOOT_COLS = "\n".join(f'<nav class="foot-col" aria-label="{label}"><h3>{label}</h3>' + "".join(f'<a href="{h}">{t}</a>' for h, t, d, k in links) + "</nav>" for label, links in MENU)
FOOTER = f'''<section class="news-band" id="newsletter">
  <div class="wrap">
    <div class="news-copy">
      <span class="eyebrow">The newsletter</span>
      <h2>Letters from latitude zero</h2>
      <p>One email when a new chapter of the move goes up. Real stories from our family, in English and Spanish. New here? Grab our free <a href="checklist.html" style="color:var(--sun);font-weight:600">moving-with-a-baby checklist</a>.</p>
    </div>
    <form class="news-form" novalidate>
      <label for="news-email" class="sr">Email address</label>
      <input id="news-email" type="email" placeholder="you@email.com" autocomplete="email" required>
      <button class="btn btn-sun" type="submit">Join the list</button>
      <p class="news-msg" role="status" hidden>Thanks! Signups open with our first letter. Until then, follow us on Instagram at @latitudezerofamily.</p>
    </form>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <a class="brand" href="./">{LOGO}<span>Latitude Zero</span></a>
        <p>An American dad, an Ecuadorian mom and their baby boy, getting ready to move from Wilkes-Barre to Ecuador, and documenting the journey.</p>
        <p class="mono">0° 00′ 00″ LAT · 78° 27′ W</p>
      </div>
      <div class="foot-connect">
        <h3>Say hola</h3>
        <code class="foot-email">hola@latitudezerofamily.com</code>
        <div class="foot-social"><span>Instagram</span><span>YouTube</span><span>TikTok</span><code>@latitudezerofamily</code></div>
        <a class="btn btn-sun foot-news" href="#newsletter">Join the newsletter</a>
      </div>
    </div>
    <div class="foot-grid">
      {FOOT_COLS}
    </div>
    <div class="foot-bottom">
      <span>© 2026 Latitude Zero · Austin, Dennisse &amp; Mateo · From Wilkes-Barre, PA to the middle of the world</span>
      <nav class="foot-legal" aria-label="Legal">
        <a href="photo-credits.html">Photo credits</a>
        <a href="privacy.html">Privacy</a>
        <a href="disclosure.html">Disclosure</a>
        <button type="button" class="cookie-link" hidden>Cookie settings</button>
        <a href="#" class="to-top">Back to top ↑</a>
      </nav>
    </div>
  </div>
</footer>
<div hidden id="lz-str"><span data-k="passport_label">Explorer passport</span><span data-k="new_stamp">New stamp:</span><span data-k="see_passport">See your passport</span><span data-k="explorer">Explorer</span><span data-k="cert_title">Certified Ecuador Explorer</span><span data-k="cert_awarded">This passport belongs to</span><span data-k="cert_line">for collecting all 12 stamps on latitudezerofamily.com</span><span data-k="votes">votes</span><span data-k="copied">Copied</span><span data-k="pc_share">A postcard from Ecuador</span><span data-k="s_story">Story reader</span><span data-k="s_quiz">Region quiz</span><span data-k="s_planner">Trip planner</span><span data-k="s_plate">Full plate</span><span data-k="s_pack">Packed and ready</span><span data-k="s_flash">Slang student</span><span data-k="s_vote">First vote</span><span data-k="s_checklist">Getting ready</span><span data-k="s_postcard">Postcard sender</span><span data-k="s_festival">Fiesta fan</span><span data-k="s_guide">Four regions</span><span data-k="s_spanish">¡Hola!</span></div>'''

MENU_JS = '''<script>
(function(){var c=document.querySelector('.countdown');if(!c||!c.dataset.date)return;var d=new Date(c.dataset.date+'T12:00:00'),n=Math.ceil((d-new Date())/864e5);
if(isNaN(n))return;var big=document.getElementById('cd-big');big.textContent=n>1?n+' days to go':n===1?'1 day to go':'We made it!';})();
</script>
<script>
(function(){try{if('scrollRestoration' in history)history.scrollRestoration='manual'}catch(e){}
function go(){var h=location.hash&&location.hash.length>1?document.getElementById(location.hash.slice(1)):null;if(h){h.scrollIntoView()}else{window.scrollTo(0,0)}}
go();window.addEventListener('load',go);window.addEventListener('pageshow',go);})();
</script>
<script>
(function(){var f=document.querySelector('.news-form');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();var i=f.querySelector('input');if(!i.checkValidity()){i.focus();i.reportValidity&&i.reportValidity();return}f.querySelector('.news-msg').hidden=false;});})();
</script>
<script>
(function(){var nav=document.querySelector('.nav'),b=document.querySelector('.menu-btn');if(!nav)return;
var groups=[].slice.call(document.querySelectorAll('.grp'));
function closeAll(ex){if(!ex)nav.classList.remove('mm-swap');groups.forEach(function(g){if(g!==ex){g.classList.remove('open');g.querySelector('.grp-btn').setAttribute('aria-expanded','false')}})}
var DESK='(hover:hover) and (min-width:1101px)',tmr=null;function desk(){return window.matchMedia(DESK).matches}
function openG(g){clearTimeout(tmr);var was=nav.querySelector('.grp.open');if(was&&was!==g)nav.classList.add('mm-swap');closeAll(g);g.classList.add('open');g.querySelector('.grp-btn').setAttribute('aria-expanded','true')}
groups.forEach(function(g){var btn=g.querySelector('.grp-btn');
  btn.addEventListener('click',function(e){e.stopPropagation();if(desk()){if(g.classList.contains('open')&&e.detail===0){closeAll(null)}else openG(g);return}var o=g.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false');closeAll(g)});
  g.addEventListener('mouseenter',function(){if(desk()){clearTimeout(tmr);tmr=setTimeout(function(){openG(g)},nav.querySelector('.grp.open')?0:70)}});
  g.addEventListener('mouseleave',function(){if(desk()){clearTimeout(tmr);tmr=setTimeout(function(){closeAll(null)},220)}});
});
document.addEventListener('click',function(e){if(!nav.contains(e.target))closeAll(null)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeAll(null);nav.classList.remove('open');b&&b.setAttribute('aria-expanded','false')}});
if(b)b.addEventListener('click',function(){var o=nav.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');document.documentElement.style.overflow=o?'hidden':'';if(o)nav.scrollTop=0});
nav.querySelectorAll('.sub a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');document.documentElement.style.overflow='';b&&b.setAttribute('aria-expanded','false')})});
})();
</script>'''

PAGES_BUILT = []
exec(open('seo.py').read())

def page(fname, title, active, body, index=False, script=""):
    head = f"<title>{title}</title>\n{seo_head(fname, title)}\n{FONTS}"
    if not index:
        head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + head + '\n<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>')
    tail = "" if index else "\n</body>\n</html>"
    head += f'\n<meta name="lz-page" content="{fname[:-5]}">'
    head += '\n<script src="config.js"></script>'
    html = f"{head}\n{nav(active)}\n{body}\n{FOOTER}\n{MENU_JS}\n{script}\n<script src=\"site.js\" defer></script><script src=\"play.js\" defer></script><script src=\"doodles.js\" defer></script><script src=\"interact.js\" defer></script><script src=\"engage.js\" defer></script>{tail}\n"
    esname = "es.html" if fname == "index.html" else fname.replace(".html", "-es.html")
    html = html.replace('href="__ES__"', f'href="{esname}"')
    html = responsive_imgs(html)
    if fname == "404.html":
        html = re.sub(r'(href|src)="(?!https?:|#|/|mailto)([^"]*)"', lambda m: f'{m.group(1)}="/{"" if m.group(2) == "./" else m.group(2)}"', html)
        html = html.replace('srcset="img/', 'srcset="/img/').replace('url(img/', 'url(/img/')
    PAGES_BUILT.append(fname)
    open(fname, "w").write(html)

HERO_PHOTO = {"About us":"cuenca","Ecuador guide":"quilotoa","The journal":"cajas","Our Ecuador bucket list":"cotopaxi","Beyond Ecuador":"chimborazo","Partnerships":"montanita","Photo credits":"ingapirca"}
POLA_CAP = {"quilotoa":"Quilotoa!","santacruz":"Galápagos pals","f_bolon":"Bolón for breakfast","cotopaxi":"Hola, Cotopaxi","mindo":"Mindo orchids","otavalo":"Market day","cuenca":"Cuenca rooftops","montanita":"Sunset surf","mitad":"Standing on 0°","banos":"Waterfall chasing","frailes":"Beach day!","sancristobal":"Sea lion nap","f_hornado":"Hornado!","f_colada":"Colada morada","chimborazo":"Hello, Chimborazo","cajas":"Lakes of El Cajas","quito":"Quito, hola","ingapirca":"Ingapirca","tena":"Napo River","f_encebollado":"Encebollado time","f_llapingachos":"Llapingachos!","isla":"Isla de la Plata"}
POLA_POOL = ["santacruz","f_bolon","mindo","quilotoa","sancristobal","f_llapingachos","banos","frailes","cotopaxi","f_encebollado","mitad","isla","otavalo","cuenca"]
POLA_ROT = [-6, 5, -4, 7, -3, 6]
def hero(eyebrow, h1, lede):
    ph = HERO_PHOTO.get(eyebrow)
    style = f' style="--photo:url(img/{ph}.jpg)"' if ph else ""
    h = sum(map(ord, eyebrow))
    pool = [p for p in POLA_POOL if p != ph]
    pp = pool[h % len(pool)]
    pola = f'<figure class="ph-pola" aria-hidden="true" style="--r:{POLA_ROT[h % 6]}deg"><img src="img/{pp}-800.jpg" alt=""><figcaption>{POLA_CAP[pp]}</figcaption></figure>'
    return f'''<header class="page-hero has-photo has-pola"{style}><div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p>{lede}</p>
  {pola}
</div></header>'''

# ---------- HOME ----------
MOVE_DATE = ""  # set to "YYYY-MM-DD" to start the countdown
STICKERS = [("the-move.html", "thinking about moving abroad", "sun", -4), ("with-a-baby.html", "traveling with little ones", "moss", 3), ("food.html", "hungry for Ecuadorian food", "coral", -2), ("trip-planner.html", "planning a family trip", "sky", 4), ("top-20.html", "dreaming about volcanoes", "cream", -3), ("es.html", "¡aquí por el español!", "deep", 2)]
BADGES = [("quiz.html", "quiz", "Region quiz", "5 questions"), ("top-20.html", "top20", "Vote on our Top 20", "Where first?"), ("trip-planner.html", "planner", "Trip planner", "Day by day"), ("festivals.html", "festivals", "Fiesta calendar", "Month by month"), ("postcard.html", "postcard", "Send a postcard", "Free, from 0°"), ("food.html", "food", "Build a plate", "Ecuadorian food")]
ROUTE = [("Ecuador", "Our future home base", "First", 8, 70), ("Colombia", "Cartagena, coffee country, Medellín", "Then", 36, 30), ("Peru", "Lima, Cusco, the Sacred Valley", "Planned", 64, 66), ("Chile & Argentina", "Patagonia, Mendoza, Buenos Aires", "Someday", 92, 28)]
home = f'''<header class="hero hm-hero" id="top">
  <div class="wrap">
    <div class="hm-hero-copy">
      <div class="coords"><span>0° 00′ 00″ LAT</span><span>78° 27′ W</span><span>ECUADOR</span></div>
      <h1>An American-Ecuadorian family moves to the <em>middle of the world.</em></h1>
      <p class="lede">We're Austin, Dennisse and baby Mateo, relocating from Pennsylvania to Ecuador. Follow the whole move as it happens, then come exploring the Andes, the coast, the Amazon and South America with us.</p>
      <div class="hero-cta">
        <a class="btn btn-sun" href="start-here.html">Start here</a>
        <a class="btn btn-ghost" href="the-move.html">Follow the move</a>
      </div>
    </div>
    <div class="hm-polas" aria-label="Places on our list">
      <figure class="hm-pola" style="--r:-7deg;--x:0%;--y:3%;--d:0s"><img src="img/quilotoa-800.jpg" alt="The Quilotoa crater lake"><figcaption>Quilotoa!</figcaption></figure>
      <figure class="hm-pola" style="--r:6deg;--x:54%;--y:0%;--d:-2s"><img src="img/santacruz-800.jpg" alt="A giant tortoise on Santa Cruz, Galápagos"><figcaption>Galápagos pals</figcaption></figure>
      <figure class="hm-pola" style="--r:-3deg;--x:22%;--y:55%;--d:-4s"><img src="img/f_bolon-800.jpg" alt="A bolón de verde, a fried green plantain ball"><figcaption>Bolón for breakfast</figcaption></figure>
      <span class="hm-note" aria-hidden="true">Tap a photo!</span>
    </div>
  </div>
  <svg class="ridge" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">
    <path d="M0 200 L0 150 L120 120 L210 140 L330 70 L380 95 L470 40 L520 20 L570 42 L650 105 L760 85 L860 120 L960 60 L1040 95 L1120 80 L1200 110 L1200 200 Z" fill="var(--moss)" opacity=".45"/>
    <path d="M490 40 L520 20 L552 38 L535 34 L520 42 L505 34 Z" fill="var(--deep-ink)" opacity=".9"/>
    <path d="M0 200 L0 170 L160 150 L300 165 L420 135 L560 160 L700 140 L840 160 L980 135 L1100 155 L1200 145 L1200 200 Z" fill="var(--bg)"/>
  </svg>
  <div class="equator" aria-hidden="true"><span>EQUATOR · 0°</span><i class="sun-dot"></i></div>
</header>
<div class="marquee" aria-hidden="true"><div class="marquee-track">{"".join(f"<span>{p}</span>" for p in ["Quito","Mitad del Mundo","Cotopaxi","Quilotoa","Otavalo","Cuenca","Baños","Chimborazo","Mindo","Ingapirca","El Cajas","Guayaquil","Montañita","Puerto López","Los Frailes","Tena","Cuyabeno","Yasuní","Santa Cruz","San Cristóbal"]*2)}</div></div>
<main class="hm">
  <section class="hm-pick">
    <div class="wrap">
      <p class="hm-pick-q">I'm here because I'm…</p>
      <svg class="hm-arrow" viewBox="0 0 120 70" aria-hidden="true"><path d="M6 10 C 40 4, 80 18, 96 52"/><path d="M84 46 L97 55 L101 39"/></svg>
      <div class="hm-stickers">{"".join(f'<a class="hm-sticker s-{c}" href="{h}" style="--r:{r}deg">{t}</a>' for h, t, c, r in STICKERS)}</div>
    </div>
  </section>
  <section class="hm-board">
    <div class="wrap hm-board-grid">
      <div class="hm-pass countdown" data-date="{MOVE_DATE}">
        <div class="hm-pass-main">
          <span class="hm-pass-air">LATITUDE ZERO AIR · BOARDING PASS</span>
          <div class="hm-pass-route"><b>AVP</b><span class="hm-pass-line" aria-hidden="true"><i></i></span><b>UIO</b></div>
          <div class="hm-pass-cities"><span>Wilkes-Barre</span><span>Quito</span></div>
          <dl class="hm-pass-info">
            <div><dt>Passengers</dt><dd>2 adults + 1 baby</dd></div>
            <div><dt>Gate</dt><dd>0°</dd></div>
            <div><dt>Status</dt><dd class="hm-blink">Packing up</dd></div>
          </dl>
        </div>
        <div class="hm-pass-stub">
          <span class="eyebrow">Moving day</span>
          <p class="cd-big" id="cd-big">Date coming soon</p>
          <p class="cd-sub">Still in Wilkes-Barre, packing up.</p>
          <a class="go" href="the-move.html">Follow the move →</a>
        </div>
      </div>
      <div class="hm-sticky word flip" role="button" tabindex="0" aria-pressed="false">
        <div class="flip-inner">
          <div class="flip-face">
            <span class="hm-hand">Word of the week</span>
            <p class="word-big">¡Achachay!</p>
            <p class="word-say">ah-chah-CHAI</p>
            <p class="flip-hint">Tap to see what it means ↻</p>
          </div>
          <div class="flip-face flip-back">
            <span class="hm-hand">It means</span>
            <p class="word-mean">"Brrr, it's cold!"</p>
            <p>An Ecuadorian exclamation from Kichwa. Dennisse says it every chilly Andes morning. Austin is still practicing.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="hm-play">
    <div class="wrap">
      <div class="hm-head"><span class="hm-hand">Go on, click something</span><h2>Things to play with</h2></div>
      <div class="hm-badges">{"".join(f'<a class="hm-badge t-{TINTS[i % 4]}" href="{h}" style="--r:{(-1) ** i * (3 + i % 3 * 2)}deg"><i>{icon(k)}</i><b>{t}</b><span>{d}</span></a>' for i, (h, k, t, d) in enumerate(BADGES))}</div>
    </div>
  </section>
  <section class="hm-now">
    <div class="wrap">
      <div class="hm-head"><span class="hm-hand">Where we are now</span><h2>Somewhere between here and there</h2></div>
      <div class="hm-trip">
        <svg class="hm-trip-svg" viewBox="0 0 1000 220" preserveAspectRatio="none" aria-hidden="true"><path class="hm-trip-path" d="M40 60 C 260 -10, 380 200, 560 140 S 860 40, 960 170"/></svg>
        <div class="hm-pin hm-pin-a"><span class="hm-dot now"></span><b id="now-place">Wilkes-Barre, Pennsylvania</b><span class="hm-bubble">We're here!</span></div>
        <div class="hm-pin hm-pin-b"><span class="hm-dot"></span><b>Ecuador · 0°</b><span>Next stop</span></div>
        <svg class="hm-trip-plane" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 2 L19 13 L30 18 L30 21 L19 18 L18 26 L22 29 L22 31 L16 29.5 L10 31 L10 29 L14 26 L13 18 L2 21 L2 18 L13 13 Z" fill="currentColor"/></svg>
      </div>
      <div class="hm-log">
        <span class="hm-log-title">The prep log</span>
        <ol><li><time>October 2026</time><p>It's official: we're moving our family to Ecuador.</p></li><li><time>October 2026</time><p>Latitude Zero is born. This is where we'll share all of it.</p></li><li class="hm-log-next"><time>Coming up</time><p>Packing up Wilkes-Barre. Stay tuned.</p></li></ol>
        <a class="link-more" href="the-move.html">Follow the whole move →</a>
      </div>
    </div>
  </section>
  <section class="hm-who">
    <div class="wrap hm-who-grid">
      <div>
        <span class="hm-hand">Who we are</span>
        <h2>Going home, for one of us. Starting over, for the rest.</h2>
        <p>Dennisse grew up in Ecuador. Austin built businesses in Wilkes-Barre, PA. When Mateo arrived, we asked where we wanted him to grow up, and the answer was Ecuador.</p>
        <a class="link-more" href="about.html">Read our story →</a>
      </div>
      <div class="hm-fam" aria-label="The family">
        <div class="hm-face f-a" style="--r:-6deg"><span class="hm-face-i" aria-hidden="true">A</span><b>Austin</b><span>Operator, builder, coffee person.</span></div>
        <div class="hm-face f-d" style="--r:5deg"><span class="hm-face-i" aria-hidden="true">D</span><b>Dennisse</b><span>Ecuadorian by birth. Our guide.</span></div>
        <div class="hm-face f-m" style="--r:-2deg"><span class="hm-face-i" aria-hidden="true">M</span><b>Mateo</b><span>The youngest member of the expedition.</span></div>
      </div>
    </div>
  </section>
  <section class="hm-regions">
    <div class="wrap">
      <div class="hm-head"><span class="hm-hand">Four worlds, one country</span><h2>Ecuador's four regions</h2></div>
      <div class="hm-arches">
        <a class="hm-arch" href="ecuador.html#costa"><span class="hm-arch-img"><img src="img/frailes-800.jpg" alt="Los Frailes beach" loading="lazy"></span><span class="alt">Pacific coast</span><b>La Costa</b><span>Pacific beaches, ceviche and cacao country.</span></a>
        <a class="hm-arch" href="ecuador.html#sierra"><span class="hm-arch-img"><img src="img/cotopaxi-800.jpg" alt="Cotopaxi volcano" loading="lazy"></span><span class="alt">The Andes</span><b>La Sierra</b><span>Quito, Cuenca and the volcanoes of the Andes.</span></a>
        <a class="hm-arch" href="ecuador.html#amazonia"><span class="hm-arch-img"><img src="img/tena-800.jpg" alt="The Napo River near Tena" loading="lazy"></span><span class="alt">Amazon rainforest</span><b>Amazonía</b><span>Rainforest, river towns and waterfalls.</span></a>
        <a class="hm-arch" href="ecuador.html#galapagos"><span class="hm-arch-img"><img src="img/santacruz-800.jpg" alt="A giant tortoise on Santa Cruz" loading="lazy"></span><span class="alt">Islands</span><b>Galápagos</b><span>Tortoises, sea lions and blue-footed boobies.</span></a>
      </div>
      <div class="hm-links"><a class="link-more" href="ecuador.html">Explore the Ecuador guide →</a><a class="link-more" href="top-20.html">Our top 20 places to visit →</a></div>
    </div>
  </section>
  <section class="hm-journal">
    <div class="wrap">
      <div class="hm-head"><span class="hm-hand">The journal</span><h2>Latest dispatches</h2></div>
      <div class="posts hm-posts">{"".join(post_card(POSTS[i]) for i in (0,3,8))}</div>
      <a class="link-more" href="journal.html">See all stories →</a>
    </div>
  </section>
  <section class="hm-route">
    <div class="wrap">
      <div class="hm-head"><span class="hm-hand">Beyond Ecuador</span><h2>Ecuador first. Then the rest of the continent.</h2></div>
      <div class="hm-map">
        <svg class="hm-map-svg" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true"><path class="hm-map-path" d="M80 210 C 200 40, 300 60, 360 90 S 560 260, 640 198 S 820 40, 920 84"/></svg>
        <ol class="hm-stops">{"".join(f'<li class="hm-stop{" now" if i == 0 else ""}" style="--x:{x}%;--y:{y}%"><span class="hm-dot{" now" if i == 0 else ""}"></span><em>{tag}</em><b>{n}</b><span>{d}</span></li>' for i, (n, d, tag, x, y) in enumerate(ROUTE))}</ol>
      </div>
      <a class="link-more" href="south-america.html">See the full route →</a>
    </div>
  </section>
</main>'''
page("index.html", "Latitude Zero", "home", home, script='<script src="home.js" defer></script>')

# ---------- ABOUT ----------
about = hero("About us", "Going home, for one of us. <em>Starting over,</em> for the rest.",
  "An American dad, an Ecuadorian mom and a baby boy, getting ready to build a new life on the equator.") + '''
<main>
  <section>
    <div class="wrap story-grid">
      <div class="story-copy">
        <p>Dennisse grew up in Ecuador. I've spent years building businesses in Wilkes-Barre, Pennsylvania, from a coffeehouse on West Market Street to a software company and a marketing agency. When Mateo arrived, we started asking a bigger question: where do we want him to grow up?</p>
        <p>The answer was Ecuador. Close to his abuela, fluent in two languages, and surrounded by volcanoes, cloud forest and the Pacific.</p>
        <p>Latitude Zero is where we document all of it. The paperwork and the logistics. Raising a baby at altitude. The food, the weekend trips and the bigger journeys across South America. The good days and the hard ones.</p>
        <p>The name comes from the line that runs through Ecuador's name and its map: 0° latitude, the equator. It's where our new life starts.</p>
      </div>
      <div class="family" aria-label="The family">
        <div class="member"><span class="initial">A</span><div><b>Austin</b><span>Operator, builder, coffee person. Learning Spanish the hard way. Writes most of the posts.</span></div></div>
        <div class="member"><span class="initial">D</span><div><b>Dennisse</b><span>Ecuadorian by birth. Our translator, guide and the reason we're going.</span></div></div>
        <div class="member"><span class="initial">M</span><div><b>Mateo</b><span>Our son. Future chief tester of strollers, beaches and abuela's cooking.</span></div></div>
      </div>
    </div>
  </section>
  <section style="padding-top:0">
    <p class="wrap drag-hint">Drag the photos around. Make a scrapbook.</p>
    <div class="wrap photo-strip">
      <figure><img src="img/quilotoa.jpg" alt="Quilotoa crater lake" loading="lazy"><figcaption>Quilotoa, Cotopaxi</figcaption></figure>
      <figure><img src="img/otavalo.jpg" alt="Otavalo market" loading="lazy"><figcaption>Otavalo, Imbabura</figcaption></figure>
      <figure><img src="img/montanita.jpg" alt="Sunset at Montañita" loading="lazy"><figcaption>Montañita, Santa Elena</figcaption></figure>
    </div>
  </section>
  <section>
    <div class="wrap th-wrap">
      <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">Two homes</span><h2>From Public Square to Plaza Grande</h2><p>Drag the slider to travel from where we live now to where we're headed.</p></div>
      <div class="two-homes">
        <img src="img/quito.jpg" alt="Plaza Grande in Quito, Ecuador">
        <img class="th-top" src="img/wb_square.jpg" alt="Public Square in Wilkes-Barre, Pennsylvania">
        <span class="th-label th-l">Wilkes-Barre</span><span class="th-label th-r">Quito</span>
        <span class="th-handle" aria-hidden="true"></span>
        <label class="sr" for="th-range">Compare Wilkes-Barre and Quito</label><input type="range" id="th-range" min="0" max="100" value="50">
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">What you'll find here</span><h2>Three kinds of stories</h2></div>
      <div class="offers">
        <div class="offer"><span class="alt">THE MOVE</span><h3>Relocating as a family</h3><p>What it takes to move a household and a baby to Ecuador: planning, packing, housing, healthcare and settling in.</p></div>
        <div class="offer"><span class="alt">LIFE</span><h3>Everyday Ecuador</h3><p>Food, family, language and the small cultural moments that make a place feel like home.</p></div>
        <div class="offer"><span class="alt">TRAVEL</span><h3>Exploring South America</h3><p>Weekend trips across Ecuador's four regions and longer journeys through the continent, with a little one in tow.</p></div>
      </div>
    </div>
  </section>
</main>'''
page("about.html", "About Us · Latitude Zero", "about", about)

# ---------- ECUADOR ----------
REGION_IMG = {"costa":("frailes","Los Frailes beach in Machalilla National Park"),"sierra":("quilotoa","The Quilotoa crater lake"),"amazonia":("cuyabeno","A lodge in the Cuyabeno Wildlife Reserve"),"galapagos":("santacruz","A giant tortoise on Santa Cruz Island")}
def region(id_, alt, w, name, side, body, tags):
    lis = "".join(f"<li>{t}</li>" for t in tags)
    im, ia = REGION_IMG[id_]
    return f'''<article class="region-detail" id="{id_}">
  <div class="side"><span class="eyebrow">{side}</span></div>
  <div class="body"><img class="detail-img" src="img/{im}.jpg" alt="{ia}" loading="lazy"><h2>{name}</h2>{body}<ul>{lis}</ul></div>
</article>'''

ecu = hero("Ecuador guide", "Four worlds in <em>one small country</em>",
  "Ecuador is about the size of Colorado, yet you can wake up on the Pacific, have lunch in the Andes and fall asleep in the Amazon. Here's the lay of the land as we get ready to explore it.") + f'''
<main>
  <section class="panels-sec">
    <div class="wrap">
      <div class="panels" role="list">
        <a class="panel" role="listitem" href="#costa" style="--img:url(img/frailes-800.jpg)"><span class="panel-tag">01</span><b>La Costa</b><span class="panel-sub">Beaches, ceviche and surf towns</span></a>
        <a class="panel open" role="listitem" href="#sierra" style="--img:url(img/quilotoa-800.jpg)"><span class="panel-tag">02</span><b>La Sierra</b><span class="panel-sub">Volcanoes, markets and colonial cities</span></a>
        <a class="panel" role="listitem" href="#amazonia" style="--img:url(img/tena-800.jpg)"><span class="panel-tag">03</span><b>Amazonía</b><span class="panel-sub">Rivers, rainforest and waterfalls</span></a>
        <a class="panel" role="listitem" href="#galapagos" style="--img:url(img/santacruz-800.jpg)"><span class="panel-tag">04</span><b>Galápagos</b><span class="panel-sub">Tortoises, sea lions and snorkeling</span></a>
      </div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Quick facts</span><h2>Before you go</h2></div>
      <dl class="facts">
        <div class="fact"><dt>Capital</dt><dd>Quito</dd></div>
        <div class="fact"><dt>Provinces</dt><dd>24</dd></div>
        <div class="fact"><dt>Languages</dt><dd>Spanish, Kichwa</dd></div>
        <div class="fact"><dt>Time zone</dt><dd>UTC−5</dd></div>
        <div class="fact"><dt>Power</dt><dd>120 V · Type A/B</dd></div>
        <div class="fact"><dt>Regions</dt><dd>Coast, Andes, Amazon, Galápagos</dd></div>
      </dl>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap">
      {region("costa","0 – 300 m",6,"La Costa","Coast","<p>Ecuador's Pacific side is warm, green and built on bananas, shrimp and cacao. Guayaquil is the biggest city in the country, and the coast is lined with surf towns and fishing villages.</p>",["Guayaquil and the Malecón 2000","Montañita and the Ruta del Spondylus","Puerto López and humpback season (roughly June to September)","Ceviche, encebollado and bolones"])}
      {region("sierra","2,500 – 6,263 m",100,"La Sierra","Highlands","<p>The Andes run straight through the middle of the country, lined with volcanoes. Spring-like weather all year, colonial cities and indigenous markets. Take altitude seriously, especially with a baby.</p>",["Quito's historic center","Cuenca, a UNESCO World Heritage city","Otavalo's Saturday market","Cotopaxi and Quilotoa","Mitad del Mundo, on the equator line"])}
      {region("amazonia","200 – 1,000 m",16,"Amazonía","Rainforest","<p>East of the Andes, the land drops into the Amazon basin. It's hot, humid and wildly biodiverse, with jungle lodges and adventure towns reachable by road from the highlands.</p>",["Baños and the Ruta de las Cascadas","Tena and the Napo River","Jungle lodges in Cuyabeno and Yasuní","Chocolate and guayusa tea"])}
      {region("galapagos","0 – 1,707 m",27,"Galápagos","Islands","<p>About 1,000 km off the coast, the islands that shaped Darwin's thinking. Animals with no fear of people, volcanic landscapes and some of the best snorkeling anywhere. Note the time zone is UTC−6.</p>",["Santa Cruz and the giant tortoises","San Cristóbal's sea lions","Island-hopping vs. live-aboard cruises","Visitor rules set by the national park"])}
      <a class="link-more" href="top-20.html">See the 20 places we plan to visit →</a>
    </div>
  </section>
</main>'''
page("ecuador.html", "Ecuador Guide · Latitude Zero", "ecuador", ecu)

# ---------- JOURNAL ----------
journal = hero("The journal", "Stories from <em>latitude zero</em>",
  "The move, everyday life and the trips in between. One new story at a time.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="chips" role="group" aria-label="Filter stories">
        <button class="chip" type="button" data-f="all" aria-pressed="true">All</button>
        <button class="chip" type="button" data-f="move" aria-pressed="false">The move</button>
        <button class="chip" type="button" data-f="family" aria-pressed="false">Family</button>
        <button class="chip" type="button" data-f="places" aria-pressed="false">Places</button>
        <button class="chip" type="button" data-f="coffee" aria-pressed="false">Coffee &amp; cacao</button>
      </div>
      <div class="posts" id="posts">{"".join(post_card(p) for p in POSTS)}</div>
    </div>
  </section>
</main>'''
jscript = '''<script>
document.querySelectorAll('.chip').forEach(function(c){c.addEventListener('click',function(){
  document.querySelectorAll('.chip').forEach(function(x){x.setAttribute('aria-pressed',x===c?'true':'false')});
  var f=c.dataset.f;document.querySelectorAll('#posts .post').forEach(function(p){p.hidden=!(f==='all'||p.dataset.group===f)});
})});
</script>'''
page("journal.html", "Journal · Latitude Zero", "journal", journal, script=jscript)

def comments_block(slug):
    return f'''  <section class="comments-sec" id="comments">
    <div class="wrap comments" data-post="{slug}">
      <div class="cm-head">
        <span class="eyebrow">Join the conversation</span>
        <h2>Comments <span class="cm-count" id="cm-count" hidden></span></h2>
        <p>Have a question, a tip or your own Ecuador story? Leave a comment. We read every one.</p>
      </div>
      <form class="cm-form" id="cm-form" novalidate>
        <div class="cm-row">
          <div class="field"><label for="cm-name">Your name</label><input id="cm-name" maxlength="60" autocomplete="given-name" required></div>
          <div class="field"><label for="cm-place">Where you're from <small>Optional</small></label><input id="cm-place" maxlength="60" placeholder="e.g. Scranton, PA or Cuenca"></div>
        </div>
        <div class="field"><label for="cm-body">Your comment</label><textarea id="cm-body" rows="4" maxlength="1000" required></textarea><span class="cm-chars" id="cm-chars">0 / 1000</span></div>
        <div class="cm-hp" aria-hidden="true"><label for="cm-website">Leave this empty</label><input id="cm-website" tabindex="-1" autocomplete="off"></div>
        <input type="hidden" id="cm-parent" value="">
        <p class="cm-replying" id="cm-replying" hidden><span>Replying to <b id="cm-replying-name"></b></span><button type="button" id="cm-cancel-reply">Cancel</button></p>
        <p class="cm-rules">Be kind. Comments are reviewed before they appear, usually within a day.</p>
        <p class="cm-err" id="cm-err" role="status" hidden>Please add your name and a comment.</p>
        <button class="btn btn-sun" type="submit" id="cm-submit">Post comment</button>
      </form>
      <div class="cm-thanks" id="cm-thanks" role="status" hidden><b>¡Gracias!</b><span id="cm-thanks-msg"></span></div>
      <ol class="cm-list" id="cm-list" aria-live="polite"></ol>
      <div class="cm-empty" id="cm-empty"><span class="cm-empty-bubble" aria-hidden="true"></span><b>No comments yet</b><span>Be the first to say hola.</span></div>
      <div hidden id="cm-str"><span data-k="reply">Reply</span><span data-k="heart">Love this comment</span><span data-k="pending">Awaiting approval · only you can see this</span><span data-k="local">Saved on this device only. Comments go public once the site is live.</span><span data-k="sent">Your comment was sent and will appear once it's approved.</span><span data-k="error">Something went wrong sending your comment. Please try again in a minute.</span><span data-k="justnow">just now</span><span data-k="min">min ago</span><span data-k="hr">h ago</span><span data-k="day">d ago</span><span data-k="one">1 comment</span><span data-k="many">comments</span><span data-k="team">Latitude Zero</span><span data-k="sending">Sending…</span><span data-k="post">Post comment</span></div>
    </div>
  </section>
'''

# ---------- SAMPLE POST ----------
post = f'''<main>
  <section>
    <div class="wrap">
      <div class="article-head">
        <a class="link-more" href="journal.html" style="margin-top:0">← All stories</a>
        <span class="eyebrow">The move</span>
        <h1 style="font-size:clamp(2.2rem,5.5vw,3.6rem)">Why we're moving our family to Ecuador</h1>
        <div class="byline"><span>By Austin</span><span>·</span><span>October 2026</span><span>·</span><span>5 min read</span></div>
      </div>
      <img class="article-art" src="img/chimborazo.jpg" alt="A vicuña below Chimborazo volcano">
      <div class="prose">
        <p>For years, my life revolved around Wilkes-Barre. A coffeehouse on West Market Street, a software company, a marketing agency. I was the guy who built things and kept them running. Then Mateo was born, and the question that mattered most changed from "what are we building?" to "where are we raising him?"</p>
        <p>Dennisse is Ecuadorian. Her family, her language and her childhood are all there. Every time we talked about Mateo's future, Ecuador kept coming up: growing up bilingual, knowing his abuela, living somewhere with mountains, rainforest and ocean all within a day's drive.</p>
        <blockquote>We didn't want Ecuador to be the place Mateo visits. We want it to be a place he's from.</blockquote>
        <h2>The doubts</h2>
        <p>None of this was a simple decision. Moving countries with a baby means rethinking healthcare, housing, schooling and how I run my businesses from another hemisphere. My Spanish is a work in progress. And leaving the place where you've built everything is hard, even when you know it's right.</p>
        <h2>What made us say yes</h2>
        <p>In the end, it came down to family and time. Time with Mateo while he's small, time with Dennisse's family, and a chance to experience a whole continent together instead of a week at a time.</p>
        <h2>What comes next</h2>
        <p>This blog is how we'll share it. The logistics, the mistakes, the food, the trips and what it's really like to start over at latitude zero. If you're thinking about a move like this yourself, follow along. We'll be honest about all of it.</p>
      </div>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap">
      <div class="engage-row">
        <div class="reactions" data-post="why-ecuador">
          <span class="eyebrow">How did this story make you feel?</span>
          <div class="rx-row">
            <button type="button" class="rx" data-r="love" aria-pressed="false"><span class="rx-e" aria-hidden="true">❤️</span>Love it<span class="rx-n"></span></button>
            <button type="button" class="rx" data-r="same" aria-pressed="false"><span class="rx-e" aria-hidden="true">🙌</span>Same here<span class="rx-n"></span></button>
            <button type="button" class="rx" data-r="go" aria-pressed="false"><span class="rx-e" aria-hidden="true">✈️</span>Want to go<span class="rx-n"></span></button>
            <button type="button" class="rx" data-r="wow" aria-pressed="false"><span class="rx-e" aria-hidden="true">🤩</span>¡Qué chévere!<span class="rx-n"></span></button>
          </div>
          <p class="rx-note" hidden>Saved on this device. Totals appear once the site is live.</p>
        </div>
        <div class="poll" data-poll="why-ecuador-abroad">
          <span class="eyebrow">Quick poll</span>
          <b class="poll-q">Have you ever thought about moving abroad with your family?</b>
          <button type="button" class="poll-opt" data-o="planning"><span class="poll-bar"></span><span class="poll-t">Yes, we're planning it</span><span class="poll-pct"></span></button>
          <button type="button" class="poll-opt" data-o="someday"><span class="poll-bar"></span><span class="poll-t">Someday, maybe</span><span class="poll-pct"></span></button>
          <button type="button" class="poll-opt" data-o="following"><span class="poll-bar"></span><span class="poll-t">Not for us, but we love following along</span><span class="poll-pct"></span></button>
          <span class="poll-total"></span>
          <p class="poll-note" hidden>Thanks for voting! Results appear once the site is live.</p>
        </div>
      </div>
      <div class="post-end">
        <div class="share-row"><span class="eyebrow">Share this story</span>
          <div class="share-links"><a class="share" data-net="fb" href="https://www.facebook.com/">Facebook</a><a class="share" data-net="wa" href="https://wa.me/">WhatsApp</a><a class="share" data-net="x" href="https://x.com/">X</a><a class="share" data-net="pin" href="https://www.pinterest.com/">Pinterest</a><button class="share" type="button" id="copy-link">Copy link</button></div>
        </div>
        <a class="next-chapter" href="the-move.html"><span class="eyebrow">Up next · Chapter 2</span><b>Packing up Wilkes-Barre</b><span>Coming soon. Get it first in the newsletter ↓</span></a>
      </div>
    </div>
  </section>
{comments_block("why-ecuador")}  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Keep reading</span><h2>More from the journal</h2></div>
      <div class="posts">{"".join(post_card(POSTS[i]) for i in (1,2,3))}</div>
    </div>
  </section>
</main>'''
SHARE_JS = '''<script>
(function(){var u=encodeURIComponent(location.href.split('#')[0]),t=encodeURIComponent(document.title);
var m={fb:'https://www.facebook.com/sharer/sharer.php?u='+u,wa:'https://wa.me/?text='+t+'%20'+u,x:'https://x.com/intent/post?text='+t+'&url='+u,pin:'https://www.pinterest.com/pin/create/button/?url='+u+'&description='+t};
document.querySelectorAll('a.share').forEach(function(a){a.href=m[a.dataset.net];a.target='_blank';a.rel='noopener'});
var c=document.getElementById('copy-link');if(c)c.addEventListener('click',function(){var l=c.textContent;try{navigator.clipboard.writeText(location.href.split('#')[0]).then(function(){c.textContent='Copied';setTimeout(function(){c.textContent=l},1600)},function(){})}catch(e){}});})();
</script>'''
page("journal-why-ecuador.html", "Why Ecuador · Latitude Zero", "journal", post, script=SHARE_JS + '<script src="comments.js" defer></script>')

# ---------- SOUTH AMERICA ----------
CODES = {"Ecuador": ("AVP", "UIO"), "Colombia": ("UIO", "BOG"), "Peru": ("UIO", "LIM"), "Chile & Argentina": ("UIO", "SCL")}
def country(cls, name, tag, desc, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    fr, to = CODES.get(name, ("UIO", "—"))
    return f'<div class="country ticket {cls}"><span class="dot" aria-hidden="true"></span><div class="ticket-main"><h3>{name}<em>{tag}</em></h3><p>{desc}</p><ul>{lis}</ul></div><div class="ticket-stub" aria-hidden="true"><span class="stub-l">FROM</span><b>{fr}</b><span class="stub-plane">✈</span><span class="stub-l">TO</span><b>{to}</b><span class="barcode"></span></div></div>'

sa = hero("Beyond Ecuador", "Ecuador first. Then <em>the continent.</em>",
  "Ecuador will be our home base. From there, we plan to head out one country at a time, with a toddler, a stroller and a lot of snacks.") + '''
<main>
  <section class="route">
    <div class="wrap">
      <div class="stops" style="display:grid">
        ''' + country("now","Ecuador","FIRST · FUTURE HOME BASE","Where we're moving, and the first country we'll explore.",["Quito, Cuenca and the Avenue of the Volcanoes","The coast from Guayaquil to Puerto López","Amazon lodges and the Galápagos"]) + \
        country("","Colombia","THEN","A short flight north and the obvious first trip.",["Cartagena's walled city","The coffee region","Medellín"]) + \
        country("","Peru","PLANNED","The food capital of South America and the road to Machu Picchu.",["Lima's restaurants","Cusco and the Sacred Valley","Lake Titicaca"]) + \
        country("","Chile & Argentina","SOMEDAY","The big one, once Mateo can hike a little on his own.",["Patagonia","Mendoza wine country","Buenos Aires"]) + '''
      </div>
    </div>
  </section>
</main>'''
page("south-america.html", "Beyond Ecuador · Latitude Zero", "sa", sa)

# ---------- WORK WITH US ----------
work = hero("Partnerships", "Partner with a family <em>starting the story</em>",
  "We work with brands, hotels and tourism boards that fit how we travel: as a family, slowly, and with real experiences to share.") + '''
<main>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Ways to collaborate</span><h2>What we offer</h2><p>New to us? Start with our <a href="media-kit.html" style="color:var(--moss);font-weight:600">media kit</a>.</p></div>
      <div class="offers">
        <div class="offer"><span class="alt">STAYS</span><h3>Family-friendly hotels &amp; lodges</h3><p>Honest stay reviews with photo and video coverage, from what the room's like with a crib to how the kitchen handles a toddler.</p></div>
        <div class="offer"><span class="alt">DESTINATIONS</span><h3>Tourism &amp; experiences</h3><p>Destination stories across Ecuador and South America for tourism boards, tour operators and experience providers.</p></div>
        <div class="offer"><span class="alt">PRODUCTS</span><h3>Travel &amp; family gear</h3><p>Real-world testing of the gear we'll actually use: strollers, carriers, luggage and anything else that makes travel with a baby easier.</p></div>
      </div>
    </div>
  </section>
  <section class="regions-bg" id="follow">
    <div class="wrap follow">
      <div class="sec-head" style="margin-bottom:0">
        <span class="eyebrow">Get in touch</span>
        <h2>Say hola.</h2>
        <p>For partnerships, media requests or questions about moving to Ecuador, email us. Our social channels launch with the move.</p>
        <div class="copy-row"><code id="email">hola@latitudezerofamily.com</code><button class="btn btn-line" type="button" id="copy">Copy email</button></div>
      </div>
      <div class="handles">
        <div class="handle"><span>Instagram</span><code>@latitudezerofamily</code></div>
        <div class="handle"><span>YouTube</span><code>@latitudezerofamily</code></div>
        <div class="handle"><span>TikTok</span><code>@latitudezerofamily</code></div>
        <div class="handle"><span>Facebook</span><code>@latitudezerofamily</code></div>
      </div>
    </div>
  </section>
</main>'''
wscript = '''<script>
document.getElementById('copy').addEventListener('click',function(){
  var b=this,t=document.getElementById('email').textContent;
  function done(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy email'},1600)}
  try{navigator.clipboard.writeText(t).then(done,sel)}catch(e){sel()}
  function sel(){var r=document.createRange();r.selectNodeContents(document.getElementById('email'));var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected'}
});
</script>'''
page("work-with-us.html", "Partnerships · Latitude Zero", "work", work, script=wscript)
exec(open("top20.py").read())
exec(open("credits.py").read())
exec(open("forms.py").read())
exec(open("newpages.py").read())
exec(open("newpages2.py").read())
exec(open("newpages3.py").read())
exec(open("newpages4.py").read())
exec(open("newpages5.py").read())
exec(open("legal.py").read())
sitemap([p for p in PAGES_BUILT if p not in ("404.html",)])
print("built")
exec(open("make_es.py").read())
