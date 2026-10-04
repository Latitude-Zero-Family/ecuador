/* Latitude Zero — playful layer: doodles, critters and little surprises */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  function svg(markup, cls) { var w = document.createElement('span'); w.className = cls; w.setAttribute('aria-hidden', 'true'); w.innerHTML = markup; return w; }

  /* hand-drawn squiggle under the highlighted words in every banner */
  var SQ = '<svg viewBox="0 0 200 16" preserveAspectRatio="none"><path d="M3 10 C 22 2, 38 2, 52 9 S 84 16, 100 8 S 134 1, 150 8 S 182 15, 197 6" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>';
  $$('.hero h1 em, .page-hero h1 em').forEach(function (em) { em.classList.add('sq-host'); em.appendChild(svg(SQ, 'squiggle')); });

  var hero = $('.hero');
  if (hero) {
    /* spinning sun, drifting clouds, a hummingbird that zips across now and then */
    var SUN = '<svg viewBox="0 0 100 100"><g class="rays" stroke="currentColor" stroke-width="5" stroke-linecap="round">' +
      [0,45,90,135,180,225,270,315].map(function (a) { return '<line x1="50" y1="8" x2="50" y2="20" transform="rotate(' + a + ' 50 50)"/>'; }).join('') +
      '</g><circle cx="50" cy="50" r="22" fill="currentColor"/><path d="M41 52 Q50 61 59 52" fill="none" stroke="#1b1a10" stroke-width="3.5" stroke-linecap="round"/><circle cx="42" cy="44" r="2.8" fill="#1b1a10"/><circle cx="58" cy="44" r="2.8" fill="#1b1a10"/></svg>';
    var CLOUD = '<svg viewBox="0 0 120 50"><path d="M20 42 Q4 42 6 30 Q8 18 24 21 Q28 6 46 9 Q60 0 72 13 Q90 6 96 22 Q114 22 112 34 Q110 44 96 42 Z" fill="currentColor"/></svg>';
    var BIRD = '<svg viewBox="0 0 80 50"><g class="hb-body"><path d="M30 26 Q44 18 58 24 Q50 32 34 32 Z" fill="currentColor"/><path d="M58 24 L78 20" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><path d="M32 30 L18 40 L28 32 Z" fill="currentColor"/><circle cx="53" cy="24" r="1.8" fill="#0f3b3a"/></g>' +
      '<path class="hb-wing" d="M42 22 Q34 2 22 6 Q30 16 40 26 Z" fill="currentColor" opacity=".85"/></svg>';
    var layer = document.createElement('div'); layer.className = 'doodles'; layer.setAttribute('aria-hidden', 'true');
    layer.appendChild(svg(SUN, 'dd dd-sun'));
    layer.appendChild(svg(CLOUD, 'dd dd-cloud c1')); layer.appendChild(svg(CLOUD, 'dd dd-cloud c2'));
    layer.appendChild(svg(BIRD, 'dd dd-bird'));
    hero.appendChild(layer);
    if (fine && !reduce) hero.addEventListener('mousemove', function (e) {
      var r = hero.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      layer.style.setProperty('--px', (x * 18).toFixed(1) + 'px'); layer.style.setProperty('--py', (y * 12).toFixed(1) + 'px');
    });
    // surprise: tap the sun
    var sun = $('.dd-sun', layer);
    sun.style.pointerEvents = 'auto'; sun.style.cursor = 'pointer';
    sun.addEventListener('click', function () { sun.classList.remove('spin'); void sun.offsetWidth; sun.classList.add('spin'); toast('¡Achachay! ☼'); });
  }
  /* small sun + cloud on inner banners too */
  $$('.page-hero.has-photo').forEach(function (h) {
    var l = document.createElement('div'); l.className = 'doodles mini'; l.setAttribute('aria-hidden', 'true');
    l.innerHTML = '<span class="dd dd-cloud c1"><svg viewBox="0 0 120 50"><path d="M20 42 Q4 42 6 30 Q8 18 24 21 Q28 6 46 9 Q60 0 72 13 Q90 6 96 22 Q114 22 112 34 Q110 44 96 42 Z" fill="currentColor"/></svg></span>';
    h.appendChild(l);
  });

  /* a tortoise strolls along the top of the footer */
  var foot = $('.site-footer');
  if (foot) {
    var T = '<svg viewBox="0 0 120 64"><g class="t-legs" fill="#5f8f6e"><rect class="leg l1" x="30" y="44" width="10" height="14" rx="4"/><rect class="leg l2" x="76" y="44" width="10" height="14" rx="4"/></g>' +
      '<g class="t-head"><ellipse cx="104" cy="40" rx="11" ry="8" fill="#5f8f6e"/><circle cx="108" cy="37" r="1.8" fill="#0f3b3a"/><path d="M103 44 Q108 46 112 43" stroke="#0f3b3a" stroke-width="1.5" fill="none" stroke-linecap="round"/></g>' +
      '<path d="M18 48 Q20 10 58 8 Q96 10 98 48 Z" fill="#c9a24a"/><path d="M38 47 L44 26 L58 18 L72 26 L78 47 M44 26 L72 26 M58 18 L58 8" stroke="#8a6a24" stroke-width="2.5" fill="none" stroke-linejoin="round"/>' +
      '<rect x="14" y="44" width="88" height="7" rx="3.5" fill="#a8843a"/><path d="M18 46 Q8 46 4 40" stroke="#5f8f6e" stroke-width="5" stroke-linecap="round" fill="none"/></svg>';
    var walk = document.createElement('div'); walk.className = 'tortoise-track'; walk.setAttribute('aria-hidden', 'true');
    var tort = svg(T, 'tortoise'); walk.appendChild(tort); foot.insertBefore(walk, foot.firstChild);
    tort.addEventListener('click', function () { tort.classList.add('hide'); toast('¡Hola!'); setTimeout(function () { tort.classList.remove('hide'); }, 1800); });
  }

  /* a little plane flies the South America route as you scroll */
  $$('.route .stops').forEach(function (route) {
    var plane = svg('<svg viewBox="0 0 32 32"><path d="M16 2 L19 13 L30 18 L30 21 L19 18 L18 26 L22 29 L22 31 L16 29.5 L10 31 L10 29 L14 26 L13 18 L2 21 L2 18 L13 13 Z" fill="currentColor"/></svg>', 'route-plane');
    route.appendChild(plane);
    function fly() {
      var r = route.getBoundingClientRect(), vh = window.innerHeight;
      var p = Math.min(1, Math.max(0, (vh * 0.7 - r.top) / (r.height || 1)));
      plane.style.top = (p * Math.max(0, r.height - 28)) + 'px';
    }
    window.addEventListener('scroll', function () { requestAnimationFrame(fly); }, { passive: true }); fly();
  });

  /* squiggle that draws under each section heading as it arrives */
  $$('.sec-head h2, .chk-group h2, .story-copy h2').forEach(function (h) { h.classList.add('draw-line'); });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('drawn'); io.unobserve(e.target); } }); }, { threshold: 0.6 });
    $$('.draw-line').forEach(function (h) { io.observe(h); });
  } else $$('.draw-line').forEach(function (h) { h.classList.add('drawn'); });

  /* chips and toggles give a little jelly bounce */
  document.addEventListener('click', function (e) {
    var c = e.target.closest && e.target.closest('.chip, .seg label, .tags label, .opt, .share');
    if (!c || reduce) return; c.classList.remove('jelly'); void c.offsetWidth; c.classList.add('jelly');
  });

  /* tiny toast for surprises */
  function toast(msg) {
    var t = document.createElement('div'); t.className = 'play-toast'; t.textContent = msg; t.setAttribute('role', 'status');
    document.body.appendChild(t); setTimeout(function () { t.classList.add('out'); }, 1400); setTimeout(function () { t.remove(); }, 1900);
  }

  /* secret: type "ecuador" anywhere for a burst of tiny suns */
  var buf = '';
  document.addEventListener('keydown', function (e) {
    if (e.target.closest && e.target.closest('input, textarea, select')) return;
    buf = (buf + (e.key || '')).slice(-7).toLowerCase();
    if (buf === 'ecuador' && !reduce) {
      for (var i = 0; i < 24; i++) (function (i) {
        var s = document.createElement('span'); s.className = 'sun-pop'; s.setAttribute('aria-hidden', 'true');
        s.style.left = (Math.random() * 100) + 'vw'; s.style.animationDelay = (i * 40) + 'ms'; s.style.setProperty('--s', (0.6 + Math.random() * 0.9).toFixed(2));
        document.body.appendChild(s); setTimeout(function () { s.remove(); }, 2600);
      })(i);
      toast('¡Viva Ecuador!');
    }
  });
})();
