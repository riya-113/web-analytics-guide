"""Сборка статического сайта «Метрика без магии».
Чтобы подставить ID счётчиков, поменяйте значения ниже и запустите: python3 build.py
"""
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

TOP100_ID = os.environ.get('TOP100_ID', 'TOP100_PROJECT_ID')   # ID проекта Sber Ads (Топ-100)
TMR_ID = os.environ.get('TMR_ID', 'MYTRACKER_COUNTER_ID')        # ID счётчика MyTracker (Top.Mail.Ru)
LI_TYPE = os.environ.get('LI_TYPE', 't14.6')                     # тип кнопки LiveInternet

SITE = 'Метрика без магии'

TOP100 = f'''<!-- Sber Ads (Top100) counter -->
<script>
(function (w, d, c) {{
(w[c] = w[c] || []).push(function() {{
    var options = {{ project: {TOP100_ID} }};
    try {{ w.top100Counter = new top100(options); }} catch(e) {{ }}
}});
var n = d.getElementsByTagName("script")[0],
s = d.createElement("script"),
f = function () {{ n.parentNode.insertBefore(s, n); }};
s.type = "text/javascript"; s.async = true;
s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//st.top100.ru/top100/top100.js";
if (w.opera == "[object Opera]") {{ d.addEventListener("DOMContentLoaded", f, false); }} else {{ f(); }}
}})(window, document, "_top100q");
</script>
<noscript><img src="//counter.rambler.ru/top100.cnt?pid={TOP100_ID}" alt="Топ-100" style="position:absolute;left:-9999px"></noscript>
<!-- /Sber Ads (Top100) counter -->''' if TOP100_ID.isdigit() else '<!-- Sber Ads (Top100): вставьте ID проекта в build.py -->'

TMR = f'''<!-- Top.Mail.Ru / MyTracker counter -->
<script>
var _tmr = window._tmr || (window._tmr = []);
_tmr.push({{id: "{TMR_ID}", type: "pageView", start: (new Date()).getTime()}});
(function (d, w, id) {{
  if (d.getElementById(id)) return;
  var ts = d.createElement("script"); ts.type = "text/javascript"; ts.async = true; ts.id = id;
  ts.src = "https://top-fwz1.mail.ru/js/code.js";
  var f = function () {{var s = d.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ts, s);}};
  if (w.opera == "[object Opera]") {{ d.addEventListener("DOMContentLoaded", f, false); }} else {{ f(); }}
}})(document, window, "tmr-code");
</script>
<noscript><div><img src="https://top-fwz1.mail.ru/counter?id={TMR_ID};js=na" style="position:absolute;left:-9999px;" alt="Top.Mail.Ru"></div></noscript>
<!-- /Top.Mail.Ru / MyTracker counter -->''' if TMR_ID.isdigit() else '<!-- MyTracker: вставьте ID счётчика в build.py -->'

LI = f'''<!--LiveInternet counter--><a href="https://www.liveinternet.ru/click" target="_blank"><img id="licnt" width="88" height="31" style="border:0" title="LiveInternet: показано число просмотров за 24 часа, посетителей за 24 часа и за сегодня" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt=""/></a><script>(function(d,s){{d.getElementById("licnt").src=
"https://counter.yadro.ru/hit?{LI_TYPE};r"+escape(d.referrer)+
((typeof(s)=="undefined")?"":";s"+s.width+"*"+s.height+"*"+
(s.colorDepth?s.colorDepth:s.pixelDepth))+";u"+escape(d.URL)+
";h"+escape(d.title.substring(0,150))+";"+Math.random()}})
(document,screen)</script><!--/LiveInternet-->'''

NAV = [('index.html', 'Главная'), ('metrics.html', 'Глоссарий'), ('counters.html', 'Счётчики'),
       ('checklist.html', 'Чек-лист'), ('quiz.html', 'Тест'), ('about.html', 'О проекте'), ('contact.html', 'Связь')]


def page(fname, title, desc, body, pid):
    nav = ''.join(f'<a href="{h}"{" class=on" if h == fname else ""}>{t}</a>' for h, t in NAV)
    fnav = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {SITE}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
{TOP100}
{TMR}
</head>
<body id="p-{pid}" data-tmr="{TMR_ID}">
<header class="top"><div class="wrap">
<a class="logo" href="index.html" data-block="logo"><i></i>{SITE}</a>
<nav data-block="menu">{nav}</nav>
</div></header>
<main class="wrap{' page' if pid != 'home' else ''}">
{body}
</main>
<footer><div class="wrap">
<div><nav data-block="footer-menu">{fnav}</nav><div style="margin-top:8px">© 2026 «{SITE}» — учебный справочник по веб-аналитике</div></div>
<div class="counters" data-block="counters">{LI}</div>
</div></footer>
<script src="main.js"></script>
</body>
</html>
'''


PAGES = {}

PAGES['index.html'] = ('Главная', 'Понятный справочник по веб-аналитике: метрики, счётчики статистики, чек-лист установки и тест.', 'home', '''
<section class="hero" data-block="hero">
<span class="tag">Справочник для студентов и начинающих маркетологов</span>
<h1>Веб-аналитика без магии: метрики, счётчики и как их читать</h1>
<p>Коротко и по делу объясняем, чем визит отличается от посетителя, какой счётчик статистики поставить на сайт и как проверить, что он работает.</p>
<a class="btn" href="metrics.html" data-goal="hero_glossary">Открыть глоссарий</a>
<a class="btn ghost" href="quiz.html" data-goal="hero_quiz">Проверить себя</a>
</section>
<section class="grid" data-block="sections">
<div class="card"><span class="tag">Глоссарий</span><h3>20 ключевых метрик</h3><p>Посетители, визиты, отказы, глубина, конверсия — с примерами расчёта.</p><a href="metrics.html">Читать →</a></div>
<div class="card"><span class="tag">Сравнение</span><h3>Счётчики статистики</h3><p>Яндекс Метрика, LiveInternet, Sber Ads, MyTracker и лог-анализаторы в одной таблице.</p><a href="counters.html">Сравнить →</a></div>
<div class="card"><span class="tag">Практика</span><h3>Чек-лист установки</h3><p>10 шагов от регистрации до проверки, что данные действительно приходят.</p><a href="checklist.html">К чек-листу →</a></div>
<div class="card"><span class="tag">Тест</span><h3>8 вопросов</h3><p>Проверьте, отличите ли вы просмотр от визита и цель от события.</p><a href="quiz.html">Пройти тест →</a></div>
</section>
<section data-block="why">
<h2>Зачем это всё</h2>
<p>Сайт без статистики похож на магазин без кассы: непонятно, кто пришёл, что посмотрел и почему ушёл. Счётчики собирают данные, а метрики превращают их в ответы: какие страницы читают, откуда приходят люди и какие действия они совершают. Этот справочник собран, чтобы разобраться в основах за один вечер.</p>
</section>
''')

TERMS = [
    ('visitors', 'Посетитель и уникальный посетитель', 'Посетитель — браузер (устройство), с которого заходили на сайт; счётчик узнаёт его по cookie. <b>Уникальный посетитель</b> учитывается один раз за выбранный период, сколько бы визитов он ни совершил.'),
    ('pageviews', 'Просмотр (хит)', 'Одна загрузка страницы с кодом счётчика. Обновление страницы — тоже просмотр.'),
    ('visit', 'Визит (сессия, сеанс)', 'Последовательность действий одного посетителя без перерыва дольше тайм-аута (обычно 30 минут).'),
    ('depth', 'Глубина просмотра', 'Среднее число просмотров за визит: <b>просмотры ÷ визиты</b>. Например, 600 просмотров за 200 визитов — глубина 3.'),
    ('single', 'Единичный просмотр', 'Визит, состоящий из одного просмотра страницы.'),
    ('bounce', 'Отказ', 'Визит, в котором посетитель провёл на сайте меньше заданного времени (в Яндекс Метрике — 15 секунд) и просмотрел одну страницу. Доля отказов — отказы ÷ визиты.'),
    ('duration', 'Длительность визита', 'Время от первого до последнего события визита. Время на последней странице без дополнительных событий неизвестно, поэтому счётчики используют «пинги» активности.'),
    ('timeonsite', 'Время на сайте', 'Суммарное или среднее время, проведённое посетителями на сайте за период.'),
    ('source', 'Источник трафика', 'Откуда пришёл посетитель: поисковая система, социальная сеть, другой сайт, реклама, прямой заход, мессенджер, рассылка.'),
    ('channel', 'Канал трафика', 'Группа однотипных источников: органический поиск, переходы по ссылкам, социальные сети, прямые заходы, реклама.'),
    ('utm', 'UTM-метки', 'Параметры в адресе ссылки (utm_source, utm_medium, utm_campaign), по которым счётчик точно определяет рекламный источник.'),
    ('goal', 'Цель', 'Действие, ради которого существует сайт: отправка формы, клик по кнопке, посещение страницы «Спасибо».'),
    ('goalvisitor', 'Целевой посетитель и целевой визит', 'Целевой визит — визит, в котором цель достигнута хотя бы раз; целевой посетитель — посетитель, совершивший такой визит.'),
    ('conversion', 'Конверсия', 'Доля визитов (или посетителей), достигших цели: <b>целевые визиты ÷ все визиты × 100%</b>.'),
    ('event', 'Событие', 'Любое зафиксированное действие: клик, прокрутка, воспроизведение видео, отправка формы. Цель — это событие, которое признано важным.'),
    ('return', 'Возвраты и интервал возврата', 'Возврат — повторный визит того же посетителя. Интервал возврата — время между визитами.'),
    ('entry', 'Точка входа', 'Первая страница визита — с неё посетитель начал знакомство с сайтом.'),
    ('exit', 'Точка выхода', 'Последняя страница визита. Много выходов с важной страницы — повод её улучшить.'),
    ('metric', 'Метрика (показатель)', 'Числовая величина, которую можно посчитать: визиты, просмотры, конверсия, время.'),
    ('dimension', 'Параметр (измерение)', 'Признак, по которому группируются данные: страна, браузер, источник, страница, устройство.'),
]
terms_html = ''.join(f'<div id="{i}"><dt>{t}</dt><dd>{d}</dd></div>' for i, t, d in TERMS)
toc_html = ''.join(f'<a href="#{i}">{t.split(" (")[0]}</a>' for i, t, d in TERMS)
PAGES['metrics.html'] = ('Глоссарий метрик', 'Определения ключевых метрик веб-аналитики: посетители, визиты, отказы, глубина, конверсия, точки входа и выхода.', 'metrics', f'''
<h1>Глоссарий метрик веб-аналитики</h1>
<p class="lead">Двадцать понятий, без которых не прочитать ни один отчёт. Нажмите на термин в списке — страница перейдёт к нужному определению.</p>
<div class="toc" data-block="glossary-toc">{toc_html}</div>
<dl class="terms" data-block="glossary">{terms_html}</dl>
''')

PAGES['counters.html'] = ('Сравнение счётчиков', 'Сравнение российских счётчиков статистики: Яндекс Метрика, LiveInternet, Sber Ads (Топ-100), MyTracker и лог-анализаторов.', 'counters', '''
<h1>Какой счётчик статистики выбрать</h1>
<p class="lead">Внешний счётчик — это фрагмент кода, который браузер посетителя выполняет при загрузке страницы и отправляет данные на сервер сервиса. Лог-анализатор, наоборот, читает журналы вашего собственного сервера.</p>
<div class="tablewrap" data-block="compare-table">
<table class="cmp">
<tr><th>Сервис</th><th>Тип</th><th>Сильные стороны</th><th>Ограничения</th></tr>
<tr><td>Яндекс Метрика</td><td>Внешний JS-счётчик</td><td>Вебвизор, карты кликов, цели, сегменты, интеграция с Директом</td><td>Данные хранятся у Яндекса, нужен аккаунт Яндекса</td></tr>
<tr><td>LiveInternet</td><td>Внешний счётчик-изображение</td><td>Регистрация за пару минут, видимая кнопка-счётчик, рейтинги сайтов</td><td>Нет целей и сегментации, простые отчёты</td></tr>
<tr><td>Sber Ads (бывший Рамблер/Топ-100)</td><td>Внешний JS-счётчик</td><td>Дашборд, конструктор отчётов, собственные события, аналитика блоков, рейтинг Топ-100</td><td>Часть функций ориентирована на рекламную платформу SberAds</td></tr>
<tr><td>MyTracker (VK)</td><td>Внешний JS-счётчик, мультиплатформенный</td><td>Сайт и приложения в одном проекте, конструктор отчётов, инсайты об интересах аудитории</td><td>Интерфейс сложнее, ориентирован в первую очередь на приложения</td></tr>
<tr><td>GoAccess, AWStats</td><td>Лог-анализатор</td><td>Не зависит от блокировщиков, видит роботов и ошибки 404</td><td>Нужен доступ к журналам сервера, нет поведения на странице</td></tr>
</table></div>
<div class="note" data-block="tip"><b>Совет.</b> Счётчики не мешают друг другу: на учебном сайте можно поставить сразу несколько и сравнить, насколько отличаются их цифры. Расхождение в 5–15% — нормально: у сервисов разные правила подсчёта визитов и фильтрации роботов.</div>
<a class="btn" href="checklist.html" data-goal="counters_to_checklist">Как установить счётчик →</a>
''')

PAGES['checklist.html'] = ('Чек-лист установки счётчика', 'Пошаговый чек-лист: как зарегистрировать сайт в сервисе статистики, установить код счётчика и проверить его работу.', 'checklist', '''
<h1>Чек-лист: устанавливаем счётчик за 10 шагов</h1>
<p class="lead">Подходит для любого внешнего сервиса статистики. Отмечайте шаги по мере выполнения.</p>
<ol class="check" data-block="checklist">
<li><b>Определите цели сайта.</b>Что должен сделать посетитель: прочитать материал, оставить заявку, скачать файл.</li>
<li><b>Зарегистрируйтесь в сервисе.</b>Создайте аккаунт и добавьте сайт: адрес, название, часовой пояс.</li>
<li><b>Укажите дополнительные домены.</b>Зеркала и поддомены, чтобы переходы между ними не считались внешними.</li>
<li><b>Скопируйте код счётчика.</b>Обычно его вставляют в &lt;head&gt; или как можно выше в &lt;body&gt; на <i>всех</i> страницах.</li>
<li><b>Опубликуйте изменения.</b>Загрузите обновлённые файлы на хостинг или нажмите «Опубликовать» в конструкторе сайтов.</li>
<li><b>Проверьте загрузку кода.</b>Откройте сайт, в инструментах разработчика (F12 → Network) найдите запрос к серверу счётчика.</li>
<li><b>Нажмите «Проверить» в сервисе.</b>Большинство счётчиков умеют сами проверить, установлен ли код.</li>
<li><b>Настройте цели и события.</b>Клик по кнопке, отправка формы, посещение страницы «Спасибо».</li>
<li><b>Исключите свой трафик.</b>Отфильтруйте собственный IP, чтобы не искажать статистику.</li>
<li><b>Подождите и смотрите отчёты.</b>Первые данные появятся через несколько минут — часов, выводы делайте не раньше чем через неделю.</li>
</ol>
<a class="btn" id="btn-checklist" href="checklist.pdf" download data-goal="checklist_download">Скачать чек-лист (PDF)</a>
''')

QUIZ = [
    ('Что увеличится, если посетитель обновит страницу три раза?', ['Число визитов', 'Число просмотров', 'Число уникальных посетителей'], 1),
    ('Как считается глубина просмотра?', ['Просмотры ÷ визиты', 'Визиты ÷ посетители', 'Время ÷ просмотры'], 0),
    ('Визит длился 5 секунд и включал одну страницу. Это…', ['Целевой визит', 'Возврат', 'Отказ'], 2),
    ('Какой параметр в ссылке указывает рекламную кампанию?', ['utm_campaign', 'utm_term', 'ref'], 0),
    ('Страница, с которой посетитель начал визит, — это…', ['Точка выхода', 'Точка входа', 'Целевая страница'], 1),
    ('Чем цель отличается от события?', ['Ничем', 'Цель — событие, признанное важным для бизнеса', 'Событие всегда важнее цели'], 1),
    ('Какой инструмент увидит визиты поисковых роботов?', ['JS-счётчик', 'Лог-анализатор', 'Ни один'], 1),
    ('Браузер «страна» в отчёте — это…', ['Метрика', 'Параметр (измерение)', 'Цель'], 1),
]
qhtml = ''
for n, (q, opts, a) in enumerate(QUIZ):
    o = ''.join(f'<label><input type="radio" name="q{n}" value="{k}"> {t}</label>' for k, t in enumerate(opts))
    qhtml += f'<div class="q" data-a="{a}"><p>{n+1}. {q}</p>{o}<div class="mark"></div></div>'
PAGES['quiz.html'] = ('Тест', 'Тест из 8 вопросов по основам веб-аналитики: просмотры, визиты, отказы, UTM-метки, цели и события.', 'quiz', f'''
<h1>Проверьте себя: 8 вопросов</h1>
<p class="lead">Ответы проверяются сразу в браузере, ничего никуда не отправляется.</p>
<form id="quizform" class="quiz" data-block="quiz">{qhtml}
<button class="btn" type="submit" id="btn-quiz">Проверить ответы</button>
<div id="result"></div>
</form>
''')

PAGES['about.html'] = ('О проекте', 'О проекте «Метрика без магии» — учебный справочник по веб-аналитике.', 'about', '''
<h1>О проекте</h1>
<p class="lead">«Метрика без магии» — некоммерческий учебный сайт, созданный в рамках дисциплины «Веб-аналитика» в Московском Политехе.</p>
<p>Задача сайта — собрать в одном месте понятные объяснения базовых метрик и инструментов веб-аналитики. На сайте установлены счётчики LiveInternet, Sber Ads и MyTracker: статистика посещений используется только в учебных целях, в обезличенном виде.</p>
<h2>Что здесь есть</h2>
<ul>
<li><a href="metrics.html">Глоссарий</a> — 20 определений с формулами;</li>
<li><a href="counters.html">Сравнение счётчиков</a> — как устроены внешние и внутренние системы статистики;</li>
<li><a href="checklist.html">Чек-лист</a> — порядок установки счётчика;</li>
<li><a href="quiz.html">Тест</a> — самопроверка.</li>
</ul>
<p>Нашли ошибку или хотите предложить тему? <a href="contact.html" data-goal="about_to_contact">Напишите нам</a>.</p>
''')

PAGES['contact.html'] = ('Обратная связь', 'Форма обратной связи сайта «Метрика без магии».', 'contact', '''
<h1>Обратная связь</h1>
<p class="lead">Расскажите, какой раздел был полезен и что добавить. Форма учебная: сообщение не сохраняется и не отправляется на сервер.</p>
<form id="feedback" class="fb" action="thanks.html" method="get" data-block="feedback-form">
<label for="role">Кто вы?</label>
<select id="role" name="role"><option>Студент</option><option>Маркетолог</option><option>Владелец сайта</option><option>Другое</option></select>
<label for="useful">Какой раздел был полезнее всего?</label>
<select id="useful" name="useful"><option>Глоссарий</option><option>Сравнение счётчиков</option><option>Чек-лист</option><option>Тест</option></select>
<label for="msg">Пожелание</label>
<textarea id="msg" name="m" placeholder="Например: добавьте раздел про воронки"></textarea>
<p><button class="btn" type="submit" id="btn-send">Отправить</button></p>
</form>
''')

PAGES['thanks.html'] = ('Спасибо', 'Спасибо за отзыв.', 'thanks', '''
<h1>Спасибо за отзыв!</h1>
<p class="lead">Ваше мнение поможет сделать справочник полезнее.</p>
<a class="btn" href="index.html">На главную</a>
''')

os.makedirs(OUT, exist_ok=True)
for fname, (title, desc, pid, body) in PAGES.items():
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as fh:
        fh.write(page(fname, title, desc, body, pid))
import shutil
here = os.path.dirname(os.path.abspath(__file__))
for f in ('style.css', 'main.js', 'favicon.svg', 'checklist.pdf'):
    if os.path.exists(os.path.join(here, f)):
        shutil.copy(os.path.join(here, f), OUT)
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n')
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
print('built', len(PAGES), 'pages ->', os.path.abspath(OUT), '| TOP100:', TOP100_ID, '| TMR:', TMR_ID)
