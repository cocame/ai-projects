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
- файл: ~/Downloads/site/index.html
- github: https://github.com/cocame/site
- деплой: git -C ~/Downloads/site add . && git -C ~/Downloads/site commit -m "update" && git -C ~/Downloads/site push

### ⚠️ ПРАВИЛО для работы над ~/Downloads/site/
При работе над этим проектом разрешено **только читать и копировать** файлы из:
- `~/Downloads/narada-travels/`
- `~/Downloads/cocame.github.io/narada-travels/`

**Редактировать эти папки категорически запрещено.**

## ai-projects — правила и манифесты
- папка: ~/AI_Projects/
- github: https://github.com/cocame/ai-projects
- деплой: cd ~/AI_Projects && git add . && git commit -m "update" && git push

---

## ПРАВИЛО: после любых изменений в коде
Всегда открывать сайт в браузере автоматически после пуша — без напоминания пользователя.

---

## ПРАВИЛА РАЗРАБОТКИ SITE — стиль Apple

### Визуальная структура (Frontend)
- HTML: hero → tours fullscreen → water-cards grid → footer bar
- Шрифт: -apple-system, BlinkMacSystemFont, SF Pro Display — системный, без Google Fonts
- Цвета: фон #0a0a0a, текст #ffffff, акцент rgba(255,255,255,0.45)
- Кнопки: border-radius 980px, border 1px solid rgba(255,255,255,0.45), без заливки
- Дизайн: без засечек, без золота, без градиентов на тексте
- Адаптив: мобилка от 390px, кнопки auto width, шрифт clamp()

### UX и поведение
- Пользователь видит Hero → листает туры → нажимает "Написать нам" → WhatsApp
- Hover на кнопках: opacity 0.75, transition 0.3s
- Scroll: parallax на фото hero, текст фиксирован

### Стек
- Один файл HTML+CSS+JS, без фреймворков
- GSAP для анимаций (только фото, не текст)
- Деплой: GitHub Pages → cocame.github.io/site
- Актуальный файл: ~/Downloads/site/index.html

### После каждого изменения
1. Перезапустить сервер: lsof -ti:8080 | xargs kill -9 2>/dev/null; mkdir -p ~/Downloads/site && cd ~/Downloads/site && python3 -m http.server 8080 > /dev/null 2>&1 &
2. Открыть браузер: open http://localhost:8080
3. Сделать скриншот и показать результат без лишних вопросов
4. Отправить в продакшен для телефона: git -C ~/Downloads/site add . && git -C ~/Downloads/site commit -m "update" && git -C ~/Downloads/site push
