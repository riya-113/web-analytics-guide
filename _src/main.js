/* Цели и события для счётчиков. ID счётчика MyTracker берётся из атрибута data-tmr на <body>. */
(function () {
  var TMR_ID = document.body.getAttribute('data-tmr');
  function goal(name, params) {
    try {
      if (TMR_ID && TMR_ID.indexOf('MYTRACKER') === -1) {
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
  // Достижение конца страницы глоссария (прочтение)
  if (document.body.id === 'p-metrics') {
    var sent = false;
    window.addEventListener('scroll', function () {
      if (!sent && window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
        sent = true; goal('glossary_read');
      }
    });
  }
  // Форма обратной связи
  var f = document.getElementById('feedback');
  if (f) f.addEventListener('submit', function () { goal('feedback_send'); });
  // Тест
  var qz = document.getElementById('quizform');
  if (qz) qz.addEventListener('submit', function (e) {
    e.preventDefault();
    var qs = qz.querySelectorAll('.q'), score = 0;
    qs.forEach(function (q) {
      var right = q.getAttribute('data-a'), ch = q.querySelector('input:checked'), m = q.querySelector('.mark');
      if (ch && ch.value === right) { score++; m.textContent = '✓ верно'; m.className = 'mark ok'; }
      else { m.textContent = '✗ правильный ответ: ' + q.querySelector('input[value="' + right + '"]').parentNode.textContent.trim(); m.className = 'mark bad'; }
    });
    document.getElementById('result').textContent = 'Результат: ' + score + ' из ' + qs.length;
    goal('quiz_complete', { score: score });
  });
})();
