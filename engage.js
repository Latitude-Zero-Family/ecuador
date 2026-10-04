/* Latitude Zero — engagement: explorer passport, reactions, polls, postcards, forms, two-homes slider */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ES = (document.documentElement.lang || '').indexOf('es') === 0;
  var DB = window.LZ_DB || {}, LIVE = !!(DB.url && DB.key);
  var page = document.documentElement.getAttribute('data-page') || '';
  var S = {}; $$('#lz-str span').forEach(function (s) { S[s.dataset.k] = s.textContent; });
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || 'null'); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
  function api(path, body) {
    return fetch(DB.url.replace(/\/$/, '') + '/rest/v1/' + path, {
      method: body ? 'POST' : 'GET',
      headers: { apikey: DB.key, Authorization: 'Bearer ' + DB.key, 'Content-Type': 'application/json' },
      body: body ? JSON.stringify(body) : undefined
    }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.status === 204 ? null : r.json(); });
  }
  function party(el) { if (window.lzConfetti && el) { var r = el.getBoundingClientRect(); window.lzConfetti(r.left + r.width / 2, r.top + 20); } }
  function link(name) { return ES ? name.replace('.html', '-es.html') : name; }

  /* ---------- 1. Explorer passport ---------- */
  var STAMPS = ['story', 'quiz', 'planner', 'plate', 'pack', 'flash', 'vote', 'checklist', 'postcard', 'festival', 'guide', 'spanish'];
  var KEY = 'lz-passport', got = store(KEY) || {};
  var badge = document.createElement('a');
  badge.className = 'passport-fab'; badge.href = link('passport.html');
  badge.setAttribute('aria-label', S.passport_label || 'Explorer passport');
  badge.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="11" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8.8 11h6.4M9 17h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="pf-n"></span>';
  document.body.appendChild(badge);
  function count() { return STAMPS.filter(function (k) { return got[k]; }).length; }
  function paintBadge() { $('.pf-n', badge).textContent = count() + '/' + STAMPS.length; badge.classList.toggle('full', count() === STAMPS.length); }
  paintBadge();
  function toast(title, sub) {
    var t = document.createElement('div'); t.className = 'stamp-toast'; t.setAttribute('role', 'status');
    t.innerHTML = '<span class="st-ink" aria-hidden="true"></span><div><b></b><span></span></div>';
    $('b', t).textContent = title; $('div span', t).textContent = sub;
    document.body.appendChild(t);
    setTimeout(function () { t.classList.add('out'); }, 3200); setTimeout(function () { t.remove(); }, 3800);
  }
  function stamp(k) {
    if (got[k] || STAMPS.indexOf(k) < 0) return;
    got[k] = new Date().toISOString(); store(KEY, got); paintBadge();
    badge.classList.remove('bump'); void badge.offsetWidth; badge.classList.add('bump');
    toast((S.new_stamp || 'New stamp:') + ' ' + (S['s_' + k] || k), count() + ' / ' + STAMPS.length + ' · ' + (S.see_passport || 'See your passport'));
    document.dispatchEvent(new CustomEvent('lz:stamp', { detail: k }));
  }
  window.lzStamp = stamp;

  // automatic stamps
  if (ES) stamp('spanish');
  if (page === 'festivals') setTimeout(function () { stamp('festival'); }, 4000);
  if (page === 'ecuador') setTimeout(function () { stamp('guide'); }, 4000);
  var end = $('#comments') || $('.post-end');
  if (end && 'IntersectionObserver' in window && page === 'journal-why-ecuador') {
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { stamp('story'); io.disconnect(); } }, { threshold: .2 }); io.observe(end);
  }
  var res = $('#results');
  if (res) new MutationObserver(function () { if ($$('.result', res).some(function (r) { return !r.hidden; })) stamp('quiz'); }).observe(res, { attributes: true, subtree: true, attributeFilter: ['hidden'] });
  var plan = $('#plan');
  if (plan) new MutationObserver(function () { if ($('.days', plan)) stamp('planner'); }).observe(plan, { childList: true });
  var plate = $('#plate-in');
  if (plate) new MutationObserver(function () { if (plate.children.length >= 3) stamp('plate'); }).observe(plate, { childList: true });
  var packs = $$('.pack-item');
  if (packs.length) document.addEventListener('click', function () { setTimeout(function () { if (packs.every(function (b) { return b.classList.contains('packed'); })) stamp('pack'); }, 50); });
  $$('.fc').forEach(function (c) { c.addEventListener('click', function () { stamp('flash'); }); });
  var vb = $('#vote-btn'); if (vb) vb.addEventListener('click', function () { if ($('#vote-pick').value) stamp('vote'); });
  $$('.chk-grid input').forEach(function (b) { b.addEventListener('change', function () { if (b.checked) stamp('checklist'); }); });

  // passport page
  var book = $('#passport-book');
  if (book) {
    var cards = $$('.pp-stamp', book);
    function paint() {
      cards.forEach(function (c) {
        var on = !!got[c.dataset.k]; c.classList.toggle('on', on);
        var d = $('.pp-date', c); if (on && d) d.textContent = new Date(got[c.dataset.k]).toLocaleDateString(ES ? 'es-EC' : 'en-US', { month: 'short', day: 'numeric', year: 'numeric' });
      });
      var n = count(); $('#pp-count').textContent = n; $('#pp-fill').style.width = (n / STAMPS.length * 100) + '%';
      $('#pp-cert').hidden = n < STAMPS.length; $('#pp-locked').hidden = n >= STAMPS.length;
    }
    paint(); document.addEventListener('lz:stamp', paint);
    var certBtn = $('#pp-make');
    if (certBtn) certBtn.addEventListener('click', function () {
      var name = ($('#pp-name').value || '').trim().slice(0, 40) || (S.explorer || 'Explorer');
      var cv = $('#pp-canvas'), x = cv.getContext('2d'), W = cv.width, H = cv.height;
      x.fillStyle = '#fdf6e3'; x.fillRect(0, 0, W, H);
      x.strokeStyle = '#0f3b3a'; x.lineWidth = 14; x.strokeRect(24, 24, W - 48, H - 48);
      x.strokeStyle = '#f2b632'; x.lineWidth = 4; x.setLineDash([14, 10]); x.strokeRect(50, 50, W - 100, H - 100); x.setLineDash([]);
      x.fillStyle = '#3d7a5a'; x.font = '600 26px "DM Mono", monospace'; x.textAlign = 'center';
      x.fillText('0° 00′ 00″ · LATITUDE ZERO', W / 2, 130);
      x.fillStyle = '#0f3b3a'; x.font = '64px "Young Serif", Georgia, serif'; x.fillText(S.cert_title || 'Certified Ecuador Explorer', W / 2, 230);
      x.fillStyle = '#56645f'; x.font = '28px Figtree, sans-serif'; x.fillText(S.cert_awarded || 'This passport belongs to', W / 2, 300);
      x.fillStyle = '#b07d0a'; x.font = '80px "Young Serif", Georgia, serif'; x.fillText(name, W / 2, 400);
      x.fillStyle = '#56645f'; x.font = '26px Figtree, sans-serif'; x.fillText(S.cert_line || 'for collecting all 12 stamps on latitudezerofamily.com', W / 2, 470);
      x.strokeStyle = '#f2b632'; x.lineWidth = 4; x.beginPath(); x.moveTo(140, 540); x.lineTo(W - 140, 540); x.stroke();
      x.fillStyle = '#f2b632'; x.beginPath(); x.arc(W / 2, 540, 16, 0, Math.PI * 2); x.fill();
      x.fillStyle = '#0f3b3a'; x.font = '24px Figtree, sans-serif';
      x.fillText(new Date().toLocaleDateString(ES ? 'es-EC' : 'en-US', { month: 'long', day: 'numeric', year: 'numeric' }) + ' · Austin, Dennisse & Mateo', W / 2, 600);
      var img = $('#pp-img'); img.src = cv.toDataURL('image/png'); img.hidden = false;
      var dl = $('#pp-dl'); dl.href = img.src; dl.hidden = false; party(img);
    });
  }

  var np = $('#now-place'); if (np && window.LZ_NOW) np.textContent = ES ? LZ_NOW.es : LZ_NOW.en;

  /* ---------- 2. Reactions ---------- */
  $$('.reactions').forEach(function (box) {
    var post = box.dataset.post, rk = 'lz-react-' + post, mine = store(rk);
    var btns = $$('.rx', box), note = $('.rx-note', box);
    function paint(counts) {
      btns.forEach(function (b) {
        b.classList.toggle('on', mine === b.dataset.r); b.setAttribute('aria-pressed', mine === b.dataset.r ? 'true' : 'false');
        var n = $('.rx-n', b); n.textContent = counts && counts[b.dataset.r] ? counts[b.dataset.r] : '';
      });
      note.hidden = LIVE || !mine;
    }
    function load() { if (!LIVE) return paint(null); api('rpc/reaction_counts', { post: post }).then(function (rows) { var c = {}; (rows || []).forEach(function (r) { c[r.reaction] = r.total; }); paint(c); }).catch(function () { paint(null); }); }
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        if (mine === b.dataset.r) return;
        var prev = mine; mine = b.dataset.r; store(rk, mine);
        b.classList.remove('pop'); void b.offsetWidth; b.classList.add('pop');
        if (!reduce) { var f = document.createElement('span'); f.className = 'rx-float'; f.textContent = $('.rx-e', b).textContent; b.appendChild(f); setTimeout(function () { f.remove(); }, 900); }
        if (LIVE) api('rpc/react', { post: post, new_reaction: mine, old_reaction: prev }).then(load).catch(load); else paint(null);
      });
    });
    load();
  });

  /* ---------- 3. Polls ---------- */
  $$('.poll').forEach(function (box) {
    var id = box.dataset.poll, pk = 'lz-poll-' + id, mine = store(pk), opts = $$('.poll-opt', box), note = $('.poll-note', box);
    function show(counts) {
      box.classList.add('voted');
      var total = 0; if (counts) Object.keys(counts).forEach(function (k) { total += counts[k]; });
      opts.forEach(function (o) {
        o.disabled = true; o.classList.toggle('mine', o.dataset.o === mine);
        var pct = counts && total ? Math.round((counts[o.dataset.o] || 0) / total * 100) : (o.dataset.o === mine ? 100 : 0);
        $('.poll-bar', o).style.width = pct + '%'; $('.poll-pct', o).textContent = counts ? pct + '%' : (o.dataset.o === mine ? '✓' : '');
      });
      $('.poll-total', box).textContent = counts ? total + ' ' + (S.votes || 'votes') : '';
      note.hidden = !!counts;
    }
    function results() { if (!LIVE) return show(null); api('rpc/poll_results', { poll: id }).then(function (rows) { var c = {}; (rows || []).forEach(function (r) { c[r.option] = r.total; }); show(c); }).catch(function () { show(null); }); }
    opts.forEach(function (o) {
      o.addEventListener('click', function () {
        if (mine) return; mine = o.dataset.o; store(pk, mine); party(o);
        if (LIVE) api('rpc/vote_poll', { poll: id, choice: mine }).then(results).catch(results); else results();
      });
    });
    if (mine) results();
  });

  /* ---------- 4. Postcards ---------- */
  var pcForm = $('#pc-form');
  if (pcForm) {
    var front = $('#pc-front'), photo = 'quilotoa';
    function upd() {
      front.style.backgroundImage = 'url(img/' + photo + '-800.jpg)';
      $('#pc-to-out').textContent = $('#pc-to').value || '…';
      $('#pc-msg-out').textContent = $('#pc-msg').value || $('#pc-msg').placeholder;
      $('#pc-from-out').textContent = $('#pc-from').value || '…';
      $('#pc-left').textContent = 200 - $('#pc-msg').value.length;
    }
    $$('.pc-pick').forEach(function (b) {
      b.addEventListener('click', function () { photo = b.dataset.p; $$('.pc-pick').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); upd(); });
    });
    ['#pc-to', '#pc-msg', '#pc-from'].forEach(function (s) { $(s).addEventListener('input', upd); });
    $('#pc-flip').addEventListener('click', function () { $('#pc-card').classList.toggle('flipped'); });
    pcForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var to = $('#pc-to').value.trim(), from = $('#pc-from').value.trim(), msg = $('#pc-msg').value.trim();
      $('#pc-err').hidden = !!(to && from && msg); if (!(to && from && msg)) return;
      var url = location.origin + location.pathname + '?p=' + encodeURIComponent(photo) + '&t=' + encodeURIComponent(to) + '&f=' + encodeURIComponent(from) + '&m=' + encodeURIComponent(msg);
      $('#pc-link').value = url; $('#pc-done').hidden = false; $('#pc-card').classList.add('flipped');
      stamp('postcard'); party($('#pc-card'));
      var share = $('#pc-share'); share.hidden = !navigator.share;
      $('#pc-done').scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
    });
    $('#pc-copy').addEventListener('click', function () {
      var b = this, l = b.textContent, v = $('#pc-link');
      try { navigator.clipboard.writeText(v.value).then(function () { b.textContent = S.copied || 'Copied'; setTimeout(function () { b.textContent = l; }, 1600); }, function () { v.select(); }); } catch (e) { v.select(); }
    });
    $('#pc-share').addEventListener('click', function () { try { navigator.share({ title: 'Latitude Zero', text: S.pc_share || 'A postcard from Ecuador', url: $('#pc-link').value }).catch(function () {}); } catch (e) {} });
    // viewing a postcard someone sent
    var q = new URLSearchParams(location.search);
    if (q.get('p') && q.get('m')) {
      var p = q.get('p').replace(/[^a-z_]/g, '');
      photo = $('.pc-pick[data-p="' + p + '"]') ? p : 'quilotoa';
      $('#pc-to').value = (q.get('t') || '').slice(0, 40); $('#pc-from').value = (q.get('f') || '').slice(0, 40); $('#pc-msg').value = (q.get('m') || '').slice(0, 200);
      $('#pc-received').hidden = false; $('#pc-card').classList.add('flipped');
    }
    upd();
  }

  /* ---------- 5. Email-to-us forms (contest, Ask Dennisse) ---------- */
  $$('form.mail-form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var req = $$('[required]', f), ok = req.every(function (i) { return i.type === 'checkbox' ? i.checked : i.value.trim(); });
      $('.mf-err', f).hidden = ok; if (!ok) return;
      var lines = $$('[data-label]', f).map(function (i) { return i.dataset.label + ': ' + (i.value || '').trim(); }).join('\n');
      var subj = f.dataset.subject, out = f.parentNode.querySelector('.mf-done');
      $('textarea', out).value = lines;
      $('.mf-mail', out).href = 'mailto:hola@latitudezerofamily.com?subject=' + encodeURIComponent(subj) + '&body=' + encodeURIComponent(lines);
      f.hidden = true; out.hidden = false; party(out);
    });
  });
  $$('.mf-copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.closest('.mf-done').querySelector('textarea'), l = b.textContent;
      try { navigator.clipboard.writeText(t.value).then(function () { b.textContent = S.copied || 'Copied'; setTimeout(function () { b.textContent = l; }, 1600); }, function () { t.select(); }); } catch (e) { t.select(); }
    });
  });

  /* ---------- 6. Two homes slider ---------- */
  $$('.two-homes').forEach(function (th) {
    var r = $('input', th), top = $('.th-top', th), handle = $('.th-handle', th);
    function set() { var v = r.value; top.style.clipPath = 'inset(0 ' + (100 - v) + '% 0 0)'; handle.style.left = v + '%'; }
    r.addEventListener('input', set); set();
  });
})();
