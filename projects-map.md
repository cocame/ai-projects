# КАРТА ПРОЕКТОВ НАРАДЫ

## ПРАВИЛО: при добавлении тура или изменении цен — обновить ВСЕ эти места

### 1. ~/Downloads/narada/index.html — прайс-калькулятор + бронь
- Массив `TOURS` — добавить объект `{ icon, name, key, rows:[{label, usd}] }`
- Объект `COMM_RATES` — добавить `'КЛЮЧ': комиссия`
- Объект `ROUTE_ALIASES` — добавить массив алиасов для распознавания тура
- github: https://github.com/cocame/narada

### 2. ~/Downloads/cocame.github.io/narada-site/index.html — публичный сайт
- CSS bento-сетка — добавить класс `.b-keyname { grid-column: span N; }` и мобильный reset
- HTML bento — добавить карточку `<div class="bc b-keyname">`
- JS объект `tours` — добавить полный объект с программой и ценами
- Форма `<select name="tour">` — добавить `<option>Название (от X$)</option>`
- github: https://github.com/cocame/cocame.github.io (папка narada-site)

### 3. ~/Downloads/tours/index.html — CRM-панель расписания
- `<select id="edutTour">` — добавить `<option>Название</option>`
- `.tour-checkboxes` — добавить `<label class="tour-check"><input type="checkbox" value="Название"> Название</label>`
- github: https://github.com/cocame/tours

---

## narada — калькулятор бронирований
- файл: ~/Downloads/narada/index.html
- github: https://github.com/cocame/narada
- деплой: git -C ~/Downloads/narada add . && git -C ~/Downloads/narada commit -m "update" && git -C ~/Downloads/narada push

## cocame.github.io — публичный сайт (narada-site)
- файл: ~/Downloads/cocame.github.io/narada-site/index.html
- github: https://github.com/cocame/cocame.github.io
- деплой: git -C ~/Downloads/cocame.github.io add . && git -C ~/Downloads/cocame.github.io commit -m "update" && git -C ~/Downloads/cocame.github.io push

## tours — CRM-панель расписания
- файл: ~/Downloads/tours/index.html
- github: https://github.com/cocame/tours
- деплой: git -C ~/Downloads/tours add . && git -C ~/Downloads/tours commit -m "update" && git -C ~/Downloads/tours push

## site — сайт narada-travels.com
- файл: ~/Downloads/site/index_v4.html
- github: https://github.com/cocame/site
- деплой: git -C ~/Downloads/site add . && git -C ~/Downloads/site commit -m "update" && git -C ~/Downloads/site push

## ai-projects — правила и манифесты
- папка: ~/AI_Projects/
- github: https://github.com/cocame/ai-projects
- деплой: cd ~/AI_Projects && git add . && git commit -m "update" && git push
