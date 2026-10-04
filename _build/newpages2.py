HERO_PHOTO.update({"Videos": "banos", "Dennisse's Ecuador": "otavalo", "Coffee & cacao": "mindo",
                   "Media kit": "guayaquil", "Moving with kids FAQ": "mitad", "What we're packing": "cajas"})

def card(href, img, alt, stamp, title, desc, status="Coming soon", pill=None):
    meta = f'<div class="meta">{f"<span class=pill>{pill}</span>" if pill else ""}<span>{status}</span></div>'
    return f'''<a class="post" href="{href}"><div class="post-art"><img src="img/{img}.jpg" alt="{alt}" loading="lazy"><span class="stamp">{stamp}</span></div><div class="post-body">{meta}<h3>{title}</h3><p>{desc}</p></div></a>'''

# ---------- VIDEOS ----------
videos = hero("Videos", "Watch the move <em>as it happens</em>",
  "A weekly family vlog on YouTube, plus short clips on Instagram and TikTok. Here's what's coming to the channel.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">On YouTube</span><h2>Three video series</h2></div>
      <div class="offers">
        <div class="offer"><span class="alt">WEEKLY · LONG FORM</span><h3>The move, week by week</h3><p>The full relocation story, from packing up Pennsylvania to settling into our new home.</p></div>
        <div class="offer"><span class="alt">ONE PLACE PER EPISODE</span><h3>Top 20 with a toddler</h3><p>All 20 places on our bucket list, filmed with Mateo along for the ride.</p></div>
        <div class="offer"><span class="alt">SHORTS</span><h3>Moments at latitude zero</h3><p>Quick daily clips: markets, meals, first words and views from the Andes.</p></div>
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">First episodes</span><h2>Coming to the channel</h2></div>
      <div class="posts">
        {card("the-move.html","quito","Plaza Grande in Quito","EP 01","Why we're leaving Pennsylvania for Ecuador","The decision, told by all three of us. Well, two of us. Mateo mostly naps.","Filming soon","The move")}
        {card("the-move.html","guayaquil","The Malecón 2000 in Guayaquil","EP 02","Moving abroad with a baby","Packing a family's life into suitcases and getting through the airport.","Filming soon","The move")}
        {card("top-20.html","mitad","The Mitad del Mundo monument","EP 03","One foot in each hemisphere","Mateo's first visit to the equator at Mitad del Mundo.","Filming soon","Top 20")}
      </div>
    </div>
  </section>
  <section>
    <div class="wrap follow">
      <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">Subscribe</span><h2>Don't miss an episode</h2><p>Search for these handles to follow along. The channels go live with our first episode.</p></div>
      <div class="handles">
        <div class="handle"><span>YouTube</span><code>@latitudezerofamily</code></div>
        <div class="handle"><span>Instagram</span><code>@latitudezerofamily</code></div>
        <div class="handle"><span>TikTok</span><code>@latitudezerofamily</code></div>
      </div>
    </div>
  </section>
</main>'''
page("videos.html", "Videos · Latitude Zero", "videos", videos)

# ---------- DENNISSE ----------
TOPICS = [("otavalo","Otavalo market","HER COLUMN","Showing Austin my Ecuador","The places I couldn't wait to share with him, and how he reacted to each one."),
          ("cuenca","Rooftops of Cuenca","FOOD","The Ecuadorian food I missed most","Every dish I dreamed about while living in the US, and where we're eating it first."),
          ("quilotoa","Quilotoa crater lake","FAMILY","Raising Mateo with my family's traditions","Passing on the songs, sayings and Sunday rituals I grew up with."),
          ("quito","Plaza Grande in Quito","CULTURE","Holidays the Ecuadorian way","Carnaval, Día de los Difuntos with colada morada and guaguas de pan, and Christmas with the family."),
          ("mitad","Mitad del Mundo","LANGUAGE","Ecuadorian Spanish, explained","The words and phrases you'll only hear in Ecuador, from ¡achachay! to ¡arrarray!"),
          ("frailes","Los Frailes beach","PLACES","The coast vs. the sierra","Two very different Ecuadors, and why every family argues about which is better.")]
dtopics = "".join(card("dennisse.html", i, a, s, t, d) for i, a, s, t, d in TOPICS)
denn = hero("Dennisse's Ecuador", "Ecuador through the eyes of <em>someone who grew up there</em>",
  "Austin is about to make Ecuador home. For Dennisse, it's a homecoming. This is her column: the food, family, language and places that shaped her.") + f'''
<main>
  <section>
    <div class="wrap story-grid">
      <div class="story-copy">
        <p>Most travel blogs about Ecuador are written by visitors. Half of this family isn't one.</p>
        <p>Dennisse grew up in Ecuador before building a life in the United States. Now she's bringing her husband and son back to the country she knows best, and she'll be writing about it in her own words, in both Spanish and English.</p>
        <p>Expect the things a guidebook can't tell you: what her family actually cooks, which places locals love, the slang that makes Austin laugh, and what it feels like to come home with a baby of her own.</p>
      </div>
      <div class="family" aria-label="About Dennisse">
        <div class="member"><span class="initial">D</span><div><b>Dennisse</b><span>Ecuadorian by birth. Mom to Mateo. The family's guide, translator and food critic.</span></div></div>
        <div class="member"><span class="initial">ES</span><div><b>Bilingual column</b><span>Written in Spanish and English</span></div></div>
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="flash-wrap">
        <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">Dennisse teaches Austin</span><h2>Ecuadorian slang flashcards</h2><p>Tap a card to flip it. Swipe or use the arrows for the next one.</p></div>
        <div class="deck">
          <div class="cards" id="cards"><div class="fc" data-i="0"><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>¡Achachay!</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>¡Achachay!</b><p>"Brrr, it's cold!" From Kichwa.</p></div></div></div><div class="fc" data-i="1" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>¡Arrarray!</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>¡Arrarray!</b><p>"Ouch, it's hot!" Also from Kichwa.</p></div></div></div><div class="fc" data-i="2" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>Guagua</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>Guagua</b><p>A baby or little kid. (In some countries it means a bus!)</p></div></div></div><div class="fc" data-i="3" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>Ñaño / ñaña</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>Ñaño / ñaña</b><p>Brother / sister. From Kichwa.</p></div></div></div><div class="fc" data-i="4" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>Chévere</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>Chévere</b><p>Cool, great, awesome.</p></div></div></div><div class="fc" data-i="5" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>¿Mande?</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>¿Mande?</b><p>"Pardon?" or "Yes?" A polite reply you'll hear in the highlands.</p></div></div></div><div class="fc" data-i="6" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>¡Qué bestia!</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>¡Qué bestia!</b><p>"Wow!" or "No way!"</p></div></div></div><div class="fc" data-i="7" hidden><div class="fc-inner"><div class="fc-face"><span class="eyebrow">Ecuadorian Spanish</span><b>¡Chuta!</b><span class="fc-hint">Tap to flip ↻</span></div><div class="fc-face fc-back"><b>¡Chuta!</b><p>"Darn!" A mild everyday exclamation.</p></div></div></div></div>
          <div class="deck-nav"><button type="button" class="dk-btn" id="fc-prev" aria-label="Previous card">‹</button><span id="fc-count">1 / 8</span><button type="button" class="dk-btn" id="fc-next" aria-label="Next card">›</button></div>
        </div>
      </div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="ask-d">
        <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">Ask Dennisse</span><h2>Your questions, her answers</h2><p>Each month Dennisse will answer reader questions about Ecuador, family, food and traditions. Send yours.</p></div>
        <div>{mail_form("ask-form", "Ask Dennisse", [("input", "ad-name", "Your first name", True, ""), ("textarea", "ad-q", "Your question", True, "e.g. What should we eat first in Quito?")], "Send my question")}</div>
      </div>
      <div class="sec-head"><span class="eyebrow">Coming from Dennisse</span><h2>Her first stories</h2></div>
      <div class="posts">{dtopics}</div>
    </div>
  </section>
</main>'''
page("dennisse.html", "Dennisse's Ecuador · Latitude Zero", "dennisse", denn)

# ---------- COFFEE & CACAO ----------
coffee = hero("Coffee & cacao", "From farm <em>to cup</em>",
  "Austin runs a coffeehouse in Wilkes-Barre. Soon he'll be living in one of the world's great origins for both coffee and chocolate. This series goes to the source.") + f'''
<main>
  <section>
    <div class="wrap story-grid">
      <div class="story-copy">
        <p>Ecuador grows coffee at almost every altitude, from the slopes around Loja in the south to the cloud forests near Quito, and even in the highlands of the Galápagos.</p>
        <p>It's also the home of Nacional cacao, the fine-flavor variety prized by chocolate makers around the world, with its famous floral "Arriba" aroma.</p>
        <p>Once we're there, we'll visit farms, roasters and chocolate makers, learn how each one works, and share what we taste along the way. Mateo is on official banana-tasting duty.</p>
      </div>
      <div class="family" aria-label="Where we're going">
        <span class="eyebrow" style="padding-bottom:10px">On our list</span>
        <div class="member"><span class="initial">L</span><div><b>Loja &amp; Zamora-Chinchipe</b><span>Southern Ecuador's best-known coffee region</span></div></div>
        <div class="member"><span class="initial">I</span><div><b>Intag Valley</b><span>Shade-grown coffee in the cloud forest of Imbabura</span></div></div>
        <div class="member"><span class="initial">M</span><div><b>Mindo</b><span>Chocolate farms and tastings near Quito</span></div></div>
        <div class="member"><span class="initial">N</span><div><b>Napo</b><span>Amazon cacao grown in Kichwa family gardens</span></div></div>
        <div class="member"><span class="initial">G</span><div><b>San Cristóbal</b><span>Coffee grown in the Galápagos highlands</span></div></div>
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="beans">
        <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">From bean to cup</span><h2>How coffee happens</h2><p>Drag the slider to follow a coffee bean from the farm to your cup.</p></div>
        <div class="bs">
          <div class="bs-visual" aria-hidden="true"><span class="bs-bean" id="bs-bean"></span><span class="bs-steam"></span></div>
          <div class="bs-steps"><div class="bs-step" data-i="0" data-c="#c8372d"><span class="eyebrow">Step 1 of 6</span><b>Cherry</b><p>Coffee grows as bright red cherries on shrubs, from Loja's hills to the cloud forest.</p></div><div class="bs-step" data-i="1" data-c="#b5442f" hidden><span class="eyebrow">Step 2 of 6</span><b>Harvest</b><p>Ripe cherries are picked by hand, often on steep slopes.</p></div><div class="bs-step" data-i="2" data-c="#a7b36a" hidden><span class="eyebrow">Step 3 of 6</span><b>Process</b><p>The fruit is removed, and the seeds inside, the beans, are washed or left to ferment.</p></div><div class="bs-step" data-i="3" data-c="#c9b98a" hidden><span class="eyebrow">Step 4 of 6</span><b>Dry</b><p>The beans dry slowly in the sun on patios or raised beds.</p></div><div class="bs-step" data-i="4" data-c="#6b3f22" hidden><span class="eyebrow">Step 5 of 6</span><b>Roast</b><p>Heat turns green beans brown and unlocks the flavor.</p></div><div class="bs-step" data-i="5" data-c="#3b2416" hidden><span class="eyebrow">Step 6 of 6</span><b>Brew</b><p>Ground and brewed. The cup we'll be sipping at the source.</p></div></div>
          <label class="sr" for="bs-range">Coffee step</label><input type="range" id="bs-range" min="0" max="5" value="0" step="1">
          <div class="bs-labels" aria-hidden="true"><span>Cherry</span><span>Harvest</span><span>Process</span><span>Dry</span><span>Roast</span><span>Brew</span></div>
        </div>
      </div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">The series</span><h2>Coming episodes</h2></div>
      <div class="posts">
        {card("coffee-cacao.html","mindo","An orchid in the Mindo cloud forest","MINDO","Our first chocolate farm","Bean to bar in the cloud forest, two hours from Quito.","Coming soon","Cacao")}
        {card("coffee-cacao.html","tena","The Napo River near Tena","NAPO","Cacao in the Amazon","How Kichwa families grow cacao alongside everything else they eat.","Coming soon","Cacao")}
        {card("coffee-cacao.html","cuenca","Rooftops of Cuenca","CAFÉ","Ecuador's café scene","The roasters and cafés we fall for in Quito and Cuenca.","Coming soon","Coffee")}
      </div>
    </div>
  </section>
</main>'''
page("coffee-cacao.html", "Coffee & Cacao · Latitude Zero", "coffee", coffee)

# ---------- MEDIA KIT ----------
kit = hero("Media kit", "Latitude Zero <em>media kit</em>",
  "For brands, hotels, tourism boards and media. Who we are, who follows us and how we like to work together.") + '''
<main>
  <section>
    <div class="wrap">
      <dl class="facts">
        <div class="fact"><dt>Who</dt><dd>Austin, Dennisse &amp; Mateo</dd></div>
        <div class="fact"><dt>Based in</dt><dd>Wilkes-Barre, PA, moving to Ecuador</dd></div>
        <div class="fact"><dt>Languages</dt><dd>English &amp; Spanish</dd></div>
        <div class="fact"><dt>Focus</dt><dd>Family relocation &amp; travel</dd></div>
        <div class="fact"><dt>Coverage</dt><dd>Ecuador &amp; South America</dd></div>
        <div class="fact"><dt>Launching</dt><dd>With our move</dd></div>
      </dl>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Our audience</span><h2>Who we're creating for</h2></div>
      <div class="offers">
        <div class="offer"><span class="alt">01 · PLANNING A MOVE</span><h3>Families thinking about moving abroad</h3><p>Parents researching a life overseas, following a real family's relocation step by step.</p></div>
        <div class="offer"><span class="alt">02 · DIASPORA</span><h3>Ecuadorians at home and abroad</h3><p>Spanish-speaking readers who'd enjoy seeing their country through a family's eyes.</p></div>
        <div class="offer"><span class="alt">03 · FAMILY TRAVEL</span><h3>Parents traveling with little ones</h3><p>Families planning trips to Ecuador and South America with babies and toddlers.</p></div>
      </div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">What we create</span><h2>Formats</h2></div>
      <div class="offers">
        <div class="offer"><span class="alt">LONG FORM</span><h3>Blog stories &amp; guides</h3><p>Written in English and Spanish, built to be found in search for years.</p></div>
        <div class="offer"><span class="alt">VIDEO</span><h3>YouTube vlogs</h3><p>Weekly family episodes and one-place-per-episode destination films.</p></div>
        <div class="offer"><span class="alt">SOCIAL</span><h3>Reels, TikToks &amp; stories</h3><p>Short vertical video and photos from our everyday life.</p></div>
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap story-grid">
      <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">How we work</span><h2>Our partnership principles</h2><p>We only feature places and products that fit how our family actually travels. Every partnership is clearly disclosed to our readers.</p></div>
      <div class="family">
        <div class="member"><span class="initial">1</span><div><b>Family-friendly first</b><span>If it doesn't work with a baby, it isn't for us.</span></div></div>
        <div class="member"><span class="initial">2</span><div><b>Real experiences only</b><span>We'll stay, eat, ride and use it ourselves before we share it.</span></div></div>
        <div class="member"><span class="initial">3</span><div><b>Always disclosed</b><span>Partnerships are labeled clearly on every post and video.</span></div></div>
        <div class="member"><span class="initial">4</span><div><b>Bilingual by default</b><span>Coverage in English and Spanish reaches both audiences.</span></div></div>
      </div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Get in touch</span><h2>Let's work together</h2><p>Email us to talk about a collaboration as we launch.</p></div>
      <div class="copy-row" style="margin-top:0"><code id="email">hola@latitudezerofamily.com</code><a class="btn btn-line" href="work-with-us.html">See partnerships</a></div>
    </div>
  </section>
</main>'''
page("media-kit.html", "Media Kit · Latitude Zero", "kit", kit)

# ---------- FAQ ----------
FAQ = [
 ("Why did you choose Ecuador?", "Dennisse is Ecuadorian, and we want Mateo to grow up close to her family, speaking both languages. The whole story is in <a href=\"journal-why-ecuador.html\">Why we're moving our family to Ecuador</a>."),
 ("Which city are you moving to?", "We'll share where we settle and why in Chapter 5 of <a href=\"the-move.html\">The move</a>, once we've lived there long enough to have an honest opinion."),
 ("Is it hard to move abroad with a baby?", "We're about to find out. We're documenting every step, from packing to the flight to the first weeks, so other families can see what it's really like."),
 ("Do you need to speak Spanish?", "Dennisse is a native speaker. Austin is learning as fast as he can. We'll share how it goes for the non-native speaker in the family, and the phrases that help most."),
 ("How do you handle visas and paperwork?", "We'll describe our own experience in The move. Requirements change, so always check the latest rules with Ecuador's official government sources or an Ecuadorian consulate before you plan."),
 ("What about altitude with a baby?", "Quito sits at about 2,850 m. We plan to take it slowly and follow our pediatrician's advice. Talk to yours before traveling to high altitude with a little one."),
 ("Is Ecuador safe for families?", "Like anywhere, it depends on where you are and how you travel. We'll share our own experiences, and we recommend checking current official travel advisories before any trip."),
 ("Can I ask you a question about moving?", "Yes. Email us at hola@latitudezerofamily.com. The best questions will become future posts and videos."),
]
faq_html = "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
faq = hero("Moving with kids FAQ", "Moving to Ecuador <em>with kids</em>",
  "The questions friends, family and readers keep asking us, answered from our own experience as it happens.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="faqs">{faq_html}</div>
      <p class="credit-note">We share our own experience, not legal, immigration or medical advice.</p>
      <div class="ask">
        <span class="eyebrow">Ask us anything</span>
        <h2>Got a question about moving, Ecuador or traveling with a baby?</h2>
        <p>Email us. The best questions become future posts and videos, and we'll credit you (first name only) if you'd like.</p>
        <div class="copy-row" style="margin-top:4px"><code id="email">hola@latitudezerofamily.com</code><button class="btn btn-line" type="button" id="copy">Copy email</button></div>
      </div>
    </div>
  </section>
</main>'''
page("moving-with-kids.html", "Moving With Kids FAQ · Latitude Zero", "faq", faq, script=wscript)

# ---------- GEAR ----------
GEAR = [("FOR THE FLIGHT", "Getting there", ["Travel car seat or car seat bag", "Lightweight travel stroller", "Baby carrier for airports and connections", "Change of clothes for everyone, in the carry-on"]),
        ("FOR THE ANDES", "Cobblestones and cool mornings", ["A carrier that handles hills and steps", "Warm layers for chilly highland nights", "Sun hat and baby-safe sunscreen for the strong equatorial sun"]),
        ("FOR THE COAST & AMAZON", "Heat, sand and humidity", ["Rash guard and swim diapers", "Bug protection safe for babies", "Light, quick-dry clothing"]),
        ("FOR SLEEP", "Naps anywhere", ["Portable travel crib", "Blackout shades for bright equatorial mornings", "White noise for new rooms and street sounds"])]
gear_html = "".join(f'<div class="offer"><span class="alt">{t}</span><h3>{h}</h3><ul class="gear-list">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for t, h, items in GEAR)
gear = hero("What we're packing", "The gear we're <em>packing</em>",
  "What we're packing to move and travel around Ecuador with a baby. We'll name the exact products we use once they've survived the trip.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="pack">
        <div class="pack-copy"><span class="eyebrow">Mini game</span><h2>Help us pack</h2><p>Tap each item to pack it into the suitcase.</p>
          <div class="pack-items" id="pack-items">{"".join(f'<button type="button" class="pack-item">{i}</button>' for t,h,items in GEAR for i in items)}</div>
          <p class="pack-msg" id="pack-msg" aria-live="polite"></p>
          <button class="btn btn-line" type="button" id="pack-reset" hidden>Unpack and play again</button>
        </div>
        <div class="suitcase" aria-hidden="true"><span class="handle"></span><div class="case"><div class="case-fill" id="case-fill"></div><span class="case-count" id="case-count">0</span></div><span class="wheel-l"></span><span class="wheel-r"></span></div>
        <div hidden id="pack-str"><span data-k="some">Keep going. There's still room.</span><span data-k="done">All packed! Ecuador, here we come.</span></div>
      </div>
      <div class="offers gear-grid">{gear_html}</div>
      <a class="link-more" href="with-a-baby.html">Read about traveling Ecuador with a baby →</a>
    </div>
  </section>
</main>'''
page("gear.html", "What We're Packing · Latitude Zero", "gear", gear)
