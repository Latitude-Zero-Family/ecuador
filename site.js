/* Latitude Zero — shared motion and interaction layer */
/* Analytics: paste a Google Analytics 4 ID (G-XXXXXXX) here to turn it on. Nothing loads until a visitor accepts. */
var LZ_ANALYTICS_ID = '';
(function () {
  var ES = (document.documentElement.lang || '').indexOf('es') === 0;
  var T = function (en, es) { return ES ? es : en; };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  /* 1. Hero headline: words rise in one by one */
  function splitWords(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null), nodes = [], n, i = 0;
    while ((n = walker.nextNode())) nodes.push(n);
    nodes.forEach(function (node) {
      var frag = document.createDocumentFragment();
      node.textContent.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
        var lead = part.match(/^[.,:;!?)»”]+/); if (lead) { frag.appendChild(document.createTextNode(lead[0])); part = part.slice(lead[0].length); if (!part) return; }
        var s = document.createElement('span'); s.className = 'w'; s.style.setProperty('--i', i++);
        s.textContent = part; frag.appendChild(s);
      });
      node.parentNode.replaceChild(frag, node);
    });
  }
  if (!reduce) $$('.hero h1, .page-hero h1').forEach(function (h) { splitWords(h); h.classList.add('split'); });
  document.documentElement.classList.add('motion-ready');

  /* 2. Reading progress + back to top */
  var bar = document.createElement('div'); bar.className = 'read-progress'; bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  var top = document.createElement('button'); top.type = 'button'; top.className = 'to-top-btn';
  top.setAttribute('aria-label', T('Back to top', 'Volver arriba')); top.innerHTML = '<span aria-hidden="true">↑</span>';
  top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });
  document.body.appendChild(top);
  var ridge = $('.ridge'), ticking = false;
  function onScroll() {
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight, y = window.scrollY || h.scrollTop;
    bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')';
    top.classList.toggle('show', y > 700);
    if (ridge && !reduce) ridge.style.transform = 'translateY(' + Math.min(60, y * 0.12) + 'px)';
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* 3. Scroll reveal — only for things that start below the fold; everything else is untouched */
  var revealSel = '.sec-head, .post, .region, .offer, .path, .dish, .place, .member, .chapter, .first, .stop, .country, .fact, .widget, .credit, .faq, .chk-group, .eat-list li, .photo-strip figure, .region-detail, .vote-card, .map, .result, .handle, .news-copy, .news-form';
  if (!reduce && 'IntersectionObserver' in window) {
    var vh = window.innerHeight, pending = [];
    $$(revealSel).forEach(function (el) {
      if (el.getBoundingClientRect().top > vh * 0.95) { el.classList.add('pre'); pending.push(el); }
    });
    // stagger siblings in the same row
    pending.forEach(function (el) {
      var sib = el.parentElement ? [].indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty('--d', (Math.min(sib, 5) * 70) + 'ms');
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.05 });
    pending.forEach(function (el) { io.observe(el); });
    // safety net: never leave anything hidden
    var sweep = function () { var h = window.innerHeight; $$('.pre').forEach(function (el) { if (el.getBoundingClientRect().top < h) { el.classList.remove('pre'); el.classList.add('in'); } }); };
    var sweepT; window.addEventListener('scroll', function () { clearTimeout(sweepT); sweepT = setTimeout(sweep, 120); }, { passive: true });
    setTimeout(function () { $$('.pre').forEach(function (el) { if (el.getBoundingClientRect().top < window.innerHeight) el.classList.remove('pre'); }); }, 2500);
    window.addEventListener('beforeprint', function () { $$('.pre').forEach(function (el) { el.classList.remove('pre'); }); });
  }

  /* 4. Gentle 3D tilt on cards (mouse only) */
  if (finePointer && !reduce) {
    $$('.post, .path, .dish, .offer, .region, .widget:not(.flip), .vote-card').forEach(function (card) {
      card.classList.add('tilt');
      card.addEventListener('mousemove', function (e) {
        var r = card.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        card.style.setProperty('--rx', (-y * 5).toFixed(2) + 'deg'); card.style.setProperty('--ry', (x * 6).toFixed(2) + 'deg');
        card.style.setProperty('--mx', ((x + 0.5) * 100).toFixed(1) + '%'); card.style.setProperty('--my', ((y + 0.5) * 100).toFixed(1) + '%');
      });
      card.addEventListener('mouseleave', function () { card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg'); });
    });
  }

  /* 5. Photo lightbox with swipe and arrow keys */
  var shots = $$('.place-img, .dish img, .photo-strip img, .detail-img, img.article-art, .result img, .credit img, .region-detail img');
  if (shots.length) {
    var lb = document.createElement('div'); lb.className = 'lightbox'; lb.hidden = true;
    lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', T('Photo viewer', 'Visor de fotos'));
    lb.innerHTML = '<button type="button" class="lb-close" aria-label="' + T('Close', 'Cerrar') + '">×</button>' +
      '<button type="button" class="lb-nav lb-prev" aria-label="' + T('Previous photo', 'Foto anterior') + '">‹</button>' +
      '<figure><img alt=""><figcaption></figcaption></figure>' +
      '<button type="button" class="lb-nav lb-next" aria-label="' + T('Next photo', 'Foto siguiente') + '">›</button>' +
      '<p class="lb-credit"><a href="' + (ES ? 'photo-credits-es.html' : 'photo-credits.html') + '">' + T('Photo credits', 'Créditos de fotos') + '</a></p>';
    document.body.appendChild(lb);
    var cur = 0, lbImg = $('img', lb), lbCap = $('figcaption', lb), lastFocus = null;
    function show(i) {
      cur = (i + shots.length) % shots.length; var s = shots[cur];
      lbImg.classList.remove('lb-in'); void lbImg.offsetWidth;
      lbImg.src = s.currentSrc || s.src; lbImg.alt = s.alt || ''; lbCap.textContent = s.alt || '';
      lbImg.classList.add('lb-in');
      $('.lb-counter', lb) || lb.insertAdjacentHTML('beforeend', '<span class="lb-counter"></span>');
      $('.lb-counter', lb).textContent = (cur + 1) + ' / ' + shots.length;
    }
    function open(i) { lastFocus = document.activeElement; lb.hidden = false; document.documentElement.style.overflow = 'hidden'; show(i); $('.lb-close', lb).focus(); }
    function close() { lb.hidden = true; document.documentElement.style.overflow = ''; lastFocus && lastFocus.focus && lastFocus.focus(); }
    shots.forEach(function (s, i) {
      s.classList.add('zoomable'); s.tabIndex = 0; s.setAttribute('role', 'button');
      s.setAttribute('aria-label', T('Enlarge photo: ', 'Ampliar foto: ') + (s.alt || ''));
      s.addEventListener('click', function (e) { e.preventDefault(); open(i); });
      s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); } });
    });
    $('.lb-close', lb).addEventListener('click', close);
    $('.lb-prev', lb).addEventListener('click', function () { show(cur - 1); });
    $('.lb-next', lb).addEventListener('click', function () { show(cur + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') close(); else if (e.key === 'ArrowRight') show(cur + 1); else if (e.key === 'ArrowLeft') show(cur - 1);
    });
    var sx = null;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { if (sx === null) return; var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1)); sx = null; });
  }

  /* 6. Top 20: list and map highlight each other; pins drop in */
  $$('.place').forEach(function (p) {
    var pin = $('.pin[href="#' + p.id + '"]');
    if (!pin) return;
    p.addEventListener('mouseenter', function () { pin.classList.add('hot'); });
    p.addEventListener('mouseleave', function () { pin.classList.remove('hot'); });
    pin.addEventListener('mouseenter', function () { p.classList.add('hot'); });
    pin.addEventListener('mouseleave', function () { p.classList.remove('hot'); });
    pin.addEventListener('click', function () { p.classList.remove('flash'); void p.offsetWidth; p.classList.add('flash'); });
  });
  $$('.pin').forEach(function (pin, i) { pin.style.setProperty('--i', i); });

  /* 7. Word of the week flips */
  $$('.flip').forEach(function (f) {
    function toggle() { var o = f.classList.toggle('flipped'); f.setAttribute('aria-pressed', o ? 'true' : 'false'); }
    f.addEventListener('click', toggle);
    f.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  });

  /* 8. Quiz: live progress bar and a little pop on each answer */
  var quiz = $('#quiz');
  if (quiz) {
    var qs = $$('.q', quiz), qbar = document.createElement('div');
    qbar.className = 'quiz-progress'; qbar.innerHTML = '<i></i>'; qbar.setAttribute('aria-hidden', 'true');
    quiz.insertBefore(qbar, quiz.firstChild);
    quiz.addEventListener('change', function (e) {
      var done = qs.filter(function (q) { return $('input:checked', q); }).length;
      $('i', qbar).style.width = (done / qs.length * 100) + '%';
      var opt = e.target.closest('.opt'); if (opt) { opt.classList.remove('pop'); void opt.offsetWidth; opt.classList.add('pop'); }
      var q = e.target.closest('.q'), next = qs[qs.indexOf(q) + 1];
      if (next && !$('input:checked', next) && !reduce) setTimeout(function () { next.scrollIntoView({ behavior: 'smooth', block: 'center' }); }, 250);
    });
  }

  /* 9. Confetti for finished checklists and quiz results */
  function confetti(x, y) {
    if (reduce) return;
    var c = document.createElement('canvas'), ctx = c.getContext('2d'), W = c.width = window.innerWidth, H = c.height = window.innerHeight;
    c.className = 'confetti'; document.body.appendChild(c);
    var cs = getComputedStyle(document.documentElement), cols = ['--sun', '--moss', '--deep', '--accent'].map(function (v) { return cs.getPropertyValue(v).trim() || '#f2b632'; });
    var ps = []; for (var i = 0; i < 90; i++) ps.push({ x: x, y: y, vx: (Math.random() - 0.5) * 9, vy: -Math.random() * 9 - 3, r: Math.random() * 6 + 3, c: cols[i % cols.length], a: Math.random() * 6, s: Math.random() * 0.3 - 0.15 });
    var t = 0;
    (function frame() {
      ctx.clearRect(0, 0, W, H); t++;
      ps.forEach(function (p) { p.vy += 0.25; p.x += p.vx; p.y += p.vy; p.a += p.s; ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.a); ctx.fillStyle = p.c; ctx.fillRect(-p.r / 2, -p.r / 4, p.r, p.r / 2); ctx.restore(); });
      if (t < 110) requestAnimationFrame(frame); else c.remove();
    })();
  }
  window.lzConfetti = confetti;
  $$('.chk-group').forEach(function (g) {
    g.addEventListener('change', function (e) {
      var boxes = $$('input', g), all = boxes.every(function (b) { return b.checked; });
      var was = g.classList.contains('done'); g.classList.toggle('done', all);
      if (all && !was && e.target.checked) { var r = e.target.getBoundingClientRect(); confetti(r.left + 10, r.top); }
    });
    if ($$('input', g).every(function (b) { return b.checked; })) g.classList.add('done');
  });
  var results = $('#results');
  if (results && 'MutationObserver' in window) {
    new MutationObserver(function () {
      var r = $$('.result', results).filter(function (x) { return !x.hidden; })[0];
      if (r && !r.dataset.party) { r.dataset.party = '1'; setTimeout(function () { var b = r.getBoundingClientRect(); confetti(b.left + b.width / 2, b.top + 40); }, 350); }
      $$('.result', results).forEach(function (x) { if (x.hidden) delete x.dataset.party; });
    }).observe(results, { attributes: true, subtree: true, attributeFilter: ['hidden'] });
  }

  /* 10. Count-up for progress numbers */
  if (!reduce) $$('[data-count]').forEach(function (el) {
    var to = +el.dataset.count, t0 = null;
    (function step(ts) { t0 = t0 || ts; var p = Math.min(1, (ts - t0) / 900); el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); })(performance.now());
  });

  /* 11. Cookie consent (only when analytics is configured) */
  function loadAnalytics() {
    if (!LZ_ANALYTICS_ID || window.__lzGA) return; window.__lzGA = true;
    var g = document.createElement('script'); g.async = true; g.src = 'https://www.googletagmanager.com/gtag/js?id=' + LZ_ANALYTICS_ID; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date()); gtag('config', LZ_ANALYTICS_ID, { anonymize_ip: true });
  }
  if (LZ_ANALYTICS_ID) {
    var KEY = 'lz-consent', choice = null;
    try { choice = localStorage.getItem(KEY); } catch (e) {}
    var link = $('.cookie-link'); if (link) link.hidden = false;
    var ban = document.createElement('div'); ban.className = 'cookie-banner'; ban.setAttribute('role', 'dialog'); ban.setAttribute('aria-label', T('Cookie choices', 'Preferencias de cookies'));
    ban.innerHTML = '<p>' + T('We use analytics cookies to see which stories people read. Is that OK?', 'Usamos cookies de analítica para saber qué historias se leen. ¿Está bien?') +
      ' <a href="' + (ES ? 'privacy-es.html' : 'privacy.html') + '">' + T('Privacy policy', 'Política de privacidad') + '</a></p>' +
      '<div class="cookie-actions"><button type="button" class="btn btn-line" data-c="no">' + T('No thanks', 'No, gracias') + '</button><button type="button" class="btn btn-sun" data-c="yes">' + T('Accept', 'Aceptar') + '</button></div>';
    ban.hidden = !!choice; document.body.appendChild(ban);
    $$('button', ban).forEach(function (b) { b.addEventListener('click', function () {
      var c = b.dataset.c; try { localStorage.setItem(KEY, c); } catch (e) {} ban.hidden = true; if (c === 'yes') loadAnalytics();
    }); });
    if (link) link.addEventListener('click', function () { ban.hidden = false; });
    if (choice === 'yes') loadAnalytics();
  }
})();
