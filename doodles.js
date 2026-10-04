/* Latitude Zero — one themed doodle and touch per page */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var m = document.querySelector('meta[name="lz-page"]');
  var id = (m && m.content) || 'index';
  id = id.replace(/-es$/, ''); if (id === 'es') id = 'index';
  document.documentElement.setAttribute('data-page', id);
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var S = 'fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"';
  var SUN = 'var(--sun)';

  var D = {
    'start-here': '<svg viewBox="0 0 120 120"><g class="d-spin"><circle cx="60" cy="60" r="44" ' + S + '/><path d="M60 22 L68 60 L60 98 L52 60 Z" fill="' + SUN + '"/><path d="M22 60 L60 54 L98 60 L60 66 Z" fill="currentColor" opacity=".55"/></g><g class="d-bounce"><path d="M60 4 C48 4 42 13 42 21 C42 33 60 46 60 46 C60 46 78 33 78 21 C78 13 72 4 60 4 Z" fill="' + SUN + '"/><circle cx="60" cy="21" r="6" fill="#0f3b3a"/></g></svg>',
    'about': '<svg viewBox="0 0 140 110"><g ' + S + '><circle cx="34" cy="34" r="10"/><path d="M18 96 Q18 56 34 56 Q50 56 50 96"/><path class="d-wave" d="M48 62 L64 44"/><circle cx="106" cy="38" r="9"/><path d="M92 96 Q92 60 106 60 Q120 60 120 96"/><path class="d-wave2" d="M92 66 L78 50"/><circle cx="70" cy="62" r="6"/><path d="M60 96 Q60 74 70 74 Q80 74 80 96"/></g><path d="M4 100 L136 100" stroke="' + SUN + '" stroke-width="5" stroke-linecap="round"/></svg>',
    'the-move': '<svg viewBox="0 0 120 120"><g class="d-bounce"><rect x="22" y="40" width="76" height="58" rx="10" ' + S + '/><path d="M46 40 V28 Q46 22 52 22 H68 Q74 22 74 28 V40" ' + S + '/><path d="M22 62 H98" ' + S + '/><circle cx="40" cy="82" r="7" fill="' + SUN + '"/><rect x="62" y="74" width="24" height="12" rx="3" fill="' + SUN + '" transform="rotate(-8 74 80)"/></g><path class="d-shadow" d="M30 112 H90" stroke="currentColor" stroke-width="4" stroke-linecap="round" opacity=".35"/></svg>',
    'dennisse': '<svg viewBox="0 0 120 120"><g class="d-spin-slow">' + [0,60,120,180,240,300].map(function (a) { return '<ellipse cx="60" cy="34" rx="12" ry="22" fill="' + SUN + '" opacity=".9" transform="rotate(' + a + ' 60 60)"/>'; }).join('') + '</g><circle cx="60" cy="60" r="13" fill="#e9f2ee"/><path d="M53 58 Q60 66 67 58" fill="none" stroke="#0f3b3a" stroke-width="3" stroke-linecap="round"/></svg>',
    'ecuador': '<svg viewBox="0 0 120 120" class="d-cycle"><g class="c c1"><path d="M10 70 Q25 55 40 70 T70 70 T100 70 T130 70" ' + S + '/><path d="M10 88 Q25 73 40 88 T70 88 T100 88" ' + S + ' opacity=".6"/></g><g class="c c2"><path d="M10 96 L48 34 L66 60 L80 42 L110 96 Z" ' + S + '/><path d="M40 47 L48 34 L56 47" fill="#e9f2ee" stroke="none"/></g><g class="c c3"><path d="M60 100 V54" ' + S + '/><path d="M60 54 Q30 50 26 24 Q52 24 60 54 Q68 24 94 24 Q90 50 60 54 Z" fill="' + SUN + '"/></g><g class="c c4"><path d="M24 80 Q26 46 60 44 Q94 46 96 80 Z" fill="' + SUN + '"/><ellipse cx="104" cy="74" rx="10" ry="7" ' + S + '/><path d="M36 80 V94 M84 80 V94" ' + S + '/></g></svg>',
    'top-20': '<svg viewBox="0 0 120 120"><path d="M14 104 L50 44 H70 L106 104 Z" fill="currentColor" opacity=".9"/><path d="M50 44 L57 58 L63 50 L70 44 Z" fill="#e9f2ee"/><circle class="puff p1" cx="60" cy="34" r="8" fill="#e9f2ee"/><circle class="puff p2" cx="60" cy="34" r="8" fill="#e9f2ee"/><circle class="puff p3" cx="60" cy="34" r="8" fill="#e9f2ee"/></svg>',
    'food': '<svg viewBox="0 0 120 120"><path class="steam s1" d="M44 40 Q36 30 44 20 Q52 10 44 2" ' + S + '/><path class="steam s2" d="M60 40 Q52 30 60 20 Q68 10 60 2" ' + S + '/><path class="steam s3" d="M76 40 Q68 30 76 20 Q84 10 76 2" ' + S + '/><path d="M14 54 H106 Q104 96 60 100 Q16 96 14 54 Z" fill="' + SUN + '"/><path d="M40 108 H80" ' + S + '/></svg>',
    'coffee-cacao': '<svg viewBox="0 0 120 120"><path class="steam s1" d="M46 38 Q38 28 46 18 Q54 8 46 0" ' + S + '/><path class="steam s2" d="M64 38 Q56 28 64 18 Q72 8 64 0" ' + S + '/><path d="M24 46 H88 V78 Q88 100 56 100 Q24 100 24 78 Z" fill="' + SUN + '"/><path d="M88 54 Q106 54 104 68 Q102 80 88 78" ' + S + '/><ellipse class="bean" cx="104" cy="104" rx="9" ry="6" fill="currentColor" transform="rotate(-30 104 104)"/><ellipse class="bean b2" cx="14" cy="104" rx="9" ry="6" fill="currentColor" transform="rotate(20 14 104)"/></svg>',
    'quiz': '<svg viewBox="0 0 140 110"><g class="q1"><path d="M22 34 Q22 16 40 16 Q58 16 58 32 Q58 44 42 48 V58" ' + S + '/><circle cx="42" cy="72" r="4" fill="currentColor"/></g><g class="q2"><path d="M74 44 Q74 24 96 24 Q118 24 118 42 Q118 56 98 60 V74" fill="none" stroke="' + SUN + '" stroke-width="6" stroke-linecap="round"/><circle cx="98" cy="92" r="5.5" fill="' + SUN + '"/></g></svg>',
    'festivals': 'BUNTING',
    'south-america': '<svg viewBox="0 0 160 90"><path class="trail" d="M6 70 Q50 10 100 40 T156 20" fill="none" stroke="currentColor" stroke-width="3" stroke-dasharray="6 7" stroke-linecap="round"/><g class="d-plane"><path d="M0 -10 L3 -2 L12 2 L12 5 L3 3 L2 9 L5 11 L5 12.5 L0 11.5 L-5 12.5 L-5 11 L-2 9 L-3 3 L-12 5 L-12 2 L-3 -2 Z" fill="' + SUN + '" transform="scale(1.6)"/></g></svg>',
    'with-a-baby': '<svg viewBox="0 0 160 70">' + [0,1,2,3,4].map(function (i) { return '<g class="foot" style="--i:' + i + '" transform="translate(' + (10 + i * 30) + ' ' + (i % 2 ? 14 : 34) + ') rotate(80)"><ellipse cx="0" cy="0" rx="8" ry="11" fill="' + SUN + '"/>' + [-6,-2,2,6].map(function (x, k) { return '<circle cx="' + x + '" cy="' + (-14 - (k === 0 ? 1 : 0)) + '" r="2.4" fill="' + SUN + '"/>'; }).join('') + '</g>'; }).join('') + '</svg>',
    'gear': '<svg viewBox="0 0 120 120"><g class="d-swing"><path d="M60 6 V26" ' + S + '/><path d="M36 26 H84 L96 46 V106 H24 V46 Z" fill="' + SUN + '"/><circle cx="60" cy="42" r="6" fill="#0f3b3a"/><path d="M38 66 H82 M38 80 H72 M38 94 H66" stroke="#0f3b3a" stroke-width="4" stroke-linecap="round"/></g></svg>',
    'checklist': '<svg viewBox="0 0 120 120"><rect x="22" y="18" width="76" height="96" rx="10" ' + S + '/><rect x="44" y="10" width="32" height="16" rx="5" fill="' + SUN + '"/>' + [44,66,88].map(function (y, i) { return '<path class="tick t' + i + '" d="M34 ' + y + ' l7 7 l13 -14" fill="none" stroke="' + SUN + '" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M62 ' + (y + 1) + ' H86" ' + S + ' opacity=".6"/>'; }).join('') + '</svg>',
    'moving-with-kids': '<svg viewBox="0 0 140 110"><g class="b1"><path d="M10 14 H72 Q80 14 80 22 V48 Q80 56 72 56 H34 L20 68 V56 H18 Q10 56 10 48 V22 Q10 14 18 14 Z" fill="' + SUN + '"/><text x="45" y="45" text-anchor="middle" font-size="30" font-weight="700" fill="#0f3b3a">?</text></g><g class="b2"><path d="M64 50 H124 Q132 50 132 58 V82 Q132 90 124 90 H118 V102 L104 90 H72 Q64 90 64 82 V58 Q64 50 72 50 Z" ' + S + '/><text x="98" y="80" text-anchor="middle" font-size="26" font-weight="700" fill="currentColor">!</text></g></svg>',
    'journal': '<svg viewBox="0 0 160 100"><path class="trail" d="M8 86 C40 86 40 30 80 40 S130 80 150 20" fill="none" stroke="currentColor" stroke-width="3" stroke-dasharray="5 7" stroke-linecap="round" opacity=".7"/><g class="d-paper"><path d="M0 0 L34 -14 L22 14 L14 4 Z" fill="' + SUN + '"/><path d="M14 4 L34 -14" stroke="#0f3b3a" stroke-width="2"/></g></svg>',
    'journal-why-ecuador': 'STAMP',
    'videos': '<svg viewBox="0 0 120 100"><rect x="8" y="14" width="104" height="72" rx="14" ' + S + '/><path class="d-play" d="M50 34 L78 50 L50 66 Z" fill="' + SUN + '"/><circle class="rec" cx="98" cy="28" r="6" fill="#ff5a4e"/></svg>',
    'work-with-us': 'SPARKLE', 'media-kit': 'SPARKLE',
    'trip-planner': '<svg viewBox="0 0 160 90"><path d="M0 70 Q40 40 80 62 T160 50" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="round" opacity=".35"/><path d="M0 70 Q40 40 80 62 T160 50" fill="none" stroke="#e9f2ee" stroke-width="2" stroke-dasharray="6 8"/><g class="d-car"><rect x="-16" y="-14" width="32" height="14" rx="5" fill="' + SUN + '"/><path d="M-9 -14 L-5 -22 H7 L11 -14 Z" fill="' + SUN + '"/><circle cx="-8" cy="1" r="4.5" fill="#0f3b3a"/><circle cx="8" cy="1" r="4.5" fill="#0f3b3a"/></g></svg>',
    'reader-stories': '<svg viewBox="0 0 120 100"><g class="d-bounce"><rect x="12" y="24" width="96" height="64" rx="8" fill="#e9f2ee"/><path d="M12 30 L60 62 L108 30" fill="none" stroke="#0f3b3a" stroke-width="4" stroke-linejoin="round"/><path d="M60 52 C52 44 44 50 50 58 L60 66 L70 58 C76 50 68 44 60 52 Z" fill="#ff5a4e"/></g></svg>',
    'photo-credits': '<svg viewBox="0 0 120 100"><rect x="10" y="28" width="100" height="62" rx="10" ' + S + '/><path d="M40 28 L48 16 H72 L80 28" ' + S + '/><circle cx="60" cy="59" r="16" fill="' + SUN + '"/><circle class="flash" cx="96" cy="40" r="5" fill="#fff"/></svg>',
    '404': '<svg viewBox="0 0 120 120"><g class="d-wobble"><circle cx="60" cy="60" r="44" ' + S + '/><path d="M60 22 L68 60 L60 98 L52 60 Z" fill="' + SUN + '"/></g><text x="96" y="30" font-size="30" font-weight="700" fill="' + SUN + '" class="q2">?</text></svg>'
  };
  var sparkle = '<svg viewBox="0 0 120 120">' + [[60, 56, 1], [24, 30, .55], [96, 92, .6], [98, 26, .4]].map(function (p, i) { return '<path class="twinkle" style="--i:' + i + '" transform="translate(' + p[0] + ' ' + p[1] + ') scale(' + p[2] + ')" d="M0 -34 Q5 -5 34 0 Q5 5 0 34 Q-5 5 -34 0 Q-5 -5 0 -34 Z" fill="' + SUN + '"/>'; }).join('') + '</svg>';
  var stamp = '<svg viewBox="0 0 120 120"><g transform="rotate(-10 60 60)"><rect x="18" y="18" width="84" height="84" rx="6" fill="none" stroke="' + SUN + '" stroke-width="4" stroke-dasharray="7 5"/><circle cx="60" cy="56" r="20" fill="none" stroke="' + SUN + '" stroke-width="4"/><path d="M36 56 H84" stroke="' + SUN + '" stroke-width="3"/><text x="60" y="94" text-anchor="middle" font-size="12" font-weight="700" letter-spacing="2" fill="' + SUN + '">0° · EC</text></g></svg>';

  var hero = $('.page-hero');
  var art = D[id];
  if (hero && art) {
    if (art === 'BUNTING') {
      var colors = ['#f2b632', '#ff5a4e', '#7fd3b0', '#e9f2ee', '#4fa3d9'];
      var b = document.createElement('div'); b.className = 'bunting'; b.setAttribute('aria-hidden', 'true');
      var html = '<svg viewBox="0 0 1000 70" preserveAspectRatio="none"><path d="M0 8 Q500 46 1000 8" fill="none" stroke="#e9f2ee" stroke-width="2" opacity=".6"/>';
      for (var i = 0; i < 22; i++) { var x = 10 + i * 45.5, y = 8 + 38 * (1 - Math.pow((x - 500) / 500, 2)) * 0.98; html += '<path class="flag" style="--i:' + i + ';transform-origin:' + (x + 15) + 'px ' + y + 'px" d="M' + x + ' ' + y + ' h30 l-6 14 l6 14 h-30 z" fill="' + colors[i % colors.length] + '" opacity=".92"/>'; }
      b.innerHTML = html + '</svg>'; hero.appendChild(b);
    } else {
      if (art === 'SPARKLE') art = sparkle; if (art === 'STAMP') art = stamp;
      var d = document.createElement('div'); d.className = 'page-doodle pd-' + id; d.setAttribute('aria-hidden', 'true'); d.innerHTML = art;
      hero.appendChild(d);
      var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
      if (fine && !reduce) hero.addEventListener('mousemove', function (e) {
        var r = hero.getBoundingClientRect(); d.style.setProperty('--px', (((e.clientX - r.left) / r.width - .5) * 22).toFixed(1) + 'px'); d.style.setProperty('--py', (((e.clientY - r.top) / r.height - .5) * 14).toFixed(1) + 'px');
      });
      d.style.pointerEvents = 'auto';
      d.addEventListener('click', function () { d.classList.remove('boing'); void d.offsetWidth; d.classList.add('boing'); });
    }
  }

  /* the move: a suitcase travels down the chapters as you scroll */
  var ch = $('.chapters');
  if (ch && !reduce) {
    var bag = document.createElement('span'); bag.className = 'chapter-bag'; bag.setAttribute('aria-hidden', 'true');
    bag.innerHTML = '<svg viewBox="0 0 40 40"><rect x="5" y="13" width="30" height="22" rx="5" fill="#f2b632"/><path d="M14 13 V8 Q14 6 16 6 H24 Q26 6 26 8 V13" fill="none" stroke="#f2b632" stroke-width="3"/><path d="M5 22 H35" stroke="#0f3b3a" stroke-width="2"/></svg>';
    ch.appendChild(bag);
    var move = function () { var r = ch.getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .6 - r.top) / (r.height || 1))); bag.style.top = (p * Math.max(0, r.height - 40)) + 'px'; };
    addEventListener('scroll', function () { requestAnimationFrame(move); }, { passive: true }); move();
  }

  /* traveling with a baby: tap a first for a little burst of stars */
  $$('.first').forEach(function (f) {
    f.tabIndex = 0;
    f.addEventListener('click', function () {
      if (reduce) return;
      for (var i = 0; i < 6; i++) { var s = document.createElement('span'); s.className = 'star-pop'; s.style.setProperty('--a', (i * 60) + 'deg'); f.appendChild(s); setTimeout(function (n) { n.remove(); }.bind(null, s), 800); }
    });
  });

  /* reader stories: a paper plane carries the pitch away */
  var cf = $('#contrib');
  if (cf && !reduce) cf.addEventListener('submit', function () {
    setTimeout(function () {
      if (!cf.hidden) return;
      var p = document.createElement('span'); p.className = 'fly-plane'; p.setAttribute('aria-hidden', 'true');
      p.innerHTML = '<svg viewBox="0 0 40 30"><path d="M0 14 L40 0 L28 30 L18 18 Z" fill="#f2b632"/><path d="M18 18 L40 0" stroke="#0f3b3a" stroke-width="2"/></svg>';
      document.body.appendChild(p); setTimeout(function () { p.remove(); }, 1600);
    }, 30);
  });
})();
