HERO_PHOTO.update({"Start here": "mitad", "The move": "quito", "Traveling with a baby": "sancristobal"})

# ---------- START HERE ----------
def series(href, tag, title, desc):
    return f'<a class="offer series" href="{href}"><span class="alt">{tag}</span><h3>{title}</h3><p>{desc}</p><span class="go">Explore →</span></a>'

start = hero("Start here", "New here? <em>Bienvenidos.</em>",
  "Latitude Zero follows one American-Ecuadorian family as we move to Ecuador with our baby son and explore South America. Here's the best place to begin.") + f'''
<main>
  <section>
    <div class="wrap story-grid">
      <div class="story-copy">
        <p>We're Austin, Dennisse and Mateo. Dennisse grew up in Ecuador. Austin grew up in Pennsylvania and spent years building businesses in Wilkes-Barre. When Mateo was born, we decided he should grow up close to his Ecuadorian family, speaking two languages, with volcanoes and the Pacific in his backyard.</p>
        <p>This site is our record of that move and everything after it. Not a polished travel guide. Just our family, figuring it out, one story at a time.</p>
        <a class="link-more" href="about.html">Read our full story →</a>
      </div>
      <div class="family" aria-label="Read these first">
        <span class="eyebrow" style="padding-bottom:10px">Read these first</span>
        <a class="member" href="journal-why-ecuador.html" style="text-decoration:none"><span class="initial">1</span><div><b>Why we're moving our family to Ecuador</b><span>Where it all starts</span></div></a>
        <a class="member" href="top-20.html" style="text-decoration:none"><span class="initial">2</span><div><b>The 20 places we plan to visit</b><span>Our Ecuador bucket list</span></div></a>
        <a class="member" href="with-a-baby.html" style="text-decoration:none"><span class="initial">3</span><div><b>Traveling with a baby</b><span>Mateo's side of the adventure</span></div></a>
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">The series</span><h2>Five ongoing stories</h2><p>Everything we publish fits into one of these.</p></div>
      <div class="offers series-grid">
        {series("the-move.html","THE MOVE","Relocating as a family","Chapter by chapter, from deciding to go to our first year at latitude zero.")}
        {series("top-20.html","TOP 20","Our Ecuador bucket list","Twenty places across four regions, each one visited and written up.")}
        {series("with-a-baby.html","FAMILY TRAVEL","Traveling with a baby","Mateo's firsts and what traveling Ecuador with a little one is really like.")}
        {series("dennisse.html","HER ECUADOR","Dennisse's Ecuador","The country through the eyes of the one of us who grew up there.")}
        {series("coffee-cacao.html","COFFEE &amp; CACAO","From farm to cup","A coffeehouse owner goes to the source of Ecuador's coffee and chocolate.")}
        {series("south-america.html","SOUTH AMERICA","Beyond Ecuador","Colombia, Peru, Chile and Argentina, one country at a time.")}
      </div>
    </div>
  </section>
  <section>
    <div class="wrap follow">
      <div class="sec-head" style="margin-bottom:0">
        <span class="eyebrow">Follow along</span>
        <h2>The best ways to keep up</h2>
        <p>Daily moments will go on Instagram and TikTok and the weekly vlog on YouTube, starting with the move. Every new chapter lands in the newsletter.</p>
      </div>
      <div class="handles">
        <div class="handle"><span>Newsletter</span><a href="#newsletter" style="color:var(--moss);font-weight:600">Join below ↓</a></div>
        <div class="handle"><span>YouTube</span><a href="videos.html" style="color:var(--moss);font-weight:600">See our videos →</a></div>
        <div class="handle"><span>Instagram</span><code>@latitudezerofamily</code></div>
        <div class="handle"><span>TikTok</span><code>@latitudezerofamily</code></div>
      </div>
    </div>
  </section>
</main>'''
page("start-here.html", "Start Here · Latitude Zero", "start", start)

# ---------- THE MOVE ----------
CHAPTERS = [
  ("now", "Chapter 1", "The decision", "Why an American dad, an Ecuadorian mom and their baby are leaving Pennsylvania for Ecuador.", "Read now", "journal-why-ecuador.html"),
  ("", "Chapter 2", "Packing up Wilkes-Barre", "Saying goodbye to friends, the coffeehouse and the house, and fitting a family's life into suitcases.", "Coming soon", ""),
  ("", "Chapter 3", "The flight south", "Our first international move with a baby, from airport security to landing on the equator.", "Coming soon", ""),
  ("", "Chapter 4", "Landing in Ecuador", "The first week: jet lag, altitude, family reunions and Mateo meeting his Ecuadorian relatives.", "Coming soon", ""),
  ("", "Chapter 5", "Finding home", "Choosing a city and a neighborhood, and what made one place feel like ours.", "Coming soon", ""),
  ("", "Chapter 6", "The first 90 days", "Routines, language, food, friendships and the moments that surprised us.", "Coming soon", ""),
  ("", "Chapter 7", "One year at latitude zero", "Looking back on a full year of life in Ecuador, and what comes next.", "Coming soon", ""),
]
ch_html = "".join(
  f'''<li class="chapter {cls}"><span class="dot" aria-hidden="true"></span><div><span class="alt">{n}</span><h3>{t}</h3><p>{d}</p>{f'<a class="link-more" style="margin-top:8px" href="{h}">{st} →</a>' if h else f'<span class="status">{st}</span>'}</div></li>'''
  for cls, n, t, d, st, h in CHAPTERS)
move = hero("The move", "Moving our family <em>to Ecuador</em>",
  "The whole relocation, told as it happens. Seven chapters, from the decision to our first year.") + f'''
<main>
  <section>
    <div class="wrap">
      <ol class="chapters">{ch_html}</ol>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">From the journal</span><h2>Stories from the move</h2></div>
      <div class="posts">{"".join(post_card(p) for p in POSTS if p[6] == "move")}</div>
      <div style="display:flex;flex-wrap:wrap;gap:0 28px"><a class="link-more" href="moving-with-kids.html">Moving to Ecuador with kids: FAQ →</a><a class="link-more" href="videos.html">Watch the move on video →</a></div>
    </div>
  </section>
</main>'''
page("the-move.html", "The Move · Latitude Zero", "move", move)

# ---------- WITH A BABY ----------
FIRSTS = [("First flight", "Pennsylvania to Ecuador"), ("First volcano", "Cotopaxi, from a safe distance"),
          ("First Pacific wave", "Los Frailes beach"), ("First giant tortoise", "Santa Cruz, Galápagos"),
          ("First Spanish word", "We're placing bets"), ("First Ecuadorian food", "Abuela gets to decide")]
firsts = "".join(f'<li class="first"><div><b>{t}</b><span>{d}</span></div><span class="status">Coming up</span></li>' for t, d in FIRSTS)
baby = hero("Traveling with a baby", "Exploring Ecuador <em>with Mateo</em>",
  "Mateo is the youngest member of the expedition. This is his side of the adventure, and what we learn traveling Ecuador with a little one.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Mateo's firsts</span><h2>Milestones at latitude zero</h2><p>We'll check these off as they happen, with photos and video.</p></div>
      <ul class="firsts">{firsts}</ul>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">How we travel</span><h2>Our family travel rules</h2><p>Our starting rules. We'll update them as Mateo teaches us what works.</p></div>
      <div class="offers">
        <div class="offer"><span class="alt">SLOW DOWN</span><h3>One big thing a day</h3><p>A volcano or a market or a beach. Never all three. Nap time decides the schedule.</p></div>
        <div class="offer"><span class="alt">GO HIGH SLOWLY</span><h3>Respect the altitude</h3><p>Quito sits at 2,850 m. We'll give ourselves time to adjust and follow our pediatrician's advice before going higher.</p></div>
        <div class="offer"><span class="alt">CARRIER &gt; STROLLER</span><h3>Pack for cobblestones</h3><p>Colonial streets, trails and sand. A good baby carrier goes everywhere a stroller can't.</p></div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:0 28px"><a class="link-more" href="gear.html">What we're packing →</a><a class="link-more" href="moving-with-kids.html">Moving with kids FAQ →</a></div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Baby-friendly picks</span><h2>Top 20 places we're most excited to share with Mateo</h2></div>
      <div class="posts">
        <a class="post" href="top-20.html"><div class="post-art"><img src="img/santacruz.jpg" alt="A giant tortoise on Santa Cruz" loading="lazy"><span class="stamp">GALÁPAGOS</span></div><div class="post-body"><h3>Giant tortoises on Santa Cruz</h3><p>Slow-moving, huge and right at toddler eye level.</p></div></a>
        <a class="post" href="top-20.html"><div class="post-art"><img src="img/frailes.jpg" alt="Los Frailes beach" loading="lazy"><span class="stamp">MANABÍ</span></div><div class="post-body"><h3>Los Frailes beach</h3><p>A protected crescent of sand for first Pacific waves.</p></div></a>
        <a class="post" href="top-20.html"><div class="post-art"><img src="img/mindo.jpg" alt="An orchid in the Mindo cloud forest" loading="lazy"><span class="stamp">MINDO</span></div><div class="post-body"><h3>Mindo cloud forest</h3><p>Hummingbirds and butterflies, lower and warmer than Quito.</p></div></a>
      </div>
    </div>
  </section>
</main>'''
page("with-a-baby.html", "Traveling With a Baby · Latitude Zero", "baby", baby)
