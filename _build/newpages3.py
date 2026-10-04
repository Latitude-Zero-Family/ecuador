HERO_PHOTO.update({"Food & recipes": "f_hornado", "Region quiz": "quilotoa", "Moving checklist": "guayaquil"})

# ---------- FOOD ----------
DISHES = [
 ("costa", "f_encebollado", "Encebollado", "A tuna and yuca soup with pickled red onion, eaten in the morning. Guayaquil's famous cure for everything."),
 ("costa", "f_bolon", "Bolón de verde", "A fist-sized ball of mashed green plantain with cheese or pork crackling. The coastal breakfast."),
 ("sierra", "f_hornado", "Hornado", "Slow-roasted whole pork with mote (hominy), potato patties, avocado and curtido. A highland market classic."),
 ("sierra", "f_llapingachos", "Llapingachos", "Golden potato and cheese patties with chorizo, fried egg and peanut sauce. Ambato's pride."),
 ("amazonia", "f_maito", "Maito", "Fish wrapped in bijao leaves and cooked over the fire. Simple, smoky and very Amazon."),
 ("seasonal", "f_fanesca", "Fanesca", "A rich soup of 12 grains and salt cod, made only during Holy Week. Every family's version is the best one."),
 ("seasonal", "f_colada", "Colada morada & guaguas de pan", "A spiced purple corn and fruit drink with bread babies, made for Día de los Difuntos on November 2."),
]
dish_cards = "".join(f'''<article class="dish" data-region="{r}"><span class="sticker" aria-hidden="true">¡Qué rico!</span><img src="img/{img}.jpg" alt="{name}" loading="lazy"><div class="dish-body"><span class="alt">{ {"costa":"COAST","sierra":"ANDES","amazonia":"AMAZON","seasonal":"SEASONAL"}[r] }</span><h3>{name}</h3><p>{d}</p></div></article>''' for r, img, name, d in DISHES)

EAT = [("Quito", "Locro de papa, empanadas de viento", "top-20.html#place-1"), ("Otavalo", "Fritada, and helados de paila in nearby Ibarra", "top-20.html#place-5"),
       ("Cuenca", "Mote pillo and hornado", "top-20.html#place-6"), ("Baños", "Melcocha, pulled taffy made in doorways", "top-20.html#place-7"),
       ("Mindo", "Bean-to-bar chocolate", "top-20.html#place-9"), ("Guayaquil", "Encebollado, bolón and crab", "top-20.html#place-12"),
       ("Manabí coast", "Viche, corviche and fresh ceviche", "top-20.html#place-15"), ("Tena", "Maito and guayusa tea", "top-20.html#place-16"),
       ("Galápagos", "Fresh fish and ceviche by the harbor", "top-20.html#place-19")]
eat_rows = "".join(f'<li><a href="{h}"><b>{p}</b><span>{w}</span></a></li>' for p, w, h in EAT)

RECIPES = [("f_llapingachos", "Llapingachos", "Dennisse's version, with the peanut sauce her family swears by."),
           ("f_colada", "Colada morada", "The November tradition, written down for the first time."),
           ("f_bolon", "Bolón de verde", "The easiest Ecuadorian breakfast to make anywhere.")]
recipe_cards = "".join(f'<article class="post recipe"><div class="post-art"><img src="img/{i}.jpg" alt="{n}" loading="lazy"><span class="stamp">RECIPE</span></div><div class="post-body"><div class="meta"><span class="pill">Dennisse\'s kitchen</span><span>Coming soon</span></div><h3>{n}</h3><p>{d}</p></div></article>' for i, n, d in RECIPES)

food = hero("Food & recipes", "Ecuador <em>on a plate</em>",
  "What to eat, region by region, the family recipes Dennisse grew up on, and Mateo's first tastes of Ecuador.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">What to eat</span><h2>Dishes we can't wait to share</h2></div>
      <div class="chips" role="group" aria-label="Filter dishes">
        <button class="chip" type="button" data-f="all" aria-pressed="true">All</button>
        <button class="chip" type="button" data-f="costa" aria-pressed="false">Coast</button>
        <button class="chip" type="button" data-f="sierra" aria-pressed="false">Andes</button>
        <button class="chip" type="button" data-f="amazonia" aria-pressed="false">Amazon</button>
        <button class="chip" type="button" data-f="seasonal" aria-pressed="false">Seasonal</button>
      </div>
      <div class="dishes" id="dishes">{dish_cards}</div>
    </div>
  </section>
  <section class="plate-sec">
    <div class="wrap plate-grid">
      <div class="plate-copy">
        <span class="eyebrow">Play with your food</span>
        <h2>Build your Ecuadorian plate</h2>
        <p>Tap up to three dishes to fill your plate.</p>
        <div class="plate-picks" id="plate-picks">{"".join(f'<button type="button" class="pick" data-img="{img}"><img src="img/{img}-800.jpg" alt=""><span>{name}</span></button>' for r, img, name, d in DISHES)}</div>
        <p class="plate-msg" id="plate-msg" aria-live="polite"></p>
        <button class="btn btn-line" type="button" id="plate-clear">Clear my plate</button>
      </div>
      <div class="plate" id="plate" aria-hidden="true"><span class="fork"></span><span class="knife"></span><div class="plate-in" id="plate-in"></div></div>
      <div hidden id="plate-str"><span data-k="1">Good start. Pick two more.</span><span data-k="2">One more and it's a feast.</span><span data-k="3">¡Buen provecho! That's a proper Ecuadorian lunch.</span><span data-k="full">Your plate is full. Clear it to start again.</span></div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Dennisse's kitchen</span><h2>Family recipes</h2><p>The dishes Dennisse grew up on, written down as she cooks them, in English and Spanish.</p></div>
      <div class="posts">{recipe_cards}</div>
    </div>
  </section>
  <section>
    <div class="wrap story-grid">
      <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">Mateo tries it</span><h2>First tastes of Ecuador</h2><p>A short video series: Mateo meets Ecuadorian food one bite at a time, with his pediatrician's go-ahead and abuela's supervision.</p><a class="link-more" href="videos.html">See our video series →</a></div>
      <div class="family" aria-label="Mateo's first tastes">
        <div class="member"><span class="initial">1</span><div><b>Mashed plantain</b><span>The Ecuadorian baby classic</span></div></div>
        <div class="member"><span class="initial">2</span><div><b>Naranjilla</b><span>The sour fruit he'll either love or hate</span></div></div>
        <div class="member"><span class="initial">3</span><div><b>Locro de papa</b><span>Potato soup, the first family dinner</span></div></div>
      </div>
    </div>
  </section>
  <section class="regions-bg">
    <div class="wrap">
      <div class="sec-head"><span class="eyebrow">Eat your way through the Top 20</span><h2>What to eat at each stop</h2></div>
      <ul class="eat-list">{eat_rows}</ul>
    </div>
  </section>
</main>'''
fscript = '''<script>
document.querySelectorAll('.chip').forEach(function(c){c.addEventListener('click',function(){
  document.querySelectorAll('.chip').forEach(function(x){x.setAttribute('aria-pressed',x===c?'true':'false')});
  var f=c.dataset.f;document.querySelectorAll('#dishes .dish').forEach(function(d){d.hidden=!(f==='all'||d.dataset.region===f)});
})});
</script>'''
page("food.html", "Food & Recipes · Latitude Zero", "food", food, script=fscript)

# ---------- QUIZ ----------
QS = [
 ("Your perfect morning in Ecuador starts with…", [("A walk on the beach", "costa"), ("A crisp mountain view and a hot coffee", "sierra"), ("Birdsong in the rainforest", "amazonia"), ("Snorkeling before breakfast", "galapagos")]),
 ("Your family's favorite kind of day out is…", [("Sandcastles and fresh seafood", "costa"), ("Markets, plazas and old churches", "sierra"), ("A river trip and a jungle walk", "amazonia"), ("Spotting animals up close", "galapagos")]),
 ("What weather makes you happiest?", [("Warm and sunny", "costa"), ("Cool mornings, sweater weather", "sierra"), ("Hot, humid and green", "amazonia"), ("Sunny with an ocean breeze", "galapagos")]),
 ("Pick a dinner:", [("Ceviche and patacones", "costa"), ("Hornado and llapingachos", "sierra"), ("Fish grilled in a leaf", "amazonia"), ("Whatever the boat caught today", "galapagos")]),
 ("How do your kids like to travel?", [("Lots of beach time and naps in the shade", "costa"), ("City strolls with a carrier", "sierra"), ("Small adventures, early bedtimes", "amazonia"), ("Big wow moments, worth the trip", "galapagos")]),
]
RES = {
 "costa": ("La Costa", "frailes", "You're coast people: warm days, Pacific beaches and the best seafood in the country.", "Los Frailes, Puerto López and Montañita"),
 "sierra": ("La Sierra", "quilotoa", "You belong in the Andes: colonial cities, volcano views, markets and cool, clear mornings.", "Quito, Cuenca, Quilotoa and Otavalo"),
 "amazonia": ("Amazonía", "tena", "You're made for the rainforest: rivers, waterfalls, wildlife and nights full of sounds.", "Tena, Cuyabeno and Yasuní"),
 "galapagos": ("Galápagos", "santacruz", "You're Galápagos people: once-in-a-lifetime wildlife, right at your kids' eye level.", "Santa Cruz and San Cristóbal"),
}
qhtml = "".join(f'''<fieldset class="q" id="q{i}"><legend><span class="alt">QUESTION {i+1} OF {len(QS)}</span>{q}</legend><div class="opts">{"".join(f'<label class="opt"><input type="radio" name="q{i}" value="{v}"><span>{t}</span></label>' for t, v in opts)}</div></fieldset>''' for i, (q, opts) in enumerate(QS))
rhtml = "".join(f'''<div class="result" data-r="{k}" hidden><img src="img/{img}.jpg" alt="{name}" loading="lazy"><div class="result-body"><span class="eyebrow">Your Ecuador region</span><h2>{name}</h2><p>{d}</p><p class="family-note"><b>Start with:</b> {picks}</p><div class="result-actions"><a class="btn btn-sun" href="ecuador.html#{k}">Explore {name}</a><button class="btn btn-line" type="button" data-copy="My family's Ecuador region is {name}! Find yours on Latitude Zero.">Copy my result</button></div></div></div>''' for k, (name, img, d, picks) in RES.items())
quiz = hero("Region quiz", "Which Ecuador region <em>fits your family?</em>",
  "Five quick questions. Find out whether your family belongs on the coast, in the Andes, in the Amazon or in the Galápagos.") + f'''
<main>
  <section>
    <div class="wrap quiz-wrap">
      <form id="quiz" class="quiz" novalidate>{qhtml}
        <p class="quiz-msg" role="status" hidden>Answer all five questions to see your region.</p>
        <button class="btn btn-sun" type="submit">See my region</button>
      </form>
      <div id="results">{rhtml}
        <button class="link-more" type="button" id="retake" hidden style="background:none;border:0;cursor:pointer;font:inherit;padding:0">Take the quiz again ↺</button>
      </div>
    </div>
  </section>
</main>'''
qscript = '''<script>
(function(){var f=document.getElementById('quiz'),msg=f.querySelector('.quiz-msg'),again=document.getElementById('retake');
f.addEventListener('submit',function(e){e.preventDefault();var score={},n=0;
  for(var i=0;i<''' + str(len(QS)) + ''';i++){var c=f.querySelector('input[name=q'+i+']:checked');if(c){n++;score[c.value]=(score[c.value]||0)+1}}
  if(n<''' + str(len(QS)) + '''){msg.hidden=false;return}
  msg.hidden=true;var best=Object.keys(score).sort(function(a,b){return score[b]-score[a]})[0];
  document.querySelectorAll('.result').forEach(function(r){r.hidden=r.dataset.r!==best});
  f.hidden=true;again.hidden=false;document.getElementById('results').scrollIntoView({behavior:'smooth'});});
again.addEventListener('click',function(){f.reset();f.hidden=false;again.hidden=true;document.querySelectorAll('.result').forEach(function(r){r.hidden=true});f.scrollIntoView()});
document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){var t=b.dataset.copy,l=b.textContent;
  function ok(){b.textContent='Copied';setTimeout(function(){b.textContent=l},1600)}
  try{navigator.clipboard.writeText(t).then(ok,function(){})}catch(e){}})});})();
</script>'''
page("quiz.html", "Region Quiz · Latitude Zero", "quiz", quiz, script=qscript)

# ---------- CHECKLIST ----------
CHECK = [
 ("Documents", ["Valid passports for every family member, including the baby", "Certified copies of birth and marriage certificates", "Check Ecuador's current entry and residency requirements with official sources", "Digital backups of every important document"]),
 ("Health", ["A check-up with your pediatrician before the move", "Copies of everyone's medical and vaccination records", "Ask your pediatrician about altitude and travel with a baby", "Pack enough of any regular prescriptions for the first weeks"]),
 ("Packing", ["Car seat that's approved for flights", "Baby carrier for airports and cobblestones", "Travel crib and familiar bedding for better sleep", "Favorite toys and books, for comfort in a new place", "Layers for cool Andes mornings and sun protection for the equator"]),
 ("Before you leave", ["Forward your mail and update your addresses", "Say proper goodbyes: friends, neighbors, favorite places", "Record a few videos of home, for later", "Plan the first night: where you'll sleep and what you'll eat"]),
 ("First week there", ["Rest. Seriously.", "Register with your embassy if that's recommended for you", "Find the nearest pediatric clinic and pharmacy", "Visit family, and let everyone meet the baby"]),
]
chk = "".join(f'<section class="chk-group"><h2>{g}</h2><ul>{"".join(f"<li><label><input type=checkbox id=chk-{gi}-{ii}><span>{t}</span></label></li>" for ii, t in enumerate(items))}</ul></section>' for gi, (g, items) in enumerate(CHECK))
total = sum(len(i) for _, i in CHECK)
cl = hero("Moving checklist", "Our checklist for moving abroad <em>with a baby</em>",
  "The list we're working through ourselves as we get ready to move to Ecuador. Tick things off as you go. Your progress stays on this device.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="progress flight"><span id="chk-count">0 of {total} done</span><div class="flight-track" aria-hidden="true"><span class="ft-from">Wilkes-Barre</span><div class="bar"><i id="chk-fill"></i><span class="ft-plane">✈</span></div><span class="ft-to">Ecuador</span></div></div>
      <div class="chk-grid">{chk}</div>
      <p class="credit-note">This is our personal list, not legal, immigration or medical advice. Always confirm requirements with official sources and your own doctors.</p>
    </div>
  </section>
</main>'''
cscript = '''<script>
(function(){var boxes=[].slice.call(document.querySelectorAll('.chk-grid input')),K='lz-checklist';var saved={};
try{saved=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
function upd(){var d=boxes.filter(function(b){return b.checked}).length;document.getElementById('chk-count').textContent=d+' of '+boxes.length+' done';document.getElementById('chk-fill').style.width=(d/boxes.length*100)+'%'}
boxes.forEach(function(b){if(saved[b.id])b.checked=true;b.addEventListener('change',function(){saved[b.id]=b.checked;try{localStorage.setItem(K,JSON.stringify(saved))}catch(e){}upd()})});upd();})();
</script>'''
page("checklist.html", "Moving Checklist · Latitude Zero", "checklist", cl, script=cscript)
