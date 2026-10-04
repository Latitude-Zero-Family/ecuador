PLACES = [
  ("sierra","Quito's Historic Center","Pichincha","One of the best-preserved colonial centers in the Americas and the first city named a UNESCO World Heritage Site. Churches, plazas and rooftop views of the volcanoes.","Mostly flat plazas, but the streets are steep. Bring a carrier."),
  ("sierra","Mitad del Mundo","Pichincha","The monument on the equator just north of Quito, plus the Intiñan museum where you can balance an egg on a nail.","A photo of Mateo with one foot in each hemisphere."),
  ("sierra","Cotopaxi National Park","Cotopaxi","One of the world's highest active volcanoes, with a near-perfect snow cone, wild horses and the Limpiopungo lagoon.","High altitude. We'll stay lower and keep the visit short."),
  ("sierra","Quilotoa Lagoon","Cotopaxi","A turquoise crater lake inside a collapsed volcano. The hike down is easy; the climb back up is not.","Viewpoint from the rim, and the hike when Mateo is older."),
  ("sierra","Otavalo Market","Imbabura","The famous Saturday market of Kichwa textiles, weavings and crafts, plus the lakes and waterfalls around town.","Saturday morning, then lunch by Lago San Pablo."),
  ("sierra","Cuenca","Azuay","A UNESCO-listed colonial city with blue-domed cathedrals, four rivers and a big expat community. Home of the Panama hat.","A strong contender for a longer stay."),
  ("sierra","Baños","Tungurahua","The adventure capital, between the Andes and the Amazon. Hot springs, the Pailón del Diablo waterfall and the swing at the end of the world.","Waterfall trails and the hot springs, slowly."),
  ("sierra","Chimborazo","Chimborazo","Ecuador's highest peak. Thanks to the equatorial bulge, its summit is the point on Earth farthest from its center.","Drive to the refuge, take the photo, come back down."),
  ("sierra","Mindo Cloud Forest","Pichincha","Misty forest about two hours from Quito, full of hummingbirds, butterflies, waterfalls and chocolate farms.","High on our list for a first weekend trip."),
  ("sierra","Ingapirca","Cañar","The largest Inca ruins in Ecuador, built around a Cañari site. The Temple of the Sun is the highlight.","An easy day trip from Cuenca."),
  ("sierra","El Cajas National Park","Azuay","Wild páramo with hundreds of glacial lakes, about 45 minutes from Cuenca.","Short lakeside trails near the visitor center."),
  ("costa","Guayaquil & the Malecón 2000","Guayas","Ecuador's largest city. The riverfront Malecón, Las Peñas neighborhood and the 444 steps up Cerro Santa Ana.","The Malecón is stroller-friendly. The 444 steps are on Austin."),
  ("costa","Montañita","Santa Elena","The coast's famous surf town, laid-back by day and lively at night.","Daytime beach and surf lessons for Austin."),
  ("costa","Puerto López & Isla de la Plata","Manabí","Base for humpback whale watching (roughly June to September) and a smaller-scale Galápagos with blue-footed boobies.","Timing the trip for whale season."),
  ("costa","Los Frailes Beach","Manabí","A protected crescent beach inside Machalilla National Park, with no buildings in sight.","A calm-water beach day."),
  ("amazonia","Tena & the Napo River","Napo","The gateway to the Amazon from the highlands. River trips, Kichwa communities and waterfalls.","A lodge stay close to town."),
  ("amazonia","Cuyabeno Wildlife Reserve","Sucumbíos","Flooded forest and blackwater lagoons with pink river dolphins, monkeys and hundreds of bird species.","A trip for when Mateo is older."),
  ("amazonia","Yasuní National Park","Orellana","One of the most biodiverse places on the planet. Deep-jungle lodges and parrot clay licks.","The big Amazon trip, someday."),
  ("galapagos","Santa Cruz Island","Galápagos","The hub of the islands. Giant tortoises in the highlands, the Charles Darwin Research Station and Tortuga Bay.","Our first Galápagos base."),
  ("galapagos","San Cristóbal Island","Galápagos","Sea lions on every bench, Kicker Rock and some of the best snorkeling in the islands.","Sea lions at eye level. Mateo will love it."),
]
COORDS=[(-0.22,-78.51),(-0.002,-78.455),(-0.68,-78.44),(-0.86,-78.90),(0.23,-78.26),(-2.90,-79.00),(-1.40,-78.42),(-1.47,-78.82),(-0.05,-78.77),(-2.54,-78.87),(-2.84,-79.25),(-2.19,-79.88),(-1.83,-80.75),(-1.56,-80.81),(-1.49,-80.79),(-0.99,-77.81),(0.0,-76.2),(-0.9,-76.1),(-0.74,-90.3),(-0.9,-89.6)]
VISITED=set()  # add place numbers here as we visit them
def mp(lat,lon): return ((lon+81.3)*62+10, (1.7-lat)*62+10)
OUTLINE=[(1.45,-78.85),(0.9,-78.2),(0.85,-77.65),(0.4,-77.4),(0.25,-76.7),(0.4,-76.0),(0.1,-75.6),(-0.1,-75.25),(-0.95,-75.2),(-1.55,-75.6),(-2.6,-76.6),(-3.0,-77.85),(-3.4,-78.3),(-4.4,-78.6),(-5.0,-79.0),(-4.6,-79.4),(-4.4,-80.0),(-4.45,-80.45),(-3.4,-80.25),(-3.1,-80.0),(-2.6,-79.85),(-2.3,-80.0),(-2.2,-80.95),(-1.95,-80.75),(-1.4,-80.85),(-0.95,-80.45),(-0.35,-80.45),(0.4,-80.1),(0.8,-80.05),(1.0,-79.6),(1.1,-79.2)]
def gp(lat,lon): return (282+(lon+91.8)*44, 330+(0.7-lat)*44)
ISL=[(-0.6,-91.1,30,20),(-0.35,-91.55,9,8),(-0.25,-90.75,10,7),(-0.65,-90.35,10,8),(-0.85,-89.5,9,6),(-1.28,-90.45,6,5),(-1.38,-89.68,5,4)]
def build_map():
    poly=" ".join(f"{mp(a,b)[0]:.0f},{mp(a,b)[1]:.0f}" for a,b in OUTLINE)
    isl="".join(f'<ellipse cx="{gp(a,b)[0]:.0f}" cy="{gp(a,b)[1]:.0f}" rx="{rx*.5:.0f}" ry="{ry*.5:.0f}" class="land"/>' for a,b,rx,ry in ISL)
    pins=""
    for i,(lat,lon) in enumerate(COORDS,1):
        x,y=(gp(lat,lon) if lon<-85 else mp(lat,lon))
        dx,dy={14:(-16,4),15:(-4,-12)}.get(i,(0,0)); x+=dx; y+=dy
        v=" visited" if i in VISITED else ""
        pins+=f'<a href="#place-{i}" class="pin{v}" aria-label="{i}. {PLACES[i-1][1]}"><circle cx="{x:.0f}" cy="{y:.0f}" r="9"/><text x="{x:.0f}" y="{y+3.5:.0f}">{i}</text></a>'
    return f'''<figure class="map"><svg viewBox="0 0 410 440" role="img" aria-label="Map of Ecuador with our 20 places">
<rect x="270" y="314" width="132" height="118" rx="10" class="inset"/><text x="280" y="428" class="map-label">GALÁPAGOS</text>
<polygon points="{poly}" class="land"/>{isl}
<line x1="0" y1="{mp(0,-81)[1]:.0f}" x2="410" y2="{mp(0,-81)[1]:.0f}" class="eq"/><text x="404" y="{mp(0,-81)[1]-6:.0f}" class="map-label eq-label" text-anchor="end">EQUATOR 0°</text>
{pins}</svg><figcaption><span class="key"><i class="k-plan"></i>Planned</span><span class="key"><i class="k-done"></i>Visited</span><span>Map is simplified, not to scale.</span></figcaption></figure>'''

LABEL = {"sierra":"Highlands","costa":"Coast","amazonia":"Amazon","galapagos":"Galápagos"}

IMGS=["quito","mitad","cotopaxi","quilotoa","otavalo","cuenca","banos","chimborazo","mindo","ingapirca","cajas","guayaquil","montanita","isla","frailes","tena","cuyabeno","yasuni","santacruz","sancristobal"]
rows = "".join(f'''<li class="place" id="place-{i}" data-region="{r}">
  <span class="num">{i:02d}</span>
  <img class="place-img" src="img/{IMGS[i-1]}.jpg" alt="{name}" loading="lazy">
  <div><h3>{name}</h3><span class="where">{LABEL[r].upper()}{" · " + where if where != LABEL[r] else ""}</span><p>{desc}</p><p class="family-note"><b>Our plan:</b> {note}</p></div>
  <span class="status{' visited' if i in VISITED else ''}">{'Visited' if i in VISITED else 'Planned'}</span>
</li>''' for i,(r,name,where,desc,note) in enumerate(PLACES,1))

top = hero("Top 20 places", "20 places we <em>plan to visit</em>",
  "Our list of the places we most want to see in Ecuador, from the Andes to the Galápagos. We'll mark each one as we go and write it up in the journal.") + f'''
<main>
  <section>
    <div class="wrap">
      <div class="map-grid">
        {build_map()}
        <div class="vote-card">
          <span class="eyebrow">Your vote</span>
          <h2>Where should we go first?</h2>
          <p>Pick the place you think we should visit first. We'll announce the winner on Instagram at @latitudezerofamily.</p>
          <label for="vote-pick" class="sr">Choose a place</label>
          <select id="vote-pick"><option value="">Choose a place…</option>{''.join(f'<option value="{i}">{i}. {p[1]}</option>' for i,p in enumerate(PLACES,1))}</select>
          <button class="btn btn-sun" type="button" id="vote-btn">Cast my vote</button>
          <p class="vote-msg" role="status" hidden></p>
          <div class="progress" style="margin:8px 0 0"><span id="count">0 of 20 visited</span><div class="bar" aria-hidden="true"><i id="fill"></i></div></div>
        </div>
      </div>
      <div class="chips" role="group" aria-label="Filter by region">
        <button class="chip" type="button" data-f="all" aria-pressed="true">All 20</button>
        <button class="chip" type="button" data-f="sierra" aria-pressed="false">Highlands</button>
        <button class="chip" type="button" data-f="costa" aria-pressed="false">Coast</button>
        <button class="chip" type="button" data-f="amazonia" aria-pressed="false">Amazon</button>
        <button class="chip" type="button" data-f="galapagos" aria-pressed="false">Galápagos</button>
        <button class="chip surprise" type="button" id="surprise">Surprise me ✦</button>
      </div>
      <ol class="places" id="places">{rows}</ol>
    </div>
  </section>
</main>'''
tscript = '''<script>
(function(){
  var all=document.querySelectorAll('#places .place'),v=document.querySelectorAll('#places .status.visited').length;
  document.getElementById('count').textContent=v+' of '+all.length+' visited';
  document.getElementById('fill').style.width=(v/all.length*100)+'%';
  var vb=document.getElementById('vote-btn'),vs=document.getElementById('vote-pick'),vm=document.querySelector('.vote-msg');
  try{var prev=localStorage.getItem('lz-vote');if(prev){vs.value=prev}}catch(e){}
  vb.addEventListener('click',function(){if(!vs.value){vm.hidden=false;vm.textContent='Choose a place first.';return}
    try{localStorage.setItem('lz-vote',vs.value)}catch(e){}
    var name=vs.options[vs.selectedIndex].text.replace(/^\d+\. /,'');vm.hidden=false;vm.textContent='Your pick: '+name+'. Tell us why on Instagram @latitudezerofamily!';});
  document.querySelectorAll('.chip').forEach(function(c){c.addEventListener('click',function(){
    var vb=document.getElementById('vote-btn'),vs=document.getElementById('vote-pick'),vm=document.querySelector('.vote-msg');
  try{var prev=localStorage.getItem('lz-vote');if(prev){vs.value=prev}}catch(e){}
  vb.addEventListener('click',function(){if(!vs.value){vm.hidden=false;vm.textContent='Choose a place first.';return}
    try{localStorage.setItem('lz-vote',vs.value)}catch(e){}
    var name=vs.options[vs.selectedIndex].text.replace(/^\d+\. /,'');vm.hidden=false;vm.textContent='Your pick: '+name+'. Tell us why on Instagram @latitudezerofamily!';});
  document.querySelectorAll('.chip').forEach(function(x){x.setAttribute('aria-pressed',x===c?'true':'false')});
    var f=c.dataset.f;all.forEach(function(p){p.hidden=!(f==='all'||p.dataset.region===f)});
  })});
})();
</script>'''
page("top-20.html", "Top 20 Places · Latitude Zero", "top20", top, script=tscript)
