/* Latitude Zero — story comments
   To go live, paste your Supabase project URL and its public "anon" key below,
   then run supabase-setup.sql once in that project. Until then, comments are
   kept only on the visitor's own device and clearly labeled that way. */
var LZ_COMMENTS = window.LZ_DB || { url: '', key: '' };

(function () {
  var root = document.querySelector('.comments'); if (!root) return;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var S = {}; $$('#cm-str span').forEach(function (s) { S[s.dataset.k] = s.textContent; });
  var POST = root.dataset.post, LANG = (document.documentElement.lang || 'en').slice(0, 2);
  var LIVE = !!(LZ_COMMENTS.url && LZ_COMMENTS.key);
  var LOCAL_KEY = 'lz-comments-' + POST, HEART_KEY = 'lz-hearts';
  var form = $('#cm-form'), list = $('#cm-list'), empty = $('#cm-empty'), count = $('#cm-count');
  var body = $('#cm-body'), chars = $('#cm-chars'), parentIn = $('#cm-parent');

  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || 'null'); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
  function api(path, opts) {
    opts = opts || {};
    return fetch(LZ_COMMENTS.url.replace(/\/$/, '') + '/rest/v1/' + path, {
      method: opts.method || 'GET',
      headers: { apikey: LZ_COMMENTS.key, Authorization: 'Bearer ' + LZ_COMMENTS.key, 'Content-Type': 'application/json', Prefer: 'return=minimal' },
      body: opts.body ? JSON.stringify(opts.body) : undefined
    }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.status === 204 || r.status === 201 ? null : r.json(); });
  }

  /* helpers */
  var COLORS = ['#3d7a5a', '#f2b632', '#4fa3d9', '#ff5a4e', '#0f3b3a', '#8a6a24'];
  function color(name) { var h = 0; for (var i = 0; i < name.length; i++) h = (h * 31 + name.charCodeAt(i)) | 0; return COLORS[Math.abs(h) % COLORS.length]; }
  function initials(name) { return name.trim().split(/\s+/).slice(0, 2).map(function (w) { return w[0]; }).join('').toUpperCase() || '?'; }
  function ago(iso) {
    var s = (Date.now() - new Date(iso).getTime()) / 1000;
    if (s < 60) return S.justnow; if (s < 3600) return Math.floor(s / 60) + ' ' + S.min;
    if (s < 86400) return Math.floor(s / 3600) + ' ' + S.hr; if (s < 86400 * 30) return Math.floor(s / 86400) + ' ' + S.day;
    return new Date(iso).toLocaleDateString(LANG === 'es' ? 'es-EC' : 'en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

  /* render */
  var hearted = store(HEART_KEY) || {};
  function item(c, pending) {
    var li = el('li', 'cm' + (pending ? ' is-pending' : '') + (c.is_team ? ' is-team' : '')); li.id = 'c-' + c.id;
    var av = el('span', 'cm-av', c.is_team ? '' : initials(c.name)); av.style.background = c.is_team ? 'var(--sun)' : color(c.name); av.setAttribute('aria-hidden', 'true');
    var box = el('div', 'cm-box');
    var meta = el('div', 'cm-meta');
    meta.appendChild(el('b', null, c.name));
    if (c.is_team) meta.appendChild(el('span', 'cm-badge', S.team));
    if (c.place) meta.appendChild(el('span', 'cm-place', c.place));
    meta.appendChild(el('time', null, ago(c.created_at)));
    var p = el('p', 'cm-text', c.body);
    box.appendChild(meta); box.appendChild(p);
    var acts = el('div', 'cm-acts');
    if (pending) acts.appendChild(el('span', 'cm-pending', LIVE ? S.pending : S.local));
    else {
      var heart = el('button', 'cm-heart' + (hearted[c.id] ? ' on' : '')); heart.type = 'button';
      heart.setAttribute('aria-label', S.heart); heart.setAttribute('aria-pressed', hearted[c.id] ? 'true' : 'false');
      heart.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.6 3.2 5 6.7 5c2 0 3.6 1.1 5.3 3 1.7-1.9 3.3-3 5.3-3 3.5 0 5.5 3.6 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg><span></span>';
      $('span', heart).textContent = c.hearts || '';
      heart.addEventListener('click', function () {
        if (hearted[c.id]) return; hearted[c.id] = 1; store(HEART_KEY, hearted);
        c.hearts = (c.hearts || 0) + 1; $('span', heart).textContent = c.hearts; heart.classList.add('on', 'pop'); heart.setAttribute('aria-pressed', 'true');
        if (LIVE) api('rpc/heart_comment', { method: 'POST', body: { comment_id: c.id } }).catch(function () {});
      });
      acts.appendChild(heart);
      if (!c.parent_id) {
        var rep = el('button', 'cm-reply', S.reply); rep.type = 'button';
        rep.addEventListener('click', function () {
          parentIn.value = c.id; $('#cm-replying-name').textContent = c.name; $('#cm-replying').hidden = false;
          form.scrollIntoView({ behavior: 'smooth', block: 'center' }); setTimeout(function () { body.focus(); }, 400);
        });
        acts.appendChild(rep);
      }
    }
    box.appendChild(acts); li.appendChild(av); li.appendChild(box);
    return li;
  }
  function render(rows) {
    var local = (store(LOCAL_KEY) || []).filter(function (l) { return !rows.some(function (r) { return r.id === l.id; }); });
    var all = rows.map(function (r) { return { c: r, pending: false }; }).concat(local.map(function (l) { return { c: l, pending: true }; }));
    list.innerHTML = '';
    var tops = all.filter(function (x) { return !x.c.parent_id; }).sort(function (a, b) { return new Date(b.c.created_at) - new Date(a.c.created_at); });
    tops.forEach(function (t) {
      var li = item(t.c, t.pending);
      var kids = all.filter(function (x) { return x.c.parent_id === t.c.id; }).sort(function (a, b) { return new Date(a.c.created_at) - new Date(b.c.created_at); });
      if (kids.length) { var ol = el('ol', 'cm-replies'); kids.forEach(function (k) { ol.appendChild(item(k.c, k.pending)); }); $('.cm-box', li).appendChild(ol); }
      list.appendChild(li);
    });
    // replies whose parent isn't visible
    all.filter(function (x) { return x.c.parent_id && !tops.some(function (t) { return t.c.id === x.c.parent_id; }); }).forEach(function (x) { list.appendChild(item(x.c, x.pending)); });
    var n = rows.length; empty.hidden = all.length > 0;
    count.hidden = !n; count.textContent = n === 1 ? S.one : n + ' ' + S.many;
  }
  function load() {
    if (!LIVE) { render([]); return; }
    api('comments?select=id,parent_id,name,place,body,hearts,is_team,created_at&post_slug=eq.' + encodeURIComponent(POST) + '&order=created_at.desc&limit=200')
      .then(function (rows) { render(rows || []); }).catch(function () { render([]); });
  }

  /* form */
  body.addEventListener('input', function () { chars.textContent = body.value.length + ' / 1000'; chars.classList.toggle('near', body.value.length > 900); });
  $('#cm-cancel-reply').addEventListener('click', function () { parentIn.value = ''; $('#cm-replying').hidden = true; });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = $('#cm-name').value.trim(), text = body.value.trim(), place = $('#cm-place').value.trim();
    var err = $('#cm-err'); err.hidden = !!(name && text); if (!name || !text) return;
    if ($('#cm-website').value) return; // spam trap
    var c = { id: (crypto.randomUUID ? crypto.randomUUID() : String(Date.now())), post_slug: POST, parent_id: parentIn.value || null, name: name.slice(0, 60), place: place.slice(0, 60) || null, body: text.slice(0, 1000), lang: LANG, created_at: new Date().toISOString() };
    var btn = $('#cm-submit'); btn.disabled = true; btn.textContent = S.sending;
    function done(ok) {
      btn.disabled = false; btn.textContent = S.post;
      if (!ok) { err.hidden = false; err.textContent = S.error; return; }
      var local = store(LOCAL_KEY) || []; local.push(c); store(LOCAL_KEY, local);
      body.value = ''; chars.textContent = '0 / 1000'; parentIn.value = ''; $('#cm-replying').hidden = true;
      var t = $('#cm-thanks'); $('#cm-thanks-msg').textContent = LIVE ? S.sent : S.local; t.hidden = false;
      t.classList.remove('pop-in'); void t.offsetWidth; t.classList.add('pop-in');
      if (window.lzConfetti) { var r = t.getBoundingClientRect(); window.lzConfetti(r.left + 40, r.top); }
      load();
    }
    if (!LIVE) { done(true); return; }
    api('comments', { method: 'POST', body: { id: c.id, post_slug: c.post_slug, parent_id: c.parent_id, name: c.name, place: c.place, body: c.body, lang: c.lang } })
      .then(function () { done(true); }).catch(function () { done(false); });
  });

  load();
})();
