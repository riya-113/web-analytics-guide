/* Цели и события для счётчиков. ID счётчика MyTracker берётся из атрибута data-tmr на <body>. */
(function () {
  var TMR_ID = document.body.getAttribute('data-tmr');
  function goal(name, params) {
    try {
      if (TMR_ID && /^\d+$/.test(TMR_ID)) {
        var _tmr = window._tmr || (window._tmr = []);
        _tmr.push({ id: TMR_ID, type: 'reachGoal', goal: name, params: params || {} });
      }
    } catch (e) {}
    try { console.log('[goal]', name, params || ''); } catch (e) {}
  }
  window.siteGoal = goal;
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-goal]');
    if (el) goal(el.getAttribute('data-goal'));
  });
  var f = document.getElementById('booking');
  if (f) f.addEventListener('submit', function () {
    goal('booking_send', { format: (f.querySelector('#format') || {}).value || '' });
  });
  // выбор формата из ссылки ?format=...
  var m = location.search.match(/format=([^&]+)/);
  if (m && document.getElementById('format')) document.getElementById('format').value = decodeURIComponent(m[1]);
})();
/* плавное появление блоков при прокрутке */
(function () {
  var els = document.querySelectorAll('main section:not(.hero), .grid > .card, .steps > div, details, .tablewrap, form.fb');
  if (!('IntersectionObserver' in window)) return;
  els.forEach(function (el, i) { el.classList.add('reveal'); el.style.transitionDelay = (i % 4) * 0.08 + 's'; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(function (el) { io.observe(el); });
})();
