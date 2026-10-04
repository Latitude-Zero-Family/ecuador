HERO_PHOTO.update({"Trip planner": "frailes", "Festival calendar": "f_colada", "Reader stories": "otavalo"})

# ---------- TRIP PLANNER ----------
# cluster order = the route we'd actually travel; cost in days; tags drive the scoring
P = {  # num: (cluster, cost, tags, no_baby)
 1: ("quito", 1, "culture food", False), 2: ("quito", .5, "culture", False),
 5: ("north", 1, "culture food", False), 9: ("north", 1, "wildlife rainforest", False),
 3: ("volc", 1, "mountains", False), 4: ("volc", 1, "mountains", False),
 7: ("banos", 2, "mountains food rainforest", False), 8: ("banos", .5, "mountains", True),
 16: ("amazon", 2, "rainforest wildlife", False), 17: ("amazon", 3, "rainforest wildlife", True), 18: ("amazon", 3, "rainforest wildlife", True),
 6: ("south", 2, "culture food", False), 10: ("south", .5, "culture", False), 11: ("south", .5, "mountains", False),
 12: ("coast", 1, "culture food", False), 13: ("coast", 1, "beaches", False), 14: ("coast", 1, "beaches wildlife", False), 15: ("coast", .5, "beaches", False),
 19: ("gal", 2, "wildlife beaches", False), 20: ("gal", 2, "wildlife beaches", False),
}
pdata = "".join(f'<li data-n="{n}" data-c="{c}" data-cost="{cost}" data-tags="{t}" data-nobaby="{1 if nb else 0}"><b>{PLACES[n-1][1]}</b><span>{PLACES[n-1][3].split('. ')[0].rstrip('.')}.</span></li>' for n, (c, cost, t, nb) in P.items())
CL = [("quito", "Quito"), ("north", "Otavalo &amp; Mindo"), ("volc", "Avenue of the Volcanoes"), ("banos", "Baños"), ("amazon", "the Amazon"), ("south", "Cuenca"), ("coast", "the Pacific coast"), ("gal", "Galápagos")]
cdata = "".join(f'<li data-c="{k}">{v}</li>' for k, v in CL)
STR = {"day": "Day", "travel": "Travel day", "travel_to": "Travel to", "rest": "Rest day", "rest_note": "A slow day with no plans. Naps, a park, a long lunch. Little travelers need these.",
       "free": "Free day", "free_note": "Room to explore, revisit a favorite or simply rest.", "fly": "Fly to the Galápagos", "fly_note": "Flights leave from Quito or Guayaquil. Arrive, settle in and see the harbor.",
       "home": "Head home", "home_note": "Back to Quito or Guayaquil for your flight.", "arrive": "Arrive in Quito", "arrive_note": "Land, rest and let everyone adjust to the altitude.",
       "summary": "Your {d}-day family plan", "nogal": "The Galápagos need at least 7 days, so we left them out of this plan.",
       "copied": "Copied", "copy": "Copy my plan", "tip": "Why go:", "baby_note": "We skipped the deep jungle lodges and Chimborazo's high refuge, which aren't a good fit for babies and toddlers."}
sdata = "".join(f'<span data-k="{k}">{v}</span>' for k, v in STR.items())

planner = hero("Trip planner", "Plan your family trip <em>to Ecuador</em>",
  "Tell us how long you have, who's coming and what you love. We'll sketch a day-by-day plan from our Top 20 places.") + f'''
<main>
  <section>
    <div class="wrap planner-grid">
      <form id="planner" class="planner" novalidate>
        <div class="field"><label for="pl-days">How many days?</label>
          <div class="range-row"><input type="range" id="pl-days" min="3" max="21" value="10"><output id="pl-days-out" for="pl-days">10</output></div></div>
        <fieldset class="field"><legend>Who's coming?</legend>
          <div class="seg">
            <label><input type="radio" name="pl-kids" value="baby" checked><span>Baby or toddler</span></label>
            <label><input type="radio" name="pl-kids" value="kids"><span>Kids 4–12</span></label>
            <label><input type="radio" name="pl-kids" value="teens"><span>Teens or adults</span></label>
          </div></fieldset>
        <fieldset class="field"><legend>What do you love? <small>Pick any</small></legend>
          <div class="tags">
            <label><input type="checkbox" name="pl-tag" value="beaches" checked><span>Beaches</span></label>
            <label><input type="checkbox" name="pl-tag" value="mountains" checked><span>Mountains &amp; volcanoes</span></label>
            <label><input type="checkbox" name="pl-tag" value="wildlife"><span>Wildlife</span></label>
            <label><input type="checkbox" name="pl-tag" value="culture" checked><span>Culture &amp; markets</span></label>
            <label><input type="checkbox" name="pl-tag" value="food"><span>Food</span></label>
            <label><input type="checkbox" name="pl-tag" value="rainforest"><span>Rainforest</span></label>
          </div></fieldset>
        <fieldset class="field"><legend>Pace</legend>
          <div class="seg">
            <label><input type="radio" name="pl-pace" value="relaxed" checked><span>Relaxed</span></label>
            <label><input type="radio" name="pl-pace" value="active"><span>Active</span></label>
          </div></fieldset>
        <label class="toggle"><input type="checkbox" id="pl-gal"><span>Include the Galápagos</span></label>
        <button class="btn btn-sun" type="submit">Build my plan</button>
      </form>
      <div class="plan" id="plan" aria-live="polite">
        <div class="plan-empty"><span class="eyebrow">Your plan</span><h2>Your days will appear here</h2><p>Choose your options and press "Build my plan." Change anything and build again as often as you like.</p></div>
      </div>
    </div>
    <div class="wrap"><p class="credit-note">This is a starting point built from our own bucket list, not a booking. Check travel times, opening hours and current travel advice, and ask your pediatrician about altitude before you go.</p></div>
    <ul hidden id="pl-places">{pdata}</ul><ul hidden id="pl-clusters">{cdata}</ul><div hidden id="pl-str">{sdata}</div>
  </section>
</main>'''
pscript = r'''<script>
(function(){
var f=document.getElementById('planner'),out=document.getElementById('plan'),days=document.getElementById('pl-days'),dout=document.getElementById('pl-days-out');
var S={};[].forEach.call(document.querySelectorAll('#pl-str span'),function(s){S[s.dataset.k]=s.textContent});
var CN={},ORDER=[];[].forEach.call(document.querySelectorAll('#pl-clusters li'),function(l){CN[l.dataset.c]=l.textContent;ORDER.push(l.dataset.c)});
var PL=[].map.call(document.querySelectorAll('#pl-places li'),function(l){return{n:+l.dataset.n,c:l.dataset.c,cost:+l.dataset.cost,tags:l.dataset.tags.split(' '),nobaby:l.dataset.nobaby==='1',name:l.querySelector('b').textContent,tip:l.querySelector('span').textContent}});
days.addEventListener('input',function(){dout.textContent=days.value});
function build(){
  var D=+days.value,kids=f.querySelector('[name=pl-kids]:checked').value,pace=f.querySelector('[name=pl-pace]:checked').value,gal=document.getElementById('pl-gal').checked;
  var tags=[].map.call(f.querySelectorAll('[name=pl-tag]:checked'),function(x){return x.value});if(!tags.length)tags=['culture','mountains','beaches'];
  var small=kids==='baby',mult=1;
  var galNote=gal&&D<7;if(galNote)gal=false;
  var M=Math.max(0,D-2),rest=pace==='relaxed'?Math.floor(M/(kids==='teens'?7:4)):0,H=(M-rest)*2;
  function halves(p){return Math.max(1,Math.round(p.cost*mult*2))}
  function tcost(c){return c==='gal'?2:1}
  var places=PL.filter(function(p){return!(small&&p.nobaby)&&(gal||p.c!=='gal')});
  places.forEach(function(p){p.score=p.tags.filter(function(t){return tags.indexOf(t)>-1}).length+(p.c==='quito'?5:0)+(p.n===1?2:0)+(p.c==='gal'?4:0)});
  var on={quito:true},picked=[];
  function tryAdd(p){if(picked.indexOf(p)>-1)return;var c=halves(p)+(on[p.c]?0:tcost(p.c));if(c<=H){H-=c;on[p.c]=true;picked.push(p)}}
  places.slice().sort(function(a,b){return b.score-a.score||a.cost-b.cost}).forEach(function(p){if(p.score>0)tryAdd(p)});
  places.filter(function(p){return on[p.c]}).sort(function(a,b){return a.cost-b.cost}).forEach(tryAdd);
  picked.sort(function(a,b){return ORDER.indexOf(a.c)-ORDER.indexOf(b.c)||a.n-b.n});
  // units of half-days, in travel order
  var units=[],cur='quito';
  picked.forEach(function(p){if(p.c!==cur){units.push({travel:1,c:p.c,h:tcost(p.c)});cur=p.c}units.push({p:p,h:halves(p)})});
  var plan=[{t:S.arrive,note:S.arrive_note,travel:1}],day=null,count=0;
  function close(){if(!day)return;
    var labels=[],links=[],note='';
    day.parts.forEach(function(u){var lab=u.travel?(u.c==='gal'?S.fly:S.travel_to+' '+CN[u.c]):u.p.name;if(labels.indexOf(lab)<0){labels.push(lab);links.push(u.travel?0:u.p.n)}
      if(!note&&!u.travel&&!u.seen)note=u.p.tip;if(!u.travel)u.seen=1;if(!note&&u.travel&&u.c==='gal')note=S.fly_note});
    plan.push({labels:labels,links:links,note:note,travel:day.parts.every(function(u){return u.travel})});day=null;count++;
    if(rest&&count%4===0){plan.push({t:S.rest,note:S.rest_note,rest:1});rest--}}
  units.forEach(function(u){if(u.travel&&u.c==='gal'&&day)close();var left=u.h;while(left>0){if(!day)day={parts:[],used:0};var take=Math.min(2-day.used,left);day.parts.push(u);day.used+=take;left-=take;if(day.used>=2)close()}});
  close();
  while(rest>0){plan.push({t:S.rest,note:S.rest_note,rest:1});rest--}
  while(plan.length<D-1)plan.push({t:S.free,note:S.free_note,rest:1});
  plan.push({t:S.home,note:S.home_note,travel:1});
  render(plan,D,galNote,small);
}
function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
var lastText='';
function render(plan,D,galNote,small){
  var h='<span class="eyebrow">'+esc(S.summary.replace('{d}',D))+'</span><ol class="days">',txt=S.summary.replace('{d}',D)+'\n\n';
  plan.forEach(function(d,i){
    var labels=d.labels||[d.t],links=d.links||[0];
    var title=labels.map(function(l,k){return links[k]?'<a href="top-20.html#place-'+links[k]+'">'+esc(l)+'</a>':esc(l)}).join(' + ');
    var hasPlace=links.some(function(x){return x});
    var note=d.note?(hasPlace?'<p><b>'+esc(S.tip)+'</b> '+esc(d.note)+'</p>':'<p>'+esc(d.note)+'</p>'):'';
    d.t=labels.join(' + ');var extra='';
    h+='<li class="day'+(d.travel?' is-travel':'')+(d.rest?' is-rest':'')+'" style="--i:'+i+'"><span class="day-n">'+esc(S.day)+' '+(i+1)+'</span><div><h3>'+title+extra+'</h3>'+note+'</div></li>';
    txt+=S.day+' '+(i+1)+': '+d.t+'\n';
  });
  h+='</ol>';
  if(galNote)h+='<p class="plan-note">'+esc(S.nogal)+'</p>';
  if(small)h+='<p class="plan-note">'+esc(S.baby_note)+'</p>';
  h+='<div class="plan-actions"><button type="button" class="btn btn-line" id="pl-copy">'+esc(S.copy)+'</button></div>';
  out.innerHTML=h;lastText=txt;
  document.getElementById('pl-copy').addEventListener('click',function(){var b=this;try{navigator.clipboard.writeText(lastText).then(function(){b.textContent=S.copied;setTimeout(function(){b.textContent=S.copy},1600)},function(){})}catch(e){}});
  if(window.innerWidth<900)out.scrollIntoView({behavior:'smooth',block:'start'});
}
f.addEventListener('submit',function(e){e.preventDefault();build()});
})();
</script>'''
page("trip-planner.html", "Trip Planner · Latitude Zero", "planner", planner, script=pscript)

# ---------- FESTIVAL CALENDAR ----------
FEST = [
 (2, "Carnaval", "Everywhere, famously Guaranda", "Water balloons, foam and music for two days before Lent. Expect to get wet. Kids love it.", "Dates change each year", "f_colada"),
 (2, "Fiesta de las Flores y las Frutas", "Ambato", "Parades of floats covered in flowers and fruit, held around Carnaval.", "Dates change each year", "quilotoa"),
 (3, "Semana Santa", "Quito and across the country", "Holy Week. Families make fanesca, and Quito's Good Friday procession fills the historic center.", "March or April, dates change", "f_fanesca"),
 (6, "Inti Raymi", "Otavalo, Cotacachi and Imbabura", "The Andean festival of the sun around the June solstice, with music and dancing in the streets.", "Around June 21", "otavalo"),
 (6, "Humpback whale season begins", "Puerto López and the Manabí coast", "Humpback whales arrive to breed off the coast. Not a festival, but a family highlight.", "About June to September", "isla"),
 (7, "Fiestas de Guayaquil", "Guayaquil", "Celebrations for the city's founding, with concerts and events along the Malecón.", "Late July", "guayaquil"),
 (8, "Primer Grito de Independencia", "Quito and nationwide", "A national holiday marking Ecuador's first call for independence in 1809.", "August 10", "quito"),
 (9, "Mama Negra", "Latacunga", "One of Ecuador's most colorful festivals, with costumed dancers and a famous procession.", "September, and again in November", "cotopaxi"),
 (10, "Independence of Guayaquil", "Guayaquil", "A national holiday celebrating the city's independence in 1820.", "October 9", "guayaquil"),
 (11, "Día de los Difuntos", "Nationwide", "Families remember loved ones, drink colada morada and share guaguas de pan.", "November 2", "f_colada"),
 (11, "Independence of Cuenca", "Cuenca", "The day after Día de los Difuntos, Cuenca celebrates with parades and fairs.", "November 3", "cuenca"),
 (12, "Fiestas de Quito", "Quito", "A week of music, parades and neighborhood parties for the city's founding.", "Early December", "quito"),
 (12, "Pase del Niño Viajero", "Cuenca", "One of the largest Christmas Eve processions in Latin America, full of costumed children.", "December 24", "cuenca"),
 (12, "Año Viejo", "Nationwide", "At midnight on New Year's Eve, families burn life-size effigies of the old year.", "December 31", "mitad"),
]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
fcards = "".join(f'''<article class="fest" data-m="{m}"><img src="img/{img}.jpg" alt="{name}" loading="lazy"><div class="fest-body"><span class="alt">{MONTHS[m-1].upper()} · {when}</span><h3>{name}</h3><span class="where">{where}</span><p>{d}</p></div></article>''' for m, name, where, d, when, img in FEST)
mchips = "".join(f'<button class="chip" type="button" data-m="{i}" aria-pressed="false">{MONTHS[i-1][:3]}</button>' for i in range(1, 13))
fest = hero("Festival calendar", "Ecuador's <em>festival calendar</em>",
  "The celebrations and seasons we can't wait to experience with Mateo, month by month.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="next-up" id="next-up" hidden><span class="eyebrow">Coming up next</span><b id="next-name"></b><span id="next-when"></span><button type="button" class="fiesta-btn" id="fiesta">¡Fiesta!</button></div>
      <div class="chips" role="group" aria-label="Filter by month"><button class="chip" type="button" data-m="all" aria-pressed="true">All</button>{mchips}</div>
      <div class="fests" id="fests">{fcards}</div>
      <p class="credit-note">Some festivals move each year, and local dates can change. Check with the town before you plan a trip around one.</p>
    </div>
  </section>
</main>'''
fscript2 = '''<script>
(function(){var cards=[].slice.call(document.querySelectorAll('.fest'));
document.querySelectorAll('.chips .chip').forEach(function(c){c.addEventListener('click',function(){
  document.querySelectorAll('.chips .chip').forEach(function(x){x.setAttribute('aria-pressed',x===c?'true':'false')});
  var m=c.dataset.m;cards.forEach(function(k){k.hidden=!(m==='all'||k.dataset.m===m)})})});
var now=new Date().getMonth()+1,next=cards.filter(function(k){return +k.dataset.m>=now})[0]||cards[0];
if(next){var n=document.getElementById('next-up');n.hidden=false;document.getElementById('next-name').textContent=next.querySelector('h3').textContent;
document.getElementById('next-when').textContent=next.querySelector('.alt').textContent;next.classList.add('is-next');}})();
</script>'''
page("festivals.html", "Festival Calendar · Latitude Zero", "festivals", fest, script=fscript2)

# ---------- READER STORIES + CONTRIBUTOR FORM ----------
stories = hero("Reader stories", "Share your family's <em>Ecuador story</em>",
  "We're building a space for families who've moved to, grown up in or traveled through Ecuador. Tell us yours.") + '''
<main>
  <section>
    <div class="wrap story-grid">
      <div class="story-copy">
        <h2 style="font-size:1.9rem">Reader stories</h2>
        <p>No reader stories have been published yet. Yours could be the first.</p>
        <p>We're looking for real experiences from real families: moving to Ecuador, raising kids there, traveling the country with little ones, or growing up Ecuadorian at home or abroad. Stories can be in English or Spanish.</p>
      </div>
      <div class="family" aria-label="Guidelines">
        <span class="eyebrow" style="padding-bottom:10px">Before you send</span>
        <div class="member"><span class="initial">1</span><div><b>Your own experience</b><span>First-hand stories only, in your own words.</span></div></div>
        <div class="member"><span class="initial">2</span><div><b>Your own photos</b><span>Only photos you took or have permission to share.</span></div></div>
        <div class="member"><span class="initial">3</span><div><b>No paid promotion</b><span>Brands and businesses can reach us through partnerships instead.</span></div></div>
        <div class="member"><span class="initial">4</span><div><b>We may edit</b><span>For length and clarity, and we'll check with you before publishing.</span></div></div>
      </div>
    </div>
  </section>
  <section class="regions-bg" id="contribute">
    <div class="wrap contrib-wrap">
      <div class="sec-head"><span class="eyebrow">Become a contributor</span><h2>Pitch your story</h2><p>Fill this in and we'll put it together for you to send. We read every pitch.</p></div>
      <form id="contrib" class="contrib" novalidate>
        <div class="two">
          <div class="field"><label for="c-name">Your name</label><input id="c-name" required autocomplete="name"></div>
          <div class="field"><label for="c-email">Email</label><input id="c-email" type="email" required autocomplete="email"></div>
        </div>
        <div class="two">
          <div class="field"><label for="c-from">Where your family is from</label><input id="c-from" placeholder="e.g. Ohio, USA or Loja, Ecuador"></div>
          <div class="field"><label for="c-family">Who's in your family?</label><input id="c-family" placeholder="e.g. 2 adults, kids aged 3 and 6"></div>
        </div>
        <div class="field"><label for="c-type">Your story is about…</label>
          <select id="c-type"><option>Moving to Ecuador</option><option>Traveling Ecuador with kids</option><option>Growing up Ecuadorian</option><option>Ecuadorian food or traditions</option><option>Something else</option></select></div>
        <div class="field"><label for="c-title">Working title</label><input id="c-title" required placeholder="e.g. Our first month in Cuenca with twins"></div>
        <div class="field"><label for="c-pitch">Tell us about it <small>A few sentences is perfect</small></label><textarea id="c-pitch" rows="6" required></textarea><span class="pitch-meter" id="pitch-meter" aria-live="polite"></span></div>
        <div hidden id="pm-str"><span data-k="0">Start with a hello.</span><span data-k="1">Nice start. Tell us a bit more.</span><span data-k="2">Perfect. That's a great pitch length.</span><span data-k="3">Lots of detail! Feel free to save some for the full story.</span></div>
        <label class="consent"><input type="checkbox" id="c-ok" required><span>This is my own experience, and I'm happy for Latitude Zero to contact me about it.</span></label>
        <p class="form-msg" role="status" hidden id="c-err">Please fill in your name, email, title and story, and tick the box.</p>
        <button class="btn btn-sun" type="submit">Prepare my pitch</button>
      </form>
      <div class="contrib-done" id="contrib-done" hidden>
        <span class="eyebrow">Almost done</span>
        <h3>Send your pitch to us</h3>
        <p>Copy your pitch below and email it to us. We'll reply by email, and ask for photos if your story is a fit.</p>
        <div class="copy-row" style="margin-top:0"><code id="email">hola@latitudezerofamily.com</code><button class="btn btn-line" type="button" id="copy">Copy email</button></div>
        <textarea id="c-out" rows="9" readonly></textarea>
        <div class="copy-row" style="margin-top:0"><button class="btn btn-sun" type="button" id="c-copy">Copy my pitch</button><a class="btn btn-line" id="c-mail" href="#">Open in email app</a></div>
      </div>
      <div hidden id="c-str"><span data-k="subj">Story pitch:</span><span data-k="name">Name</span><span data-k="from">From</span><span data-k="family">Family</span><span data-k="type">About</span><span data-k="title">Title</span><span data-k="pitch">Pitch</span><span data-k="copied">Copied</span><span data-k="copy">Copy my pitch</span></div>
    </div>
  </section>
</main>'''
cscript2 = '''<script>
(function(){var f=document.getElementById('contrib'),S={};[].forEach.call(document.querySelectorAll('#c-str span'),function(s){S[s.dataset.k]=s.textContent});
function v(id){return document.getElementById(id).value.trim()}
f.addEventListener('submit',function(e){e.preventDefault();
  var ok=v('c-name')&&/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v('c-email'))&&v('c-title')&&v('c-pitch')&&document.getElementById('c-ok').checked;
  document.getElementById('c-err').hidden=!!ok;if(!ok)return;
  var t=S.title+': '+v('c-title')+'\\n'+S.name+': '+v('c-name')+' ('+v('c-email')+')\\n'+S.from+': '+v('c-from')+'\\n'+S.family+': '+v('c-family')+'\\n'+S.type+': '+document.getElementById('c-type').value+'\\n\\n'+S.pitch+':\\n'+v('c-pitch');
  document.getElementById('c-out').value=t;
  document.getElementById('c-mail').href='mailto:hola@latitudezerofamily.com?subject='+encodeURIComponent(S.subj+' '+v('c-title'))+'&body='+encodeURIComponent(t);
  f.hidden=true;var d=document.getElementById('contrib-done');d.hidden=false;d.scrollIntoView({behavior:'smooth',block:'start'})});
document.getElementById('c-copy').addEventListener('click',function(){var b=this,o=document.getElementById('c-out');
  try{navigator.clipboard.writeText(o.value).then(function(){b.textContent=S.copied;setTimeout(function(){b.textContent=S.copy},1600)},function(){o.select()})}catch(e){o.select()}});
})();
</script>'''
page("reader-stories.html", "Reader Stories · Latitude Zero", "stories", stories, script=cscript2 + wscript)
