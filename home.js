/* Latitude Zero — home page play */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $$ = function (s) { return [].slice.call(document.querySelectorAll(s)); };

  /* Polaroids: tap one to bring it to the front with a fresh tilt */
  var z = 3;
  $$('.hm-pola').forEach(function (p) {
    p.tabIndex = 0;
    function lift() {
      p.style.zIndex = ++z;
      p.style.setProperty('--r', (Math.random() * 14 - 7).toFixed(1) + 'deg');
      p.classList.remove('hop'); void p.offsetWidth; p.classList.add('hop');
      var n = document.querySelector('.hm-note'); if (n) n.classList.add('gone');
    }
    p.addEventListener('click', lift);
    p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); lift(); } });
  });

  /* Sections wake up as they scroll in: paths draw, pins drop, stickers land */
  var wake = $$('.hm-pick, .hm-play, .hm-now, .hm-who, .hm-regions, .hm-route');
  if (reduce || !('IntersectionObserver' in window)) { wake.forEach(function (s) { s.classList.add('awake'); }); }
  else {
    document.documentElement.classList.add('hm-anim');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('awake'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.1 });
    wake.forEach(function (s) { io.observe(s); });
    setTimeout(function () { wake.forEach(function (s) { if (s.getBoundingClientRect().top < innerHeight) s.classList.add('awake'); }); }, 2500);
  }

  /* Badges: a little spin when you hover or focus */
  $$('.hm-badge').forEach(function (b) {
    function spin() { b.classList.remove('spin'); void b.offsetWidth; b.classList.add('spin'); }
    b.addEventListener('mouseenter', spin); b.addEventListener('focus', spin);
  });

  /* The plane on the route map follows the dashed line as you scroll */
  var map = document.querySelector('.hm-map'), path = document.querySelector('.hm-map-path');
  if (map && path && path.getTotalLength && !reduce) {
    var plane = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    plane.setAttribute('viewBox', '0 0 32 32'); plane.setAttribute('class', 'hm-map-plane'); plane.setAttribute('aria-hidden', 'true');
    plane.innerHTML = '<path d="M16 2 L19 13 L30 18 L30 21 L19 18 L18 26 L22 29 L22 31 L16 29.5 L10 31 L10 29 L14 26 L13 18 L2 21 L2 18 L13 13 Z" fill="currentColor"/>';
    map.appendChild(plane);
    var svg = path.ownerSVGElement, L = path.getTotalLength(), ticking = false;
    function fly() {
      ticking = false;
      var r = map.getBoundingClientRect(), vh = innerHeight;
      var t = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (vh * 0.85)));
      var p = path.getPointAtLength(t * L), q = path.getPointAtLength(Math.min(L, t * L + 2));
      var sx = r.width / 1000, sy = r.height / 300;
      var ang = Math.atan2((q.y - p.y) * sy, (q.x - p.x) * sx) * 180 / Math.PI + 90;
      plane.style.transform = 'translate(' + (p.x * sx - 14) + 'px,' + (p.y * sy - 14) + 'px) rotate(' + ang + 'deg)';
    }
    addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(fly); } }, { passive: true });
    addEventListener('resize', fly); fly();
  }
})();
