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
