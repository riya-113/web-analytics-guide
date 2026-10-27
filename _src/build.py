"""Сборка статического сайта студии пилатеса «Линия».
Чтобы подставить ID счётчиков, поменяйте значения ниже и запустите: python3 build.py
"""
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

TOP100_ID = os.environ.get('TOP100_ID', '7753235')   # ID проекта Sber Ads (Топ-100)
TMR_ID = os.environ.get('TMR_ID', '3808235')        # ID счётчика MyTracker (Top.Mail.Ru)
LI_TYPE = os.environ.get('LI_TYPE', 't14.6')                     # тип кнопки LiveInternet

SITE = 'Линия'

TOP100 = f'''<!-- Top100 (Kraken) Counter / Sber Ads -->
<script>
(function (w, d, c) {{
(w[c] = w[c] || []).push(function() {{
    var options = {{
        project: {TOP100_ID},
        attributes_dataset: [ "block" ],
        trackHashes: true,
        user_id: null,
    }};
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
<!-- END Top100 (Kraken) Counter -->''' if TOP100_ID.isdigit() else '<!-- Sber Ads (Top100): вставьте ID проекта в build.py -->'

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

LI_HIT = """<!--LiveInternet counter--><script>
new Image().src = "https://counter.yadro.ru/hit?r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";h"+escape(document.title.substring(0,150))+
";"+Math.random();</script><!--/LiveInternet-->"""
LI = """<!--LiveInternet logo--><a href="https://www.liveinternet.ru/click"
target="_blank"><img src="https://counter.yadro.ru/logo?23.6"
title="LiveInternet: показано число посетителей за сегодня"
alt="" style="border:0" width="88" height="15"/></a><!--/LiveInternet-->"""

NAV = [('index.html', 'Главная'), ('classes.html', 'Направления'), ('schedule.html', 'Расписание'),
       ('prices.html', 'Цены'), ('studio.html', 'О студии'), ('faq.html', 'Вопросы'), ('booking.html', 'Запись')]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">'

REFORMER = '''<svg viewBox="0 0 400 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Иллюстрация: реформер">
<circle cx="300" cy="120" r="70" fill="#e6c9c9"/>
<g fill="none" stroke="#6a121a" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<path d="M40 400h320"/><path d="M60 400v40M340 400v40"/><path d="M70 380h180"/><path d="M250 380v-60"/>
<path d="M330 400v-110"/><path d="M300 290h60"/>
<path d="M110 372h110" stroke="#9e2a35" stroke-width="12"/>
<path d="M330 330h-80M330 345h-80" stroke-width="2.5"/>
</g>
<path d="M40 470h320" stroke="#bdb9b3" stroke-width="4" stroke-linecap="round"/>
</svg>'''


def page(fname, title, desc, body, pid):
    nav = ''.join(f'<a href="{h}"{" class=on" if h == fname else ""}>{t}</a>' for h, t in NAV)
    fnav = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — пилатес-студия «{SITE}», Красносельский район</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
{TOP100}
{TMR}
</head>
<body id="p-{pid}" data-tmr="{TMR_ID}">
{LI_HIT}
<header class="top"><div class="wrap">
<a class="logo" href="index.html" data-block="logo">ЛИНИЯ<small>pilates</small></a>
<nav data-block="menu">{nav}</nav>
</div></header>
<main class="wrap{' page' if pid != 'home' else ''}">
{body}
</main>
<footer><div class="wrap">
<div><nav data-block="footer-menu">{fnav}</nav>
<div style="margin-top:8px">© 2026 Пилатес-студия «{SITE}» · Красносельский район, Санкт-Петербург</div>
<div style="font-size:12px;margin-top:4px">Студия готовится к открытию. Сайт — учебный проект по дисциплине «Веб-аналитика»; заявки на сайте не сохраняются. Фотографии интерьера иллюстративные.</div></div>
<div class="counters" data-block="counters">{LI}<a class="top100-badge" href="https://top100.rambler.ru/" target="_blank" rel="noopener" title="Рейтинг Топ-100 — Статистика от SberAds"><span>ТОП</span><b>100</b></a></div>
</div></footer>
<script src="main.js"></script>
</body>
</html>
'''


PAGES = {}

PAGES['index.html'] = ('Пилатес на реформерах', 'Камерная студия пилатеса на реформерах в Красносельском районе Санкт-Петербурга: мини-группы до 4 человек, индивидуальные и парные занятия.', 'home', f'''
<section class="hero" data-block="hero">
<div>
<span class="eyebrow">Красносельский район · скоро открытие</span>
<h1>Пилатес на реформерах рядом с домом</h1>
<p>Камерная студия на четыре реформера: тренер видит каждого, а занятие подстраивается под ваше тело — без переполненных залов и поездок через весь город.</p>
<div class="ctas">
<a class="btn" id="btn-trial" href="booking.html?format=Пробное" data-goal="trial_click">Записаться на пробное</a>
<a class="btn ghost" href="classes.html" data-goal="hero_classes">Выбрать направление</a>
</div>
</div>
<div class="art photo" data-block="hero-art"><img src="img/studio-hall.jpg" alt="Зал студии: реформеры в бордово-кремовых тонах" width="678" height="452"></div>
</section>
<section data-block="benefits">
<span class="eyebrow">Почему «Линия»</span>
<h2>Маленькая студия — большое внимание</h2>
<div class="grid">
<div class="card"><h3>До 4 человек</h3><p>Мини-группы по числу реформеров: тренер поправит технику каждого.</p></div>
<div class="card"><h3>Для любого уровня</h3><p>Первое занятие — знакомство с аппаратом и подбор нагрузки.</p></div>
<div class="card"><h3>Рядом с домом</h3><p>Красносельский район: не нужно ехать в центр после работы.</p></div>
<div class="card"><h3>Удобная запись</h3><p>Оставьте заявку на сайте — мы подберём время и напомним о занятии.</p></div>
</div>
</section>
<section data-block="how">
<span class="eyebrow">Как начать</span>
<h2>Три шага до первого занятия</h2>
<div class="steps">
<div><h3>Заявка</h3><p>Выберите формат и удобное время в форме записи.</p></div>
<div><h3>Пробное</h3><p>Познакомитесь с реформером, тренер оценит подвижность и цели.</p></div>
<div><h3>Абонемент</h3><p>Подберём формат и частоту занятий под ваш ритм.</p></div>
</div>
<p style="margin-top:28px"><a class="btn" href="prices.html" data-goal="home_prices">Посмотреть цены</a></p>
</section>
''')

PAGES['classes.html'] = ('Направления', 'Направления студии: групповые занятия на реформерах, индивидуальные и парные тренировки, вводный курс для новичков.', 'classes', '''
<h1>Направления</h1>
<p class="lead">Все занятия проходят на реформерах — тренажёрах с подвижной кареткой и пружинами, которые дают мягкое сопротивление и поддержку.</p>
<div class="grid" style="margin-top:28px" data-block="classes">
<div class="card"><span class="meta">55 минут · до 4 человек</span><h3>Reformer Group</h3><p>Основной формат: упражнения на всё тело, работа с осанкой, балансом и глубокими мышцами.</p><a href="booking.html?format=Группа" data-goal="class_group">Записаться →</a></div>
<div class="card"><span class="meta">4 занятия · новичкам</span><h3>Вводный курс</h3><p>Принципы пилатеса, дыхание и безопасная работа с аппаратом перед переходом в группу.</p><a href="booking.html?format=Вводный курс" data-goal="class_intro">Записаться →</a></div>
<div class="card"><span class="meta">55 минут · 1 человек</span><h3>Персональная</h3><p>Программа под ваши задачи и уровень подготовки, полное внимание тренера.</p><a href="booking.html?format=Персональная" data-goal="class_personal">Записаться →</a></div>
<div class="card"><span class="meta">55 минут · 2 человека</span><h3>Дуэт</h3><p>Персональный формат для двоих — с подругой, мамой или партнёром.</p><a href="booking.html?format=Дуэт" data-goal="class_duo">Записаться →</a></div>
</div>
<div class="note">Впервые на реформере? Прочитайте <a href="faq.html#q1">ответ для новичков</a> и <a href="faq.html#q2">что взять с собой</a>. Если есть травмы или ограничения по здоровью, перед началом занятий проконсультируйтесь с врачом и предупредите тренера.</div>
''')

SCH = [('Пн', '08:00 Group', '19:00 Group', '20:15 Group'), ('Вт', '10:00 Вводный', '19:00 Group', '20:15 Персональные'),
       ('Ср', '08:00 Group', '19:00 Group', '20:15 Group'), ('Чт', '10:00 Вводный', '19:00 Group', '20:15 Дуэт'),
       ('Пт', '08:00 Group', '18:30 Group', '—'), ('Сб', '10:00 Group', '11:15 Group', '12:30 Вводный'), ('Вс', '11:00 Group', '12:15 Персональные', '—')]
rows = ''.join(f'<tr><td><b>{d}</b></td><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for d, a, b, c in SCH)
PAGES['schedule.html'] = ('Расписание', 'Расписание занятий пилатес-студии «Линия»: утренние, вечерние и выходные слоты.', 'schedule', f'''
<h1>Расписание</h1>
<p class="lead">Предварительное расписание на время открытия. Каждый слот — максимум 4 места.</p>
<div class="tablewrap" data-block="schedule"><table class="sch">
<tr><th>День</th><th>Утро</th><th>Вечер</th><th>Поздний вечер</th></tr>{rows}</table></div>
<a class="btn" href="booking.html" data-goal="schedule_booking">Выбрать время</a>
''')

PAGES['prices.html'] = ('Цены', 'Стоимость занятий пилатесом на реформерах: пробное, разовое, абонементы на 4, 8 и 12 занятий, персональные тренировки.', 'prices', '''
<h1>Цены</h1>
<p class="lead">Ориентировочные цены на время открытия студии.</p>
<div class="grid" style="margin-top:28px" data-block="prices">
<div class="card"><span class="meta">знакомство</span><h3>Пробное</h3><div class="price">900 ₽</div><p>Мини-группа, 55 минут</p><a href="booking.html?format=Пробное" data-goal="price_trial">Записаться →</a></div>
<div class="card"><span class="meta">разовое</span><h3>Group</h3><div class="price">1 800 ₽</div><p>Одно занятие в мини-группе</p></div>
<div class="card feat"><span class="meta">популярный</span><h3>8 занятий</h3><div class="price">12 800 ₽</div><p>1 600 ₽ за занятие, срок 6 недель</p><a href="booking.html?format=Абонемент 8" data-goal="price_8" style="color:#fff">Оформить →</a></div>
<div class="card"><span class="meta">выгоднее всего</span><h3>12 занятий</h3><div class="price">17 400 ₽</div><p>1 450 ₽ за занятие, срок 8 недель</p></div>
<div class="card"><span class="meta">1 человек</span><h3>Персональная</h3><div class="price">3 500 ₽</div><p>Индивидуальная программа</p></div>
<div class="card"><span class="meta">2 человека</span><h3>Дуэт</h3><div class="price">4 800 ₽</div><p>Цена за двоих</p></div>
</div>
''')

PAGES['studio.html'] = ('О студии', 'О пилатес-студии «Линия»: камерный зал на 4 реформера в Красносельском районе Санкт-Петербурга.', 'studio', '''
<h1>О студии</h1>
<p class="lead">«Линия» — камерная студия пилатеса на реформерах для жителей юго-запада Петербурга.</p>
<section data-block="about">
<p>Мы сознательно ограничили зал четырьмя реформерами: так в группе остаётся время на каждого, а тренировки проходят спокойно и сосредоточенно. Пилатес на реформере помогает укрепить мышцы кора, улучшить осанку и подвижность суставов — нагрузку легко подобрать под любой уровень.</p>
<div class="gallery" data-block="gallery">
<figure class="wide"><img src="img/studio-hall.jpg" alt="Зал с реформерами" loading="lazy"><figcaption>Зал на четыре реформера</figcaption></figure>
<figure><img src="img/studio-lockers.jpg" alt="Раздевалка с зеркалами и шкафчиками" loading="lazy"><figcaption>Раздевалка</figcaption></figure>
</div>
<h2>Что внутри</h2>
<div class="grid">
<div class="card"><h3>Зал</h3><p>Четыре профессиональных реформера, естественный свет, тихая музыка.</p></div>
<div class="card"><h3>Раздевалка</h3><p>Шкафчики, душ, фен и всё необходимое после тренировки.</p></div>
<div class="card"><h3>Чай и вода</h3><p>Можно прийти заранее и выпить чаю перед занятием.</p></div>
</div>
</section>
<section data-block="map">
<h2>Как добраться</h2>
<p>Красносельский район, Санкт-Петербург. Точный адрес сообщим при записи.</p>
<a class="btn ghost" href="https://yandex.ru/maps/?text=Красносельский%20район%20Санкт-Петербург" target="_blank" rel="noopener" data-goal="route_click">Открыть карту района</a>
</section>
''')

FAQ = [
    ('Я никогда не занималась пилатесом. Мне подойдёт?', 'Да. Начните с пробного занятия или вводного курса: тренер покажет, как работать с реформером, и подберёт нагрузку.'),
    ('Что взять с собой?', 'Удобную облегающую одежду и носки с нескользящей подошвой. Полотенце и воду выдадим в студии.'),
    ('Чем реформер отличается от пилатеса на коврике?', 'Пружины реформера дают регулируемое сопротивление и поддержку, поэтому упражнения можно точнее дозировать и усложнять.'),
    ('Как часто нужно заниматься?', 'Оптимально 2–3 раза в неделю: так результат заметен уже через месяц.'),
    ('Можно ли заморозить абонемент?', 'Да, один раз на срок до 14 дней.'),
    ('Как отменить занятие?', 'Сообщите не позднее чем за 12 часов — занятие не будет списано.'),
]
faq = ''.join(f'<details id="q{i}" data-goal="faq_open"><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(FAQ, 1))
PAGES['faq.html'] = ('Вопросы и ответы', 'Частые вопросы о занятиях пилатесом на реформерах: новичкам, что взять, как часто заниматься, заморозка и отмена.', 'faq', f'''
<h1>Вопросы и ответы</h1>
<p class="lead">Если не нашли ответ — спросите в форме записи, мы ответим.</p>
<div data-block="faq" style="margin-top:24px">{faq}</div>
''')

PAGES['booking.html'] = ('Запись', 'Запись на пробное занятие и абонементы в пилатес-студию «Линия».', 'booking', '''
<h1>Запись на занятие</h1>
<p class="lead">Выберите формат и удобное время. Студия готовится к открытию: форма учебная, данные никуда не отправляются и не сохраняются.</p>
<form id="booking" class="fb" action="thanks.html" method="get" data-block="booking-form">
<label for="format">Формат</label>
<select id="format" name="format"><option>Пробное</option><option>Группа</option><option>Вводный курс</option><option>Персональная</option><option>Дуэт</option><option>Абонемент 8</option></select>
<label for="time">Удобное время</label>
<select id="time" name="time"><option>Утро (8:00–12:00)</option><option>Вечер (18:30–21:00)</option><option>Выходные</option></select>
<label for="level">Опыт пилатеса</label>
<select id="level" name="level"><option>Нет опыта</option><option>Занималась на коврике</option><option>Занималась на реформере</option></select>
<label for="msg">Комментарий</label>
<textarea id="msg" name="m" placeholder="Например: хочу укрепить спину"></textarea>
<p><button class="btn" type="submit" id="btn-send">Отправить заявку</button></p>
</form>
''')

PAGES['thanks.html'] = ('Заявка отправлена', 'Спасибо за заявку.', 'thanks', '''
<h1>Спасибо!</h1>
<p class="lead">Заявка получена. Когда студия откроется, мы свяжемся с вами и подберём время первого занятия.</p>
<a class="btn" href="index.html">На главную</a>
''')

os.makedirs(OUT, exist_ok=True)
for fname, (title, desc, pid, body) in PAGES.items():
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as fh:
        fh.write(page(fname, title, desc, body, pid))
import shutil
here = os.path.dirname(os.path.abspath(__file__))
for f in ('style.css', 'main.js', 'favicon.svg'):
    shutil.copy(os.path.join(here, f), OUT)
shutil.copytree(os.path.join(here, 'fonts'), os.path.join(OUT, 'fonts'), dirs_exist_ok=True)
shutil.copytree(os.path.join(here, 'img'), os.path.join(OUT, 'img'), dirs_exist_ok=True)
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n')
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
print('built', len(PAGES), 'pages ->', os.path.abspath(OUT), '| TOP100:', TOP100_ID, '| TMR:', TMR_ID)
