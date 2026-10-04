/* Latitude Zero — page interactions: games, wheels, decks and sliders */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  function strs(id) { var o = {}; $$('#' + id + ' span').forEach(function (s) { o[s.dataset.k] = s.textContent; }); return o; }
  function party(el) { if (window.lzConfetti && el) { var r = el.getBoundingClientRect(); window.lzConfetti(r.left + r.width / 2, r.top + r.height / 3); } }

  /* HOME: spin the wheel */
  var wheel = $('#wheel');
  if (wheel) {
    var items = $$('#wheel-data li'), n = items.length, seg = 360 / n, cols = ['#f2b632', '#0f3b3a', '#3d7a5a', '#e9f2ee'];
    wheel.style.background = 'conic-gradient(' + items.map(function (_, i) { return cols[i % 4] + ' ' + (i * seg) + 'deg ' + ((i + 1) * seg) + 'deg'; }).join(',') + ')';
    items.forEach(function (li, i) {
      var t = document.createElement('span'); t.className = 'wl'; t.textContent = li.dataset.n;
      t.style.transform = 'rotate(' + (i * seg + seg / 2) + 'deg)'; t.style.color = (i % 4 === 1 || i % 4 === 2) ? '#e9f2ee' : '#0f3b3a';
      wheel.appendChild(t);
    });
    var turn = 0, busy = false;
    function spin() {
      if (busy) return; busy = true;
      var pick = Math.floor(Math.random() * n), target = 360 - (pick * seg + seg / 2);
      turn += (reduce ? 0 : 360 * 5) + ((target - turn % 360) + 360) % 360;
      wheel.style.transform = 'rotate(' + turn + 'deg)';
      setTimeout(function () {
        busy = false; var li = items[pick];
        $('#spin-name').textContent = li.textContent; $('#spin-link').href = 'top-20.html#place-' + li.dataset.n;
        var r = $('#spin-result'); r.hidden = false; r.classList.remove('pop-in'); void r.offsetWidth; r.classList.add('pop-in'); party(r);
      }, reduce ? 50 : 4200);
    }
    $('#spin-btn').addEventListener('click', spin); $('#spin-btn2').addEventListener('click', spin);
  }

  /* ABOUT: drag the polaroids around */
  $$('.photo-strip figure').forEach(function (f, k) {
    if (document.documentElement.getAttribute('data-page') !== 'about') return;
    var x = 0, y = 0, sx, sy, z = 1;
    f.style.touchAction = 'none';
    f.addEventListener('pointerdown', function (e) {
      if (e.target.closest('.zoomable') && e.detail > 1) return;
      sx = e.clientX - x; sy = e.clientY - y; f.setPointerCapture(e.pointerId); f.classList.add('dragging'); f.style.zIndex = ++z + 10;
      var moved = false;
      function mv(ev) { moved = true; x = ev.clientX - sx; y = ev.clientY - sy; f.style.translate = x + 'px ' + y + 'px'; }
      function up() { f.classList.remove('dragging'); f.removeEventListener('pointermove', mv); f.removeEventListener('pointerup', up); if (moved) f.dataset.moved = '1'; setTimeout(function () { delete f.dataset.moved; }, 50); }
      f.addEventListener('pointermove', mv); f.addEventListener('pointerup', up);
    });
    f.addEventListener('click', function (e) { if (f.dataset.moved) { e.stopPropagation(); e.preventDefault(); } }, true);
  });

  /* ECUADOR: expanding region panels */
  var panels = $$('.panel');
  panels.forEach(function (p) {
    function open() { panels.forEach(function (o) { o.classList.toggle('open', o === p); }); }
    p.addEventListener('mouseenter', open); p.addEventListener('focus', open);
    p.addEventListener('click', function (e) { if (!p.classList.contains('open')) { e.preventDefault(); open(); } });
  });

  /* TOP 20: surprise me */
  var sur = $('#surprise');
  if (sur) sur.addEventListener('click', function () {
    var vis = $$('.place').filter(function (p) { return !p.hidden; }); if (!vis.length) return;
    var p = vis[Math.floor(Math.random() * vis.length)];
    p.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
    p.classList.remove('flash'); void p.offsetWidth; p.classList.add('flash');
    var pin = $('.pin[href="#' + p.id + '"]'); if (pin) { pin.classList.add('hot'); setTimeout(function () { pin.classList.remove('hot'); }, 2200); }
  });

  /* FOOD: build a plate */
  var plateIn = $('#plate-in');
  if (plateIn) {
    var PS = strs('plate-str'), on = [], msg = $('#plate-msg');
    function draw() {
      plateIn.innerHTML = '';
      on.forEach(function (img, i) { var d = document.createElement('span'); d.className = 'scoop s' + i + (on.length === 1 ? ' solo' : ''); d.style.backgroundImage = 'url(img/' + img + '-800.jpg)'; plateIn.appendChild(d); });
      $$('.pick').forEach(function (b) { b.classList.toggle('on', on.indexOf(b.dataset.img) > -1); b.setAttribute('aria-pressed', on.indexOf(b.dataset.img) > -1); });
      msg.textContent = on.length ? PS[String(on.length)] : '';
    }
    $$('.pick').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = on.indexOf(b.dataset.img);
        if (i > -1) on.splice(i, 1);
        else if (on.length >= 3) { msg.textContent = PS.full; return; }
        else { on.push(b.dataset.img); if (on.length === 3) setTimeout(function () { party($('#plate')); }, 300); }
        draw();
      });
    });
    $('#plate-clear').addEventListener('click', function () { on = []; draw(); });
  }

  /* COFFEE: bean to cup slider */
  var bs = $('#bs-range');
  if (bs) {
    var steps = $$('.bs-step'), bean = $('#bs-bean'), labs = $$('.bs-labels span');
    function upd() {
      var i = +bs.value; steps.forEach(function (s, k) { s.hidden = k !== i; });
      bean.style.background = steps[i].dataset.c; bean.setAttribute('data-step', i);
      labs.forEach(function (l, k) { l.classList.toggle('on', k === i); });
      bs.style.setProperty('--p', (i / 5 * 100) + '%');
    }
    bs.addEventListener('input', upd); upd();
    labs.forEach(function (l, k) { l.addEventListener('click', function () { bs.value = k; upd(); }); });
  }

  /* DENNISSE: slang flashcards */
  var cards = $$('.fc');
  if (cards.length) {
    var ci = 0, cnt = $('#fc-count');
    function show(i) { ci = (i + cards.length) % cards.length; cards.forEach(function (c, k) { c.hidden = k !== ci; c.classList.remove('flipped'); if (k === ci) { c.classList.remove('deal'); void c.offsetWidth; c.classList.add('deal'); } }); cnt.textContent = (ci + 1) + ' / ' + cards.length; }
    cards.forEach(function (c) { c.tabIndex = 0; c.setAttribute('role', 'button'); c.addEventListener('click', function () { c.classList.toggle('flipped'); }); c.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); c.classList.toggle('flipped'); } }); });
    $('#fc-next').addEventListener('click', function () { show(ci + 1); }); $('#fc-prev').addEventListener('click', function () { show(ci - 1); });
    var sx = null, deck = $('#cards');
    deck.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    deck.addEventListener('touchend', function (e) { if (sx === null) return; var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(ci + (dx < 0 ? 1 : -1)); sx = null; });
  }

  /* GEAR: pack the suitcase */
  var packItems = $$('.pack-item');
  if (packItems.length) {
    var KS = strs('pack-str'), packed = 0, fill = $('#case-fill'), count = $('#case-count'), pm = $('#pack-msg'), reset = $('#pack-reset');
    function upd2() {
      fill.style.height = (packed / packItems.length * 100) + '%'; count.textContent = packed + '/' + packItems.length;
      pm.textContent = packed === packItems.length ? KS.done : (packed ? KS.some : ''); reset.hidden = !packed;
    }
    packItems.forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.classList.contains('packed')) return;
        b.classList.add('packed'); b.setAttribute('aria-pressed', 'true'); packed++;
        var cs = $('.suitcase'); cs.classList.remove('gulp'); void cs.offsetWidth; cs.classList.add('gulp');
        upd2(); if (packed === packItems.length) party(cs);
      });
    });
    reset.addEventListener('click', function () { packed = 0; packItems.forEach(function (b) { b.classList.remove('packed'); b.setAttribute('aria-pressed', 'false'); }); upd2(); });
    upd2();
  }

  /* CHECKLIST: plane flies from Wilkes-Barre to Ecuador */
  var plane = $('.ft-plane'), chkFill = $('#chk-fill');
  if (plane && chkFill && 'MutationObserver' in window) {
    var sync = function () { plane.style.left = chkFill.style.width || '0%'; };
    new MutationObserver(sync).observe(chkFill, { attributes: true, attributeFilter: ['style'] }); sync();
  }

  /* FESTIVALS: ¡Fiesta! */
  var fb = $('#fiesta');
  if (fb) fb.addEventListener('click', function () { party(fb); fb.classList.remove('jelly'); void fb.offsetWidth; fb.classList.add('jelly'); });

  /* FAQ: answers arrive like chat messages */
  $$('.faq').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open || reduce) return;
      d.classList.add('typing'); setTimeout(function () { d.classList.remove('typing'); }, 650);
    });
  });

  /* READER STORIES: friendly pitch meter */
  var pitch = $('#c-pitch'), meter = $('#pitch-meter');
  if (pitch && meter) {
    var MS = strs('pm-str');
    var pm2 = function () { var w = pitch.value.trim().split(/\s+/).filter(Boolean).length; var k = w === 0 ? 0 : w < 25 ? 1 : w < 160 ? 2 : 3; meter.textContent = MS[k] + (w ? ' (' + w + ')' : ''); meter.setAttribute('data-k', k); };
    pitch.addEventListener('input', pm2); pm2();
  }
})();
