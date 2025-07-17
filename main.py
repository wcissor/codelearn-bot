from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔥 Начать обучение", callback_data="start_learning")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Start/старт",
        reply_markup=reply_markup
    )


async def zero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "start_learning":
        keyboard = [
            [InlineKeyboardButton("русский", callback_data="russian")],
            [InlineKeyboardButton("english", callback_data="english")],
            [InlineKeyboardButton("中國人", callback_data="firstchinese")],
            [InlineKeyboardButton("Türkçe", callback_data="tuk")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌍 *Choose your language / Выберите язык / Dil seçin / 選擇語言*\n\n"
                                      "🇬🇧 English\n"
                               
                                      "🇷🇺 Русский\n"
                                      "🇦🇿 Azərbaycan dili\n"
                                      "🇹🇷 Türkçe\n"
                                      "🇹🇼 繁體中文\n"
                                      "➡️ Please tap your language / Пожалуйста, выберите язык / Zəhmət olmasa, dili seçin / 請選擇語言",
                                      reply_markup=reply_markup
                                      )


async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "russian":
        keyboard = [[InlineKeyboardButton("🔥 Начать обучение", callback_data="xxx")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Привет! Готов учиться программированию?\n"
            ,
            reply_markup=reply_markup
        )
    elif query.data == "xxx":
        keyboard = [
            [InlineKeyboardButton("Языки программирования", callback_data="continue_learning")],
            [InlineKeyboardButton("Кибербезопасность", callback_data="cybersecurity")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🚀 Отлично! Теперь выбери, что хочешь изучать:",
            reply_markup=reply_markup
        )
    elif query.data == "continue_learning":
        keyboard = [
            [InlineKeyboardButton("🐍 Python ", callback_data="python")],
            [InlineKeyboardButton("⚙️ C++ ", callback_data="cpp")],
            [InlineKeyboardButton("🟨 Javascript", callback_data="script")],
            [InlineKeyboardButton("☕ Java ", callback_data="toomycash")],
            [InlineKeyboardButton("💻 C", callback_data="huggywuggy")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "ХОРОШО!! Теперь выберите, какой язык вы хотите изучать:",
            reply_markup=reply_markup
        )

    elif query.data == "cybersecurity":
        keyboard = [
            [InlineKeyboardButton("📡Networks", callback_data="cyber")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Давайте начнем!\nГлава 1",
            reply_markup=reply_markup
        )

    elif query.data == "cyber":
        keyboard = [
            [InlineKeyboardButton("следующая глава➡️", callback_data="next")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 Сети — это просто связанные между собой объекты.\n"
                                      "Например, ваш круг друзей: вы связаны между собой благодаря общим интересам,\n"
                                      "хобби, навыкам и другим вещам. 🧠🤝\n\n"
                                      "📡 Сети встречаются повсюду:\n"
                                      " - 🚇 Общественный транспорт в городе\n"
                                      " - ⚡ Инфраструктура, такая как национальная электросеть\n"
                                      " - 🏘️ Общение с соседями\n"
                                      " - ✉️ Почтовые системы для отправки писем и посылок\n\n"
                                      "💻 В информатике — та же идея, но применённая к технологиям.\n"
                                      "Возьмём ваш телефон 📱: причина, по которой вы его используете — доступ к информации.\n\n"
                                      "📶 Мы рассмотрим, как устройства обмениваются данными и какие правила при этом действуют.\n\n"
                                      "🖥️ В вычислительной технике сеть может состоять от 2 до миллиардов устройств.\n"
                                      "Сюда входят:\n"
                                      " - 💻 Ноутбуки\n"
                                      " - 📱 Смартфоны\n"
                                      " - 📷 Камеры видеонаблюдения\n"
                                      " - 🚦 Светофоры\n"
                                      " - 🌾 Даже фермерская техника!\n\n"
                                      "🔌 Сети встроены в нашу повседневную жизнь:\n"
                                      " - ⛅ Сбор данных о погоде\n"
                                      " - ⚡ Подача электроэнергии в дома\n"
                                      " - 🚦 Определение приоритета движения на дороге\n\n"
                                      "🛡️ Поскольку сети стали неотъемлемой частью современной жизни,\n"
                                      "понимание принципов сетей — это основа для изучения кибербезопасности.\n\n"
                                      "👥 Посмотрите на схему ниже: Алиса, Боб и Джим образовали свою сеть!\n"
                                      "К этому мы ещё вернёмся позже...\n"
                                      "The first chapter is here!!\n"
                                      "Первая глава уже здесь!!"
                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "next":
        keyboard = [
            [InlineKeyboardButton("следующая глава➡️", callback_data="two")],
            [InlineKeyboardButton("прошлая глава",callback_data = "creschekgrfhrihiginggvfgigisthgifenjidhffkdnnvkjb")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Глава 2: Погружаемся в Интернет!*\n\n"
                                      "Теперь, когда ты понял, что такое сеть — просто соединённые между собой устройства — давай разберёмся, как работает Интернет.\n\n"
                                      "📡 Интернет — это просто *огромная сеть*, которая состоит из множества маленьких сетей, объединённых между собой.\n\n"
                                      "👫 Представь, что у Алисы появились новые друзья — Зейн и Тоби. Она хочет познакомить их с Бобом и Джимом. Но есть одна проблема: "
                                      "только Алиса понимает язык обеих групп. Поэтому она становится *связующим звеном* — теперь все могут общаться через неё. Это пример новой сети.\n\n"
                                      "📜 Первая версия Интернета появилась в конце 1960-х в рамках проекта *ARPANET*, финансируемого военными США. "
                                      "Это была первая реально работающая сеть между компьютерами.\n\n"
                                      "🌍 А в 1989 году Тим Бернерс-Ли предложил концепцию *Всемирной паутины (WWW)*, которая превратила Интернет в удобное средство для обмена и хранения информации.\n\n"
                                      "🔌 Интернет сегодня — это как огромный клуб из тысяч маленьких команд. Есть два типа сетей:\n"
                                      " - 🔒 Частные сети (Private Networks)\n"
                                      " - 🌐 Публичные сети (Public Networks), которые и составляют то, что мы называем Интернетом\n\n"
                                      "💡 Устройства в сети используют специальные *идентификаторы* (мы поговорим о них дальше), чтобы находить друг друга и передавать данные.\n"
                                      "последняя глава здесь!!!"
                                      ,
                                      reply_markup=reply_markup)
    elif query.data == "creschekgrfhrihiginggvfgigisthgifenjidhffkdnnvkjb":
        keyboard = [
            [InlineKeyboardButton("следующая глава➡️", callback_data="next")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 Сети — это просто связанные между собой объекты.\n"
                                      "Например, ваш круг друзей: вы связаны между собой благодаря общим интересам,\n"
                                      "хобби, навыкам и другим вещам. 🧠🤝\n\n"
                                      "📡 Сети встречаются повсюду:\n"
                                      " - 🚇 Общественный транспорт в городе\n"
                                      " - ⚡ Инфраструктура, такая как национальная электросеть\n"
                                      " - 🏘️ Общение с соседями\n"
                                      " - ✉️ Почтовые системы для отправки писем и посылок\n\n"
                                      "💻 В информатике — та же идея, но применённая к технологиям.\n"
                                      "Возьмём ваш телефон 📱: причина, по которой вы его используете — доступ к информации.\n\n"
                                      "📶 Мы рассмотрим, как устройства обмениваются данными и какие правила при этом действуют.\n\n"
                                      "🖥️ В вычислительной технике сеть может состоять от 2 до миллиардов устройств.\n"
                                      "Сюда входят:\n"
                                      " - 💻 Ноутбуки\n"
                                      " - 📱 Смартфоны\n"
                                      " - 📷 Камеры видеонаблюдения\n"
                                      " - 🚦 Светофоры\n"
                                      " - 🌾 Даже фермерская техника!\n\n"
                                      "🔌 Сети встроены в нашу повседневную жизнь:\n"
                                      " - ⛅ Сбор данных о погоде\n"
                                      " - ⚡ Подача электроэнергии в дома\n"
                                      " - 🚦 Определение приоритета движения на дороге\n\n"
                                      "🛡️ Поскольку сети стали неотъемлемой частью современной жизни,\n"
                                      "понимание принципов сетей — это основа для изучения кибербезопасности.\n\n"
                                      "👥 Посмотрите на схему ниже: Алиса, Боб и Джим образовали свою сеть!\n"
                                      "К этому мы ещё вернёмся позже...\n"
                                      "The first chapter is here!!\n"
                                      "Первая глава уже здесь!!"
                                      ,
                                      reply_markup=reply_markup)


    elif query.data == "two":
        keyboard = [
            [InlineKeyboardButton("следующая глава➡️", callback_data="three")],
            [InlineKeyboardButton("прошлая глава", callback_data="creschemolecresclecreschemole")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("""
📡 Чтобы устройства могли общаться и поддерживать порядок в сети, они должны:\n
— Узнавать себя\n
— Быть узнаваемыми другими\n

💡 Устройства в этом похожи на людей:\n
— У нас есть имя (можно сменить)\n
— И отпечатки пальцев (уникальны навсегда)\n

📱 Устройства тоже имеют два типа "идентификации":\n
— IP-адрес (📍можно изменить)\n
— MAC-адрес (🔒постоянный, как отпечаток пальца)\n

=====================\n
🔹 IP-адреса\n
=====================\n
IP-адрес — это как временное имя устройства в сети.\n
Он состоит из 4 чисел (октетов), разделённых точками:\n
Пример: `192.168.0.1`\n

🔁 Один IP может быть передан другому устройству, но два устройства с одним IP **не могут** работать одновременно в одной сети.\n

🌍 Существуют два вида IP-адресов:\n
— **Приватный IP** — используется внутри локальной сети (дом, офис)\n
— **Публичный IP** — виден в Интернете\n

🧾 Пример:\n
| Устройство      | Приватный IP     | Публичный IP      |\n
|----------------|------------------|-------------------|\n
| Мой ПК         | 192.168.1.77     | 86.157.52.21      |\n
| Другой ПК      | 192.168.1.74     | 86.157.52.21      |\n

🔍 Оба устройства имеют **одинаковый публичный IP** (один модем), но **разные приватные** — так они могут общаться в одной сети.\n

=====================\n
🌐 Проблема: адресов не хватает!\n
=====================\n
IPv4 = 4.29 миллиарда адресов (2^32). Но устройств в мире — **десятки миллиардов**.\n

💡 Решение:\n
— IPv6 = 340+ триллионов адресов (2^128)\n
— Более эффективно\n
— Гораздо больше адресов\n

Пример:\n
— IPv4: `192.168.1.1`\n
— IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`\n

=====================\n
🔹 MAC-адреса\n
=====================\n
Каждое устройство имеет сетевой адаптер с уникальным адресом — **MAC-адрес**.\n
Формат: `a4:c3:f0:85:ac:2d` (6 байт в 16-ричной форме)\n

🛠 Первые 6 символов — производитель.\n
📌 Последние 6 — уникальный номер устройства.\n

💥 Но MAC-адрес можно подделать — это называется **спуфинг**:\n
— Злоумышленник может выдать себя за другое устройство.\n
— Если, например, firewall пропускает только MAC-адрес админа — его можно обмануть!\n

=====================\n
📌 Вывод:\n
=====================\n
🔹 IP — меняется, зависит от сети.\n
🔹 MAC — постоянный, уникальный.\n
🔹 Для безопасности важно учитывать, что ни IP, ни MAC не гарантируют подлинность.\n
последняя глава здесь!!!
""",
                                      reply_markup=reply_markup)
    elif query.data == "creschemolecresclecreschemole":
        keyboard = [
            [InlineKeyboardButton("следующая глава➡️", callback_data="two")],
            [InlineKeyboardButton("прошлая глава", callback_data="creschekgrfhrihiginggvfgigisthgifenjidhffkdnnvkjb")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Глава 2: Погружаемся в Интернет!*\n\n"
                                      "Теперь, когда ты понял, что такое сеть — просто соединённые между собой устройства — давай разберёмся, как работает Интернет.\n\n"
                                      "📡 Интернет — это просто *огромная сеть*, которая состоит из множества маленьких сетей, объединённых между собой.\n\n"
                                      "👫 Представь, что у Алисы появились новые друзья — Зейн и Тоби. Она хочет познакомить их с Бобом и Джимом. Но есть одна проблема: "
                                      "только Алиса понимает язык обеих групп. Поэтому она становится *связующим звеном* — теперь все могут общаться через неё. Это пример новой сети.\n\n"
                                      "📜 Первая версия Интернета появилась в конце 1960-х в рамках проекта *ARPANET*, финансируемого военными США. "
                                      "Это была первая реально работающая сеть между компьютерами.\n\n"
                                      "🌍 А в 1989 году Тим Бернерс-Ли предложил концепцию *Всемирной паутины (WWW)*, которая превратила Интернет в удобное средство для обмена и хранения информации.\n\n"
                                      "🔌 Интернет сегодня — это как огромный клуб из тысяч маленьких команд. Есть два типа сетей:\n"
                                      " - 🔒 Частные сети (Private Networks)\n"
                                      " - 🌐 Публичные сети (Public Networks), которые и составляют то, что мы называем Интернетом\n\n"
                                      "💡 Устройства в сети используют специальные *идентификаторы* (мы поговорим о них дальше), чтобы находить друг друга и передавать данные.\n"
                                      "последняя глава здесь!!!"
                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "three":
        keyboard = [[InlineKeyboardButton("прошлая глава",callback_data = "crmovefveiuorhoe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Ping — это базовый сетевой инструмент, позволяющий проверить наличие соединения между двумя устройствами.\n"
            "Он работает на основе протокола ICMP (Internet Control Message Protocol),\n"
            "отправляя специальные эхо-запросы и ожидая эхо-ответов от целевого узла.\n\n"

            "С помощью ping можно определить, работает ли соединение, и насколько оно стабильно.\n"
            "Также можно измерить, за сколько миллисекунд пакеты проходят от одного устройства до другого.\n\n"

            "Этот инструмент уже встроен в большинство операционных систем, включая Linux и Windows.\n"
            "Чтобы выполнить пинг, достаточно ввести команду:\n"
            "`ping IP-адрес` или `ping имя_сайта` в терминале или командной строке.\n\n"

            "Например, если выполнить команду `ping 192.168.1.254`,\n"
            "можно увидеть, сколько пакетов было отправлено и получено,\n"
            "а также узнать среднее время отклика (например, 4.16 мс).", reply_markup = reply_markup)
    elif query.data == "crmovefveiuorhoe":
        keyboard = [
            [InlineKeyboardButton("следующая глава➡️", callback_data="three")],
            [InlineKeyboardButton("прошлая глава", callback_data="creschemolecresclecreschemole")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("""
        📡 Чтобы устройства могли общаться и поддерживать порядок в сети, они должны:\n
        — Узнавать себя\n
        — Быть узнаваемыми другими\n

        💡 Устройства в этом похожи на людей:\n
        — У нас есть имя (можно сменить)\n
        — И отпечатки пальцев (уникальны навсегда)\n

        📱 Устройства тоже имеют два типа "идентификации":\n
        — IP-адрес (📍можно изменить)\n
        — MAC-адрес (🔒постоянный, как отпечаток пальца)\n

        =====================\n
        🔹 IP-адреса\n
        =====================\n
        IP-адрес — это как временное имя устройства в сети.\n
        Он состоит из 4 чисел (октетов), разделённых точками:\n
        Пример: `192.168.0.1`\n

        🔁 Один IP может быть передан другому устройству, но два устройства с одним IP **не могут** работать одновременно в одной сети.\n

        🌍 Существуют два вида IP-адресов:\n
        — **Приватный IP** — используется внутри локальной сети (дом, офис)\n
        — **Публичный IP** — виден в Интернете\n

        🧾 Пример:\n
        | Устройство      | Приватный IP     | Публичный IP      |\n
        |----------------|------------------|-------------------|\n
        | Мой ПК         | 192.168.1.77     | 86.157.52.21      |\n
        | Другой ПК      | 192.168.1.74     | 86.157.52.21      |\n

        🔍 Оба устройства имеют **одинаковый публичный IP** (один модем), но **разные приватные** — так они могут общаться в одной сети.\n

        =====================\n
        🌐 Проблема: адресов не хватает!\n
        =====================\n
        IPv4 = 4.29 миллиарда адресов (2^32). Но устройств в мире — **десятки миллиардов**.\n

        💡 Решение:\n
        — IPv6 = 340+ триллионов адресов (2^128)\n
        — Более эффективно\n
        — Гораздо больше адресов\n

        Пример:\n
        — IPv4: `192.168.1.1`\n
        — IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`\n

        =====================\n
        🔹 MAC-адреса\n
        =====================\n
        Каждое устройство имеет сетевой адаптер с уникальным адресом — **MAC-адрес**.\n
        Формат: `a4:c3:f0:85:ac:2d` (6 байт в 16-ричной форме)\n

        🛠 Первые 6 символов — производитель.\n
        📌 Последние 6 — уникальный номер устройства.\n

        💥 Но MAC-адрес можно подделать — это называется **спуфинг**:\n
        — Злоумышленник может выдать себя за другое устройство.\n
        — Если, например, firewall пропускает только MAC-адрес админа — его можно обмануть!\n

        =====================\n
        📌 Вывод:\n
        =====================\n
        🔹 IP — меняется, зависит от сети.\n
        🔹 MAC — постоянный, уникальный.\n
        🔹 Для безопасности важно учитывать, что ни IP, ни MAC не гарантируют подлинность.\n
        последняя глава здесь!!!
        """,
                                      reply_markup=reply_markup)


    elif query.data == "python":
        keyboard = [[
            InlineKeyboardButton("погнали", callback_data="numberone")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "«ХОРОШО!! Давайте начнем наше путешествие по Python 🐍»",
            reply_markup=reply_markup)
    elif query.data == "cpp":
        keyboard = [[
            InlineKeyboardButton("глава 1", callback_data="cpone")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "ХОРОШО!! Давайте начнем наше путешествие по C++ ⚙️",
            reply_markup=reply_markup)
    elif query.data == "script":
        keyboard = [[
            InlineKeyboardButton("глава 1", callback_data="jvone")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "ХОРОШО!! Давайте начнем наше путешествие по 🟨 джаваскрипт ",
            reply_markup=reply_markup)
    elif query.data == "numberone":
        keyboard = [[InlineKeyboardButton("🐍Начать", callback_data="mcqueen")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Давайте начнем!\nГлава 1:", reply_markup=reply_markup)

    elif query.data == "mcqueen":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="fuckincarti")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Установка Python 64-bit и подключение к PyCharm Community*\n\n"
            "🔹 *Шаг 1: Скачай Python*\n"
            "[Скачать Python](https://www.python.org/downloads/) — выбери Windows x86-64 executable installer\n\n"
            "🔹 *Шаг 2: Установка*\n"
            "— Поставь галочку Add Python to PATH\n"
            "— Выбери Customize Installation → Next → Install for all users → Install\n\n"
            "🔹 *Шаг 3: Проверка*\n"
            "`python --version` в терминале — должно быть Python 3.X.X\n\n"
            "🔹 *Шаг 4: Скачай PyCharm*\n"
            "[Скачать PyCharm](https://www.jetbrains.com/pycharm/download)\n"
            "— Установи версию Community\n\n"
            "🔹 *Шаг 5: Подключи Python*\n"
            "New Project → ⚙️ Add Interpreter → System Interpreter → путь:\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *Проверка:*\n"
            "Создай файл с кодом:\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "Нажми ▶️ Run",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "fuckincarti":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="ifelifelse")],
                    [InlineKeyboardButton("прошлая глава",callback_data = "nikogonebudetprostopodpishi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Переменные и типы данных в Python*\n\n"
            "🔹 *Что такое переменная?*\n"
            "— Это имя для хранения данных. Тип определяется автоматически.\n\n"
            "🔹 *Примеры переменных:*\n"
            "`x = 10` — целое число (int)\n"
            "`name = \"Tom\"` — строка (str)\n"
            "`pi = 3.14` — число с плавающей точкой (float)\n\n"
            "🔹 *Основные типы данных:*\n"
            "- int — целые числа\n"
            "- float — числа с десятичной точкой\n"
            "- str — текстовые строки\n"
            "- bool — True / False (логика)\n\n"
            "🔹 *Как вывести данные?*\n"
            "`print(x)`\n`print(name)`\n`print(pi)`\n\n"
            "✅ *Попробуй сам:*\n"
            "```python\nage = 15\ncity = \"Москва\"\nis_student = True\n\n"
            "print(\"Возраст:\", age)\nprint(\"Город:\", city)\nprint(\"Студент:\", is_student)\n```",
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "nikogonebudetprostopodpishi":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="fuckincarti")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Установка Python 64-bit и подключение к PyCharm Community*\n\n"
            "🔹 *Шаг 1: Скачай Python*\n"
            "[Скачать Python](https://www.python.org/downloads/) — выбери Windows x86-64 executable installer\n\n"
            "🔹 *Шаг 2: Установка*\n"
            "— Поставь галочку Add Python to PATH\n"
            "— Выбери Customize Installation → Next → Install for all users → Install\n\n"
            "🔹 *Шаг 3: Проверка*\n"
            "`python --version` в терминале — должно быть Python 3.X.X\n\n"
            "🔹 *Шаг 4: Скачай PyCharm*\n"
            "[Скачать PyCharm](https://www.jetbrains.com/pycharm/download)\n"
            "— Установи версию Community\n\n"
            "🔹 *Шаг 5: Подключи Python*\n"
            "New Project → ⚙️ Add Interpreter → System Interpreter → путь:\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *Проверка:*\n"
            "Создай файл с кодом:\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "Нажми ▶️ Run",
            parse_mode="Markdown", reply_markup=reply_markup
        )


    elif query.data == "ifelifelse":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="sezer")],
                    [InlineKeyboardButton("прошлая глава",callback_data = "egegeggeeggemeoreoy")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Условия в Python: if, elif, else*\n\n"
            "🔹 *Что такое условие?*\n"
            "— Это способ выполнять код, только если выполнено определённое условие.\n"
            "— Используется if, elif, else\n\n"
            "🔹 *Синтаксис:*\n"
            "```python\nage = 16\n\nif age >= 18:\n    print(\"Ты совершеннолетний\")\n"
            "elif age >= 14:\n    print(\"Ты подросток\")\nelse:\n    print(\"Ты ребёнок\")\n```\n\n"
            "🔹 *Операторы сравнения:* ==, !=, >, <, >=, <=\n"
            "🔹 *Логические операторы:* and, or, not\n\n"
            "✅ *Попробуй сам:*\n"
            "```python\nname = input(\"Твоё имя: \")\nif name == \"Tom\":\n    print(\"Привет, Том!\")\n"
            "else:\n    print(\"Привет, гость!\")\n```",
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "egegeggeeggemeoreoy":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="ifelifelse")],
                    [InlineKeyboardButton("прошлая глава", callback_data="nikogonebudetprostopodpishi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Переменные и типы данных в Python*\n\n"
            "🔹 *Что такое переменная?*\n"
            "— Это имя для хранения данных. Тип определяется автоматически.\n\n"
            "🔹 *Примеры переменных:*\n"
            "`x = 10` — целое число (int)\n"
            "`name = \"Tom\"` — строка (str)\n"
            "`pi = 3.14` — число с плавающей точкой (float)\n\n"
            "🔹 *Основные типы данных:*\n"
            "- int — целые числа\n"
            "- float — числа с десятичной точкой\n"
            "- str — текстовые строки\n"
            "- bool — True / False (логика)\n\n"
            "🔹 *Как вывести данные?*\n"
            "`print(x)`\n`print(name)`\n`print(pi)`\n\n"
            "✅ *Попробуй сам:*\n"
            "```python\nage = 15\ncity = \"Москва\"\nis_student = True\n\n"
            "print(\"Возраст:\", age)\nprint(\"Город:\", city)\nprint(\"Студент:\", is_student)\n```",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "sezer":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="tututu")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zabiliibudemjitdalse")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python: Циклы for и while*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Это конструкция для повторного выполнения блока кода.\n"
                                      "— Используется для перебора списков, чисел и других коллекций.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл for:*\n"
                                      "```python\nfor i in range(5):\n    print(i)\n```\n"
                                      "— Выведет числа от 0 до 4.\n\n"
                                      "🔸 range(5) создаёт последовательность: 0, 1, 2, 3, 4\n\n"
                                      "============================\n"
                                      "🔹 *Цикл while:*\n"
                                      "```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```\n"
                                      "— Повторяет блок кода, пока условие истинно.\n\n"
                                      "============================\n"
                                      "🔹 *Перебор списка с for:*\n"
                                      "```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- for — удобен для перебора элементов\n"
                                      "- while — пока условие выполняется, цикл продолжается\n"
                                      "- Чтобы остановить цикл досрочно, можно использовать `break`\n\n"
                                      "💡 Циклы — основа автоматизации и обработки больших объёмов данных!\n"
                                      "Попробуй сам написать простой цикл и вывести список чисел или слов!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "zabiliibudemjitdalse":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="sezer")],
                    [InlineKeyboardButton("прошлая глава", callback_data="egegeggeeggemeoreoy")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Условия в Python: if, elif, else*\n\n"
            "🔹 *Что такое условие?*\n"
            "— Это способ выполнять код, только если выполнено определённое условие.\n"
            "— Используется if, elif, else\n\n"
            "🔹 *Синтаксис:*\n"
            "```python\nage = 16\n\nif age >= 18:\n    print(\"Ты совершеннолетний\")\n"
            "elif age >= 14:\n    print(\"Ты подросток\")\nelse:\n    print(\"Ты ребёнок\")\n```\n\n"
            "🔹 *Операторы сравнения:* ==, !=, >, <, >=, <=\n"
            "🔹 *Логические операторы:* and, or, not\n\n"
            "✅ *Попробуй сам:*\n"
            "```python\nname = input(\"Твоё имя: \")\nif name == \"Tom\":\n    print(\"Привет, Том!\")\n"
            "else:\n    print(\"Привет, гость!\")\n```",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "tututu":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="onyx")],
                    [InlineKeyboardButton("прошлая глава", callback_data="posletakoyjenshini")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python: Списки (list)*\n\n"
                                      "🔹 *Что такое список?*\n"
                                      "— Это упорядоченная коллекция элементов.\n"
                                      "— Можно хранить числа, строки и даже другие списки внутри.\n\n"
                                      "============================\n"
                                      "🔹 *Пример списка:*\n"
                                      "```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\n```\n"
                                      "— Список из трёх строк.\n\n"
                                      "🔸 Доступ по индексу:\n"
                                      "`fruits[0]` → \"яблоко\"\n"
                                      "`fruits[2]` → \"вишня\"\n\n"
                                      "============================\n"
                                      "🔹 *Изменение и добавление элементов:*\n"
                                      "```python\nfruits[1] = \"киви\"  # Замена 'банан' на 'киви'\nfruits.append(\"груша\")  # Добавляем элемент\n```\n\n"
                                      "============================\n"
                                      "🔹 *Перебор списка:*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 Выводит каждый элемент списка.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Индексы начинаются с 0\n"
                                      "- Можно хранить элементы разных типов\n"
                                      "- Списки изменяемы (можно добавлять, удалять элементы)\n\n"
                                      "💡 Списки — один из самых мощных инструментов для работы с коллекциями данных в Python.\n"
                                      "Попробуй создать свой список и перебрать его в цикле!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "posletakoyjenshini":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="tututu")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zabiliibudemjitdalse")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python: Циклы for и while*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Это конструкция для повторного выполнения блока кода.\n"
                                      "— Используется для перебора списков, чисел и других коллекций.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл for:*\n"
                                      "```python\nfor i in range(5):\n    print(i)\n```\n"
                                      "— Выведет числа от 0 до 4.\n\n"
                                      "🔸 range(5) создаёт последовательность: 0, 1, 2, 3, 4\n\n"
                                      "============================\n"
                                      "🔹 *Цикл while:*\n"
                                      "```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```\n"
                                      "— Повторяет блок кода, пока условие истинно.\n\n"
                                      "============================\n"
                                      "🔹 *Перебор списка с for:*\n"
                                      "```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- for — удобен для перебора элементов\n"
                                      "- while — пока условие выполняется, цикл продолжается\n"
                                      "- Чтобы остановить цикл досрочно, можно использовать `break`\n\n"
                                      "💡 Циклы — основа автоматизации и обработки больших объёмов данных!\n"
                                      "Попробуй сам написать простой цикл и вывести список чисел или слов!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "onyx":
        keyboard = [[InlineKeyboardButton("прошлая глава",callback_data = "kilogramovitsteyke")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🛠️ *Функции в Python*\n\n"
                                      "🔹 *Что такое функция?*\n"
                                      "— Это блок кода, который выполняет определённую задачу.\n"
                                      "— Функции помогают избежать повторения кода и делают программы понятнее.\n\n"
                                      "============================\n"
                                      "🔹 *Простейшая функция:*\n"
                                      "```python\ndef say_hello():\n    print(\"Привет, мир!\")\n\nsay_hello()  # Вызов функции\n```\n"
                                      "— Ключевое слово `def`, имя функции, круглые скобки и двоеточие.\n"
                                      "— Всё, что внутри — выполняется при вызове функции.\n\n"
                                      "============================\n"
                                      "🔹 *Функция с параметрами:*\n"
                                      "```python\ndef greet(name):\n    print(\"Привет,\", name)\n\ngreet(\"Алиса\")\n```\n"
                                      "— Можно передавать значения в функцию.\n"
                                      "— Они называются аргументами или параметрами.\n\n"
                                      "============================\n"
                                      "🔹 *Функция с возвратом значения (`return`):*\n"
                                      "```python\ndef square(x):\n    return x * x\n\nresult = square(5)\nprint(result)\n```\n"
                                      "— `return` возвращает результат работы функции.\n"
                                      "— Можно сохранить результат в переменную.\n\n"
                                      "============================\n"
                                      "✅ *Почему функции важны?*\n"
                                      "- Делают код компактным и читаемым\n"
                                      "- Позволяют переиспользовать один и тот же блок кода\n"
                                      "- Можно разбивать большие программы на логические части\n\n"
                                      "💡 Сначала попробуй написать функцию, которая выводит твоё имя, потом — функцию, которая возвращает сумму двух чисел!\n"
                                      "Функции — это основа любого языка программирования! 🚀",
                                      parse_mode="Markdown",reply_markup = reply_markup
                                      )
    elif query.data == "kilogramovitsteyke":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="onyx")],
                    [InlineKeyboardButton("прошлая глава", callback_data="posletakoyjenshini")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python: Списки (list)*\n\n"
                                      "🔹 *Что такое список?*\n"
                                      "— Это упорядоченная коллекция элементов.\n"
                                      "— Можно хранить числа, строки и даже другие списки внутри.\n\n"
                                      "============================\n"
                                      "🔹 *Пример списка:*\n"
                                      "```python\nfruits = [\"яблоко\", \"банан\", \"вишня\"]\n```\n"
                                      "— Список из трёх строк.\n\n"
                                      "🔸 Доступ по индексу:\n"
                                      "`fruits[0]` → \"яблоко\"\n"
                                      "`fruits[2]` → \"вишня\"\n\n"
                                      "============================\n"
                                      "🔹 *Изменение и добавление элементов:*\n"
                                      "```python\nfruits[1] = \"киви\"  # Замена 'банан' на 'киви'\nfruits.append(\"груша\")  # Добавляем элемент\n```\n\n"
                                      "============================\n"
                                      "🔹 *Перебор списка:*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 Выводит каждый элемент списка.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Индексы начинаются с 0\n"
                                      "- Можно хранить элементы разных типов\n"
                                      "- Списки изменяемы (можно добавлять, удалять элементы)\n\n"
                                      "💡 Списки — один из самых мощных инструментов для работы с коллекциями данных в Python.\n"
                                      "Попробуй создать свой список и перебрать его в цикле!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "cpone":
        keyboard = [[InlineKeyboardButton("⚙ Начать", callback_data="rezer")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("«Начнем!\nГлава 1:»", reply_markup=reply_markup)

    elif query.data == "rezer":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="vezer")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙*Установка и старт C++:*\n\n"
            "🔹 *Шаг 1: Установи компилятор*\n"
            "[Скачать MinGW](https://sourceforge.net/projects/mingw/)\n"
            "— Установи gcc и добавь путь к bin в PATH\n\n"
            "🔹 *Шаг 2: Скачай редактор*\n"
            "[Скачать Visual Studio Code](https://code.visualstudio.com/)\n\n"
            "🔹 *Шаг 3: Проверь компилятор:*\n"
            "`g++ --version`\n\n"
            "🔹 *Шаг 4: Простой код:*\n"
            "```cpp\n#include <iostream>\nint main() {\n"
            "    std::cout << \"Hello, world!\";\n    return 0;\n}\n```\n"
            "Сохрани как `main.cpp`, скомпилируй:\n"
            "`g++ main.cpp -o main`\n`./main`",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "vezer":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="cpp3")],
                    [InlineKeyboardButton("прошлая глава", callback_data="watisthisdokkwomwmamacoco")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++: Переменные и типы данных*\n\n"
            "🔹 *Что такое переменная?*\n"
            "— Это именованная область памяти для хранения данных.\n"
            "— Перед использованием переменную нужно объявить с типом.\n\n"
            "🔹 *Примеры:*\n"
            "`int age = 15;`\n`double pi = 3.14;`\n`char grade = 'A';`\n"
            "`bool isOnline = true;`\n`std::string name = \"Tom\";`\n\n"
            "🔹 *Пример вывода:*\n"
            "```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n"
            "    int age = 15;\n    std::string name = \"Tom\";\n"
            "    std::cout << \"Имя: \" << name << \"\\n\";\n"
            "    std::cout << \"Возраст: \" << age << \"\\n\";\n    return 0;\n}\n```",
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "watisthisdokkwomwmamacoco":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="vezer")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙*Установка и старт C++:*\n\n"
            "🔹 *Шаг 1: Установи компилятор*\n"
            "[Скачать MinGW](https://sourceforge.net/projects/mingw/)\n"
            "— Установи gcc и добавь путь к bin в PATH\n\n"
            "🔹 *Шаг 2: Скачай редактор*\n"
            "[Скачать Visual Studio Code](https://code.visualstudio.com/)\n\n"
            "🔹 *Шаг 3: Проверь компилятор:*\n"
            "`g++ --version`\n\n"
            "🔹 *Шаг 4: Простой код:*\n"
            "```cpp\n#include <iostream>\nint main() {\n"
            "    std::cout << \"Hello, world!\";\n    return 0;\n}\n```\n"
            "Сохрани как `main.cpp`, скомпилируй:\n"
            "`g++ main.cpp -o main`\n`./main`",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "cpp3":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="bejing")],
                    [InlineKeyboardButton("прошлая глава", callback_data="vsevashipismafalyifotki")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++: Условия (if, else, else if)*\n\n"
            "🔹 *Что такое условие?*\n"
            "— Позволяет выполнять код при выполнении условий.\n\n"
            "🔹 *Пример:*\n"
            "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int age = 16;\n"
            "    if (age >= 18) {\n        cout << \"Ты совершеннолетний\";\n"
            "    } else if (age >= 14) {\n        cout << \"Ты подросток\";\n"
            "    } else {\n        cout << \"Ты ребёнок\";\n    }\n    return 0;\n}\n```\n\n"
            "🔹 *Операторы:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Логика:* `&&`, `||`, `!`\n\n"
            "✅ *Попробуй сам!*",
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "vsevashipismafalyifotki":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="cpp3")],
                    [InlineKeyboardButton("прошлая глава", callback_data="watisthisdokkwomwmamacoco")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++: Переменные и типы данных*\n\n"
            "🔹 *Что такое переменная?*\n"
            "— Это именованная область памяти для хранения данных.\n"
            "— Перед использованием переменную нужно объявить с типом.\n\n"
            "🔹 *Примеры:*\n"
            "`int age = 15;`\n`double pi = 3.14;`\n`char grade = 'A';`\n"
            "`bool isOnline = true;`\n`std::string name = \"Tom\";`\n\n"
            "🔹 *Пример вывода:*\n"
            "```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n"
            "    int age = 15;\n    std::string name = \"Tom\";\n"
            "    std::cout << \"Имя: \" << name << \"\\n\";\n"
            "    std::cout << \"Возраст: \" << age << \"\\n\";\n    return 0;\n}\n```",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "bejing":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="venomous")],
                    [InlineKeyboardButton("прошлая глава", callback_data="soniceandsasyyilimeem")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *C++: Циклы (for, while, do while)*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Это способ многократно выполнять один и тот же блок кода, пока выполняется условие.\n\n"
                                      "🔹 *Типы циклов в C++:*\n"
                                      "- `for` — когда заранее известно количество повторений\n"
                                      "- `while` — пока условие истинно\n"
                                      "- `do while` — сначала делает, потом проверяет условие\n\n"
                                      "============================\n"
                                      "🔹 *Пример: for*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << i << \" \";\n}\n```\n"
                                      "🔸 Вывод: `0 1 2 3 4`\n\n"
                                      "============================\n"
                                      "🔹 *Пример: while*\n"
                                      "```cpp\nint i = 0;\nwhile (i < 3) {\n    cout << i << endl;\n    i++;\n}\n```\n"
                                      "🔸 Вывод: `0`, `1`, `2`\n\n"
                                      "============================\n"
                                      "🔹 *Пример: do while*\n"
                                      "```cpp\nint i = 0;\ndo {\n    cout << i << endl;\n    i++;\n} while (i < 2);\n```\n"
                                      "🔸 Вывод: `0`, `1`\n\n"
                                      "============================\n"
                                      "✅ *Когда использовать?*\n"
                                      "- `for` — удобно для счётчиков (i = 0; i < N; i++)\n"
                                      "- `while` — когда заранее не знаешь, сколько раз\n"
                                      "- `do while` — минимум 1 раз выполнение гарантировано\n\n"
                                      "Попробуй сам!"
                                      ,
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "soniceandsasyyilimeem":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="bejing")],
                    [InlineKeyboardButton("прошлая глава", callback_data="vsevashipismafalyifotki")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++: Условия (if, else, else if)*\n\n"
            "🔹 *Что такое условие?*\n"
            "— Позволяет выполнять код при выполнении условий.\n\n"
            "🔹 *Пример:*\n"
            "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int age = 16;\n"
            "    if (age >= 18) {\n        cout << \"Ты совершеннолетний\";\n"
            "    } else if (age >= 14) {\n        cout << \"Ты подросток\";\n"
            "    } else {\n        cout << \"Ты ребёнок\";\n    }\n    return 0;\n}\n```\n\n"
            "🔹 *Операторы:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Логика:* `&&`, `||`, `!`\n\n"
            "✅ *Попробуй сам!*",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "venomous":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="zerotrust")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zdravstvuytesergeyvladimirovic")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++: Массивы (Arrays)*\n\n"
                                      "🔹 *Что такое массив?*\n"
                                      "— Это набор элементов **одного типа**, расположенных в памяти подряд.\n"
                                      "— Каждый элемент имеет свой индекс (нумерация с 0).\n\n"
                                      "============================\n"
                                      "🔹 *Пример массива:*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\n```\n"
                                      "— Создаёт массив из 5 элементов типа int.\n\n"
                                      "🔸 Доступ к элементу:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Вывод всех элементов через цикл:*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << numbers[i] << \" \";\n}\n```\n"
                                      "🔸 Вывод: `10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *Ввод значений от пользователя:*\n"
                                      "```cpp\nint a[3];\nfor (int i = 0; i < 3; i++) {\n    cin >> a[i];\n}\n```\n"
                                      "🔸 Сохраняет 3 числа в массив.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Индексы от `0` до `n - 1`\n"
                                      "- Выход за границы массива = ❌ ошибка (UB — undefined behavior)\n"
                                      "- Все элементы одного типа (int, float, char и т.д.)\n\n"
                                      "💡 Массивы — это основа. С ними ты изучишь работу с памятью, сортировку, алгоритмы!\n\n"
                                      "Попробуй создать массив и вывести его элементы!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "zdravstvuytesergeyvladimirovic":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="venomous")],
                    [InlineKeyboardButton("прошлая глава", callback_data="soniceandsasyyilimeem")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *C++: Циклы (for, while, do while)*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Это способ многократно выполнять один и тот же блок кода, пока выполняется условие.\n\n"
                                      "🔹 *Типы циклов в C++:*\n"
                                      "- `for` — когда заранее известно количество повторений\n"
                                      "- `while` — пока условие истинно\n"
                                      "- `do while` — сначала делает, потом проверяет условие\n\n"
                                      "============================\n"
                                      "🔹 *Пример: for*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << i << \" \";\n}\n```\n"
                                      "🔸 Вывод: `0 1 2 3 4`\n\n"
                                      "============================\n"
                                      "🔹 *Пример: while*\n"
                                      "```cpp\nint i = 0;\nwhile (i < 3) {\n    cout << i << endl;\n    i++;\n}\n```\n"
                                      "🔸 Вывод: `0`, `1`, `2`\n\n"
                                      "============================\n"
                                      "🔹 *Пример: do while*\n"
                                      "```cpp\nint i = 0;\ndo {\n    cout << i << endl;\n    i++;\n} while (i < 2);\n```\n"
                                      "🔸 Вывод: `0`, `1`\n\n"
                                      "============================\n"
                                      "✅ *Когда использовать?*\n"
                                      "- `for` — удобно для счётчиков (i = 0; i < N; i++)\n"
                                      "- `while` — когда заранее не знаешь, сколько раз\n"
                                      "- `do while` — минимум 1 раз выполнение гарантировано\n\n"
                                      "Попробуй сам!"
                                      ,
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "zerotrust":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="amburanmall")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ueleonoriestdoci")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++: Строки (Strings)*\n\n"
                                      "🔹 *Что такое строка?*\n"
                                      "— Это последовательность символов, например, имя или фраза.\n"
                                      "— В C++ можно использовать массив символов или класс `std::string`.\n\n"
                                      "============================\n"
                                      "🔹 *Строка как массив символов:*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\n```\n"
                                      "🔸 Символ `\\0` автоматически добавляется в конце — это конец строки.\n"
                                      "🔸 Размер массива должен быть больше длины строки.\n\n"
                                      "============================\n"
                                      "🔹 *Строки с `std::string`:*\n"
                                      "```cpp\n#include <string>\n\nstd::string city = \"Baku\";\n```\n"
                                      "— Такой способ удобнее и безопаснее.\n\n"
                                      "============================\n"
                                      "🔹 *Основные операции:*\n"
                                      "```cpp\nstd::string name = \"Tom\";\n\n"
                                      "cout << name << endl;         // Вывод строки\n"
                                      "cout << name.length() << endl; // Длина строки\n"
                                      "name += \" Hardy\";             // Конкатенация (сложение)\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *Ввод строки от пользователя:*\n"
                                      "```cpp\nstd::string userName;\ncout << \"Введите имя: \";\ncin >> userName;\n```\n"
                                      "❗ `cin` читает до первого пробела. Если нужна фраза:\n"
                                      "```cpp\nstd::string fullName;\ngetline(cin, fullName);\n```\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- `std::string` проще и безопаснее, чем массивы `char`\n"
                                      "- Можно легко соединять строки, измерять длину, искать символы\n"
                                      "- Для русских символов может понадобиться настройка кодировки\n\n"
                                      "💡 Строки — это основа работы с текстом, формами, сообщениями!\n"
                                      "Попробуй создать строку и вывести её на экран! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "ueleonoriestdoci":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="zerotrust")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zdravstvuytesergeyvladimirovic")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++: Массивы (Arrays)*\n\n"
                                      "🔹 *Что такое массив?*\n"
                                      "— Это набор элементов **одного типа**, расположенных в памяти подряд.\n"
                                      "— Каждый элемент имеет свой индекс (нумерация с 0).\n\n"
                                      "============================\n"
                                      "🔹 *Пример массива:*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\n```\n"
                                      "— Создаёт массив из 5 элементов типа int.\n\n"
                                      "🔸 Доступ к элементу:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Вывод всех элементов через цикл:*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << numbers[i] << \" \";\n}\n```\n"
                                      "🔸 Вывод: `10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *Ввод значений от пользователя:*\n"
                                      "```cpp\nint a[3];\nfor (int i = 0; i < 3; i++) {\n    cin >> a[i];\n}\n```\n"
                                      "🔸 Сохраняет 3 числа в массив.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Индексы от `0` до `n - 1`\n"
                                      "- Выход за границы массива = ❌ ошибка (UB — undefined behavior)\n"
                                      "- Все элементы одного типа (int, float, char и т.д.)\n\n"
                                      "💡 Массивы — это основа. С ними ты изучишь работу с памятью, сортировку, алгоритмы!\n\n"
                                      "Попробуй создать массив и вывести его элементы!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "amburanmall":
        keyboard = [
                    [InlineKeyboardButton("прошлая глава", callback_data="tvoyotecnaoralkatyue")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C++: Функции*\n\n"
                                      "🔹 *Что такое функция?*\n"
                                      "— Это блок кода, выполняющий определённую задачу.\n"
                                      "— Помогает структурировать программу и избежать повторений.\n\n"
                                      "============================\n"
                                      "🔹 *Простейшая функция:*\n"
                                      "```cpp\nvoid sayHello() {\n    cout << \"Привет, мир!\" << endl;\n}\n\nint main() {\n    sayHello();\n    return 0;\n}\n```\n"
                                      "— Ключевое слово `void` означает, что функция ничего не возвращает.\n"
                                      "— Вызываем функцию просто по имени.\n\n"
                                      "============================\n"
                                      "🔹 *Функция с параметрами:*\n"
                                      "```cpp\nvoid greet(string name) {\n    cout << \"Привет, \" << name << endl;\n}\n\nint main() {\n    greet(\"Алиса\");\n    return 0;\n}\n```\n"
                                      "— Можно передавать данные внутрь функции.\n"
                                      "— Параметры указываются в скобках при объявлении.\n\n"
                                      "============================\n"
                                      "🔹 *Функция с возвращаемым значением:*\n"
                                      "```cpp\nint square(int x) {\n    return x * x;\n}\n\nint main() {\n    int res = square(5);\n    cout << res;\n    return 0;\n}\n```\n"
                                      "— Указываем тип возвращаемого значения (например, `int`).\n"
                                      "— Используем `return` для возврата результата.\n\n"
                                      "============================\n"
                                      "✅ *Почему функции важны?*\n"
                                      "- Код становится компактным и понятным\n"
                                      "- Можно переиспользовать один и тот же код\n"
                                      "- Программа легко делится на части\n\n"
                                      "💡 Попробуй написать свою функцию, которая считает сумму двух чисел и возвращает результат!\n"
                                      "Функции — это фундамент хорошего кода на C++! 🚀",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "tvoyotecnaoralkatyue":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="amburanmall")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ueleonoriestdoci")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++: Строки (Strings)*\n\n"
                                      "🔹 *Что такое строка?*\n"
                                      "— Это последовательность символов, например, имя или фраза.\n"
                                      "— В C++ можно использовать массив символов или класс `std::string`.\n\n"
                                      "============================\n"
                                      "🔹 *Строка как массив символов:*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\n```\n"
                                      "🔸 Символ `\\0` автоматически добавляется в конце — это конец строки.\n"
                                      "🔸 Размер массива должен быть больше длины строки.\n\n"
                                      "============================\n"
                                      "🔹 *Строки с `std::string`:*\n"
                                      "```cpp\n#include <string>\n\nstd::string city = \"Baku\";\n```\n"
                                      "— Такой способ удобнее и безопаснее.\n\n"
                                      "============================\n"
                                      "🔹 *Основные операции:*\n"
                                      "```cpp\nstd::string name = \"Tom\";\n\n"
                                      "cout << name << endl;         // Вывод строки\n"
                                      "cout << name.length() << endl; // Длина строки\n"
                                      "name += \" Hardy\";             // Конкатенация (сложение)\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *Ввод строки от пользователя:*\n"
                                      "```cpp\nstd::string userName;\ncout << \"Введите имя: \";\ncin >> userName;\n```\n"
                                      "❗ `cin` читает до первого пробела. Если нужна фраза:\n"
                                      "```cpp\nstd::string fullName;\ngetline(cin, fullName);\n```\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- `std::string` проще и безопаснее, чем массивы `char`\n"
                                      "- Можно легко соединять строки, измерять длину, искать символы\n"
                                      "- Для русских символов может понадобиться настройка кодировки\n\n"
                                      "💡 Строки — это основа работы с текстом, формами, сообщениями!\n"
                                      "Попробуй создать строку и вывести её на экран! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "jvone":
        keyboard = [[InlineKeyboardButton("⚙ Начать", callback_data="lexustural")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Давайте начнем!\nГлава 1:", reply_markup=reply_markup)
    elif query.data == "lexustural":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="lextural")],
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Установка и старт JavaScript:*\n\n"
                                      "🔹 *Шаг 1: Скачай редактор*\n"
                                      "[Скачать Visual Studio Code](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Шаг 2: Проверь наличие Node.js*\n"
                                      "[Скачать Node.js](https://nodejs.org/)\n"
                                      "— Установи и проверь версию:\n"
                                      "`node --version`\n\n"
                                      "🔹 *Шаг 3: Простой код:*\n"
                                      "Создай файл `main.js` с кодом:\n"
                                      "```js\nconsole.log(\"Hello, world!\");\n```\n"
                                      "Запусти через терминал:\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript — это первый шаг к созданию сайтов, ботов и приложений!*",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "lextural":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="lexturalss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="drruuuororiridididir")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Переменные и типы данных*\n\n"
                                      "🔹 *Что такое переменная?*\n"
                                      "— Это именованное хранилище данных.\n"
                                      "— Объявляется через `let`, `const` или старый способ `var`.\n\n"
                                      "🔹 *Примеры:*\n"
                                      "`let age = 15;`\n`const pi = 3.14;`\n`let name = \"Tom\";`\n`let isOnline = true;`\n\n"
                                      "🔹 *Вывод в консоль:*\n"
                                      "```js\nlet age = 15;\nlet name = \"Tom\";\nconsole.log(\"Имя:\", name);\nconsole.log(\"Возраст:\", age);\n```\n"
                                      "💡 *Совет:* Используй `const` для значений, которые не меняются, и `let` для изменяемых переменных.",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "drruuuororiridididir":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="lextural")],
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Установка и старт JavaScript:*\n\n"
                                      "🔹 *Шаг 1: Скачай редактор*\n"
                                      "[Скачать Visual Studio Code](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Шаг 2: Проверь наличие Node.js*\n"
                                      "[Скачать Node.js](https://nodejs.org/)\n"
                                      "— Установи и проверь версию:\n"
                                      "`node --version`\n\n"
                                      "🔹 *Шаг 3: Простой код:*\n"
                                      "Создай файл `main.js` с кодом:\n"
                                      "```js\nconsole.log(\"Hello, world!\");\n```\n"
                                      "Запусти через терминал:\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript — это первый шаг к созданию сайтов, ботов и приложений!*",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )

    elif query.data == "lexturalss":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="porschetunar")],
                    [InlineKeyboardButton("прошлая глава", callback_data="celuymenyanazlojidfienewjf")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *JavaScript: Условия и сравнения*\n\n"
            "🔹 *Что такое условие?*\n"
            "— Это проверка, при которой код внутри блока выполняется, если результат выражения — `true`.\n"
            "— В JavaScript для этого используется конструкция `if`.\n\n"
            "🔹 *Пример:*\n"
            "```js\nlet age = 18;\nif (age >= 18) {\n    console.log(\"Доступ разрешён\");\n} else {\n    console.log(\"Доступ запрещён\");\n}\n```\n\n"
            "🔹 *Операторы сравнения:*\n"
            "`==` — сравнение по значению (может преобразовывать типы)\n"
            "`===` — строгое сравнение (учитывает и тип, и значение)\n"
            "`!=` — не равно (по значению)\n"
            "`!==` — строгое не равно (по типу и значению)\n"
            "`>` — больше\n"
            "`<` — меньше\n"
            "`>=` — больше или равно\n"
            "`<=` — меньше или равно\n\n"
            "💡 *Важно:* Лучше использовать `===` и `!==` для избежания неожиданных ошибок из-за преобразования типов.",
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "celuymenyanazlojidfienewjf":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="lexturalss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="drruuuororiridididir")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Переменные и типы данных*\n\n"
                                      "🔹 *Что такое переменная?*\n"
                                      "— Это именованное хранилище данных.\n"
                                      "— Объявляется через `let`, `const` или старый способ `var`.\n\n"
                                      "🔹 *Примеры:*\n"
                                      "`let age = 15;`\n`const pi = 3.14;`\n`let name = \"Tom\";`\n`let isOnline = true;`\n\n"
                                      "🔹 *Вывод в консоль:*\n"
                                      "```js\nlet age = 15;\nlet name = \"Tom\";\nconsole.log(\"Имя:\", name);\nconsole.log(\"Возраст:\", age);\n```\n"
                                      "💡 *Совет:* Используй `const` для значений, которые не меняются, и `let` для изменяемых переменных.",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "porschetunar":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="ferraritunar")],
                    [InlineKeyboardButton("прошлая глава", callback_data="vprincipeyamogutebepomocye")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Логические операторы*\n\n"
                                      "🔹 *Что это?*\n"
                                      "— Логические операторы помогают объединять условия.\n"
                                      "— С ними можно проверять сразу несколько условий одновременно.\n\n"
                                      "🔹 *Виды логических операторов:*\n"
                                      "`&&` — И (оба условия должны быть истинны)\n"
                                      "`||` — ИЛИ (достаточно одного истинного условия)\n"
                                      "`!` — НЕ (отрицание, меняет значение на противоположное)\n\n"
                                      "🔹 *Примеры:*\n"
                                      "```js\nlet age = 20;\nlet hasPassport = true;\n\nif (age >= 18 && hasPassport) {\n    console.log(\"Доступ разрешён\");\n} else {\n    console.log(\"Доступ запрещён\");\n}\n```\n\n"
                                      "```js\nlet isOnline = false;\nif (!isOnline) {\n    console.log(\"Пользователь оффлайн\");\n}\n```\n\n"
                                      "💡 *Важно:* Сначала проверяется логика внутри скобок, затем применяются операторы.",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "vprincipeyamogutebepomocye":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="porschetunar")],
                    [InlineKeyboardButton("прошлая глава", callback_data="celuymenyanazlojidfienewjf")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *JavaScript: Условия и сравнения*\n\n"
            "🔹 *Что такое условие?*\n"
            "— Это проверка, при которой код внутри блока выполняется, если результат выражения — `true`.\n"
            "— В JavaScript для этого используется конструкция `if`.\n\n"
            "🔹 *Пример:*\n"
            "```js\nlet age = 18;\nif (age >= 18) {\n    console.log(\"Доступ разрешён\");\n} else {\n    console.log(\"Доступ запрещён\");\n}\n```\n\n"
            "🔹 *Операторы сравнения:*\n"
            "`==` — сравнение по значению (может преобразовывать типы)\n"
            "`===` — строгое сравнение (учитывает и тип, и значение)\n"
            "`!=` — не равно (по значению)\n"
            "`!==` — строгое не равно (по типу и значению)\n"
            "`>` — больше\n"
            "`<` — меньше\n"
            "`>=` — больше или равно\n"
            "`<=` — меньше или равно\n\n"
            "💡 *Важно:* Лучше использовать `===` и `!==` для избежания неожиданных ошибок из-за преобразования типов.",
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "ferraritunar":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="dodgevaper")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zughtjfrhegjhfeuewfwefhwfhu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript: Циклы*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Это способ повторять блок кода несколько раз.\n"
                                      "— Используется для работы с массивами, повторяющихся задач и автоматизации.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл for*\n"
                                      "```js\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n```\n"
                                      "— Выводит числа от 0 до 4.\n"
                                      "`i++` — увеличивает счётчик на 1 каждый раз.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл while*\n"
                                      "```js\nlet x = 0;\nwhile (x < 3) {\n    console.log(x);\n    x++;\n}\n```\n"
                                      "— Пока `x < 3`, код выполняется.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл do...while*\n"
                                      "```js\nlet y = 0;\ndo {\n    console.log(y);\n    y++;\n} while (y < 2);\n```\n"
                                      "— Код выполнится хотя бы один раз, даже если условие сразу false.\n\n"
                                      "============================\n"
                                      "🔹 *Пример: перебор массива*\n"
                                      "```js\nlet fruits = [\"🍎\", \"🍌\", \"🍇\"];\nfor (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}\n```\n"
                                      "— Перебор всех элементов массива.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Легко создать бесконечный цикл (не забывай изменять счётчик!)\n"
                                      "- Можно использовать `break` для выхода из цикла\n"
                                      "- `continue` — пропускает текущую итерацию\n\n"
                                      "💡 Циклы — ключевой инструмент при работе со структурами данных и автоматизации задач!\n"
                                      "Попробуй написать цикл, который выводит числа от 10 до 1 в обратном порядке! 🚀",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "zughtjfrhegjhfeuewfwefhwfhu":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="ferraritunar")],
                    [InlineKeyboardButton("прошлая глава", callback_data="vprincipeyamogutebepomocye")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Логические операторы*\n\n"
                                      "🔹 *Что это?*\n"
                                      "— Логические операторы помогают объединять условия.\n"
                                      "— С ними можно проверять сразу несколько условий одновременно.\n\n"
                                      "🔹 *Виды логических операторов:*\n"
                                      "`&&` — И (оба условия должны быть истинны)\n"
                                      "`||` — ИЛИ (достаточно одного истинного условия)\n"
                                      "`!` — НЕ (отрицание, меняет значение на противоположное)\n\n"
                                      "🔹 *Примеры:*\n"
                                      "```js\nlet age = 20;\nlet hasPassport = true;\n\nif (age >= 18 && hasPassport) {\n    console.log(\"Доступ разрешён\");\n} else {\n    console.log(\"Доступ запрещён\");\n}\n```\n\n"
                                      "```js\nlet isOnline = false;\nif (!isOnline) {\n    console.log(\"Пользователь оффлайн\");\n}\n```\n\n"
                                      "💡 *Важно:* Сначала проверяется логика внутри скобок, затем применяются операторы.",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )

    elif query.data == "dodgevaper":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="xzero")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ppsdjoscdjfvojfsnojnsjosonj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Функции подробно*\n\n"
                                      "🔹 *Что такое функция?*\n"
                                      "— Это именованный блок кода, который выполняет определённую задачу.\n"
                                      "— Функцию можно вызывать сколько угодно раз, не дублируя код.\n"
                                      "— Это основа структурированного программирования.\n\n"
                                      "🔹 *Зачем нужны функции:*\n"
                                      "✔ Чтобы не повторять одинаковый код\n"
                                      "✔ Чтобы разделять программу на логические части\n"
                                      "✔ Чтобы принимать данные (аргументы) и возвращать результат\n\n"
                                      "🔹 *Пример простой функции:*\n"
                                      "```js\nfunction sayHello() {\n    console.log(\"Привет!\");\n}\n\nsayHello(); // вызов функции\n```\n"
                                      "💡 Функция `sayHello` выводит \"Привет!\" каждый раз, когда её вызывают.\n\n"
                                      "🔹 *Функция с параметрами:*\n"
                                      "```js\nfunction greet(name) {\n    console.log(\"Привет, \" + name);\n}\n\ngreet(\"Том\");\ngreet(\"Анна\");\n```\n"
                                      "💡 Параметр `name` позволяет передавать в функцию разные значения.\n\n"
                                      "🔹 *Функция, которая что-то возвращает:*\n"
                                      "```js\nfunction square(number) {\n    return number * number;\n}\n\nconsole.log(square(4)); // 16\n```\n"
                                      "💡 `return` возвращает результат, который можно сохранить или вывести.\n\n"
                                      "🔹 *Важно:*\n"
                                      "✔ Функцию можно вызвать в любом месте после её объявления\n"
                                      "✔ Код внутри функции выполняется только при вызове\n"
                                      "✔ Можно передавать сколько угодно аргументов\n\n"
                                      "Функции делают код чище, проще и гибче.",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "ppsdjoscdjfvojfsnojnsjosonj":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="dodgevaper")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zughtjfrhegjhfeuewfwefhwfhu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript: Циклы*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Это способ повторять блок кода несколько раз.\n"
                                      "— Используется для работы с массивами, повторяющихся задач и автоматизации.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл for*\n"
                                      "```js\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n```\n"
                                      "— Выводит числа от 0 до 4.\n"
                                      "`i++` — увеличивает счётчик на 1 каждый раз.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл while*\n"
                                      "```js\nlet x = 0;\nwhile (x < 3) {\n    console.log(x);\n    x++;\n}\n```\n"
                                      "— Пока `x < 3`, код выполняется.\n\n"
                                      "============================\n"
                                      "🔹 *Цикл do...while*\n"
                                      "```js\nlet y = 0;\ndo {\n    console.log(y);\n    y++;\n} while (y < 2);\n```\n"
                                      "— Код выполнится хотя бы один раз, даже если условие сразу false.\n\n"
                                      "============================\n"
                                      "🔹 *Пример: перебор массива*\n"
                                      "```js\nlet fruits = [\"🍎\", \"🍌\", \"🍇\"];\nfor (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}\n```\n"
                                      "— Перебор всех элементов массива.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Легко создать бесконечный цикл (не забывай изменять счётчик!)\n"
                                      "- Можно использовать `break` для выхода из цикла\n"
                                      "- `continue` — пропускает текущую итерацию\n\n"
                                      "💡 Циклы — ключевой инструмент при работе со структурами данных и автоматизации задач!\n"
                                      "Попробуй написать цикл, который выводит числа от 10 до 1 в обратном порядке! 🚀",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "xzero":
        keyboard = [[InlineKeyboardButton("прошлая глава", callback_data="debroutroutroute")],
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *JavaScript: Объекты (Objects)*\n\n"
                                      "🔹 *Что такое объект?*\n"
                                      "— Это структура для хранения связанных данных и функций.\n"
                                      "— Состоит из пар \"ключ: значение\".\n\n"
                                      "============================\n"
                                      "🔹 *Пример простого объекта:*\n"
                                      "```js\n"
                                      "let person = {\n"
                                      "  name: \"Tom\",\n"
                                      "  age: 25,\n"
                                      "  isStudent: true\n"
                                      "};\n"
                                      "```\n"
                                      "🔸 Доступ к данным:\n"
                                      "`person.name` → \"Tom\"\n"
                                      "`person[\"age\"]` → 25\n\n"
                                      "============================\n"
                                      "🔹 *Объект с методом:*\n"
                                      "```js\n"
                                      "let car = {\n"
                                      "  brand: \"Toyota\",\n"
                                      "  start: function() {\n"
                                      "    console.log(\"Двигатель запущен\");\n"
                                      "  }\n"
                                      "};\n\n"
                                      "car.start();\n"
                                      "```\n"
                                      "============================\n"
                                      "✅ *Зачем нужны объекты?*\n"
                                      "- Хранят сложные данные в одной переменной\n"
                                      "- Позволяют моделировать реальные объекты\n"
                                      "- Используются повсюду: DOM, серверные запросы, игры\n\n"
                                      "💡 Попробуй создать объект \"phone\" с полями \"model\", \"year\" и методом \"call()\"!",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "debroutroutroute":
        keyboard = [[InlineKeyboardButton("следующая глава➡️", callback_data="xzero")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ppsdjoscdjfvojfsnojnsjosonj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Функции подробно*\n\n"
                                      "🔹 *Что такое функция?*\n"
                                      "— Это именованный блок кода, который выполняет определённую задачу.\n"
                                      "— Функцию можно вызывать сколько угодно раз, не дублируя код.\n"
                                      "— Это основа структурированного программирования.\n\n"
                                      "🔹 *Зачем нужны функции:*\n"
                                      "✔ Чтобы не повторять одинаковый код\n"
                                      "✔ Чтобы разделять программу на логические части\n"
                                      "✔ Чтобы принимать данные (аргументы) и возвращать результат\n\n"
                                      "🔹 *Пример простой функции:*\n"
                                      "```js\nfunction sayHello() {\n    console.log(\"Привет!\");\n}\n\nsayHello(); // вызов функции\n```\n"
                                      "💡 Функция `sayHello` выводит \"Привет!\" каждый раз, когда её вызывают.\n\n"
                                      "🔹 *Функция с параметрами:*\n"
                                      "```js\nfunction greet(name) {\n    console.log(\"Привет, \" + name);\n}\n\ngreet(\"Том\");\ngreet(\"Анна\");\n```\n"
                                      "💡 Параметр `name` позволяет передавать в функцию разные значения.\n\n"
                                      "🔹 *Функция, которая что-то возвращает:*\n"
                                      "```js\nfunction square(number) {\n    return number * number;\n}\n\nconsole.log(square(4)); // 16\n```\n"
                                      "💡 `return` возвращает результат, который можно сохранить или вывести.\n\n"
                                      "🔹 *Важно:*\n"
                                      "✔ Функцию можно вызвать в любом месте после её объявления\n"
                                      "✔ Код внутри функции выполняется только при вызове\n"
                                      "✔ Можно передавать сколько угодно аргументов\n\n"
                                      "Функции делают код чище, проще и гибче.",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "toomycash":
        keyboard = [[InlineKeyboardButton("☕ Начните изучать Java", callback_data="officess")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Java", reply_markup=reply_markup)
    elif query.data == "officess":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirens")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java: Установка и первый проект*\n\n"
                                      "🔹 *Шаг 1: Скачай и установи JDK*\n"
                                      "[🔗 Официальная страница загрузки](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— Выбери Java SE Development Kit (JDK) под свою операционную систему\n"
                                      "— Во время установки отметь галочку `Add JAVA to PATH` (если доступна)\n\n"
                                      "🔹 *Шаг 2: Проверь установку*\n"
                                      "Открой терминал или командную строку и введи:\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "Если появились версии — установка прошла успешно!\n\n"
                                      "🔹 *Шаг 3: Установи среду разработки (IDE)*\n"
                                      "✅ [IntelliJ IDEA Community (рекомендуется)](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + расширение Java](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Шаг 4: Напиши свой первый Java-код!*\n"
                                      "Создай файл с именем `Main.java` и введи:\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "Затем запусти его в терминале:\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ Ожидаемый вывод: `Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *Ты готов начать изучать Java!*\n"
                                      "Дальше: переменные, условия, циклы, функции и объектно-ориентированное программирование!\n\n"
                                      "👇 Нажми кнопку ниже, чтобы перейти к следующему уроку!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "sirens":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="styles")],
                    [InlineKeyboardButton("прошлая глава", callback_data="pozitivnoyevliyaniyeigr")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Переменные и типы данных*\n\n"
                                      "🔹 *Что такое переменная?*\n"
                                      "— Переменная — это имя, которое используется для хранения данных.\n"
                                      "— Каждая переменная должна быть объявлена с конкретным типом данных.\n\n"
                                      "🔹 *Основные типы данных:*\n"
                                      "- `int`: целые числа, например `42`\n"
                                      "- `double`: числа с плавающей точкой, например `3.14`\n"
                                      "- `char`: одиночный символ, например `'A'`\n"
                                      "- `boolean`: логические значения — `true` или `false`\n"
                                      "- `String`: текстовая строка, например `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *Объявление и использование переменных:*\n"
                                      "```java\n"
                                      "int age = 18;\n"
                                      "double pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "boolean isStudent = true;\n"
                                      "String name = \"Tom\";\n"
                                      "```\n\n"
                                      "🔸 Используй `System.out.println()` для вывода значений:\n"
                                      "```java\n"
                                      "System.out.println(name);\n"
                                      "System.out.println(age);\n"
                                      "```\n"
                                      "🔸 Вывод:\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *Полезные советы:*\n"
                                      "- Java — строго типизированный язык, каждый параметр должен иметь тип\n"
                                      "- Java чувствителен к регистру: `Name` ≠ `name`\n"
                                      "- Используй понятные имена: `int n = 5;` ❌, `int score = 5;` ✅\n\n"
                                      "💡 Попробуй сам объявить переменные и вывести их через `System.out.println()`!",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "pozitivnoyevliyaniyeigr":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirens")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java: Установка и первый проект*\n\n"
                                      "🔹 *Шаг 1: Скачай и установи JDK*\n"
                                      "[🔗 Официальная страница загрузки](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— Выбери Java SE Development Kit (JDK) под свою операционную систему\n"
                                      "— Во время установки отметь галочку `Add JAVA to PATH` (если доступна)\n\n"
                                      "🔹 *Шаг 2: Проверь установку*\n"
                                      "Открой терминал или командную строку и введи:\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "Если появились версии — установка прошла успешно!\n\n"
                                      "🔹 *Шаг 3: Установи среду разработки (IDE)*\n"
                                      "✅ [IntelliJ IDEA Community (рекомендуется)](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + расширение Java](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Шаг 4: Напиши свой первый Java-код!*\n"
                                      "Создай файл с именем `Main.java` и введи:\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "Затем запусти его в терминале:\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ Ожидаемый вывод: `Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *Ты готов начать изучать Java!*\n"
                                      "Дальше: переменные, условия, циклы, функции и объектно-ориентированное программирование!\n\n"
                                      "👇 Нажми кнопку ниже, чтобы перейти к следующему уроку!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "styles":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="fors")],
                    [InlineKeyboardButton("прошлая глава", callback_data="nikadsidjiofsale")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📚 *Java: Условные операторы (if, else, else if)*\n\n"
            "🔹 *Что такое условный оператор?*\n"
            "— Это конструкция, которая позволяет выполнять разный код в зависимости от условия.\n\n"
            "============================\n"
            "🔹 *Пример кода:*\n"
            "```java\n"
            "if (age >= 18) {\n"
            "    System.out.println(\"Вы совершеннолетний\");\n"
            "} else if (age >= 14) {\n"
            "    System.out.println(\"Вы подросток\");\n"
            "} else {\n"
            "    System.out.println(\"Вы ребенок\");\n"
            "}\n"
            "```\n\n"
            "🔹 *Операторы сравнения:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Логические операторы:* `&&` (и), `||` (или), `!` (не)\n\n"
            "✅ *Попробуй это:*\n"
            "Напиши программу, которая выводит сообщение в зависимости от возраста человека!",
            parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "nikadsidjiofsale":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="styles")],
                    [InlineKeyboardButton("прошлая глава", callback_data="pozitivnoyevliyaniyeigr")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Переменные и типы данных*\n\n"
                                      "🔹 *Что такое переменная?*\n"
                                      "— Переменная — это имя, которое используется для хранения данных.\n"
                                      "— Каждая переменная должна быть объявлена с конкретным типом данных.\n\n"
                                      "🔹 *Основные типы данных:*\n"
                                      "- `int`: целые числа, например `42`\n"
                                      "- `double`: числа с плавающей точкой, например `3.14`\n"
                                      "- `char`: одиночный символ, например `'A'`\n"
                                      "- `boolean`: логические значения — `true` или `false`\n"
                                      "- `String`: текстовая строка, например `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *Объявление и использование переменных:*\n"
                                      "```java\n"
                                      "int age = 18;\n"
                                      "double pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "boolean isStudent = true;\n"
                                      "String name = \"Tom\";\n"
                                      "```\n\n"
                                      "🔸 Используй `System.out.println()` для вывода значений:\n"
                                      "```java\n"
                                      "System.out.println(name);\n"
                                      "System.out.println(age);\n"
                                      "```\n"
                                      "🔸 Вывод:\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *Полезные советы:*\n"
                                      "- Java — строго типизированный язык, каждый параметр должен иметь тип\n"
                                      "- Java чувствителен к регистру: `Name` ≠ `name`\n"
                                      "- Используй понятные имена: `int n = 5;` ❌, `int score = 5;` ✅\n\n"
                                      "💡 Попробуй сам объявить переменные и вывести их через `System.out.println()`!",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "fors":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="mens")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ghyuhbrdyimmvtygnmybnmutycvbnhhubtrftc")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: Циклы*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Цикл позволяет выполнить один и тот же блок кода несколько раз.\n"
                                      "— Полезен для повторяющихся действий, автоматизации и обработки данных.\n\n"
                                      "============================\n"
                                      "🔹 *Пример цикла for:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— Выводит числа от 0 до 4.\n\n"
                                      "============================\n"
                                      "🔹 *Пример цикла while:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n"
                                      "— Повторяет действия, пока условие истинно.\n\n"
                                      "============================\n"
                                      "🔹 *Пример цикла do...while:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— Код выполняется хотя бы один раз, даже если условие ложно.\n\n"
                                      "============================\n"
                                      "✅ *Полезно знать:*\n"
                                      "- Используйте `break`, чтобы досрочно выйти из цикла\n"
                                      "- Используйте `continue`, чтобы перейти к следующей итерации\n"
                                      "- Избегайте бесконечных циклов, корректно обновляя условие\n\n"
                                      "💡 Попробуйте написать цикл, который считает от 10 до 1 в обратном порядке!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "ghyuhbrdyimmvtygnmybnmutycvbnhhubtrftc":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="fors")],
                    [InlineKeyboardButton("прошлая глава", callback_data="nikadsidjiofsale")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📚 *Java: Условные операторы (if, else, else if)*\n\n"
            "🔹 *Что такое условный оператор?*\n"
            "— Это конструкция, которая позволяет выполнять разный код в зависимости от условия.\n\n"
            "============================\n"
            "🔹 *Пример кода:*\n"
            "```java\n"
            "if (age >= 18) {\n"
            "    System.out.println(\"Вы совершеннолетний\");\n"
            "} else if (age >= 14) {\n"
            "    System.out.println(\"Вы подросток\");\n"
            "} else {\n"
            "    System.out.println(\"Вы ребенок\");\n"
            "}\n"
            "```\n\n"
            "🔹 *Операторы сравнения:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Логические операторы:* `&&` (и), `||` (или), `!` (не)\n\n"
            "✅ *Попробуй это:*\n"
            "Напиши программу, которая выводит сообщение в зависимости от возраста человека!",
            parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "mens":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="brandss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zeoohyfrbn")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Массивы*\n\n"
                                      "🔹 *Что такое массив?*\n"
                                      "— Массив — это коллекция элементов одного типа, хранящихся последовательно в памяти.\n"
                                      "— Каждый элемент имеет индекс (начиная с 0).\n\n"
                                      "============================\n"
                                      "🔹 *Создание массива целых чисел:*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— Создаёт массив из 5 целых чисел.\n\n"
                                      "🔸 Доступ к элементам:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Вывод всех элементов с помощью цикла for:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— `numbers.length` возвращает размер массива.\n\n"
                                      "============================\n"
                                      "🔹 *Ввод значений от пользователя:*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— Сохраняет 3 числа, введённые пользователем.\n\n"
                                      "============================\n"
                                      "✅ *Полезные напоминания:*\n"
                                      "- Индексы идут от `0` до `n - 1`\n"
                                      "- Размер массива фиксирован\n"
                                      "- Выход за границы массива вызовет ошибку (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 Массивы — основа структур данных, сортировок и алгоритмов!\n"
                                      "Попробуй создать свой массив и вывести его элементы!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "zeoohyfrbn":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="mens")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ghyuhbrdyimmvtygnmybnmutycvbnhhubtrftc")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: Циклы*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Цикл позволяет выполнить один и тот же блок кода несколько раз.\n"
                                      "— Полезен для повторяющихся действий, автоматизации и обработки данных.\n\n"
                                      "============================\n"
                                      "🔹 *Пример цикла for:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— Выводит числа от 0 до 4.\n\n"
                                      "============================\n"
                                      "🔹 *Пример цикла while:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n"
                                      "— Повторяет действия, пока условие истинно.\n\n"
                                      "============================\n"
                                      "🔹 *Пример цикла do...while:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— Код выполняется хотя бы один раз, даже если условие ложно.\n\n"
                                      "============================\n"
                                      "✅ *Полезно знать:*\n"
                                      "- Используйте `break`, чтобы досрочно выйти из цикла\n"
                                      "- Используйте `continue`, чтобы перейти к следующей итерации\n"
                                      "- Избегайте бесконечных циклов, корректно обновляя условие\n\n"
                                      "💡 Попробуйте написать цикл, который считает от 10 до 1 в обратном порядке!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "brandss":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="itss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="porbugyy")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java: Методы (Функции)*\n\n"
                                      "🔹 *Что такое метод?*\n"
                                      "— Метод — это блок кода, который выполняет конкретную задачу.\n"
                                      "— Его можно вызывать много раз без повторного написания кода.\n\n"
                                      "============================\n"
                                      "🔹 *Зачем использовать методы?*\n"
                                      "✔️ Избегать дублирования кода\n"
                                      "✔️ Делать программу понятнее и проще для поддержки\n"
                                      "✔️ Принимать параметры и возвращать результат\n\n"
                                      "============================\n"
                                      "🔹 *Простой пример:*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"Привет!\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // вызов метода\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— Метод `sayHello` выводит \"Привет!\".\n\n"
                                      "============================\n"
                                      "🔹 *Метод с параметрами:*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"Привет, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"Алиса\");\n"
                                      "```\n"
                                      "— Параметры делают метод универсальнее.\n\n"
                                      "============================\n"
                                      "🔹 *Метод с возвращаемым значением:*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— `return` возвращает результат метода.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Все методы должны находиться внутри класса\n"
                                      "- `main()` — это точка входа в программу\n"
                                      "- `void` означает, что метод ничего не возвращает\n\n"
                                      "💡 Попробуй написать свой метод, который выводит твоё имя или складывает два числа! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "porbugyy":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="brandss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="zeoohyfrbn")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Массивы*\n\n"
                                      "🔹 *Что такое массив?*\n"
                                      "— Массив — это коллекция элементов одного типа, хранящихся последовательно в памяти.\n"
                                      "— Каждый элемент имеет индекс (начиная с 0).\n\n"
                                      "============================\n"
                                      "🔹 *Создание массива целых чисел:*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— Создаёт массив из 5 целых чисел.\n\n"
                                      "🔸 Доступ к элементам:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Вывод всех элементов с помощью цикла for:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— `numbers.length` возвращает размер массива.\n\n"
                                      "============================\n"
                                      "🔹 *Ввод значений от пользователя:*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— Сохраняет 3 числа, введённые пользователем.\n\n"
                                      "============================\n"
                                      "✅ *Полезные напоминания:*\n"
                                      "- Индексы идут от `0` до `n - 1`\n"
                                      "- Размер массива фиксирован\n"
                                      "- Выход за границы массива вызовет ошибку (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 Массивы — основа структур данных, сортировок и алгоритмов!\n"
                                      "Попробуй создать свой массив и вывести его элементы!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "itss":
        keyboard = [
                    [InlineKeyboardButton("прошлая глава", callback_data="sitiporosaaututjj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🏗️ *Java: Классы и объекты*\n\n"
                                      "🔹 *Что такое класс?*\n"
                                      "— Класс — это шаблон (blueprint) для создания объектов.\n"
                                      "— Он определяет свойства (данные) и поведение (методы) объектов.\n\n"
                                      "🔹 *Что такое объект?*\n"
                                      "— Объект — это экземпляр, созданный на основе класса. Это реальный участник программы.\n\n"
                                      "============================\n"
                                      "🔹 *Простой пример:*\n"
                                      "```java\n"
                                      "public class Dog {\n"
                                      "    String name;\n"
                                      "    int age;\n\n"
                                      "    void bark() {\n"
                                      "        System.out.println(name + \": Гав-гав!\");\n"
                                      "    }\n"
                                      "}\n\n"
                                      "public class Main {\n"
                                      "    public static void main(String[] args) {\n"
                                      "        Dog myDog = new Dog();\n"
                                      "        myDog.name = \"Шарик\";\n"
                                      "        myDog.age = 3;\n"
                                      "        myDog.bark();\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— Класс `Dog` имеет два свойства и один метод.\n"
                                      "— `myDog` — это объект класса `Dog`, который может вызывать методы и изменять данные.\n\n"
                                      "============================\n"
                                      "🔹 *Важные понятия:*\n"
                                      "- Названия классов пишутся с заглавной буквы: `Person`, `Car`, `Animal` и т.д.\n"
                                      "- `new` используется для создания объектов\n"
                                      "- В методах можно обращаться к свойствам объекта\n\n"
                                      "✅ *Классы и объекты — это основа Java*\n"
                                      "— Почти все Java-программы построены вокруг объектов!\n\n"
                                      "💡 Далее мы изучим конструкторы, инкапсуляцию, наследование и полиморфизм! 🚀",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "sitiporosaaututjj":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="itss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="porbugyy")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java: Методы (Функции)*\n\n"
                                      "🔹 *Что такое метод?*\n"
                                      "— Метод — это блок кода, который выполняет конкретную задачу.\n"
                                      "— Его можно вызывать много раз без повторного написания кода.\n\n"
                                      "============================\n"
                                      "🔹 *Зачем использовать методы?*\n"
                                      "✔️ Избегать дублирования кода\n"
                                      "✔️ Делать программу понятнее и проще для поддержки\n"
                                      "✔️ Принимать параметры и возвращать результат\n\n"
                                      "============================\n"
                                      "🔹 *Простой пример:*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"Привет!\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // вызов метода\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— Метод `sayHello` выводит \"Привет!\".\n\n"
                                      "============================\n"
                                      "🔹 *Метод с параметрами:*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"Привет, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"Алиса\");\n"
                                      "```\n"
                                      "— Параметры делают метод универсальнее.\n\n"
                                      "============================\n"
                                      "🔹 *Метод с возвращаемым значением:*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— `return` возвращает результат метода.\n\n"
                                      "============================\n"
                                      "✅ *Важно помнить:*\n"
                                      "- Все методы должны находиться внутри класса\n"
                                      "- `main()` — это точка входа в программу\n"
                                      "- `void` означает, что метод ничего не возвращает\n\n"
                                      "💡 Попробуй написать свой метод, который выводит твоё имя или складывает два числа! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "huggywuggy":
        keyboard = [[InlineKeyboardButton("«Начнём!\n»«*Глава 1:*", callback_data="yveskarl")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("<<>>", reply_markup=reply_markup)
    elif query.data == "yveskarl":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="legs")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *Установка C и настройка в CLion IDE*\n\n"
                                      "🔹 *Шаг 1: Скачайте компилятор MinGW*\n"
                                      "[Скачать MinGW](https://sourceforge.net/projects/mingw/) — установите gcc и добавьте папку `bin` в системную переменную PATH\n\n"
                                      "🔹 *Шаг 2: Скачайте CLion IDE*\n"
                                      "[Скачать CLion](https://www.jetbrains.com/clion/download/) — установите Community или Trial версию\n\n"
                                      "🔹 *Шаг 3: Проверьте установку*\n"
                                      "Откройте терминал и выполните:\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *Шаг 4: Напишите простой C-программу*\n"
                                      "Создайте файл `main.c` с кодом:\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Привет, мир!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Шаг 5: Скомпилируйте и запустите программу*\n"
                                      "В терминале выполните:\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "Запустите программу:\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *Проверьте результат:*\n"
                                      "Вы должны увидеть:\n"
                                      "```\nПривет, мир!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "legs":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="armsss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="igogoogogogogogog")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Переменные и типы данных в C*\n\n"
                                      "🔹 *Что такое переменная?*\n"
                                      "— Имя для хранения данных в памяти.\n"
                                      "— Каждая переменная имеет тип, который определяет, какие данные она хранит.\n\n"
                                      "🔹 *Основные типы данных:*\n"
                                      "- `int` — целые числа, например: `42`\n"
                                      "- `float` — числа с плавающей точкой, например: `3.14`\n"
                                      "- `char` — один символ, например: `'A'`\n"
                                      "- `double` — более точные числа с плавающей точкой\n\n"
                                      "============================\n"
                                      "🔹 *Объявление переменных:*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *Вывод на экран:*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"Возраст: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Попробуйте сами:* объявите несколько переменных и выведите их значения!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "igogoogogogogogog":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="legs")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *Установка C и настройка в CLion IDE*\n\n"
                                      "🔹 *Шаг 1: Скачайте компилятор MinGW*\n"
                                      "[Скачать MinGW](https://sourceforge.net/projects/mingw/) — установите gcc и добавьте папку `bin` в системную переменную PATH\n\n"
                                      "🔹 *Шаг 2: Скачайте CLion IDE*\n"
                                      "[Скачать CLion](https://www.jetbrains.com/clion/download/) — установите Community или Trial версию\n\n"
                                      "🔹 *Шаг 3: Проверьте установку*\n"
                                      "Откройте терминал и выполните:\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *Шаг 4: Напишите простой C-программу*\n"
                                      "Создайте файл `main.c` с кодом:\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Привет, мир!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Шаг 5: Скомпилируйте и запустите программу*\n"
                                      "В терминале выполните:\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "Запустите программу:\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *Проверьте результат:*\n"
                                      "Вы должны увидеть:\n"
                                      "```\nПривет, мир!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "armsss":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirenseacreature")],
                    [InlineKeyboardButton("прошлая глава", callback_data="tushdlyauveliceniyaobyema")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Операторы и выражения в C*\n\n"
                                      "🔹 *Что такое оператор?*\n"
                                      "— Символ или комбинация символов, которые выполняют операции над данными.\n\n"
                                      "🔹 *Типы операторов:*\n"
                                      "- Арифметические: `+`, `-`, `*`, `/`, `%`\n"
                                      "- Присваивания: `=`, `+=`, `-=`, `*=` и т.д.\n"
                                      "- Сравнения: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                                      "- Логические: `&&`, `||`, `!`\n\n"
                                      "============================\n"
                                      "🔹 *Пример арифметических операций:*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int sum = a + b;       // 13\n"
                                      "int diff = a - b;      // 7\n"
                                      "int product = a * b;   // 30\n"
                                      "int quotient = a / b;  // 3\n"
                                      "int remainder = a % b; // 1\n"
                                      "```\n\n"
                                      "🔹 *Пример сравнения и логики:*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x меньше y и y положительное\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Задание:* попробуйте написать выражения с разными операторами и вывести результаты!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "tushdlyauveliceniyaobyema":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="armsss")],
                    [InlineKeyboardButton("прошлая глава", callback_data="igogoogogogogogog")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Переменные и типы данных в C*\n\n"
                                      "🔹 *Что такое переменная?*\n"
                                      "— Имя для хранения данных в памяти.\n"
                                      "— Каждая переменная имеет тип, который определяет, какие данные она хранит.\n\n"
                                      "🔹 *Основные типы данных:*\n"
                                      "- `int` — целые числа, например: `42`\n"
                                      "- `float` — числа с плавающей точкой, например: `3.14`\n"
                                      "- `char` — один символ, например: `'A'`\n"
                                      "- `double` — более точные числа с плавающей точкой\n\n"
                                      "============================\n"
                                      "🔹 *Объявление переменных:*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *Вывод на экран:*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"Возраст: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Попробуйте сами:* объявите несколько переменных и выведите их значения!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "sirenseacreature":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirenseacreatur")],
                    [InlineKeyboardButton("прошлая глава", callback_data="nozamoyeobidniye")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Условные операторы в C: if, else if, else*\n\n"
                                      "🔹 *Что такое условный оператор?*\n"
                                      "— Позволяет выполнять разные части кода в зависимости от условий.\n\n"
                                      "🔹 *Синтаксис if:*\n"
                                      "```c\n"
                                      "if (условие) {\n"
                                      "    // код, если условие истинно\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Использование else if и else:*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"Положительное число\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"Ноль\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"Отрицательное число\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Логические операторы для условий:*\n"
                                      "- `&&` — И (AND)\n"
                                      "- `||` — ИЛИ (OR)\n"
                                      "- `!`  — НЕ (NOT)\n\n"
                                      "✅ *Задание:* напишите программу, которая проверяет число и выводит сообщение о его знаке!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "nozamoyeobidniye":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirenseacreature")],
                    [InlineKeyboardButton("прошлая глава", callback_data="tushdlyauveliceniyaobyema")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Операторы и выражения в C*\n\n"
                                      "🔹 *Что такое оператор?*\n"
                                      "— Символ или комбинация символов, которые выполняют операции над данными.\n\n"
                                      "🔹 *Типы операторов:*\n"
                                      "- Арифметические: `+`, `-`, `*`, `/`, `%`\n"
                                      "- Присваивания: `=`, `+=`, `-=`, `*=` и т.д.\n"
                                      "- Сравнения: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                                      "- Логические: `&&`, `||`, `!`\n\n"
                                      "============================\n"
                                      "🔹 *Пример арифметических операций:*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int sum = a + b;       // 13\n"
                                      "int diff = a - b;      // 7\n"
                                      "int product = a * b;   // 30\n"
                                      "int quotient = a / b;  // 3\n"
                                      "int remainder = a % b; // 1\n"
                                      "```\n\n"
                                      "🔹 *Пример сравнения и логики:*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x меньше y и y положительное\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Задание:* попробуйте написать выражения с разными операторами и вывести результаты!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "sirenseacreatur":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirenseacreatu")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ututututututrejfjwoejfpjqwp")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Циклы в C: for, while, do-while*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Позволяет повторять блок кода несколько раз.\n\n"
                                      "🔹 *Цикл for:*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"Итерация %d\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Цикл while:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"Итерация %d\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Цикл do-while:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"Итерация %d\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *Задание:* попробуйте написать цикл, который выводит числа от 1 до 10!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "ututututututrejfjwoejfpjqwp":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirenseacreatur")],
                    [InlineKeyboardButton("прошлая глава", callback_data="nozamoyeobidniye")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Условные операторы в C: if, else if, else*\n\n"
                                      "🔹 *Что такое условный оператор?*\n"
                                      "— Позволяет выполнять разные части кода в зависимости от условий.\n\n"
                                      "🔹 *Синтаксис if:*\n"
                                      "```c\n"
                                      "if (условие) {\n"
                                      "    // код, если условие истинно\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Использование else if и else:*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"Положительное число\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"Ноль\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"Отрицательное число\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Логические операторы для условий:*\n"
                                      "- `&&` — И (AND)\n"
                                      "- `||` — ИЛИ (OR)\n"
                                      "- `!`  — НЕ (NOT)\n\n"
                                      "✅ *Задание:* напишите программу, которая проверяет число и выводит сообщение о его знаке!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "sirenseacreatu":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="tentiics")],
                    [InlineKeyboardButton("прошлая глава", callback_data="isdippsjjaias")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Функции в C*\n\n"
                                      "🔹 *Что такое функция?*\n"
                                      "— Блок кода, который выполняет определённую задачу.\n"
                                      "— Позволяет структурировать программу и повторно использовать код.\n\n"
                                      "🔹 *Объявление и вызов функции:*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"Привет, мир!\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // вызов функции\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Функция с параметрами:*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"Привет, %s!\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Том\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Функция с возвращаемым значением:*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"Квадрат 5 равен %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Попробуйте написать функцию, которая складывает два числа и возвращает результат!*\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "isdippsjjaias":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="sirenseacreatu")],
                    [InlineKeyboardButton("прошлая глава", callback_data="ututututututrejfjwoejfpjqwp")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Циклы в C: for, while, do-while*\n\n"
                                      "🔹 *Что такое цикл?*\n"
                                      "— Позволяет повторять блок кода несколько раз.\n\n"
                                      "🔹 *Цикл for:*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"Итерация %d\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Цикл while:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"Итерация %d\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Цикл do-while:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"Итерация %d\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *Задание:* попробуйте написать цикл, который выводит числа от 1 до 10!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "tentiics":
        keyboard = [[InlineKeyboardButton("прошлая глава", callback_data="diaaaadajgaa")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📌 *Указатели в C*\n\n"
                                      "🔹 *Что такое указатель?*\n"
                                      "— Указатель — это переменная, которая хранит адрес другой переменной.\n"
                                      "— Используются для эффективной работы с памятью, массивами, функциями.\n\n"
                                      "🔹 *Пример простого указателя:*\n"
                                      "```c\n"
                                      "int x = 10;\n"
                                      "int* ptr = &x;\n"
                                      "printf(\"Значение: %d\\n\", *ptr); // разыменование\n"
                                      "```\n"
                                      "— `&x` — адрес переменной `x`\n"
                                      "— `*ptr` — доступ к значению по адресу\n\n"
                                      "🔹 *Пояснение:*\n"
                                      "- `int* ptr;` — указатель на целое число\n"
                                      "- `*` — разыменование (получение значения по адресу)\n"
                                      "- `&` — получение адреса переменной\n\n"
                                      "============================\n"
                                      "🔹 *Изменение значения через указатель:*\n"
                                      "```c\n"
                                      "int a = 5;\n"
                                      "int* p = &a;\n"
                                      "*p = 100;\n"
                                      "printf(\"%d\\n\", a); // выведет 100\n"
                                      "```\n"
                                      "✅ Указатель изменяет значение по адресу переменной.\n\n"
                                      "============================\n"
                                      "🔹 *Печать адресов:*\n"
                                      "```c\n"
                                      "int val = 42;\n"
                                      "printf(\"Адрес переменной: %p\\n\", &val);\n"
                                      "```\n"
                                      "— `%p` используется для вывода адресов.\n\n"
                                      "============================\n"
                                      "💡 Указатели — это фундаментальная часть C.\n"
                                      "Они применяются в массивах, строках, передаче данных в функции и в управлении памятью.\n\n"
                                      "📎 В следующей главе ты узнаешь про *массивы и указатели*!\n",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "diaaaadajgaa":
        keyboard = [[InlineKeyboardButton("Следующая глава ➡", callback_data="tentiics")],
                    [InlineKeyboardButton("прошлая глава", callback_data="isdippsjjaias")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Функции в C*\n\n"
                                      "🔹 *Что такое функция?*\n"
                                      "— Блок кода, который выполняет определённую задачу.\n"
                                      "— Позволяет структурировать программу и повторно использовать код.\n\n"
                                      "🔹 *Объявление и вызов функции:*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"Привет, мир!\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // вызов функции\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Функция с параметрами:*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"Привет, %s!\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Том\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Функция с возвращаемым значением:*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"Квадрат 5 равен %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Попробуйте написать функцию, которая складывает два числа и возвращает результат!*\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    if query.data == "english":
        keyboard = [[InlineKeyboardButton("🔥 Start learning", callback_data="xxxx")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "HI! Do you ready to study programming?",
            reply_markup=reply_markup
        )
    elif query.data == "xxxx":
        keyboard = [
            [InlineKeyboardButton("Programming languages", callback_data="continue")],
            [InlineKeyboardButton("Cybersecurity", callback_data="cybersec")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🚀 Great! Now choose what you want to study:",
            reply_markup=reply_markup
        )
    elif query.data == "continue":
        keyboard = [
            [InlineKeyboardButton("🐍 Python ", callback_data="pyt")],
            [InlineKeyboardButton("⚙️ C++ ", callback_data="cp")],
            [InlineKeyboardButton("🟨 Javascript", callback_data="scrip")],
            [InlineKeyboardButton("☕ Java ", callback_data="toomycas")],
            [InlineKeyboardButton("💻 C", callback_data="huggywugg")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "GOOD!! now choose which language you want to study",
            reply_markup=reply_markup
        )

    elif query.data == "cybersec":
        keyboard = [
            [InlineKeyboardButton("📡Networks", callback_data="cyberx")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Let's start!\nChapter 1:",
            reply_markup=reply_markup
        )

    elif query.data == "cyberx":
        keyboard = [
            [InlineKeyboardButton("next chapter➡️", callback_data="nextx")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 *Networks* are simply connected objects.\n"
                                      "For example, your circle of friends: you are connected by common interests,\n"
                                      "hobbies, skills, and other things. 🧠🤝\n\n"
                                      "📡 Networks are everywhere:\n"
                                      " - 🚇 Public transportation in a city\n"
                                      " - ⚡ Infrastructure like the national power grid\n"
                                      " - 🏘️ Chatting with neighbors\n"
                                      " - ✉️ Mail systems for sending letters and packages\n\n"
                                      "💻 In computing, it’s the same idea applied to technology.\n"
                                      "Take your phone 📱: the reason you use it is to access information.\n\n"
                                      "📶 We will look at how devices exchange data and what rules apply\\.\n\n"
                                      "🖥️ In computing, a network can consist of 2 to billions of devices.\n"
                                      "These include:\n"
                                      " - 💻 Laptops\n"
                                      " - 📱 Smartphones\n"
                                      " - 📷 Surveillance cameras\n"
                                      " - 🚦 Traffic lights\n"
                                      " - 🌾 Even farming equipment!\n\n"
                                      "🔌 Networks are embedded in our daily life:\n"
                                      " - ⛅ Weather data collection\n"
                                      " - ⚡ Power supply to homes\n"
                                      " - 🚦 Prioritizing road traffic\n\n"
                                      "🛡️ Since networks are an integral part of modern life,\n"
                                      "understanding network principles is the foundation for studying cybersecurity.\n\n"
                                      "👥 Check the diagram below: Alice, Bob, and Jim formed their own network!\n"
                                      "We will come back to this later.\n\n"
                                      "*The first chapter is here!!*\n*Первая глава уже здесь!!*"
                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "nextx":
        keyboard = [
            [InlineKeyboardButton("next chapter➡️", callback_data="twop")],
            [InlineKeyboardButton("last chapter", callback_data="outofmymind")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Chapter 2: Diving into the Internet!*\n\n"
                                      "Now that you understand what a network is — simply devices connected together — let’s figure out how the Internet works.\n\n"
                                      "📡 The Internet is just a *huge network* made up of many small networks connected to each other.\n\n"
                                      "👫 Imagine Alice has made new friends — Zayn and Toby. She wants to introduce them to Bob and Jim. But there’s one problem: only Alice understands the language of both groups. So she becomes a *bridge* — now everyone can communicate through her. This is an example of a new network.\n\n"
                                      "📜 The first version of the Internet appeared in the late 1960s as part of the *ARPANET* project, funded by the U.S. military.\n"
                                      "It was the first real working network between computers.\n\n"
                                      "🌍 In 1989, Tim Berners-Lee proposed the concept of the *World Wide Web (WWW)*, which turned the Internet into a convenient tool for sharing and storing information.\n\n"
                                      "🔌 Today, the Internet is like a huge club made of thousands of small teams. There are two types of networks:\n"
                                      " - 🔒 Private Networks\n"
                                      " - 🌐 Public Networks, which together form what we call the Internet\n\n"
                                      "💡 Devices on a network use special *identifiers* (we’ll talk about these later) to find each other and exchange data."

                                      ,
                                      reply_markup=reply_markup)
    elif query.data == "outofmymind":
        keyboard = [
            [InlineKeyboardButton("next chapter➡️", callback_data="nextx")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 *Networks* are simply connected objects.\n"
                                      "For example, your circle of friends: you are connected by common interests,\n"
                                      "hobbies, skills, and other things. 🧠🤝\n\n"
                                      "📡 Networks are everywhere:\n"
                                      " - 🚇 Public transportation in a city\n"
                                      " - ⚡ Infrastructure like the national power grid\n"
                                      " - 🏘️ Chatting with neighbors\n"
                                      " - ✉️ Mail systems for sending letters and packages\n\n"
                                      "💻 In computing, it’s the same idea applied to technology.\n"
                                      "Take your phone 📱: the reason you use it is to access information.\n\n"
                                      "📶 We will look at how devices exchange data and what rules apply\\.\n\n"
                                      "🖥️ In computing, a network can consist of 2 to billions of devices.\n"
                                      "These include:\n"
                                      " - 💻 Laptops\n"
                                      " - 📱 Smartphones\n"
                                      " - 📷 Surveillance cameras\n"
                                      " - 🚦 Traffic lights\n"
                                      " - 🌾 Even farming equipment!\n\n"
                                      "🔌 Networks are embedded in our daily life:\n"
                                      " - ⛅ Weather data collection\n"
                                      " - ⚡ Power supply to homes\n"
                                      " - 🚦 Prioritizing road traffic\n\n"
                                      "🛡️ Since networks are an integral part of modern life,\n"
                                      "understanding network principles is the foundation for studying cybersecurity.\n\n"
                                      "👥 Check the diagram below: Alice, Bob, and Jim formed their own network!\n"
                                      "We will come back to this later.\n\n"
                                      "*The first chapter is here!!*\n*Первая глава уже здесь!!*"
                                      ,
                                      reply_markup=reply_markup)


    elif query.data == "twop":
        keyboard = [
            [InlineKeyboardButton("next chapter➡️", callback_data="threep")],
            [InlineKeyboardButton("last chapter", callback_data="dvauksazactotisact")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("""📡 For devices to communicate and keep order in the network, they must:
— Recognize themselves
— Be recognizable by others

💡 Devices are like people:
— We have names (which can be changed)
— And fingerprints (unique forever)

📱 Devices also have two types of "identification":
— IP address (📍 can be changed)
— MAC address (🔒 permanent, like a fingerprint)

=====================
🔹 IP Addresses
An IP address is like a device’s temporary name in the network.
It consists of 4 numbers (octets) separated by dots:
Example: 192.168.0.1

🔁 One IP can be assigned to another device, but two devices cannot work simultaneously with the same IP in one network.

🌍 There are two types of IP addresses:
— Private IP — used inside a local network (home, office)
— Public IP — visible on the Internet

🧾 Example:

Device	Private IP	Public IP
My PC	192.168.1.77	86.157.52.21
Other PC	192.168.1.74	86.157.52.21

🔍 Both devices have the same public IP (one modem) but different private IPs — that’s how they communicate in one network.

=====================
🌐 Problem: not enough addresses!
IPv4 = 4.29 billion addresses (2^32). But devices worldwide — tens of billions.

💡 Solution:
— IPv6 = 340+ trillion addresses (2^128)
— More efficient
— Much more addresses

Example:
— IPv4: 192.168.1.1
— IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

=====================
🔹 MAC Addresses
Each device has a network adapter with a unique address — MAC address.
Format: a4:c3:f0:85:ac:2d (6 bytes in hex form)

🛠 The first 6 characters — manufacturer.
📌 The last 6 — unique device number.

💥 But MAC address can be faked — this is called spoofing:
— An attacker can pretend to be another device.
— For example, if a firewall allows only the admin’s MAC — it can be tricked!

=====================
📌 Summary:
🔹 IP — changes depending on the network.
🔹 MAC — permanent and unique.
🔹 For security, keep in mind neither IP nor MAC guarantees authenticity.

""",
                                      reply_markup=reply_markup)
    elif query.data == "dvauksazactotisact":
        keyboard = [
            [InlineKeyboardButton("next chapter➡️", callback_data="twop")],
            [InlineKeyboardButton("last chapter", callback_data="outofmymind")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Chapter 2: Diving into the Internet!*\n\n"
                                      "Now that you understand what a network is — simply devices connected together — let’s figure out how the Internet works.\n\n"
                                      "📡 The Internet is just a *huge network* made up of many small networks connected to each other.\n\n"
                                      "👫 Imagine Alice has made new friends — Zayn and Toby. She wants to introduce them to Bob and Jim. But there’s one problem: only Alice understands the language of both groups. So she becomes a *bridge* — now everyone can communicate through her. This is an example of a new network.\n\n"
                                      "📜 The first version of the Internet appeared in the late 1960s as part of the *ARPANET* project, funded by the U.S. military.\n"
                                      "It was the first real working network between computers.\n\n"
                                      "🌍 In 1989, Tim Berners-Lee proposed the concept of the *World Wide Web (WWW)*, which turned the Internet into a convenient tool for sharing and storing information.\n\n"
                                      "🔌 Today, the Internet is like a huge club made of thousands of small teams. There are two types of networks:\n"
                                      " - 🔒 Private Networks\n"
                                      " - 🌐 Public Networks, which together form what we call the Internet\n\n"
                                      "💡 Devices on a network use special *identifiers* (we’ll talk about these later) to find each other and exchange data."

                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "threep":
        keyboard = [[InlineKeyboardButton("last chapter", callback_data="bablateperebatpizdec")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Ping is a basic network tool used to check connectivity between two devices."
            "It works using the ICMP protocol (Internet Control Message Protocol),"
            "sending special echo requests and waiting for echo replies from the target node."

            "With ping, you can determine if the connection is working and how stable it is."
            "You can also measure how many milliseconds it takes for packets to travel from one device to another."

            "This tool is built into most operating systems, including Linux and Windows."
            "To run ping, just enter the command:"
            "`ping IP-address` or `ping website-name` in the terminal or command prompt."

            "For example, if you run the command `ping 192.168.1.254`,"
            "you’ll see how many packets were sent and received,",
            "and the average response time (e.g., 4.16 ms).",reply_markup = reply_markup)
    elif query.data == "bablateperebatpizdec":
        keyboard = [
            [InlineKeyboardButton("next chapter➡️", callback_data="threep")],
            [InlineKeyboardButton("last chapter", callback_data="dvauksazactotisact")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("""📡 For devices to communicate and keep order in the network, they must:
        — Recognize themselves
        — Be recognizable by others

        💡 Devices are like people:
        — We have names (which can be changed)
        — And fingerprints (unique forever)

        📱 Devices also have two types of "identification":
        — IP address (📍 can be changed)
        — MAC address (🔒 permanent, like a fingerprint)

        =====================
        🔹 IP Addresses
        An IP address is like a device’s temporary name in the network.
        It consists of 4 numbers (octets) separated by dots:
        Example: 192.168.0.1

        🔁 One IP can be assigned to another device, but two devices cannot work simultaneously with the same IP in one network.

        🌍 There are two types of IP addresses:
        — Private IP — used inside a local network (home, office)
        — Public IP — visible on the Internet

        🧾 Example:

        Device	Private IP	Public IP
        My PC	192.168.1.77	86.157.52.21
        Other PC	192.168.1.74	86.157.52.21

        🔍 Both devices have the same public IP (one modem) but different private IPs — that’s how they communicate in one network.

        =====================
        🌐 Problem: not enough addresses!
        IPv4 = 4.29 billion addresses (2^32). But devices worldwide — tens of billions.

        💡 Solution:
        — IPv6 = 340+ trillion addresses (2^128)
        — More efficient
        — Much more addresses

        Example:
        — IPv4: 192.168.1.1
        — IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

        =====================
        🔹 MAC Addresses
        Each device has a network adapter with a unique address — MAC address.
        Format: a4:c3:f0:85:ac:2d (6 bytes in hex form)

        🛠 The first 6 characters — manufacturer.
        📌 The last 6 — unique device number.

        💥 But MAC address can be faked — this is called spoofing:
        — An attacker can pretend to be another device.
        — For example, if a firewall allows only the admin’s MAC — it can be tricked!

        =====================
        📌 Summary:
        🔹 IP — changes depending on the network.
        🔹 MAC — permanent and unique.
        🔹 For security, keep in mind neither IP nor MAC guarantees authenticity.

        """,
                                      reply_markup=reply_markup)


    elif query.data == "pyt":
        keyboard = [[
            InlineKeyboardButton("GO", callback_data="numberones")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "GOOD!! Let's start our Python trip 🐍»",
            reply_markup=reply_markup)
    elif query.data == "cp":
        keyboard = [[
            InlineKeyboardButton("*Chapter 1*", callback_data="cpones")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "GOOD!! Let's start our C++ trip ⚙️",
            reply_markup=reply_markup)
    elif query.data == "scrip":
        keyboard = [[
            InlineKeyboardButton("chapter 1", callback_data="jvones")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "GOOD!! Let's start our 🟨 Javascript trip",
            reply_markup=reply_markup)
    elif query.data == "numberones":
        keyboard = [[InlineKeyboardButton("🐍Start", callback_data="mcqueens")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Let's get started!\n"
                                      "*Chapter 1:*", reply_markup=reply_markup)
    elif query.data == "mcqueens":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="f")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Installing Python 64-bit and Connecting to PyCharm Community*\n\n"
            "🔹 *Step 1: Download Python*\n"
            "[Download Python](https://www.python.org/downloads/) — choose Windows x86-64 executable installer\n\n"
            "🔹 *Step 2: Installation*\n"
            "— Check 'Add Python to PATH'\n"
            "— Choose Customize Installation → Next → Install for all users → Install\n\n"
            "🔹 *Step 3: Verification*\n"
            "`python --version` in terminal — should show Python 3.X.X\n\n"
            "🔹 *Step 4: Download PyCharm*\n"
            "[Download PyCharm](https://www.jetbrains.com/pycharm/download)\n"
            "— Install the Community edition\n\n"
            "🔹 *Step 5: Connect Python*\n"
            "New Project → ⚙️ Add Interpreter → System Interpreter → path:\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *Check:*\n"
            "Create a file with code:\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "Press ▶️ Run"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "f":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="ifelif")],
                    [InlineKeyboardButton("last chapter", callback_data="socsinyourmouthe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Variables and Data Types in Python*\n\n"
            "🔹 *What is a variable?*\n"
            "— It’s a name for storing data. The type is determined automatically.\n\n"
            "🔹 *Variable examples:*\n"
            "`x = 10` — integer (int)\n"
            "`name = \"Tom\"` — string (str)\n"
            "`pi = 3.14` — floating point number (float)\n\n"
            "🔹 *Main data types:*\n"
            "- int — whole numbers\n"
            "- float — decimal numbers\n"
            "- str — text strings\n"
            "- bool — True / False (logic)\n\n"
            "🔹 *How to print data?*\n"
            "`print(x)`\n"
            "`print(name)`\n"
            "`print(pi)`\n\n"
            "✅ *Try it yourself:*\n"
            "```python\nage = 15\ncity = \"Moscow\"\nis_student = True\n\n"
            "print(\"Age:\", age)\nprint(\"City:\", city)\nprint(\"Student:\", is_student)\n```"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "socsinyourmouthe":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="f")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Installing Python 64-bit and Connecting to PyCharm Community*\n\n"
            "🔹 *Step 1: Download Python*\n"
            "[Download Python](https://www.python.org/downloads/) — choose Windows x86-64 executable installer\n\n"
            "🔹 *Step 2: Installation*\n"
            "— Check 'Add Python to PATH'\n"
            "— Choose Customize Installation → Next → Install for all users → Install\n\n"
            "🔹 *Step 3: Verification*\n"
            "`python --version` in terminal — should show Python 3.X.X\n\n"
            "🔹 *Step 4: Download PyCharm*\n"
            "[Download PyCharm](https://www.jetbrains.com/pycharm/download)\n"
            "— Install the Community edition\n\n"
            "🔹 *Step 5: Connect Python*\n"
            "New Project → ⚙️ Add Interpreter → System Interpreter → path:\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *Check:*\n"
            "Create a file with code:\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "Press ▶️ Run"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )


    elif query.data == "ifelif":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="sezere")],
                    [InlineKeyboardButton("last chapter", callback_data="ebatttttttttt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Conditions in Python: if, elif, else*\n\n"
            "🔹 *What is a condition?*\n"
            "— It’s a way to run code only if a certain condition is met.\n"
            "— Uses if, elif, else\n\n"
            "🔹 *Syntax:*\n"
            "```python\nage = 16\n\nif age >= 18:\n    print(\"You are an adult\")\n"
            "elif age >= 14:\n    print(\"You are a teenager\")\nelse:\n    print(\"You are a child\")\n```\n\n"
            "🔹 *Comparison operators:* ==, !=, >, <, >=, <=\n"
            "🔹 *Logical operators:* and, or, not\n\n"
            "✅ *Try it yourself:*\n"
            "```python\nname = input(\"Your name: \")\nif name == \"Tom\":\n    print(\"Hello, Tom!\")\n"
            "else:\n    print(\"Hello, guest!\")\n```"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "ebatttttttttt":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="ifelif")],
                    [InlineKeyboardButton("last chapter", callback_data="socsinyourmouthe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Variables and Data Types in Python*\n\n"
            "🔹 *What is a variable?*\n"
            "— It’s a name for storing data. The type is determined automatically.\n\n"
            "🔹 *Variable examples:*\n"
            "`x = 10` — integer (int)\n"
            "`name = \"Tom\"` — string (str)\n"
            "`pi = 3.14` — floating point number (float)\n\n"
            "🔹 *Main data types:*\n"
            "- int — whole numbers\n"
            "- float — decimal numbers\n"
            "- str — text strings\n"
            "- bool — True / False (logic)\n\n"
            "🔹 *How to print data?*\n"
            "`print(x)`\n"
            "`print(name)`\n"
            "`print(pi)`\n\n"
            "✅ *Try it yourself:*\n"
            "```python\nage = 15\ncity = \"Moscow\"\nis_student = True\n\n"
            "print(\"Age:\", age)\nprint(\"City:\", city)\nprint(\"Student:\", is_student)\n```"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "sezere":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="tututut")],
                    [InlineKeyboardButton("last chapter", callback_data="ebaniyzavozastviiii")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python: for and while Loops*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— It’s a construct to repeatedly execute a block of code.\n"
                                      "— Used to iterate over lists, numbers, and other collections.\n\n"
                                      "============================\n"
                                      "🔹 *for loop:*\n"
                                      "```python\nfor i in range(5):\n    print(i)\n```\n"
                                      "— Prints numbers from 0 to 4.\n\n"
                                      "🔸 range(5) creates a sequence: 0, 1, 2, 3, 4\n\n"
                                      "============================\n"
                                      "🔹 *while loop:*\n"
                                      "```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```\n"
                                      "— Repeats the block while the condition is true.\n\n"
                                      "============================\n"
                                      "🔹 *Iterate over list with for:*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- for — good for iterating elements\n"
                                      "- while — runs as long as condition is true\n"
                                      "- To stop the loop early, use `break`\n\n"
                                      "💡 Loops are the foundation for automation and processing large data!\n"
                                      "Try writing a simple loop yourself to print a list of numbers or words!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "ebaniyzavozastviiii":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="sezere")],
                    [InlineKeyboardButton("last chapter", callback_data="ebatttttttttt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Conditions in Python: if, elif, else*\n\n"
            "🔹 *What is a condition?*\n"
            "— It’s a way to run code only if a certain condition is met.\n"
            "— Uses if, elif, else\n\n"
            "🔹 *Syntax:*\n"
            "```python\nage = 16\n\nif age >= 18:\n    print(\"You are an adult\")\n"
            "elif age >= 14:\n    print(\"You are a teenager\")\nelse:\n    print(\"You are a child\")\n```\n\n"
            "🔹 *Comparison operators:* ==, !=, >, <, >=, <=\n"
            "🔹 *Logical operators:* and, or, not\n\n"
            "✅ *Try it yourself:*\n"
            "```python\nname = input(\"Your name: \")\nif name == \"Tom\":\n    print(\"Hello, Tom!\")\n"
            "else:\n    print(\"Hello, guest!\")\n```"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "tututut":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="onyxx")],
                    [InlineKeyboardButton("last chapter", callback_data="pizdecebaniystozasmertvnishite")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python: Lists*\n\n"
                                      "🔹 *What is a list?*\n"
                                      "— It’s an ordered collection of elements.\n"
                                      "— You can store numbers, strings, and even other lists inside.\n\n"
                                      "============================\n"
                                      "🔹 *List example:*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\n```\n"
                                      "— A list of three strings.\n\n"
                                      "🔸 Access by index:\n"
                                      "`fruits[0]` → \"apple\"\n"
                                      "`fruits[2]` → \"cherry\"\n\n"
                                      "============================\n"
                                      "🔹 *Modify and add elements:*\n"
                                      "```python\nfruits[1] = \"kiwi\"  # Replace 'banana' with 'kiwi'\nfruits.append(\"pear\")  # Add element\n```\n\n"
                                      "============================\n"
                                      "🔹 *Iterate over the list:*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 Prints each element in the list.\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- Indexes start at 0\n"
                                      "- Can store elements of different types\n"
                                      "- Lists are mutable (you can add, remove elements)\n\n"
                                      "💡 Lists are one of the most powerful tools for working with data collections in Python.\n"
                                      "Try creating your own list and looping through it!"
                                      ,
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "pizdecebaniystozasmertvnishite":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="tututut")],
                    [InlineKeyboardButton("last chapter", callback_data="ebaniyzavozastviiii")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python: for and while Loops*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— It’s a construct to repeatedly execute a block of code.\n"
                                      "— Used to iterate over lists, numbers, and other collections.\n\n"
                                      "============================\n"
                                      "🔹 *for loop:*\n"
                                      "```python\nfor i in range(5):\n    print(i)\n```\n"
                                      "— Prints numbers from 0 to 4.\n\n"
                                      "🔸 range(5) creates a sequence: 0, 1, 2, 3, 4\n\n"
                                      "============================\n"
                                      "🔹 *while loop:*\n"
                                      "```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```\n"
                                      "— Repeats the block while the condition is true.\n\n"
                                      "============================\n"
                                      "🔹 *Iterate over list with for:*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- for — good for iterating elements\n"
                                      "- while — runs as long as condition is true\n"
                                      "- To stop the loop early, use `break`\n\n"
                                      "💡 Loops are the foundation for automation and processing large data!\n"
                                      "Try writing a simple loop yourself to print a list of numbers or words!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "onyxx":
        keyboard = [[InlineKeyboardButton("last chapter", callback_data="xoxoxooxooxoxeeetoyavovremayaprisel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🛠️ *Functions in Python*\n\n"
                                      "🔹 *What is a function?*\n"
                                      "— It’s a block of code that performs a specific task.\n"
                                      "— Functions help avoid code repetition and make programs easier to understand.\n\n"
                                      "============================\n"
                                      "🔹 *Simple function:*\n"
                                      "```python\ndef say_hello():\n    print(\"Hello, world!\")\n\nsay_hello()  # Call the function\n```\n"
                                      "— The keyword `def`, function name, parentheses, and colon.\n"
                                      "— Everything inside runs when the function is called.\n\n"
                                      "============================\n"
                                      "🔹 *Function with parameters:*\n"
                                      "```python\ndef greet(name):\n    print(\"Hello,\", name)\n\ngreet(\"Alice\")\n```\n"
                                      "— You can pass values into the function.\n"
                                      "— These are called arguments or parameters.\n\n"
                                      "============================\n"
                                      "🔹 *Function with return value (`return`):*\n"
                                      "```python\ndef square(x):\n    return x * x\n\nresult = square(5)\nprint(result)\n```\n"
                                      "— `return` sends back the result of the function.\n"
                                      "— You can save the result into a variable.\n\n"
                                      "============================\n"
                                      "✅ *Why are functions important?*\n"
                                      "- Make code compact and readable\n"
                                      "- Allow reusing the same code block\n"
                                      "- Enable splitting large programs into logical parts\n\n"
                                      "💡 First, try writing a function that prints your name, then one that returns the sum of two numbers!\n"
                                      "Functions are the foundation of any programming language! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "xoxoxooxooxoxeeetoyavovremayaprisel":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="onyxx")],
                    [InlineKeyboardButton("last chapter", callback_data="pizdecebaniystozasmertvnishite")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python: Lists*\n\n"
                                      "🔹 *What is a list?*\n"
                                      "— It’s an ordered collection of elements.\n"
                                      "— You can store numbers, strings, and even other lists inside.\n\n"
                                      "============================\n"
                                      "🔹 *List example:*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\n```\n"
                                      "— A list of three strings.\n\n"
                                      "🔸 Access by index:\n"
                                      "`fruits[0]` → \"apple\"\n"
                                      "`fruits[2]` → \"cherry\"\n\n"
                                      "============================\n"
                                      "🔹 *Modify and add elements:*\n"
                                      "```python\nfruits[1] = \"kiwi\"  # Replace 'banana' with 'kiwi'\nfruits.append(\"pear\")  # Add element\n```\n\n"
                                      "============================\n"
                                      "🔹 *Iterate over the list:*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 Prints each element in the list.\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- Indexes start at 0\n"
                                      "- Can store elements of different types\n"
                                      "- Lists are mutable (you can add, remove elements)\n\n"
                                      "💡 Lists are one of the most powerful tools for working with data collections in Python.\n"
                                      "Try creating your own list and looping through it!"
                                      ,
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "cpones":
        keyboard = [[InlineKeyboardButton("⚙ Start", callback_data="rezere")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("«»", reply_markup=reply_markup)

    elif query.data == "rezere":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="vezere")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++ Setup and Start:*\n\n"
            "🔹 *Step 1: Install the compiler*\n"
            "[Download MinGW](https://sourceforge.net/projects/mingw/)\n"
            "— Install gcc and add the bin path to your PATH environment variable\n\n"
            "🔹 *Step 2: Download an editor*\n"
            "[Download Visual Studio Code](https://code.visualstudio.com/)\n\n"
            "🔹 *Step 3: Check the compiler:*\n"
            "`g++ --version`\n\n"
            "🔹 *Step 4: Simple code:*\n"
            "```cpp\n#include <iostream>\\nint main\\(\\) {\\n"
            "    std::cout << \"Hello, world!\";\\n    return 0;\\n}\\n```\n"
            "Save as `main.cpp`, compile:\n"
            "`g++ main.cpp -o main`\n"
            "`./main`"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "vezere":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="cpp4")],
                    [InlineKeyboardButton("last chapter", callback_data="modaiskustvokulinariya")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++: Variables and Data Types*\n\n"
            "🔹 *What is a variable?*\n"
            "— It’s a named memory area for storing data.\n"
            "— You must declare a variable with a type before using it.\n\n"
            "🔹 *Examples:*\n"
            "`int age = 15;`\n"
            "`double pi = 3.14;`\n"
            "`char grade = 'A';`\n"
            "`bool isOnline = true;`\n"
            "`std::string name = \"Tom\";`\n\n"
            "🔹 *Example output:*\n"
            "```cpp\n#include <iostream>\\n#include <string>\\n\\nint main\\(\\) {\\n"
            "    int age = 15;\\n    std::string name = \"Tom\";\\n"
            "    std::cout << \"Name: \" << name << \"\\n\";\\n"
            "    std::cout << \"Age: \" << age << \"\\n\";\\n    return 0;\\n}\\n```"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "modaiskustvokulinariya":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="vezere")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++ Setup and Start:*\n\n"
            "🔹 *Step 1: Install the compiler*\n"
            "[Download MinGW](https://sourceforge.net/projects/mingw/)\n"
            "— Install gcc and add the bin path to your PATH environment variable\n\n"
            "🔹 *Step 2: Download an editor*\n"
            "[Download Visual Studio Code](https://code.visualstudio.com/)\n\n"
            "🔹 *Step 3: Check the compiler:*\n"
            "`g++ --version`\n\n"
            "🔹 *Step 4: Simple code:*\n"
            "```cpp\n#include <iostream>\\nint main\\(\\) {\\n"
            "    std::cout << \"Hello, world!\";\\n    return 0;\\n}\\n```\n"
            "Save as `main.cpp`, compile:\n"
            "`g++ main.cpp -o main`\n"
            "`./main`"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )


    elif query.data == "cpp4":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="bejingg")],
                    [InlineKeyboardButton("last chapter", callback_data="soliiiiiiinaranuebalat")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++: Conditions (if, else, else if)*\n\n"
            "🔹 *What is a condition?*\n"
            "— Allows executing code when conditions are met.\n\n"
            "🔹 *Example:*\n"
            "```cpp\n#include <iostream>\\nusing namespace std;\\n\\nint main\\(\\) {\\n"
            "    int age = 16;\\n"
            "    if \\(age >= 18\\) {\\n        cout << \"You are an adult\";\\n"
            "    } else if \\(age >= 14\\) {\\n        cout << \"You are a teenager\";\\n"
            "    } else {\\n        cout << \"You are a child\";\\n    }\\n    return 0;\\n}\\n```\n\n"
            "🔹 *Operators:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Logic:* `&&`, `||`, `!`\n\n"
            "✅ *Try it yourself!*"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )
    elif query.data == "soliiiiiiinaranuebalat":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="cpp4")],
                    [InlineKeyboardButton("last chapter", callback_data="modaiskustvokulinariya")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++: Variables and Data Types*\n\n"
            "🔹 *What is a variable?*\n"
            "— It’s a named memory area for storing data.\n"
            "— You must declare a variable with a type before using it.\n\n"
            "🔹 *Examples:*\n"
            "`int age = 15;`\n"
            "`double pi = 3.14;`\n"
            "`char grade = 'A';`\n"
            "`bool isOnline = true;`\n"
            "`std::string name = \"Tom\";`\n\n"
            "🔹 *Example output:*\n"
            "```cpp\n#include <iostream>\\n#include <string>\\n\\nint main\\(\\) {\\n"
            "    int age = 15;\\n    std::string name = \"Tom\";\\n"
            "    std::cout << \"Name: \" << name << \"\\n\";\\n"
            "    std::cout << \"Age: \" << age << \"\\n\";\\n    return 0;\\n}\\n```"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "bejingg":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="venomouss")],
                    [InlineKeyboardButton("last chapter", callback_data="owiworweuwruworwwe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *C++: Loops (for, while, do while)*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— It’s a way to repeatedly execute the same block of code while a condition is true.\n\n"
                                      "🔹 *Types of loops in C++:*\n"
                                      "- `for` — when you know the number of iterations beforehand\n"
                                      "- `while` — runs while the condition is true\n"
                                      "- `do while` — runs first, then checks the condition\n\n"
                                      "============================\n"
                                      "🔹 *Example: for*\n"
                                      "```cpp\nfor \\(int i = 0; i < 5; i\\+\\+\\) {\\n    cout << i << \" \"\\;\\n}\\n```\n"
                                      "🔸 Output: `0 1 2 3 4`\n\n"
                                      "============================\n"
                                      "🔹 *Example: while*\n"
                                      "```cpp\nint i = 0;\\nwhile \\(i < 3\\) {\\n    cout << i << endl;\\n    i\\+\\+;\\n}\\n```\n"
                                      "🔸 Output: `0`, `1`, `2`\n\n"
                                      "============================\n"
                                      "🔹 *Example: do while*\n"
                                      "```cpp\nint i = 0;\\ndo {\\n    cout << i << endl;\\n    i\\+\\+;\\n} while \\(i < 2\\);\\n```\n"
                                      "🔸 Output: `0`, `1`\n\n"
                                      "============================\n"
                                      "✅ *When to use?*\n"
                                      "- `for` — convenient for counters (`i = 0; i < N; i++`)\n"
                                      "- `while` — when you don’t know how many times in advance\n"
                                      "- `do while` — guarantees at least one run\n\n"
                                      "Try it yourself!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "owiworweuwruworwwe":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="bejingg")],
                    [InlineKeyboardButton("last chapter", callback_data="soliiiiiiinaranuebalat")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++: Conditions (if, else, else if)*\n\n"
            "🔹 *What is a condition?*\n"
            "— Allows executing code when conditions are met.\n\n"
            "🔹 *Example:*\n"
            "```cpp\n#include <iostream>\\nusing namespace std;\\n\\nint main\\(\\) {\\n"
            "    int age = 16;\\n"
            "    if \\(age >= 18\\) {\\n        cout << \"You are an adult\";\\n"
            "    } else if \\(age >= 14\\) {\\n        cout << \"You are a teenager\";\\n"
            "    } else {\\n        cout << \"You are a child\";\\n    }\\n    return 0;\\n}\\n```\n\n"
            "🔹 *Operators:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Logic:* `&&`, `||`, `!`\n\n"
            "✅ *Try it yourself!*"
            ,
            parse_mode="Markdown", reply_markup=reply_markup
        )

    elif query.data == "venomouss":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="zerotrusts")],
                    [InlineKeyboardButton("last chapter", callback_data="izsamariamsimd")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++: Arrays*\n\n"
                                      "🔹 *What is an array?*\n"
                                      "— It’s a collection of elements of **the same type**, stored contiguously in memory.\n"
                                      "— Each element has its own index (starting at 0).\n\n"
                                      "============================\n"
                                      "🔹 *Array example:*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\\n```\n"
                                      "— Creates an array of 5 elements of type int.\n\n"
                                      "🔸 Access elements:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Print all elements using a loop:*\n"
                                      "```cpp\nfor \\(int i = 0; i < 5; i\\+\\+\\) {\\n    cout << numbers\\[i\\] << \" \"\\;\\n}\\n```\n"
                                      "🔸 Output: `10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *Input values from user:*\n"
                                      "```cpp\nint a[3];\\nfor \\(int i = 0; i < 3; i\\+\\+\\) {\\n    cin >> a\\[i\\];\\n}\\n```\n"
                                      "🔸 Stores 3 numbers in the array.\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- Indexes go from `0` to `n - 1`\n"
                                      "- Going out of array bounds = ❌ error (UB — undefined behavior)\n"
                                      "- All elements are the same type (int, float, char, etc.)\n\n"
                                      "💡 Arrays are fundamental. With them, you’ll learn memory management, sorting, algorithms!\n\n"
                                      "Try creating an array and printing its elements!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "izsamariamsimd":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="venomouss")],
                    [InlineKeyboardButton("last chapter", callback_data="owiworweuwruworwwe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *C++: Loops (for, while, do while)*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— It’s a way to repeatedly execute the same block of code while a condition is true.\n\n"
                                      "🔹 *Types of loops in C++:*\n"
                                      "- `for` — when you know the number of iterations beforehand\n"
                                      "- `while` — runs while the condition is true\n"
                                      "- `do while` — runs first, then checks the condition\n\n"
                                      "============================\n"
                                      "🔹 *Example: for*\n"
                                      "```cpp\nfor \\(int i = 0; i < 5; i\\+\\+\\) {\\n    cout << i << \" \"\\;\\n}\\n```\n"
                                      "🔸 Output: `0 1 2 3 4`\n\n"
                                      "============================\n"
                                      "🔹 *Example: while*\n"
                                      "```cpp\nint i = 0;\\nwhile \\(i < 3\\) {\\n    cout << i << endl;\\n    i\\+\\+;\\n}\\n```\n"
                                      "🔸 Output: `0`, `1`, `2`\n\n"
                                      "============================\n"
                                      "🔹 *Example: do while*\n"
                                      "```cpp\nint i = 0;\\ndo {\\n    cout << i << endl;\\n    i\\+\\+;\\n} while \\(i < 2\\);\\n```\n"
                                      "🔸 Output: `0`, `1`\n\n"
                                      "============================\n"
                                      "✅ *When to use?*\n"
                                      "- `for` — convenient for counters (`i = 0; i < N; i++`)\n"
                                      "- `while` — when you don’t know how many times in advance\n"
                                      "- `do while` — guarantees at least one run\n\n"
                                      "Try it yourself!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "zerotrusts":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="amburanmal")],
                    [InlineKeyboardButton("last chapter", callback_data="zinanzinsnedeji")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++: Strings*\n\n"
                                      "🔹 *What is a string?*\n"
                                      "— It’s a sequence of characters, like a name or phrase.\n"
                                      "— In C++, you can use a char array or the `std::string` class.\n\n"
                                      "============================\n"
                                      "🔹 *String as a char array:*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\\n```\n"
                                      "🔸 The `\\0` character is automatically added at the end — it marks the string’s end.\n"
                                      "🔸 The array size must be larger than the string length.\n\n"
                                      "============================\n"
                                      "🔹 *Strings with `std::string`:*\n"
                                      "```cpp\n#include <string>\\n\\nstd::string city = \"Baku\";\\n```\n"
                                      "— This method is easier and safer.\n\n"
                                      "============================\n"
                                      "🔹 *Basic operations:*\n"
                                      "```cpp\nstd::string name = \"Tom\";\\n\\n"
                                      "cout << name << endl;         // Print the string\\n"
                                      "cout << name.length() << endl; // String length\\n"
                                      "name += \" Hardy\";             // Concatenation\\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *User input for string:*\n"
                                      "```cpp\nstd::string userName;\\ncout << \"Enter name: \";\\ncin >> userName;\\n```\n"
                                      "❗ `cin` reads input until the first space. For a full phrase:\n"
                                      "```cpp\nstd::string fullName;\\ngetline(cin, fullName);\\n```\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- `std::string` is easier and safer than `char` arrays\n"
                                      "- You can easily concatenate, measure length, and find characters\n"
                                      "- For Cyrillic or other unicode, encoding setup may be needed\n\n"
                                      "💡 Strings are the foundation for working with text, forms, messages!\n"
                                      "Try creating a string and printing it! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "zinanzinsnedeji":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="zerotrusts")],
                    [InlineKeyboardButton("last chapter", callback_data="izsamariamsimd")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++: Arrays*\n\n"
                                      "🔹 *What is an array?*\n"
                                      "— It’s a collection of elements of **the same type**, stored contiguously in memory.\n"
                                      "— Each element has its own index (starting at 0).\n\n"
                                      "============================\n"
                                      "🔹 *Array example:*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\\n```\n"
                                      "— Creates an array of 5 elements of type int.\n\n"
                                      "🔸 Access elements:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Print all elements using a loop:*\n"
                                      "```cpp\nfor \\(int i = 0; i < 5; i\\+\\+\\) {\\n    cout << numbers\\[i\\] << \" \"\\;\\n}\\n```\n"
                                      "🔸 Output: `10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *Input values from user:*\n"
                                      "```cpp\nint a[3];\\nfor \\(int i = 0; i < 3; i\\+\\+\\) {\\n    cin >> a\\[i\\];\\n}\\n```\n"
                                      "🔸 Stores 3 numbers in the array.\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- Indexes go from `0` to `n - 1`\n"
                                      "- Going out of array bounds = ❌ error (UB — undefined behavior)\n"
                                      "- All elements are the same type (int, float, char, etc.)\n\n"
                                      "💡 Arrays are fundamental. With them, you’ll learn memory management, sorting, algorithms!\n\n"
                                      "Try creating an array and printing its elements!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "amburanmal":
        keyboard = [[InlineKeyboardButton("last chapter", callback_data="crchemole")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C++: Functions*\n\n"
                                      "🔹 *What is a function?*\n"
                                      "— It’s a block of code that performs a specific task.\n"
                                      "— Helps structure the program and avoid repetition.\n\n"
                                      "============================\n"
                                      "🔹 *Simple function:*\n"
                                      "```cpp\nvoid sayHello\\(\\) {\\n    cout << \"Hello, world!\" << endl;\\n}\\n\\nint main\\(\\) {\\n    sayHello\\(\\);\\n    return 0;\\n}\\n```\n"
                                      "— The keyword `void` means the function returns nothing.\n"
                                      "— Call the function by its name.\n\n"
                                      "============================\n"
                                      "🔹 *Function with parameters:*\n"
                                      "```cpp\nvoid greet\\(string name\\) {\\n    cout << \"Hello, \" << name << endl;\\n}\\n\\nint main\\(\\) {\\n    greet\\(\"Alice\"\\);\\n    return 0;\\n}\\n```\n"
                                      "— You can pass data into the function.\n"
                                      "— Parameters are specified in parentheses in the declaration.\n\n"
                                      "============================\n"
                                      "🔹 *Function with return value:*\n"
                                      "```cpp\nint square\\(int x\\) {\\n    return x * x;\\n}\\n\\nint main\\(\\) {\\n    int res = square\\(5\\);\\n    cout << res;\\n    return 0;\\n}\\n```\n"
                                      "— Specify the return type (e.g., `int`).\n"
                                      "— Use `return` to send back the result.\n\n"
                                      "============================\n"
                                      "✅ *Why are functions important?*\n"
                                      "- Code becomes compact and clear\n"
                                      "- You can reuse the same code\n"
                                      "- The program is easy to split into parts\n\n"
                                      "💡 Try writing your own function that sums two numbers and returns the result!\n"
                                      "Functions are the foundation of good C++ code! 🚀",
                                      reply_markup=reply_markup)
    elif query.data == "crchemole":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="amburanmal")],
                    [InlineKeyboardButton("last chapter", callback_data="zinanzinsnedeji")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++: Strings*\n\n"
                                      "🔹 *What is a string?*\n"
                                      "— It’s a sequence of characters, like a name or phrase.\n"
                                      "— In C++, you can use a char array or the `std::string` class.\n\n"
                                      "============================\n"
                                      "🔹 *String as a char array:*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\\n```\n"
                                      "🔸 The `\\0` character is automatically added at the end — it marks the string’s end.\n"
                                      "🔸 The array size must be larger than the string length.\n\n"
                                      "============================\n"
                                      "🔹 *Strings with `std::string`:*\n"
                                      "```cpp\n#include <string>\\n\\nstd::string city = \"Baku\";\\n```\n"
                                      "— This method is easier and safer.\n\n"
                                      "============================\n"
                                      "🔹 *Basic operations:*\n"
                                      "```cpp\nstd::string name = \"Tom\";\\n\\n"
                                      "cout << name << endl;         // Print the string\\n"
                                      "cout << name.length() << endl; // String length\\n"
                                      "name += \" Hardy\";             // Concatenation\\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *User input for string:*\n"
                                      "```cpp\nstd::string userName;\\ncout << \"Enter name: \";\\ncin >> userName;\\n```\n"
                                      "❗ `cin` reads input until the first space. For a full phrase:\n"
                                      "```cpp\nstd::string fullName;\\ngetline(cin, fullName);\\n```\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- `std::string` is easier and safer than `char` arrays\n"
                                      "- You can easily concatenate, measure length, and find characters\n"
                                      "- For Cyrillic or other unicode, encoding setup may be needed\n\n"
                                      "💡 Strings are the foundation for working with text, forms, messages!\n"
                                      "Try creating a string and printing it! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "jvones":
        keyboard = [[InlineKeyboardButton("⚙ Start", callback_data="lexust")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Let's start!\nChapter 1:", reply_markup=reply_markup)
    elif query.data == "lexust":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="lex")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript Setup and Start:*\n\n"
                                      "🔹 *Step 1: Download an editor*\n"
                                      "[Download Visual Studio Code](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Step 2: Check Node\\.js installation*\n"
                                      "[Download Node\\.js](https://nodejs.org/)\n"
                                      "— Install and check version:\n"
                                      "`node --version`\n\n"
                                      "🔹 *Step 3: Simple code:*\n"
                                      "Create a file `main.js` with code:\n"
                                      "```js\nconsole.log\\(\"Hello, world!\"\\);\\n```\n"
                                      "Run it in the terminal:\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript is your first step to creating websites, bots, and apps!*",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "lex":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="lextu")],
                    [InlineKeyboardButton("last chapter", callback_data="tiutuosiojimvpsiieee")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Variables and Data Types*\n\n"
                                      "🔹 *What is a variable?*\n"
                                      "— It’s a named container for data.\n"
                                      "— Declared with `let`, `const`, or the older `var` keyword.\n\n"
                                      "🔹 *Examples:*\n"
                                      "`let age = 15;`\n"
                                      "`const pi = 3.14;`\n"
                                      "`let name = \"Tom\";`\n"
                                      "`let isOnline = true;`\n\n"
                                      "🔹 *Console output:*\n"
                                      "```js\nlet age = 15;\\nlet name = \"Tom\";\\nconsole.log\\(\"Name:\\\", name\\);\\nconsole.log\\(\"Age:\\\", age\\);\\n```\n"
                                      "💡 *Tip:* Use `const` for values that don’t change and `let` for variables that can change."
                                      ,
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "tiutuosiojimvpsiieee":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="lex")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript Setup and Start:*\n\n"
                                      "🔹 *Step 1: Download an editor*\n"
                                      "[Download Visual Studio Code](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Step 2: Check Node\\.js installation*\n"
                                      "[Download Node\\.js](https://nodejs.org/)\n"
                                      "— Install and check version:\n"
                                      "`node --version`\n\n"
                                      "🔹 *Step 3: Simple code:*\n"
                                      "Create a file `main.js` with code:\n"
                                      "```js\nconsole.log\\(\"Hello, world!\"\\);\\n```\n"
                                      "Run it in the terminal:\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript is your first step to creating websites, bots, and apps!*",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )

    elif query.data == "lextu":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="porsche")],
                    [InlineKeyboardButton("last chapter", callback_data="marlonmogspercentofpeople")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Conditions and Comparisons*\n\n"
                                      "🔹 *What is a condition?*\n"
                                      "— It’s a check where the code inside the block runs if the expression evaluates to `true`.\n"
                                      "— In JavaScript, this is done with the `if` statement.\n\n"
                                      "🔹 *Example:*\n"
                                      "```js\nlet age = 18;\\nif \\(age >= 18\\) {\\n    console.log\\(\"Access granted\"\\);\\n} else {\\n    console.log\\(\"Access denied\"\\);\\n}\\n```\n\n"
                                      "🔹 *Comparison operators:*\n"
                                      "`==` — compares by value (can convert types)\n"
                                      "`===` — strict comparison (checks both type and value)\n"
                                      "`!=` — not equal (by value)\n"
                                      "`!==` — strict not equal (by type and value)\n"
                                      "`>` — greater than\n"
                                      "`<` — less than\n"
                                      "`>=` — greater or equal\n"
                                      "`<=` — less or equal\n\n"
                                      "💡 *Important:* It’s better to use `===` and `!==` to avoid unexpected errors caused by type coercion."
                                      ,
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "marlonmogspercentofpeople":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="lextu")],
                    [InlineKeyboardButton("last chapter", callback_data="tiutuosiojimvpsiieee")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Variables and Data Types*\n\n"
                                      "🔹 *What is a variable?*\n"
                                      "— It’s a named container for data.\n"
                                      "— Declared with `let`, `const`, or the older `var` keyword.\n\n"
                                      "🔹 *Examples:*\n"
                                      "`let age = 15;`\n"
                                      "`const pi = 3.14;`\n"
                                      "`let name = \"Tom\";`\n"
                                      "`let isOnline = true;`\n\n"
                                      "🔹 *Console output:*\n"
                                      "```js\nlet age = 15;\\nlet name = \"Tom\";\\nconsole.log\\(\"Name:\\\", name\\);\\nconsole.log\\(\"Age:\\\", age\\);\\n```\n"
                                      "💡 *Tip:* Use `const` for values that don’t change and `let` for variables that can change."
                                      ,
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )

    elif query.data == "porsche":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="ferrari")],
                    [InlineKeyboardButton("last chapter", callback_data="popaodkpaskpopofpajmamam")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Logical Operators*\n\n"
                                      "🔹 *What are they?*\n"
                                      "— Logical operators help combine conditions.\n"
                                      "— They allow checking multiple conditions at once.\n\n"
                                      "🔹 *Types of logical operators:*\n"
                                      "`&&` — AND (both conditions must be true)\n"
                                      "`||` — OR (at least one condition is true)\n"
                                      "`!` — NOT (negation, flips the value)\n\n"
                                      "🔹 *Examples:*\n"
                                      "```js\nlet age = 20;\\nlet hasPassport = true;\\n\nif \\(age >= 18 && hasPassport\\) {\\n    console.log\\(\"Access granted\"\\);\\n} else {\\n    console.log\\(\"Access denied\"\\);\\n}\\n```\n\n"
                                      "```js\nlet isOnline = false;\\nif \\(!isOnline\\) {\\n    console.log\\(\"User is offline\"\\);\\n}\\n```\n\n"
                                      "💡 *Important:* Parentheses are evaluated first, then operators.",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )
    elif query.data == "popaodkpaskpopofpajmamam":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="porsche")],
                    [InlineKeyboardButton("last chapter", callback_data="marlonmogspercentofpeople")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Conditions and Comparisons*\n\n"
                                      "🔹 *What is a condition?*\n"
                                      "— It’s a check where the code inside the block runs if the expression evaluates to `true`.\n"
                                      "— In JavaScript, this is done with the `if` statement.\n\n"
                                      "🔹 *Example:*\n"
                                      "```js\nlet age = 18;\\nif \\(age >= 18\\) {\\n    console.log\\(\"Access granted\"\\);\\n} else {\\n    console.log\\(\"Access denied\"\\);\\n}\\n```\n\n"
                                      "🔹 *Comparison operators:*\n"
                                      "`==` — compares by value (can convert types)\n"
                                      "`===` — strict comparison (checks both type and value)\n"
                                      "`!=` — not equal (by value)\n"
                                      "`!==` — strict not equal (by type and value)\n"
                                      "`>` — greater than\n"
                                      "`<` — less than\n"
                                      "`>=` — greater or equal\n"
                                      "`<=` — less or equal\n\n"
                                      "💡 *Important:* It’s better to use `===` and `!==` to avoid unexpected errors caused by type coercion."
                                      ,
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )

    elif query.data == "ferrari":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="dod")],
                    [InlineKeyboardButton("last chapter", callback_data="viytisuximizvodi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript: Loops*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— It’s a way to repeat a block of code multiple times.\n"
                                      "— Used for working with arrays, repetitive tasks, and automation.\n\n"
                                      "============================\n"
                                      "🔹 *for loop*\n"
                                      "```js\nfor \\(let i = 0; i < 5; i\\+\\+\\) {\\n    console.log\\(i\\);\\n}\\n```\n"
                                      "— Prints numbers from 0 to 4.\n"
                                      "`i++` means increase the counter by 1 each time.\n\n"
                                      "============================\n"
                                      "🔹 *while loop*\n"
                                      "```js\nlet x = 0;\\nwhile \\(x < 3\\) {\\n    console.log\\(x\\);\\n    x\\+\\+;\\n}\\n```\n"
                                      "— Runs the code while `x < 3`.\n\n"
                                      "============================\n"
                                      "🔹 *do...while loop*\n"
                                      "```js\nlet y = 0;\\ndo {\\n    console.log\\(y\\);\\n    y\\+\\+;\\n} while \\(y < 2\\);\\n```\n"
                                      "— Executes the code at least once even if the condition is false.\n\n"
                                      "============================\n"
                                      "🔹 *Example: looping over an array*\n"
                                      "```js\nlet fruits = \\[\"🍎\", \"🍌\", \"🍇\"\\];\\nfor \\(let i = 0; i < fruits.length; i\\+\\+\\) {\\n    console.log\\(fruits\\[i\\]\\);\\n}\\n```\n"
                                      "— Iterates over all elements in the array.\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- Easy to create an infinite loop (don’t forget to update the counter!)\n"
                                      "- Use `break` to exit the loop\n"
                                      "- `continue` skips the current iteration\n\n"
                                      "💡 Loops are a key tool for working with data structures and automating tasks!\n"
                                      "Try writing a loop that prints numbers from 10 down to 1 in reverse order! 🚀",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "viytisuximizvodi":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="ferrari")],
                    [InlineKeyboardButton("last chapter", callback_data="popaodkpaskpopofpajmamam")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Logical Operators*\n\n"
                                      "🔹 *What are they?*\n"
                                      "— Logical operators help combine conditions.\n"
                                      "— They allow checking multiple conditions at once.\n\n"
                                      "🔹 *Types of logical operators:*\n"
                                      "`&&` — AND (both conditions must be true)\n"
                                      "`||` — OR (at least one condition is true)\n"
                                      "`!` — NOT (negation, flips the value)\n\n"
                                      "🔹 *Examples:*\n"
                                      "```js\nlet age = 20;\\nlet hasPassport = true;\\n\nif \\(age >= 18 && hasPassport\\) {\\n    console.log\\(\"Access granted\"\\);\\n} else {\\n    console.log\\(\"Access denied\"\\);\\n}\\n```\n\n"
                                      "```js\nlet isOnline = false;\\nif \\(!isOnline\\) {\\n    console.log\\(\"User is offline\"\\);\\n}\\n```\n\n"
                                      "💡 *Important:* Parentheses are evaluated first, then operators.",
                                      parse_mode="Markdown", reply_markup=reply_markup
                                      )

    elif query.data == "dod":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="sremon")],
                    [InlineKeyboardButton("last chapter", callback_data="nunutireihgtj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Functions explained*\n\n"
                                      "🔹 *What is a function?*\n"
                                      "— A named piece of code that does a specific job.\n"
                                      "— You can call it many times without copying code.\n"
                                      "— It’s the base of structured programming.\n\n"
                                      "🔹 *Why use functions?*\n"
                                      "✔ Avoid repeating code\n"
                                      "✔ Split program into logical parts\n"
                                      "✔ Take inputs \\(arguments\\) and return results\n\n"
                                      "🔹 *Simple function example:*\n"
                                      "```js\n"
                                      "function sayHello() {\n"
                                      "  console.log(\"Hello!\"\\);\n"
                                      "}\n\n"
                                      "sayHello\\(\\); // call function\n"
                                      "```\n"
                                      "💡 `sayHello` prints \"Hello!\" every time it’s called.\n\n"
                                      "🔹 *Function with parameters:*\n"
                                      "```js\n"
                                      "function greet\\(name\\) {\n"
                                      "  console.log\\(\"Hello, \" + name\\);\n"
                                      "}\n\n"
                                      "greet\\(\"Tom\"\\);\n"
                                      "greet\\(\"Anna\"\\);\n"
                                      "```\n"
                                      "💡 `name` lets you send different values to the function.\n\n"
                                      "🔹 *Function that returns a value:*\n"
                                      "```js\n"
                                      "function square\\(number\\) {\n"
                                      "  return number * number;\n"
                                      "}\n\n"
                                      "console.log\\(square\\(4\\)\\); // 16\n"
                                      "```\n"
                                      "💡 `return` gives back the result to use later.\n\n"
                                      "🔹 *Remember:*\n"
                                      "✔ Call functions only after declaring them\n"
                                      "✔ Code inside runs only when called\n"
                                      "✔ You can pass many arguments\n\n"
                                      "Functions make your code cleaner, easier, and flexible!",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "nunutireihgtj":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="dod")],
                    [InlineKeyboardButton("last chapter", callback_data="viytisuximizvodi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript: Loops*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— It’s a way to repeat a block of code multiple times.\n"
                                      "— Used for working with arrays, repetitive tasks, and automation.\n\n"
                                      "============================\n"
                                      "🔹 *for loop*\n"
                                      "```js\nfor \\(let i = 0; i < 5; i\\+\\+\\) {\\n    console.log\\(i\\);\\n}\\n```\n"
                                      "— Prints numbers from 0 to 4.\n"
                                      "`i++` means increase the counter by 1 each time.\n\n"
                                      "============================\n"
                                      "🔹 *while loop*\n"
                                      "```js\nlet x = 0;\\nwhile \\(x < 3\\) {\\n    console.log\\(x\\);\\n    x\\+\\+;\\n}\\n```\n"
                                      "— Runs the code while `x < 3`.\n\n"
                                      "============================\n"
                                      "🔹 *do...while loop*\n"
                                      "```js\nlet y = 0;\\ndo {\\n    console.log\\(y\\);\\n    y\\+\\+;\\n} while \\(y < 2\\);\\n```\n"
                                      "— Executes the code at least once even if the condition is false.\n\n"
                                      "============================\n"
                                      "🔹 *Example: looping over an array*\n"
                                      "```js\nlet fruits = \\[\"🍎\", \"🍌\", \"🍇\"\\];\\nfor \\(let i = 0; i < fruits.length; i\\+\\+\\) {\\n    console.log\\(fruits\\[i\\]\\);\\n}\\n```\n"
                                      "— Iterates over all elements in the array.\n\n"
                                      "============================\n"
                                      "✅ *Important to remember:*\n"
                                      "- Easy to create an infinite loop (don’t forget to update the counter!)\n"
                                      "- Use `break` to exit the loop\n"
                                      "- `continue` skips the current iteration\n\n"
                                      "💡 Loops are a key tool for working with data structures and automating tasks!\n"
                                      "Try writing a loop that prints numbers from 10 down to 1 in reverse order! 🚀",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "sremon":
        keyboard = [[InlineKeyboardButton("last chapter", callback_data="rioioirrrroeoirpire")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *JavaScript: Objects*\n\n"
                                      "🔹 *What is an object?*\n"
                                      "— A structure to store related data and functions.\n"
                                      "— Consists of \"key: value\" pairs.\n\n"
                                      "============================\n"
                                      "🔹 *Simple object example:*\n"
                                      "```js\n"
                                      "let person = {\n"
                                      "  name: \"Tom\",\n"
                                      "  age: 25,\n"
                                      "  isStudent: true\n"
                                      "};\n"
                                      "```\n"
                                      "🔸 Access properties:\n"
                                      "`person.name` → \"Tom\"\n"
                                      "`person[\"age\"]` → 25\n\n"
                                      "============================\n"
                                      "🔹 *Object with a method:*\n"
                                      "```js\n"
                                      "let car = {\n"
                                      "  brand: \"Toyota\",\n"
                                      "  start: function() {\n"
                                      "    console.log(\"Engine started\");\n"
                                      "  }\n"
                                      "};\n\n"
                                      "car.start();\n"
                                      "```\n"
                                      "============================\n"
                                      "✅ *Why use objects?*\n"
                                      "- Store complex data together\n"
                                      "- Model real-world entities\n"
                                      "- Essential for DOM, APIs, games\n\n"
                                      "💡 Try creating an object \"phone\" with properties \"model\", \"year\" and a method \"call()\"!",
                                      parse_mode="Markdown",reply_markup = reply_markup )
    elif query.data == "rioioirrrroeoirpire":
        keyboard = [[InlineKeyboardButton("next chapter➡️", callback_data="sremon")],
                    [InlineKeyboardButton("last chapter", callback_data="nunutireihgtj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Functions explained*\n\n"
                                      "🔹 *What is a function?*\n"
                                      "— A named piece of code that does a specific job.\n"
                                      "— You can call it many times without copying code.\n"
                                      "— It’s the base of structured programming.\n\n"
                                      "🔹 *Why use functions?*\n"
                                      "✔ Avoid repeating code\n"
                                      "✔ Split program into logical parts\n"
                                      "✔ Take inputs \\(arguments\\) and return results\n\n"
                                      "🔹 *Simple function example:*\n"
                                      "```js\n"
                                      "function sayHello() {\n"
                                      "  console.log(\"Hello!\"\\);\n"
                                      "}\n\n"
                                      "sayHello\\(\\); // call function\n"
                                      "```\n"
                                      "💡 `sayHello` prints \"Hello!\" every time it’s called.\n\n"
                                      "🔹 *Function with parameters:*\n"
                                      "```js\n"
                                      "function greet\\(name\\) {\n"
                                      "  console.log\\(\"Hello, \" + name\\);\n"
                                      "}\n\n"
                                      "greet\\(\"Tom\"\\);\n"
                                      "greet\\(\"Anna\"\\);\n"
                                      "```\n"
                                      "💡 `name` lets you send different values to the function.\n\n"
                                      "🔹 *Function that returns a value:*\n"
                                      "```js\n"
                                      "function square\\(number\\) {\n"
                                      "  return number * number;\n"
                                      "}\n\n"
                                      "console.log\\(square\\(4\\)\\); // 16\n"
                                      "```\n"
                                      "💡 `return` gives back the result to use later.\n\n"
                                      "🔹 *Remember:*\n"
                                      "✔ Call functions only after declaring them\n"
                                      "✔ Code inside runs only when called\n"
                                      "✔ You can pass many arguments\n\n"
                                      "Functions make your code cleaner, easier, and flexible!",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "toomycas":
        keyboard = [[InlineKeyboardButton("☕ Start learning Java", callback_data="office")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Java", reply_markup=reply_markup)
    elif query.data == "office":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="siren")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java: Installation & First Project*\n\n"
                                      "🔹 *Step 1: Download and Install JDK*\n"
                                      "[🔗 Official Download Page](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— Choose the Java SE Development Kit (JDK) for your operating system\n"
                                      "— During installation, check `Add JAVA to PATH` (if available)\n\n"
                                      "🔹 *Step 2: Verify Installation*\n"
                                      "Open your terminal or command prompt and type:\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "If versions appear, installation was successful!\n\n"
                                      "🔹 *Step 3: Install an IDE (Development Tool)*\n"
                                      "✅ [IntelliJ IDEA Community (Recommended)](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + Java Extension](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Step 4: Write Your First Java Code!*\n"
                                      "Create a file named `Main.java` and enter:\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "Then run it in your terminal:\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ Expected output: `Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *You’re ready to start learning Java!*\n"
                                      "Next up: variables, conditionals, loops, functions, and object-oriented programming!\n\n"
                                      "👇 Click the button below to start the next lesson!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "siren":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="style")],
                    [InlineKeyboardButton("last chapter", callback_data="prptprppeprepeppafroiguhtgksahs")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Variables and Data Types*\n\n"
                                      "🔹 *What is a variable?*\n"
                                      "— A variable is a name used to store data.\n"
                                      "— Each variable must be defined with a specific data type.\n\n"
                                      "🔹 *Basic data types:*\n"
                                      "- `int`: integers, e.g. `42`\n"
                                      "- `double`: decimals, e.g. `3.14`\n"
                                      "- `char`: single character, e.g. `'A'`\n"
                                      "- `boolean`: logic values, `true` or `false`\n"
                                      "- `String`: text, e.g. `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *Declaring and using variables:*\n"
                                      "```java\nint age = 18;\ndouble pi = 3.14;\nchar grade = 'A';\nboolean isStudent = true;\nString name = \"Tom\";\n```\n\n"
                                      "🔸 Use `System.out.println()` to print variables:\n"
                                      "```java\nSystem.out.println(name);\nSystem.out.println(age);\n```\n"
                                      "🔸 Output:\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *Tips:*\n"
                                      "- Java is a statically typed language, so every variable needs a type.\n"
                                      "- Variable names are case-sensitive: `Name` ≠ `name`\n"
                                      "- Use clear names: `int n = 5;` ❌, `int score = 5;` ✅\n\n"
                                      "💡 Try declaring your own variables and print them using `System.out.println()`!",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "prptprppeprepeppafroiguhtgksahs":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="siren")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java: Installation & First Project*\n\n"
                                      "🔹 *Step 1: Download and Install JDK*\n"
                                      "[🔗 Official Download Page](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— Choose the Java SE Development Kit (JDK) for your operating system\n"
                                      "— During installation, check `Add JAVA to PATH` (if available)\n\n"
                                      "🔹 *Step 2: Verify Installation*\n"
                                      "Open your terminal or command prompt and type:\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "If versions appear, installation was successful!\n\n"
                                      "🔹 *Step 3: Install an IDE (Development Tool)*\n"
                                      "✅ [IntelliJ IDEA Community (Recommended)](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + Java Extension](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Step 4: Write Your First Java Code!*\n"
                                      "Create a file named `Main.java` and enter:\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "Then run it in your terminal:\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ Expected output: `Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *You’re ready to start learning Java!*\n"
                                      "Next up: variables, conditionals, loops, functions, and object-oriented programming!\n\n"
                                      "👇 Click the button below to start the next lesson!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "style":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="for")],
                    [InlineKeyboardButton("last chapter", callback_data="ooptoripitprittoiprt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Java: Conditional Statements (if, else, else if)*\n\n"
                                      "🔹 *What is a conditional statement?*\n"
                                      "— It lets the program run different code depending on a condition.\n\n"
                                      "============================\n"
                                      "🔹 *Example code:*\n"
                                      "```java\n"
                                      "if (age >= 18) {\n"
                                      "    System.out.println(\"You are an adult\");\n"
                                      "} else if (age >= 14) {\n"
                                      "    System.out.println(\"You are a teenager\");\n"
                                      "} else {\n"
                                      "    System.out.println(\"You are a child\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Comparison operators:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
                                      "🔹 *Logical operators:* `&&` (and), `||` (or), `!` (not)\n\n"
                                      "✅ *Try this:*\n"
                                      "Write a program that prints a message based on a person’s age!",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "ooptoripitprittoiprt":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="style")],
                    [InlineKeyboardButton("last chapter", callback_data="prptprppeprepeppafroiguhtgksahs")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Variables and Data Types*\n\n"
                                      "🔹 *What is a variable?*\n"
                                      "— A variable is a name used to store data.\n"
                                      "— Each variable must be defined with a specific data type.\n\n"
                                      "🔹 *Basic data types:*\n"
                                      "- `int`: integers, e.g. `42`\n"
                                      "- `double`: decimals, e.g. `3.14`\n"
                                      "- `char`: single character, e.g. `'A'`\n"
                                      "- `boolean`: logic values, `true` or `false`\n"
                                      "- `String`: text, e.g. `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *Declaring and using variables:*\n"
                                      "```java\nint age = 18;\ndouble pi = 3.14;\nchar grade = 'A';\nboolean isStudent = true;\nString name = \"Tom\";\n```\n\n"
                                      "🔸 Use `System.out.println()` to print variables:\n"
                                      "```java\nSystem.out.println(name);\nSystem.out.println(age);\n```\n"
                                      "🔸 Output:\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *Tips:*\n"
                                      "- Java is a statically typed language, so every variable needs a type.\n"
                                      "- Variable names are case-sensitive: `Name` ≠ `name`\n"
                                      "- Use clear names: `int n = 5;` ❌, `int score = 5;` ✅\n\n"
                                      "💡 Try declaring your own variables and print them using `System.out.println()`!",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "for":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="men")],
                    [InlineKeyboardButton("last chapter", callback_data="crchcscddddddddddsdlkjnfhkl")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: Loops*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— A loop lets you run a block of code multiple times.\n"
                                      "— Useful for repetition, automation, and working with data.\n\n"
                                      "============================\n"
                                      "🔹 *for loop example:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— Prints numbers from 0 to 4.\n\n"
                                      "============================\n"
                                      "🔹 *while loop example:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n"
                                      "— Repeats while the condition is true.\n\n"
                                      "============================\n"
                                      "🔹 *do...while loop example:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— Runs the block at least once, even if condition is false.\n\n"
                                      "============================\n"
                                      "✅ *Good to know:*\n"
                                      "- Use `break` to exit a loop early\n"
                                      "- Use `continue` to skip to the next iteration\n"
                                      "- Avoid infinite loops by updating conditions\n\n"
                                      "💡 Try writing a loop that counts down from 10 to 1!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "crchcscddddddddddsdlkjnfhkl":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="for")],
                    [InlineKeyboardButton("last chapter", callback_data="ooptoripitprittoiprt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Java: Conditional Statements (if, else, else if)*\n\n"
                                      "🔹 *What is a conditional statement?*\n"
                                      "— It lets the program run different code depending on a condition.\n\n"
                                      "============================\n"
                                      "🔹 *Example code:*\n"
                                      "```java\n"
                                      "if (age >= 18) {\n"
                                      "    System.out.println(\"You are an adult\");\n"
                                      "} else if (age >= 14) {\n"
                                      "    System.out.println(\"You are a teenager\");\n"
                                      "} else {\n"
                                      "    System.out.println(\"You are a child\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Comparison operators:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
                                      "🔹 *Logical operators:* `&&` (and), `||` (or), `!` (not)\n\n"
                                      "✅ *Try this:*\n"
                                      "Write a program that prints a message based on a person’s age!",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "men":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="brands")],
                    [InlineKeyboardButton("last chapter", callback_data="potipotipoti")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Arrays*\n\n"
                                      "🔹 *What is an array?*\n"
                                      "— An array is a collection of elements of the same type, stored in sequence in memory.\n"
                                      "— Each element has an index (starting from 0).\n\n"
                                      "============================\n"
                                      "🔹 *Creating an integer array:*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— This creates an array of 5 integers.\n\n"
                                      "🔸 Accessing elements:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Print all elements using a for loop:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— `numbers.length` gives the size of the array.\n\n"
                                      "============================\n"
                                      "🔹 *Get input from the user:*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— This stores 3 numbers entered by the user.\n\n"
                                      "============================\n"
                                      "✅ *Key Reminders:*\n"
                                      "- Indexes go from `0` to `n - 1`\n"
                                      "- Array size is fixed\n"
                                      "- Going out of bounds causes an error (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 Arrays are the foundation of data structures, sorting, and algorithms!\n"
                                      "Try creating your own array and printing its elements!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "potipotipoti":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="men")],
                    [InlineKeyboardButton("last chapter", callback_data="crchcscddddddddddsdlkjnfhkl")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: Loops*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— A loop lets you run a block of code multiple times.\n"
                                      "— Useful for repetition, automation, and working with data.\n\n"
                                      "============================\n"
                                      "🔹 *for loop example:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— Prints numbers from 0 to 4.\n\n"
                                      "============================\n"
                                      "🔹 *while loop example:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n"
                                      "— Repeats while the condition is true.\n\n"
                                      "============================\n"
                                      "🔹 *do...while loop example:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— Runs the block at least once, even if condition is false.\n\n"
                                      "============================\n"
                                      "✅ *Good to know:*\n"
                                      "- Use `break` to exit a loop early\n"
                                      "- Use `continue` to skip to the next iteration\n"
                                      "- Avoid infinite loops by updating conditions\n\n"
                                      "💡 Try writing a loop that counts down from 10 to 1!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "brands":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="its")],
                    [InlineKeyboardButton("last chapter", callback_data="kkhkhhkkjkjhkhkoji")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java: Methods (Functions)*\n\n"
                                      "🔹 *What is a method?*\n"
                                      "— A method is a block of code that performs a specific task.\n"
                                      "— You can call it multiple times without rewriting the code.\n\n"
                                      "============================\n"
                                      "🔹 *Why use methods?*\n"
                                      "✔️ Avoid code repetition\n"
                                      "✔️ Makes the program clearer and easier to maintain\n"
                                      "✔️ Can accept parameters and return results\n\n"
                                      "============================\n"
                                      "🔹 *Simple example:*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"Hello!\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // Call the method\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— The `sayHello` method prints \"Hello!\".\n\n"
                                      "============================\n"
                                      "🔹 *Method with parameters:*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"Hello, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"Alice\");\n"
                                      "```\n"
                                      "— Parameters make methods more flexible.\n\n"
                                      "============================\n"
                                      "🔹 *Method with return value:*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— Use `return` to send back the result.\n\n"
                                      "============================\n"
                                      "✅ *Remember:*\n"
                                      "- All methods must be inside a class\n"
                                      "- `main()` is the program’s entry point\n"
                                      "- `void` means no value is returned\n\n"
                                      "💡 Try writing your own method to print your name or add two numbers! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "kkhkhhkkjkjhkhkoji":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="brands")],
                    [InlineKeyboardButton("last chapter", callback_data="potipotipoti")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Arrays*\n\n"
                                      "🔹 *What is an array?*\n"
                                      "— An array is a collection of elements of the same type, stored in sequence in memory.\n"
                                      "— Each element has an index (starting from 0).\n\n"
                                      "============================\n"
                                      "🔹 *Creating an integer array:*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— This creates an array of 5 integers.\n\n"
                                      "🔸 Accessing elements:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Print all elements using a for loop:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— `numbers.length` gives the size of the array.\n\n"
                                      "============================\n"
                                      "🔹 *Get input from the user:*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— This stores 3 numbers entered by the user.\n\n"
                                      "============================\n"
                                      "✅ *Key Reminders:*\n"
                                      "- Indexes go from `0` to `n - 1`\n"
                                      "- Array size is fixed\n"
                                      "- Going out of bounds causes an error (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 Arrays are the foundation of data structures, sorting, and algorithms!\n"
                                      "Try creating your own array and printing its elements!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "its":
        keyboard = [[InlineKeyboardButton("last chapter", callback_data="baybaybygridlskdfrgreoji")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🏗️ *Java: Classes & Objects*\n\n"
                                      "🔹 *What is a class?*\n"
                                      "— A class is a blueprint for creating objects.\n"
                                      "— It defines the properties (data) and behaviors (methods) of objects.\n\n"
                                      "🔹 *What is an object?*\n"
                                      "— An instance created based on a class; the actual member in the program.\n\n"
                                      "============================\n"
                                      "🔹 *Simple example:*\n"
                                      "```java\n"
                                      "public class Dog {\n"
                                      "    String name;\n"
                                      "    int age;\n\n"
                                      "    void bark() {\n"
                                      "        System.out.println(name + \": Woof!\" );\n"
                                      "    }\n"
                                      "}\n\n"
                                      "public class Main {\n"
                                      "    public static void main(String[] args) {\n"
                                      "        Dog myDog = new Dog();\n"
                                      "        myDog.name = \"Blackie\";\n"
                                      "        myDog.age = 3;\n"
                                      "        myDog.bark();\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— The class `Dog` has two properties and one method.\n"
                                      "— `myDog` is an object of class `Dog`, which can call methods and set properties.\n\n"
                                      "============================\n"
                                      "🔹 *Important concepts:*\n"
                                      "- Class names should start with uppercase letters: `Person`, `Car`, `Animal`, etc.\n"
                                      "- Use `new` to create objects\n"
                                      "- Methods can access the object’s properties\n\n"
                                      "✅ *Classes and objects are the core of Java*\n"
                                      "— Almost all Java programs are designed around objects!\n\n"
                                      "💡 Next, we will dive into constructors, encapsulation, inheritance, and polymorphism! 🚀",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "baybaybygridlskdfrgreoji":
        keyboard = [[InlineKeyboardButton("Next Chapter ➡", callback_data="its")],
                    [InlineKeyboardButton("last chapter", callback_data="kkhkhhkkjkjhkhkoji")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java: Methods (Functions)*\n\n"
                                      "🔹 *What is a method?*\n"
                                      "— A method is a block of code that performs a specific task.\n"
                                      "— You can call it multiple times without rewriting the code.\n\n"
                                      "============================\n"
                                      "🔹 *Why use methods?*\n"
                                      "✔️ Avoid code repetition\n"
                                      "✔️ Makes the program clearer and easier to maintain\n"
                                      "✔️ Can accept parameters and return results\n\n"
                                      "============================\n"
                                      "🔹 *Simple example:*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"Hello!\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // Call the method\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— The `sayHello` method prints \"Hello!\".\n\n"
                                      "============================\n"
                                      "🔹 *Method with parameters:*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"Hello, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"Alice\");\n"
                                      "```\n"
                                      "— Parameters make methods more flexible.\n\n"
                                      "============================\n"
                                      "🔹 *Method with return value:*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— Use `return` to send back the result.\n\n"
                                      "============================\n"
                                      "✅ *Remember:*\n"
                                      "- All methods must be inside a class\n"
                                      "- `main()` is the program’s entry point\n"
                                      "- `void` means no value is returned\n\n"
                                      "💡 Try writing your own method to print your name or add two numbers! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "huggywugg":
        keyboard = [[InlineKeyboardButton("Let's begin!\n""*Chapter 1:*", callback_data="yveskarlina")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("<<>>", reply_markup=reply_markup)
    elif query.data == "yveskarlina":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="legsaca")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *Installing C and Setting Up in CLion IDE*\n\n"
                                      "🔹 *Step 1: Download MinGW Compiler*\n"
                                      "[Download MinGW](https://sourceforge.net/projects/mingw/) — install `gcc` and add the `bin` folder to your system PATH\n\n"
                                      "🔹 *Step 2: Download CLion IDE*\n"
                                      "[Download CLion](https://www.jetbrains.com/clion/download/) — install the Community or Trial version\n\n"
                                      "🔹 *Step 3: Verify the Installation*\n"
                                      "Open terminal and run:\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *Step 4: Write a Simple C Program*\n"
                                      "Create a `main.c` file with the following code:\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Step 5: Compile and Run the Program*\n"
                                      "In the terminal, run:\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "Then run the program:\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *Check the Output:*\n"
                                      "You should see:\n"
                                      "```\nHello, world!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "legsaca":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="armsakina")],
                    [InlineKeyboardButton("last chapter", callback_data="hastworexes")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Variables and Data Types in C*\n\n"
                                      "🔹 *What is a variable?*\n"
                                      "— A name used to store data in memory.\n"
                                      "— Each variable has a type that defines what kind of data it holds.\n\n"
                                      "🔹 *Common data types:*\n"
                                      "- `int` — integers, e.g.: `42`\n"
                                      "- `float` — floating-point numbers, e.g.: `3.14`\n"
                                      "- `char` — a single character, e.g.: `'A'`\n"
                                      "- `double` — more precise floating-point numbers\n\n"
                                      "============================\n"
                                      "🔹 *Declaring variables:*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *Printing to the screen:*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"Age: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Try it yourself:* declare some variables and print their values!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "hastworexes":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="legsaca")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *Installing C and Setting Up in CLion IDE*\n\n"
                                      "🔹 *Step 1: Download MinGW Compiler*\n"
                                      "[Download MinGW](https://sourceforge.net/projects/mingw/) — install `gcc` and add the `bin` folder to your system PATH\n\n"
                                      "🔹 *Step 2: Download CLion IDE*\n"
                                      "[Download CLion](https://www.jetbrains.com/clion/download/) — install the Community or Trial version\n\n"
                                      "🔹 *Step 3: Verify the Installation*\n"
                                      "Open terminal and run:\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *Step 4: Write a Simple C Program*\n"
                                      "Create a `main.c` file with the following code:\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Step 5: Compile and Run the Program*\n"
                                      "In the terminal, run:\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "Then run the program:\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *Check the Output:*\n"
                                      "You should see:\n"
                                      "```\nHello, world!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "armsakina":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="sirenseacreaturrank")],
                    [InlineKeyboardButton("last chapter", callback_data="uusuasdaudodsuodaioasdau")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Operators and Expressions in C*\n\n"
                                      "🔹 *What is an operator?*\n"
                                      "— A symbol or combination of symbols that perform operations on data.\n\n"
                                      "🔹 *Types of operators:*\n"
                                      "- Arithmetic: `+`, `-`, `*`, `/`, `%`\n"
                                      "- Assignment: `=`, `+=`, `-=`, `*=`, etc.\n"
                                      "- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                                      "- Logical: `&&`, `||`, `!`\n\n"
                                      "============================\n"
                                      "🔹 *Example of arithmetic operations:*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int sum = a + b;       // 13\n"
                                      "int diff = a - b;      // 7\n"
                                      "int product = a * b;   // 30\n"
                                      "int quotient = a / b;  // 3\n"
                                      "int remainder = a % b; // 1\n"
                                      "```\n\n"
                                      "🔹 *Example of comparison and logic:*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x is less than y and y is positive\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Try it yourself:* write expressions using different operators and print the results!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "uusuasdaudodsuodaioasdau":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="armsakina")],
                    [InlineKeyboardButton("last chapter", callback_data="hastworexes")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Variables and Data Types in C*\n\n"
                                      "🔹 *What is a variable?*\n"
                                      "— A name used to store data in memory.\n"
                                      "— Each variable has a type that defines what kind of data it holds.\n\n"
                                      "🔹 *Common data types:*\n"
                                      "- `int` — integers, e.g.: `42`\n"
                                      "- `float` — floating-point numbers, e.g.: `3.14`\n"
                                      "- `char` — a single character, e.g.: `'A'`\n"
                                      "- `double` — more precise floating-point numbers\n\n"
                                      "============================\n"
                                      "🔹 *Declaring variables:*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *Printing to the screen:*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"Age: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Try it yourself:* declare some variables and print their values!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "sirenseacreaturrank":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="rankrankrank")],
                    [InlineKeyboardButton("last chapter", callback_data="goluboysahpmurnejdet")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Conditional Statements in C: if, else if, else*\n\n"
                                      "🔹 *What is a conditional statement?*\n"
                                      "— It allows you to execute different parts of code depending on conditions.\n\n"
                                      "🔹 *Syntax of if:*\n"
                                      "```c\n"
                                      "if (condition) {\n"
                                      "    // code if condition is true\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Using else if and else:*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"Positive number\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"Zero\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"Negative number\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Logical operators for conditions:*\n"
                                      "- `&&` — AND\n"
                                      "- `||` — OR\n"
                                      "- `!` — NOT\n\n"
                                      "✅ *Task:* Write a program that checks a number and prints whether it’s positive, negative, or zero!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "goluboysahpmurnejdet":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="sirenseacreaturrank")],
                    [InlineKeyboardButton("last chapter", callback_data="uusuasdaudodsuodaioasdau")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Operators and Expressions in C*\n\n"
                                      "🔹 *What is an operator?*\n"
                                      "— A symbol or combination of symbols that perform operations on data.\n\n"
                                      "🔹 *Types of operators:*\n"
                                      "- Arithmetic: `+`, `-`, `*`, `/`, `%`\n"
                                      "- Assignment: `=`, `+=`, `-=`, `*=`, etc.\n"
                                      "- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                                      "- Logical: `&&`, `||`, `!`\n\n"
                                      "============================\n"
                                      "🔹 *Example of arithmetic operations:*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int sum = a + b;       // 13\n"
                                      "int diff = a - b;      // 7\n"
                                      "int product = a * b;   // 30\n"
                                      "int quotient = a / b;  // 3\n"
                                      "int remainder = a % b; // 1\n"
                                      "```\n\n"
                                      "🔹 *Example of comparison and logic:*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x is less than y and y is positive\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Try it yourself:* write expressions using different operators and print the results!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "rankrankrank":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="krisarank")],
                    [InlineKeyboardButton("last chapter", callback_data="etocecenskiyflot")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Loops in C: for, while, do-while*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— Allows repeating a block of code multiple times.\n\n"
                                      "🔹 *for loop:*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"Iteration %d\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *while loop:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"Iteration %d\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *do-while loop:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"Iteration %d\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *Try it yourself:* write a loop that prints numbers from 1 to 10!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "etocecenskiyflot":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="rankrankrank")],
                    [InlineKeyboardButton("last chapter", callback_data="goluboysahpmurnejdet")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Conditional Statements in C: if, else if, else*\n\n"
                                      "🔹 *What is a conditional statement?*\n"
                                      "— It allows you to execute different parts of code depending on conditions.\n\n"
                                      "🔹 *Syntax of if:*\n"
                                      "```c\n"
                                      "if (condition) {\n"
                                      "    // code if condition is true\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Using else if and else:*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"Positive number\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"Zero\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"Negative number\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Logical operators for conditions:*\n"
                                      "- `&&` — AND\n"
                                      "- `||` — OR\n"
                                      "- `!` — NOT\n\n"
                                      "✅ *Task:* Write a program that checks a number and prints whether it’s positive, negative, or zero!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )


    elif query.data == "krisarank":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="tentiicsranking")],
                    [InlineKeyboardButton("last chapter", callback_data="eroutuwrfnmzxnj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Functions in C*\n\n"
                                      "🔹 *What is a function?*\n"
                                      "— A block of code that performs a specific task.\n"
                                      "— Helps organize the program and reuse code.\n\n"
                                      "🔹 *Declaring and calling a function:*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // function call\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Function with parameters:*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"Hello, %s!\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Tom\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Function with return value:*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"The square of 5 is %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Try writing a function that adds two numbers and returns the result!*\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "eroutuwrfnmzxnj":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="krisarank")],
                    [InlineKeyboardButton("last chapter", callback_data="etocecenskiyflot")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Loops in C: for, while, do-while*\n\n"
                                      "🔹 *What is a loop?*\n"
                                      "— Allows repeating a block of code multiple times.\n\n"
                                      "🔹 *for loop:*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"Iteration %d\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *while loop:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"Iteration %d\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *do-while loop:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"Iteration %d\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *Try it yourself:* write a loop that prints numbers from 1 to 10!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "tentiicsranking":
        keyboard = [[InlineKeyboardButton("last chapter", callback_data="nbxbhdbschdsivud")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📌 *Pointers in C*\n\n"
                                      "🔹 *What is a pointer?*\n"
                                      "— A pointer is a variable that stores the memory address of another variable.\n"
                                      "— Used for efficient memory handling, arrays, and function manipulation.\n\n"
                                      "🔹 *Basic pointer example:*\n"
                                      "```c\n"
                                      "int x = 10;\n"
                                      "int* ptr = &x;\n"
                                      "printf(\"Value: %d\\n\", *ptr); // dereferencing\n"
                                      "```\n"
                                      "— `&x` gets the address of variable `x`\n"
                                      "— `*ptr` accesses the value at that address\n\n"
                                      "🔹 *Explanation:*\n"
                                      "- `int* ptr;` — pointer to an integer\n"
                                      "- `*` — dereferencing (get value at address)\n"
                                      "- `&` — address-of operator\n\n"
                                      "============================\n"
                                      "🔹 *Modifying value through a pointer:*\n"
                                      "```c\n"
                                      "int a = 5;\n"
                                      "int* p = &a;\n"
                                      "*p = 100;\n"
                                      "printf(\"%d\\n\", a); // prints 100\n"
                                      "```\n"
                                      "✅ The pointer modifies the original variable's value.\n\n"
                                      "============================\n"
                                      "🔹 *Printing addresses:*\n"
                                      "```c\n"
                                      "int val = 42;\n"
                                      "printf(\"Address of variable: %p\\n\", &val);\n"
                                      "```\n"
                                      "— `%p` is used to print memory addresses.\n\n"
                                      "============================\n"
                                      "💡 Pointers are a fundamental part of C.\n"
                                      "They are essential for working with arrays, strings, functions, and memory management.\n\n"
                                      "📎 In the next chapter, you'll learn about *arrays and pointers*!\n",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "nbxbhdbschdsivud":
        keyboard = [[InlineKeyboardButton("Next chapter ➡", callback_data="tentiicsranking")],
                    [InlineKeyboardButton("last chapter", callback_data="eroutuwrfnmzxnj")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *Functions in C*\n\n"
                                      "🔹 *What is a function?*\n"
                                      "— A block of code that performs a specific task.\n"
                                      "— Helps organize the program and reuse code.\n\n"
                                      "🔹 *Declaring and calling a function:*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // function call\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Function with parameters:*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"Hello, %s!\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Tom\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Function with return value:*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"The square of 5 is %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Try writing a function that adds two numbers and returns the result!*\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)




    if query.data == "firstchinese":
        keyboard = [[InlineKeyboardButton("🔥 開始學習", callback_data="zzz")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "嗨！你準備好學習程式設計了嗎？",
            reply_markup=reply_markup)
    elif query.data == "zzz":
        keyboard = [
            [InlineKeyboardButton("程式設計語言", callback_data="cont")],
            [InlineKeyboardButton("網路安全", callback_data="cybers")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🚀 太棒了！現在選擇你想學習的內容：",
            reply_markup=reply_markup
        )
    elif query.data == "cont":
        keyboard = [
            [InlineKeyboardButton("🐍 Python ", callback_data="pt")],
            [InlineKeyboardButton("⚙️ C++ ", callback_data="qew")],
            [InlineKeyboardButton("🟨 Javascript", callback_data="srip")],
            [InlineKeyboardButton("☕ Java 語言課程", callback_data="java_start")],
            [InlineKeyboardButton("💻 C", callback_data="huggywug")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "好！現在選擇你想學習的語言",
            reply_markup=reply_markup
        )

    elif query.data == "cybers":
        keyboard = [
            [InlineKeyboardButton("📡網絡", callback_data="cyberxx")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "開始吧！ \n第 1 章：",
            reply_markup=reply_markup
        )

    elif query.data == "cyberxx":
        keyboard = [
            [InlineKeyboardButton("下一章➡️", callback_data="nextxx")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 *網路 (Networks)* 是簡單的連接物件。\n"
                                      "例如，你的朋友圈：你們透過共同興趣、愛好、技能等彼此連結。🧠🤝\n\n"
                                      "📡 *網路無處不在：*\n"
                                      "　- 🚇 城市的公共交通系統\n"
                                      "　- ⚡ 國家的電力基礎設施\n"
                                      "　- 🏘️ 鄰居之間的交流\n"
                                      "　- ✉️ 郵政系統傳遞信件和包裹\n\n"
                                      "💻 *在科技領域，概念相同，只是應用在設備之間。*\n"
                                      "想想你的手機 📱：你使用它是為了取得資訊。\n\n"
                                      "📶 *我們將一起學習設備如何交換資料，以及它們遵循的規則。*\n\n"
                                      "🖥️ *網路可以包含 2 個到數十億個設備：*\n"
                                      "　- 💻 筆記型電腦\n"
                                      "　- 📱 智慧型手機\n"
                                      "　- 📷 監控攝影機\n"
                                      "　- 🚦 紅綠燈\n"
                                      "　- 🌾 農業設備\n\n"
                                      "🔌 *網路已經深入我們的日常生活：*\n"
                                      "　- ⛅ 天氣資料的蒐集\n"
                                      "　- ⚡ 電力供應給家庭\n"
                                      "　- 🚦 道路交通管理\n\n"
                                      "🛡️ 因為網路是現代生活不可或缺的一部分，\n"
                                      "了解網路基本原理是學習資安的基礎。\n\n"
                                      "👥 請看下圖：Alice、Bob 和 Jim 建立了自己的小網路！\n"
                                      "我們稍後會回到這個話題……\n\n"
                                      "*第一章就在這裡！！*\n"
                                      "*第一章已經開始！！*",
                                      parse_mode="Markdown"
                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "nextxx":
        keyboard = [
            [InlineKeyboardButton("下一章➡️", callback_data="twopp")],
            [InlineKeyboardButton("最後一章", callback_data="imgladifdjvjfdvnifnvrecvbryyee")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *第二章：深入了解網際網路！*\n\n"
                                      "現在你已經知道網路是什麼——簡單來說就是連接在一起的設備——接下來我們來了解網際網路是如何運作的。\n\n"
                                      "📡 網際網路就是由許多小型網路相互連接組成的一個*龐大網路*。\n\n"
                                      "👫 想像 Alice 認識了新朋友 Zayn 和 Toby，她想介紹他們給 Bob 和 Jim 認識。但有個問題：只有 Alice 能理解兩組人的語言。於是她成為了一座*橋樑*，現在大家都可以透過她溝通。這就是一個新的網路例子。\n\n"
                                      "📜 網際網路的第一個版本出現在1960年代末，作為美國軍方資助的*ARPANET*專案的一部分。\n"
                                      "這是第一個真正運作的電腦網路。\n\n"
                                      "🌍 1989年，Tim Berners-Lee 提出了*全球資訊網 (WWW)*的概念，讓網際網路成為分享與儲存資訊的便利工具。\n\n"
                                      "🔌 如今，網際網路就像一個由數千個小團隊組成的巨大俱樂部。網路分為兩種類型：\n"
                                      "　- 🔒 私人網路\n"
                                      "　- 🌐 公共網路，兩者合起來就是我們所說的網際網路\n\n"
                                      "💡 網路上的設備使用特殊的*識別碼*（我們稍後會講到）來尋找彼此並交換資料。",
                                      parse_mode="Markdown"

                                      ,
                                      reply_markup=reply_markup)
    elif query.data == "imgladifdjvjfdvnifnvrecvbryyee":
        keyboard = [
            [InlineKeyboardButton("下一章➡️", callback_data="nextxx")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 *網路 (Networks)* 是簡單的連接物件。\n"
                                      "例如，你的朋友圈：你們透過共同興趣、愛好、技能等彼此連結。🧠🤝\n\n"
                                      "📡 *網路無處不在：*\n"
                                      "　- 🚇 城市的公共交通系統\n"
                                      "　- ⚡ 國家的電力基礎設施\n"
                                      "　- 🏘️ 鄰居之間的交流\n"
                                      "　- ✉️ 郵政系統傳遞信件和包裹\n\n"
                                      "💻 *在科技領域，概念相同，只是應用在設備之間。*\n"
                                      "想想你的手機 📱：你使用它是為了取得資訊。\n\n"
                                      "📶 *我們將一起學習設備如何交換資料，以及它們遵循的規則。*\n\n"
                                      "🖥️ *網路可以包含 2 個到數十億個設備：*\n"
                                      "　- 💻 筆記型電腦\n"
                                      "　- 📱 智慧型手機\n"
                                      "　- 📷 監控攝影機\n"
                                      "　- 🚦 紅綠燈\n"
                                      "　- 🌾 農業設備\n\n"
                                      "🔌 *網路已經深入我們的日常生活：*\n"
                                      "　- ⛅ 天氣資料的蒐集\n"
                                      "　- ⚡ 電力供應給家庭\n"
                                      "　- 🚦 道路交通管理\n\n"
                                      "🛡️ 因為網路是現代生活不可或缺的一部分，\n"
                                      "了解網路基本原理是學習資安的基礎。\n\n"
                                      "👥 請看下圖：Alice、Bob 和 Jim 建立了自己的小網路！\n"
                                      "我們稍後會回到這個話題……\n\n"
                                      "*第一章就在這裡！！*\n"
                                      "*第一章已經開始！！*",
                                      parse_mode="Markdown"
                                      ,
                                      reply_markup=reply_markup)


    elif query.data == "twopp":
        keyboard = [
            [InlineKeyboardButton("下一章➡️", callback_data="threepp")],
            [InlineKeyboardButton("最後一章", callback_data="yapyupizdatiyviskimolodoye")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📡 為了讓設備能在網路中通信並保持秩序，它們必須：\n"
                                      "— 辨認自己\n"
                                      "— 被其他設備辨認\n\n"
                                      "💡 設備就像人一樣：\n"
                                      "— 我們有名字（可以改變）\n"
                                      "— 也有指紋（永遠唯一）\n\n"
                                      "📱 設備也有兩種「識別」方式：\n"
                                      "— IP 位址（📍 可變）\n"
                                      "— MAC 位址（🔒 永久，像指紋）\n\n"
                                      "=====================\n"
                                      "🔹 IP 位址\n"
                                      "IP 位址就像設備在網路中的暫時名字。\n"
                                      "它由4個數字（八位元組）組成，中間用點分隔：\n"
                                      "範例：192.168.0.1\n\n"
                                      "🔁 一個 IP 可以被分配給另一個設備，但同一網路中不能有兩台設備同時使用相同的 IP。\n\n"
                                      "🌍 IP 有兩種類型：\n"
                                      "— 私人 IP — 用於區域網路（家裡、辦公室）\n"
                                      "— 公共 IP — 在網際網路上可見\n\n"
                                      "🧾 範例：\n\n"
                                      "設備\t私人 IP\t公共 IP\n"
                                      "我的電腦\t192.168.1.77\t86.157.52.21\n"
                                      "另一台電腦\t192.168.1.74\t86.157.52.21\n\n"
                                      "🔍 兩台設備有相同的公共 IP（同一個調製解調器），但不同的私人 IP，這就是它們如何在同一網路中通訊。\n\n"
                                      "=====================\n"
                                      "🌐 問題：IP 位址不夠用！\n"
                                      "IPv4 有約42.9億個位址（2^32），但全球設備數量達數百億。\n\n"
                                      "💡 解決方案：\n"
                                      "— IPv6 有超過340兆個位址（2^128）\n"
                                      "— 更有效率\n"
                                      "— 位址數量多得多\n\n"
                                      "範例：\n"
                                      "— IPv4: 192.168.1.1\n"
                                      "— IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334\n\n"
                                      "=====================\n"
                                      "🔹 MAC 位址\n"
                                      "每個設備有一個網路介面卡，帶有唯一的 MAC 位址。\n"
                                      "格式：a4:c3:f0:85:ac:2d（6個位元組的十六進制）\n\n"
                                      "🛠 前6個字元是製造商編碼。\n"
                                      "📌 後6個字元是設備唯一編號。\n\n"
                                      "💥 但 MAC 位址可以被偽造，稱為偽裝（spoofing）：\n"
                                      "— 攻擊者可假裝成另一設備。\n"
                                      "— 例如，若防火牆只允許管理員的 MAC，攻擊者就能欺騙系統！\n\n"
                                      "=====================\n"
                                      "📌 總結：\n"
                                      "🔹 IP — 會隨網路改變。\n"
                                      "🔹 MAC — 永久且唯一。\n"
                                      "🔹 安全考量：IP 和 MAC 都不保證真實身份。\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "yapyupizdatiyviskimolodoye":
        keyboard = [
            [InlineKeyboardButton("下一章➡️", callback_data="twopp")],
            [InlineKeyboardButton("最後一章", callback_data="imgladifdjvjfdvnifnvrecvbryyee")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *第二章：深入了解網際網路！*\n\n"
                                      "現在你已經知道網路是什麼——簡單來說就是連接在一起的設備——接下來我們來了解網際網路是如何運作的。\n\n"
                                      "📡 網際網路就是由許多小型網路相互連接組成的一個*龐大網路*。\n\n"
                                      "👫 想像 Alice 認識了新朋友 Zayn 和 Toby，她想介紹他們給 Bob 和 Jim 認識。但有個問題：只有 Alice 能理解兩組人的語言。於是她成為了一座*橋樑*，現在大家都可以透過她溝通。這就是一個新的網路例子。\n\n"
                                      "📜 網際網路的第一個版本出現在1960年代末，作為美國軍方資助的*ARPANET*專案的一部分。\n"
                                      "這是第一個真正運作的電腦網路。\n\n"
                                      "🌍 1989年，Tim Berners-Lee 提出了*全球資訊網 (WWW)*的概念，讓網際網路成為分享與儲存資訊的便利工具。\n\n"
                                      "🔌 如今，網際網路就像一個由數千個小團隊組成的巨大俱樂部。網路分為兩種類型：\n"
                                      "　- 🔒 私人網路\n"
                                      "　- 🌐 公共網路，兩者合起來就是我們所說的網際網路\n\n"
                                      "💡 網路上的設備使用特殊的*識別碼*（我們稍後會講到）來尋找彼此並交換資料。",
                                      parse_mode="Markdown"

                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "threepp":
        keyboard = [[InlineKeyboardButton("最後一章",callback_data="doctorhannibalpsycho")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📡 Ping 是一種基本的網路工具，用來檢查兩個設備之間的連接狀態。\n"
            "它使用 ICMP 協議（網際網路控制訊息協議），\n"
            "傳送特殊的回聲請求，並等待目標節點的回聲回覆。\n\n"
            "透過 Ping，你可以判斷連線是否正常以及穩定度。\n"
            "也能測量封包從一台設備傳送到另一台設備所需的毫秒數。\n\n"
            "這個工具內建於大多數作業系統中，包括 Linux 和 Windows。\n"
            "執行 Ping 指令，只需在終端機或命令提示字元輸入：\n"
            "`ping IP位址` 或 `ping 網站名稱`。\n\n"
            "例如，執行指令 `ping 192.168.1.254`，\n"
            "你會看到送出和接收的封包數量，\n"
            "以及平均回應時間（例如：4.16 毫秒）。",
            parse_mode="Markdown",
            reply_markup = reply_markup
        )
    elif query.data == "doctorhannibalpsycho":
        keyboard = [
            [InlineKeyboardButton("下一章➡️", callback_data="threepp")],
            [InlineKeyboardButton("最後一章", callback_data="yapyupizdatiyviskimolodoye")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📡 為了讓設備能在網路中通信並保持秩序，它們必須：\n"
                                      "— 辨認自己\n"
                                      "— 被其他設備辨認\n\n"
                                      "💡 設備就像人一樣：\n"
                                      "— 我們有名字（可以改變）\n"
                                      "— 也有指紋（永遠唯一）\n\n"
                                      "📱 設備也有兩種「識別」方式：\n"
                                      "— IP 位址（📍 可變）\n"
                                      "— MAC 位址（🔒 永久，像指紋）\n\n"
                                      "=====================\n"
                                      "🔹 IP 位址\n"
                                      "IP 位址就像設備在網路中的暫時名字。\n"
                                      "它由4個數字（八位元組）組成，中間用點分隔：\n"
                                      "範例：192.168.0.1\n\n"
                                      "🔁 一個 IP 可以被分配給另一個設備，但同一網路中不能有兩台設備同時使用相同的 IP。\n\n"
                                      "🌍 IP 有兩種類型：\n"
                                      "— 私人 IP — 用於區域網路（家裡、辦公室）\n"
                                      "— 公共 IP — 在網際網路上可見\n\n"
                                      "🧾 範例：\n\n"
                                      "設備\t私人 IP\t公共 IP\n"
                                      "我的電腦\t192.168.1.77\t86.157.52.21\n"
                                      "另一台電腦\t192.168.1.74\t86.157.52.21\n\n"
                                      "🔍 兩台設備有相同的公共 IP（同一個調製解調器），但不同的私人 IP，這就是它們如何在同一網路中通訊。\n\n"
                                      "=====================\n"
                                      "🌐 問題：IP 位址不夠用！\n"
                                      "IPv4 有約42.9億個位址（2^32），但全球設備數量達數百億。\n\n"
                                      "💡 解決方案：\n"
                                      "— IPv6 有超過340兆個位址（2^128）\n"
                                      "— 更有效率\n"
                                      "— 位址數量多得多\n\n"
                                      "範例：\n"
                                      "— IPv4: 192.168.1.1\n"
                                      "— IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334\n\n"
                                      "=====================\n"
                                      "🔹 MAC 位址\n"
                                      "每個設備有一個網路介面卡，帶有唯一的 MAC 位址。\n"
                                      "格式：a4:c3:f0:85:ac:2d（6個位元組的十六進制）\n\n"
                                      "🛠 前6個字元是製造商編碼。\n"
                                      "📌 後6個字元是設備唯一編號。\n\n"
                                      "💥 但 MAC 位址可以被偽造，稱為偽裝（spoofing）：\n"
                                      "— 攻擊者可假裝成另一設備。\n"
                                      "— 例如，若防火牆只允許管理員的 MAC，攻擊者就能欺騙系統！\n\n"
                                      "=====================\n"
                                      "📌 總結：\n"
                                      "🔹 IP — 會隨網路改變。\n"
                                      "🔹 MAC — 永久且唯一。\n"
                                      "🔹 安全考量：IP 和 MAC 都不保證真實身份。\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)


    elif query.data == "pt":
        keyboard = [[
            InlineKeyboardButton("去", callback_data="numberoness")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "好啦！ ！開始我們的 Python 之旅吧🐍»",
            reply_markup=reply_markup)
    elif query.data == "qew":
        keyboard = [[
            InlineKeyboardButton("*第一章*", callback_data="cponess")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "好啦！ ！開始我們的 C++ 之旅⚙️",
            reply_markup=reply_markup)
    elif query.data == "srip":
        keyboard = [[
            InlineKeyboardButton("第1章", callback_data="jvonesss")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "好啦！ ！開啟我們的🟨 JavaScript 之旅吧！",
            reply_markup=reply_markup)
    elif query.data == "numberoness":
        keyboard = [[InlineKeyboardButton("🐍開始", callback_data="mcqueenss")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("讓我們開始吧！\n"
                                      "*第一章：*", reply_markup=reply_markup)
    elif query.data == "mcqueenss":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="fsociety")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *安装 Python 64 位及连接 PyCharm Community*\n\n"
            "🔹 *步骤 1：下载 Python*\n"
            "[下载 Python](https://www.python.org/downloads/) — 选择 Windows x86-64 可执行安装程序\n\n"
            "🔹 *步骤 2：安装*\n"
            "— 勾选 “Add Python to PATH”\n"
            "— 选择自定义安装 → 下一步 → 为所有用户安装 → 安装\n\n"
            "🔹 *步骤 3：验证安装*\n"
            "在终端输入 `python --version` — 应显示 Python 3.X.X\n\n"
            "🔹 *步骤 4：下载 PyCharm*\n"
            "[下载 PyCharm](https://www.jetbrains.com/pycharm/download) — 安装 Community 版本\n\n"
            "🔹 *步骤 5：连接 Python*\n"
            "新建项目 → ⚙️ 添加解释器 → 系统解释器 → 路径：\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *检查：*\n"
            "创建文件，输入代码：\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "点击 ▶️ 运行\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "fsociety":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="if")],
                    [InlineKeyboardButton("最後一章",callback_data="vmineocenmnogoonblkjfnv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Python 的變數與資料型態*\n\n"
            "🔹 *什麼是變數？*\n"
            "— 用來儲存資料的名稱，資料型態會自動判斷。\n\n"
            "🔹 *變數範例：*\n"
            "`x = 10` — 整數 (int)\n"
            "`name = \"Tom\"` — 字串 (str)\n"
            "`pi = 3.14` — 浮點數 (float)\n\n"
            "🔹 *主要資料型態：*\n"
            "- `int` — 整數\n"
            "- `float` — 小數\n"
            "- `str` — 文字字串\n"
            "- `bool` — 布林值：`True` 或 `False`\n\n"
            "🔹 *如何輸出資料？*\n"
            "`print(x)`\n"
            "`print(name)`\n"
            "`print(pi)`\n\n"
            "✅ *自己試試看：*\n"
            "```python\nage = 15\ncity = \"莫斯科\"\nis_student = True\n\n"
            "print(\"年齡:\", age)\nprint(\"城市:\", city)\nprint(\"學生:\", is_student)\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "vmineocenmnogoonblkjfnv":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="fsociety")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *安装 Python 64 位及连接 PyCharm Community*\n\n"
            "🔹 *步骤 1：下载 Python*\n"
            "[下载 Python](https://www.python.org/downloads/) — 选择 Windows x86-64 可执行安装程序\n\n"
            "🔹 *步骤 2：安装*\n"
            "— 勾选 “Add Python to PATH”\n"
            "— 选择自定义安装 → 下一步 → 为所有用户安装 → 安装\n\n"
            "🔹 *步骤 3：验证安装*\n"
            "在终端输入 `python --version` — 应显示 Python 3.X.X\n\n"
            "🔹 *步骤 4：下载 PyCharm*\n"
            "[下载 PyCharm](https://www.jetbrains.com/pycharm/download) — 安装 Community 版本\n\n"
            "🔹 *步骤 5：连接 Python*\n"
            "新建项目 → ⚙️ 添加解释器 → 系统解释器 → 路径：\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *检查：*\n"
            "创建文件，输入代码：\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "点击 ▶️ 运行\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "if":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="sezeresx")],
                    [InlineKeyboardButton("最後一章",callback_data="copagangsmysfhnur")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Python 條件語句：if、elif、else*\n\n"
            "🔹 *什麼是條件語句？*\n"
            "— 僅當特定條件成立時才執行程式碼。\n"
            "— 使用 if、elif、else 結構。\n\n"
            "🔹 *語法範例：*\n"
            "```python\nage = 16\n\nif age >= 18:\n    print(\"你是成年人\")\nelif age >= 14:\n    print(\"你是青少年\")\nelse:\n    print(\"你是小孩\")\n```\n\n"
            "🔹 *比較運算子：* `==`、`!=`、`>`、`<`、`>=`、`<=`\n"
            "🔹 *邏輯運算子：* `and`、`or`、`not`\n\n"
            "✅ *自己試試看：*\n"
            "```python\nname = input(\"你的名字：\")\nif name == \"Tom\":\n    print(\"哈囉，Tom！\")\nelse:\n    print(\"哈囉，訪客！\")\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "copagangsmysfhnur":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="if")],
                    [InlineKeyboardButton("最後一章", callback_data="vmineocenmnogoonblkjfnv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Python 的變數與資料型態*\n\n"
            "🔹 *什麼是變數？*\n"
            "— 用來儲存資料的名稱，資料型態會自動判斷。\n\n"
            "🔹 *變數範例：*\n"
            "`x = 10` — 整數 (int)\n"
            "`name = \"Tom\"` — 字串 (str)\n"
            "`pi = 3.14` — 浮點數 (float)\n\n"
            "🔹 *主要資料型態：*\n"
            "- `int` — 整數\n"
            "- `float` — 小數\n"
            "- `str` — 文字字串\n"
            "- `bool` — 布林值：`True` 或 `False`\n\n"
            "🔹 *如何輸出資料？*\n"
            "`print(x)`\n"
            "`print(name)`\n"
            "`print(pi)`\n\n"
            "✅ *自己試試看：*\n"
            "```python\nage = 15\ncity = \"莫斯科\"\nis_student = True\n\n"
            "print(\"年齡:\", age)\nprint(\"城市:\", city)\nprint(\"學生:\", is_student)\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "sezeresx":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="tut")],
                    [InlineKeyboardButton("最後一章",callback_data="yobraputatiriajd")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python：for 與 while 迴圈*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 迴圈用來重複執行一段程式碼。\n"
                                      "— 常用來遍歷列表、數字序列或其他集合。\n\n"
                                      "============================\n"
                                      "🔹 *for 迴圈範例：*\n"
                                      "```python\nfor i in range(5):\n    print(i)\n```\n"
                                      "— 輸出數字 0 到 4。\n\n"
                                      "🔸 `range(5)` 會產生序列：0、1、2、3、4\n\n"
                                      "============================\n"
                                      "🔹 *while 迴圈範例：*\n"
                                      "```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```\n"
                                      "— 當條件為真，程式碼區塊會重複執行。\n\n"
                                      "============================\n"
                                      "🔹 *用 for 遍歷列表：*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- `for` 適合逐個處理集合元素\n"
                                      "- `while` 依條件重複執行\n"
                                      "- 若要提前結束迴圈，使用 `break`\n\n"
                                      "💡 迴圈是自動化與資料處理的基礎！\n"
                                      "試著寫一個簡單的迴圈來輸出數字或單詞吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "yobraputatiriajd":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="sezeresx")],
                    [InlineKeyboardButton("最後一章", callback_data="copagangsmysfhnur")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Python 條件語句：if、elif、else*\n\n"
            "🔹 *什麼是條件語句？*\n"
            "— 僅當特定條件成立時才執行程式碼。\n"
            "— 使用 if、elif、else 結構。\n\n"
            "🔹 *語法範例：*\n"
            "```python\nage = 16\n\nif age >= 18:\n    print(\"你是成年人\")\nelif age >= 14:\n    print(\"你是青少年\")\nelse:\n    print(\"你是小孩\")\n```\n\n"
            "🔹 *比較運算子：* `==`、`!=`、`>`、`<`、`>=`、`<=`\n"
            "🔹 *邏輯運算子：* `and`、`or`、`not`\n\n"
            "✅ *自己試試看：*\n"
            "```python\nname = input(\"你的名字：\")\nif name == \"Tom\":\n    print(\"哈囉，Tom！\")\nelse:\n    print(\"哈囉，訪客！\")\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "tut":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="yxx")],
                    [InlineKeyboardButton("最後一章",callback_data="letmeshowwhatyougiveup")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python：列表（List）*\n\n"
                                      "🔹 *什麼是列表？*\n"
                                      "— 有序的元素集合。\n"
                                      "— 可以存放數字、字串，甚至其他列表。\n\n"
                                      "============================\n"
                                      "🔹 *列表範例：*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\n```\n"
                                      "— 包含三個字串的列表。\n\n"
                                      "🔸 透過索引存取元素：\n"
                                      "`fruits[0]` → \"apple\"\n"
                                      "`fruits[2]` → \"cherry\"\n\n"
                                      "============================\n"
                                      "🔹 *修改與新增元素：*\n"
                                      "```python\nfruits[1] = \"kiwi\"  # 將 'banana' 改為 'kiwi'\nfruits.append(\"pear\")  # 新增元素\n```\n\n"
                                      "============================\n"
                                      "🔹 *遍歷列表：*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 逐個輸出列表中的元素。\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- 索引從 0 開始計算\n"
                                      "- 列表可存放不同類型的元素\n"
                                      "- 列表是可變的（可新增、刪除元素）\n\n"
                                      "💡 列表是 Python 中處理資料集合的強大工具。\n"
                                      "試著自己創建列表並用迴圈遍歷它吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "letmeshowwhatyougiveup":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="tut")],
                    [InlineKeyboardButton("最後一章", callback_data="yobraputatiriajd")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python：for 與 while 迴圈*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 迴圈用來重複執行一段程式碼。\n"
                                      "— 常用來遍歷列表、數字序列或其他集合。\n\n"
                                      "============================\n"
                                      "🔹 *for 迴圈範例：*\n"
                                      "```python\nfor i in range(5):\n    print(i)\n```\n"
                                      "— 輸出數字 0 到 4。\n\n"
                                      "🔸 `range(5)` 會產生序列：0、1、2、3、4\n\n"
                                      "============================\n"
                                      "🔹 *while 迴圈範例：*\n"
                                      "```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```\n"
                                      "— 當條件為真，程式碼區塊會重複執行。\n\n"
                                      "============================\n"
                                      "🔹 *用 for 遍歷列表：*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- `for` 適合逐個處理集合元素\n"
                                      "- `while` 依條件重複執行\n"
                                      "- 若要提前結束迴圈，使用 `break`\n\n"
                                      "💡 迴圈是自動化與資料處理的基礎！\n"
                                      "試著寫一個簡單的迴圈來輸出數字或單詞吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "yxx":
        keyboard = [[InlineKeyboardButton("最後一章",callback_data="imyoungblackandrcihiadnpussylicker")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🛠️ *Python：函式（Functions）*\n\n"
                                      "🔹 *什麼是函式？*\n"
                                      "— 一段執行特定任務的程式碼區塊。\n"
                                      "— 函式可以避免重複程式碼，讓程式更易讀、更有條理。\n\n"
                                      "============================\n"
                                      "🔹 *簡單的函式：*\n"
                                      "```python\ndef say_hello():\n    print(\"Hello, world!\")\n\nsay_hello()  # 呼叫函式\n```\n"
                                      "— 使用 `def` 關鍵字、函式名稱、括號與冒號。\n"
                                      "— 函式內的程式碼只有在呼叫時才會執行。\n\n"
                                      "============================\n"
                                      "🔹 *帶參數的函式：*\n"
                                      "```python\ndef greet(name):\n    print(\"Hello,\", name)\n\ngreet(\"Alice\")\n```\n"
                                      "— 可以傳入值到函式內部，這些值稱為參數（arguments）。\n\n"
                                      "============================\n"
                                      "🔹 *帶回傳值的函式（`return`）：*\n"
                                      "```python\ndef square(x):\n    return x * x\n\nresult = square(5)\nprint(result)\n```\n"
                                      "— `return` 用來回傳結果。\n"
                                      "— 回傳的結果可以存入變數。\n\n"
                                      "============================\n"
                                      "✅ *為什麼函式重要？*\n"
                                      "- 讓程式碼更精簡、易讀\n"
                                      "- 可重複使用同一段邏輯\n"
                                      "- 可將大型程式拆分成小部分，提升結構性\n\n"
                                      "💡 試著寫一個函式印出你的名字，再寫一個函式回傳兩數相加的結果！\n"
                                      "函式是每種程式語言的基礎！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "imyoungblackandrcihiadnpussylicker":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="yxx")],
                    [InlineKeyboardButton("最後一章", callback_data="letmeshowwhatyougiveup")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python：列表（List）*\n\n"
                                      "🔹 *什麼是列表？*\n"
                                      "— 有序的元素集合。\n"
                                      "— 可以存放數字、字串，甚至其他列表。\n\n"
                                      "============================\n"
                                      "🔹 *列表範例：*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\n```\n"
                                      "— 包含三個字串的列表。\n\n"
                                      "🔸 透過索引存取元素：\n"
                                      "`fruits[0]` → \"apple\"\n"
                                      "`fruits[2]` → \"cherry\"\n\n"
                                      "============================\n"
                                      "🔹 *修改與新增元素：*\n"
                                      "```python\nfruits[1] = \"kiwi\"  # 將 'banana' 改為 'kiwi'\nfruits.append(\"pear\")  # 新增元素\n```\n\n"
                                      "============================\n"
                                      "🔹 *遍歷列表：*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 逐個輸出列表中的元素。\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- 索引從 0 開始計算\n"
                                      "- 列表可存放不同類型的元素\n"
                                      "- 列表是可變的（可新增、刪除元素）\n\n"
                                      "💡 列表是 Python 中處理資料集合的強大工具。\n"
                                      "試著自己創建列表並用迴圈遍歷它吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "cponess":
        keyboard = [[InlineKeyboardButton("⚙ 開始", callback_data="rezeress")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("«»", reply_markup=reply_markup)

    elif query.data == "rezeress":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="vezeress")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++ 安裝與開始：*\n\n"
            "🔹 *步驟 1：安裝編譯器*\n"
            "[下載 MinGW](https://sourceforge.net/projects/mingw/)\n"
            "— 安裝 gcc 並將 bin 資料夾路徑加入系統環境變數 PATH\n\n"
            "🔹 *步驟 2：下載編輯器*\n"
            "[下載 Visual Studio Code](https://code.visualstudio.com/)\n\n"
            "🔹 *步驟 3：檢查編譯器*\n"
            "`g++ --version`\n\n"
            "🔹 *步驟 4：簡單程式碼*\n"
            "```cpp\n#include <iostream>\nint main() {\n"
            "    std::cout << \"Hello, world!\";\n    return 0;\n}\n```\n"
            "將檔案儲存為 `main.cpp`，編譯指令：\n"
            "`g++ main.cpp -o main`\n"
            "執行：\n"
            "`./main`",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "vezeress":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="cpp5")],
                    [InlineKeyboardButton("最後一章",callback_data="aasaaasasas")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++：變數與資料型態*\n\n"
            "🔹 *什麼是變數？*\n"
            "— 變數是具名的記憶體空間，用來儲存資料。\n"
            "— 必須先宣告變數的型態，才能使用。\n\n"
            "🔹 *範例：*\n"
            "`int age = 15;`  // 整數\n"
            "`double pi = 3.14;`  // 浮點數\n"
            "`char grade = 'A';`  // 字元\n"
            "`bool isOnline = true;`  // 布林值\n"
            "`std::string name = \"Tom\";`  // 字串\n\n"
            "🔹 *輸出示例：*\n"
            "```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n"
            "    int age = 15;\n    std::string name = \"Tom\";\n"
            "    std::cout << \"姓名：\" << name << \"\\n\";\n"
            "    std::cout << \"年齡：\" << age << \"\\n\";\n    return 0;\n}\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "aasaaasasas":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="vezeress")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++ 安裝與開始：*\n\n"
            "🔹 *步驟 1：安裝編譯器*\n"
            "[下載 MinGW](https://sourceforge.net/projects/mingw/)\n"
            "— 安裝 gcc 並將 bin 資料夾路徑加入系統環境變數 PATH\n\n"
            "🔹 *步驟 2：下載編輯器*\n"
            "[下載 Visual Studio Code](https://code.visualstudio.com/)\n\n"
            "🔹 *步驟 3：檢查編譯器*\n"
            "`g++ --version`\n\n"
            "🔹 *步驟 4：簡單程式碼*\n"
            "```cpp\n#include <iostream>\nint main() {\n"
            "    std::cout << \"Hello, world!\";\n    return 0;\n}\n```\n"
            "將檔案儲存為 `main.cpp`，編譯指令：\n"
            "`g++ main.cpp -o main`\n"
            "執行：\n"
            "`./main`",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "cpp5":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="jingg")],
                    [InlineKeyboardButton("最後一章",callback_data="guilty")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++：條件判斷（if、else、else if）*\n\n"
            "🔹 *什麼是條件？*\n"
            "— 當特定條件成立時，執行相對應的程式碼。\n\n"
            "🔹 *範例：*\n"
            "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int age = 16;\n"
            "    if (age >= 18) {\n        cout << \"你是成年人\";\n"
            "    } else if (age >= 14) {\n        cout << \"你是青少年\";\n"
            "    } else {\n        cout << \"你是小孩\";\n    }\n"
            "    return 0;\n}\n```\n\n"
            "🔹 *運算符：* `==`、`!=`、`>`、`<`、`>=`、`<=`\n"
            "🔹 *邏輯符號：* `&&`、`||`、`!`\n\n"
            "✅ *試著自己寫一個條件判斷吧！*",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "guilty":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="cpp5")],
                    [InlineKeyboardButton("最後一章", callback_data="aasaaasasas")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++：變數與資料型態*\n\n"
            "🔹 *什麼是變數？*\n"
            "— 變數是具名的記憶體空間，用來儲存資料。\n"
            "— 必須先宣告變數的型態，才能使用。\n\n"
            "🔹 *範例：*\n"
            "`int age = 15;`  // 整數\n"
            "`double pi = 3.14;`  // 浮點數\n"
            "`char grade = 'A';`  // 字元\n"
            "`bool isOnline = true;`  // 布林值\n"
            "`std::string name = \"Tom\";`  // 字串\n\n"
            "🔹 *輸出示例：*\n"
            "```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n"
            "    int age = 15;\n    std::string name = \"Tom\";\n"
            "    std::cout << \"姓名：\" << name << \"\\n\";\n"
            "    std::cout << \"年齡：\" << age << \"\\n\";\n    return 0;\n}\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "jingg":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="venuss")],
                    [InlineKeyboardButton("最後一章",callback_data="yoxagzuvayoxunpoz")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🔁 *C++：迴圈（for、while、do while）*\n\n"
            "🔹 *什麼是迴圈？*\n"
            "— 當條件成立時，重複執行同一段程式碼。\n\n"
            "🔹 *C++ 中的迴圈類型：*\n"
            "- `for` — 預先知道執行次數時使用\n"
            "- `while` — 條件為真時持續執行\n"
            "- `do while` — 先執行一次，再檢查條件\n\n"
            "============================\n"
            "🔹 *範例：for*\n"
            "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << i << \" \";\n}\n```\n"
            "🔸 輸出：`0 1 2 3 4`\n\n"
            "============================\n"
            "🔹 *範例：while*\n"
            "```cpp\nint i = 0;\nwhile (i < 3) {\n    cout << i << endl;\n    i++;\n}\n```\n"
            "🔸 輸出：`0`、`1`、`2`\n\n"
            "============================\n"
            "🔹 *範例：do while*\n"
            "```cpp\nint i = 0;\ndo {\n    cout << i << endl;\n    i++;\n} while (i < 2);\n```\n"
            "🔸 輸出：`0`、`1`\n\n"
            "============================\n"
            "✅ *何時使用？*\n"
            "- `for` — 適合已知次數的計數器（如 `i = 0; i < N; i++`）\n"
            "- `while` — 不知道確切執行次數時\n"
            "- `do while` — 保證至少執行一次\n\n"
            "💡 試著自己寫寫看吧！",
            parse_mode="Markdown",
            reply_markup=reply_markup)
    elif query.data == "yoxagzuvayoxunpoz":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="jingg")],
                    [InlineKeyboardButton("最後一章", callback_data="guilty")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++：條件判斷（if、else、else if）*\n\n"
            "🔹 *什麼是條件？*\n"
            "— 當特定條件成立時，執行相對應的程式碼。\n\n"
            "🔹 *範例：*\n"
            "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int age = 16;\n"
            "    if (age >= 18) {\n        cout << \"你是成年人\";\n"
            "    } else if (age >= 14) {\n        cout << \"你是青少年\";\n"
            "    } else {\n        cout << \"你是小孩\";\n    }\n"
            "    return 0;\n}\n```\n\n"
            "🔹 *運算符：* `==`、`!=`、`>`、`<`、`>=`、`<=`\n"
            "🔹 *邏輯符號：* `&&`、`||`、`!`\n\n"
            "✅ *試著自己寫一個條件判斷吧！*",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "venuss":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="zerotrustss")],
                    [InlineKeyboardButton("最後一章",callback_data="crchemaadsasdadad")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++：陣列（Arrays）*\n\n"
                                      "🔹 *什麼是陣列？*\n"
                                      "— 一組**相同類型**的元素，連續存放於記憶體中。\n"
                                      "— 每個元素有自己的索引（從 0 開始）。\n\n"
                                      "============================\n"
                                      "🔹 *陣列範例：*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\n```\n"
                                      "— 建立一個包含 5 個 int 元素的陣列。\n\n"
                                      "🔸 存取元素：\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *用迴圈輸出所有元素：*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << numbers[i] << \" \";\n}\n```\n"
                                      "🔸 輸出結果：`10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *從使用者輸入值：*\n"
                                      "```cpp\nint a[3];\nfor (int i = 0; i < 3; i++) {\n    cin >> a[i];\n}\n```\n"
                                      "🔸 將 3 個數字儲存在陣列中。\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- 索引從 `0` 到 `n - 1`\n"
                                      "- 超出陣列邊界會造成錯誤（未定義行為）❌\n"
                                      "- 所有元素必須是相同類型（int、float、char 等）\n\n"
                                      "💡 陣列是基礎。透過陣列，你會學到記憶體管理、排序與演算法！\n\n"
                                      "試著建立陣列並輸出元素吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "crchemaadsasdadad":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="venuss")],
                    [InlineKeyboardButton("最後一章", callback_data="yoxagzuvayoxunpoz")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🔁 *C++：迴圈（for、while、do while）*\n\n"
            "🔹 *什麼是迴圈？*\n"
            "— 當條件成立時，重複執行同一段程式碼。\n\n"
            "🔹 *C++ 中的迴圈類型：*\n"
            "- `for` — 預先知道執行次數時使用\n"
            "- `while` — 條件為真時持續執行\n"
            "- `do while` — 先執行一次，再檢查條件\n\n"
            "============================\n"
            "🔹 *範例：for*\n"
            "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << i << \" \";\n}\n```\n"
            "🔸 輸出：`0 1 2 3 4`\n\n"
            "============================\n"
            "🔹 *範例：while*\n"
            "```cpp\nint i = 0;\nwhile (i < 3) {\n    cout << i << endl;\n    i++;\n}\n```\n"
            "🔸 輸出：`0`、`1`、`2`\n\n"
            "============================\n"
            "🔹 *範例：do while*\n"
            "```cpp\nint i = 0;\ndo {\n    cout << i << endl;\n    i++;\n} while (i < 2);\n```\n"
            "🔸 輸出：`0`、`1`\n\n"
            "============================\n"
            "✅ *何時使用？*\n"
            "- `for` — 適合已知次數的計數器（如 `i = 0; i < N; i++`）\n"
            "- `while` — 不知道確切執行次數時\n"
            "- `do while` — 保證至少執行一次\n\n"
            "💡 試著自己寫寫看吧！",
            parse_mode="Markdown",
            reply_markup=reply_markup)

    elif query.data == "zerotrustss":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="amburanmalll")],
                    [InlineKeyboardButton("最後一章",callback_data="anasnimetsmenyaremenlousvi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++：字串（Strings）*\n\n"
                                      "🔹 *什麼是字串？*\n"
                                      "— 一連串的字元，例如名字或詞句。\n"
                                      "— 在 C++ 中，你可以使用字元陣列（char array）或 `std::string` 類別。\n\n"
                                      "============================\n"
                                      "🔹 *字串作為字元陣列：*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\n```\n"
                                      "🔸 `\\0` 字元會自動加在字串末尾，用來標記字串結束。\n"
                                      "🔸 陣列大小必須大於字串長度。\n\n"
                                      "============================\n"
                                      "🔹 *使用 `std::string`：*\n"
                                      "```cpp\n#include <string>\n\nstd::string city = \"Baku\";\n```\n"
                                      "— 這種方法更簡單也更安全。\n\n"
                                      "============================\n"
                                      "🔹 *基本操作：*\n"
                                      "```cpp\nstd::string name = \"Tom\";\n\n"
                                      "cout << name << endl;         // 輸出字串\n"
                                      "cout << name.length() << endl; // 字串長度\n"
                                      "name += \" Hardy\";             // 串接字串\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *從使用者輸入字串：*\n"
                                      "```cpp\nstd::string userName;\ncout << \"Enter name: \";\ncin >> userName;\n```\n"
                                      "❗ `cin` 讀取到第一個空白即停止。如需整句輸入：\n"
                                      "```cpp\nstd::string fullName;\ngetline(cin, fullName);\n```\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- `std::string` 比字元陣列更簡單安全\n"
                                      "- 可以輕鬆串接、取得長度、搜尋字元\n"
                                      "- 處理西里爾文或其他 Unicode 可能需設定編碼\n\n"
                                      "💡 字串是處理文字、表單、訊息的基礎！\n"
                                      "試著建立字串並輸出吧！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "anasnimetsmenyaremenlousvi":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="zerotrustss")],
                    [InlineKeyboardButton("最後一章", callback_data="crchemaadsasdadad")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++：陣列（Arrays）*\n\n"
                                      "🔹 *什麼是陣列？*\n"
                                      "— 一組**相同類型**的元素，連續存放於記憶體中。\n"
                                      "— 每個元素有自己的索引（從 0 開始）。\n\n"
                                      "============================\n"
                                      "🔹 *陣列範例：*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\n```\n"
                                      "— 建立一個包含 5 個 int 元素的陣列。\n\n"
                                      "🔸 存取元素：\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *用迴圈輸出所有元素：*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << numbers[i] << \" \";\n}\n```\n"
                                      "🔸 輸出結果：`10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *從使用者輸入值：*\n"
                                      "```cpp\nint a[3];\nfor (int i = 0; i < 3; i++) {\n    cin >> a[i];\n}\n```\n"
                                      "🔸 將 3 個數字儲存在陣列中。\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- 索引從 `0` 到 `n - 1`\n"
                                      "- 超出陣列邊界會造成錯誤（未定義行為）❌\n"
                                      "- 所有元素必須是相同類型（int、float、char 等）\n\n"
                                      "💡 陣列是基礎。透過陣列，你會學到記憶體管理、排序與演算法！\n\n"
                                      "試著建立陣列並輸出元素吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "amburanmalll":
        keyboard = [
                    [InlineKeyboardButton("最後一章",callback_data="rytttttt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C++：函式（Functions）*\n\n"
                                      "🔹 *什麼是函式？*\n"
                                      "— 一段執行特定任務的程式碼區塊。\n"
                                      "— 幫助組織程式碼並避免重複。\n\n"
                                      "============================\n"
                                      "🔹 *簡單的函式：*\n"
                                      "```cpp\nvoid sayHello() {\n    cout << \"Hello, world!\" << endl;\n}\n\nint main() {\n    sayHello();\n    return 0;\n}\n```\n"
                                      "— `void` 表示函式無回傳值。\n"
                                      "— 透過函式名稱呼叫。\n\n"
                                      "============================\n"
                                      "🔹 *帶參數的函式：*\n"
                                      "```cpp\nvoid greet(string name) {\n    cout << \"Hello, \" << name << endl;\n}\n\nint main() {\n    greet(\"Alice\");\n    return 0;\n}\n```\n"
                                      "— 可以傳入資料給函式。\n"
                                      "— 參數在宣告時寫在括號中。\n\n"
                                      "============================\n"
                                      "🔹 *有回傳值的函式：*\n"
                                      "```cpp\nint square(int x) {\n    return x * x;\n}\n\nint main() {\n    int res = square(5);\n    cout << res;\n    return 0;\n}\n```\n"
                                      "— 指定回傳型別（如 `int`）。\n"
                                      "— 使用 `return` 回傳結果。\n\n"
                                      "============================\n"
                                      "✅ *為何函式重要？*\n"
                                      "- 使程式碼更精簡與清晰\n"
                                      "- 可重複使用相同程式碼\n"
                                      "- 易於拆分成多個部分\n\n"
                                      "💡 嘗試寫一個函式，傳入兩個數字並回傳它們的和！\n"
                                      "函式是良好 C++ 程式碼的基礎！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "rytttttt":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="amburanmalll")],
                    [InlineKeyboardButton("最後一章", callback_data="anasnimetsmenyaremenlousvi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++：字串（Strings）*\n\n"
                                      "🔹 *什麼是字串？*\n"
                                      "— 一連串的字元，例如名字或詞句。\n"
                                      "— 在 C++ 中，你可以使用字元陣列（char array）或 `std::string` 類別。\n\n"
                                      "============================\n"
                                      "🔹 *字串作為字元陣列：*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\n```\n"
                                      "🔸 `\\0` 字元會自動加在字串末尾，用來標記字串結束。\n"
                                      "🔸 陣列大小必須大於字串長度。\n\n"
                                      "============================\n"
                                      "🔹 *使用 `std::string`：*\n"
                                      "```cpp\n#include <string>\n\nstd::string city = \"Baku\";\n```\n"
                                      "— 這種方法更簡單也更安全。\n\n"
                                      "============================\n"
                                      "🔹 *基本操作：*\n"
                                      "```cpp\nstd::string name = \"Tom\";\n\n"
                                      "cout << name << endl;         // 輸出字串\n"
                                      "cout << name.length() << endl; // 字串長度\n"
                                      "name += \" Hardy\";             // 串接字串\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *從使用者輸入字串：*\n"
                                      "```cpp\nstd::string userName;\ncout << \"Enter name: \";\ncin >> userName;\n```\n"
                                      "❗ `cin` 讀取到第一個空白即停止。如需整句輸入：\n"
                                      "```cpp\nstd::string fullName;\ngetline(cin, fullName);\n```\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- `std::string` 比字元陣列更簡單安全\n"
                                      "- 可以輕鬆串接、取得長度、搜尋字元\n"
                                      "- 處理西里爾文或其他 Unicode 可能需設定編碼\n\n"
                                      "💡 字串是處理文字、表單、訊息的基礎！\n"
                                      "試著建立字串並輸出吧！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "jvonesss":
        keyboard = [[InlineKeyboardButton("⚙ 開始", callback_data="lexustt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("開始吧！ \n第 1 章：", reply_markup=reply_markup)
    elif query.data == "lexustt":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="lexx")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript 安裝與入門：*\n\n"
                                      "🔹 *步驟 1：下載編輯器*\n"
                                      "[下載 Visual Studio Code](https://code.visualstudio.com/)\n\n"
                                      "🔹 *步驟 2：確認 Node.js 是否安裝*\n"
                                      "[下載 Node.js](https://nodejs.org/)\n"
                                      "— 安裝後執行版本確認指令：\n"
                                      "`node --version`\n\n"
                                      "🔹 *步驟 3：簡單程式碼：*\n"
                                      "建立檔案 `main.js`，內容：\n"
                                      "```js\nconsole.log(\"Hello, world!\");\n```\n"
                                      "在終端機執行：\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript 是你邁向製作網站、機器人和應用程式的第一步！*",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "lexx":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="lextutu")],
                    [InlineKeyboardButton("最後一章",callback_data="zatofotkipizdatiyeele")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript：變數與資料類型*\n\n"
                                      "🔹 *什麼是變數？*\n"
                                      "— 是用來儲存資料的命名容器。\n"
                                      "— 使用 `let`、`const`，或舊版的 `var` 來宣告。\n\n"
                                      "🔹 *範例：*\n"
                                      "`let age = 15;`\n"
                                      "`const pi = 3.14;`\n"
                                      "`let name = \"Tom\";`\n"
                                      "`let isOnline = true;`\n\n"
                                      "🔹 *輸出到控制台：*\n"
                                      "```js\nlet age = 15;\nlet name = \"Tom\";\nconsole.log(\"Name:\", name);\nconsole.log(\"Age:\", age);\n```\n"
                                      "💡 *提示：* 不變的值用 `const`，可變的用 `let`。",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "zatofotkipizdatiyeele":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="lexx")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript 安裝與入門：*\n\n"
                                      "🔹 *步驟 1：下載編輯器*\n"
                                      "[下載 Visual Studio Code](https://code.visualstudio.com/)\n\n"
                                      "🔹 *步驟 2：確認 Node.js 是否安裝*\n"
                                      "[下載 Node.js](https://nodejs.org/)\n"
                                      "— 安裝後執行版本確認指令：\n"
                                      "`node --version`\n\n"
                                      "🔹 *步驟 3：簡單程式碼：*\n"
                                      "建立檔案 `main.js`，內容：\n"
                                      "```js\nconsole.log(\"Hello, world!\");\n```\n"
                                      "在終端機執行：\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript 是你邁向製作網站、機器人和應用程式的第一步！*",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "lextutu":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="porsc")],
                    [InlineKeyboardButton("最後一章",callback_data="kaknasoxranenkaxe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript：條件判斷與比較*\n\n"
                                      "🔹 *什麼是條件？*\n"
                                      "— 是一種檢查，當條件為 `true` 時，區塊內的程式碼會執行。\n"
                                      "— 在 JavaScript 中，使用 `if` 語句來實現。\n\n"
                                      "🔹 *範例：*\n"
                                      "```js\nlet age = 18;\nif (age >= 18) {\n    console.log(\"允許進入\");\n} else {\n    console.log(\"拒絕進入\");\n}\n```\n\n"
                                      "🔹 *比較運算子：*\n"
                                      "`==` — 值相等（會自動轉型）\n"
                                      "`===` — 嚴格相等（類型和值都相等）\n"
                                      "`!=` — 不等於（值比較）\n"
                                      "`!==` — 嚴格不等（類型或值不同）\n"
                                      "`>` — 大於\n"
                                      "`<` — 小於\n"
                                      "`>=` — 大於或等於\n"
                                      "`<=` — 小於或等於\n\n"
                                      "💡 *重要提示：* 建議使用 `===` 和 `!==` 以避免因類型轉換引起的錯誤。",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "kaknasoxranenkaxe":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="lextutu")],
                    [InlineKeyboardButton("最後一章", callback_data="zatofotkipizdatiyeele")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript：變數與資料類型*\n\n"
                                      "🔹 *什麼是變數？*\n"
                                      "— 是用來儲存資料的命名容器。\n"
                                      "— 使用 `let`、`const`，或舊版的 `var` 來宣告。\n\n"
                                      "🔹 *範例：*\n"
                                      "`let age = 15;`\n"
                                      "`const pi = 3.14;`\n"
                                      "`let name = \"Tom\";`\n"
                                      "`let isOnline = true;`\n\n"
                                      "🔹 *輸出到控制台：*\n"
                                      "```js\nlet age = 15;\nlet name = \"Tom\";\nconsole.log(\"Name:\", name);\nconsole.log(\"Age:\", age);\n```\n"
                                      "💡 *提示：* 不變的值用 `const`，可變的用 `let`。",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "porsc":
        keyboard = [[InlineKeyboardButton("下一章➡️️", callback_data="ferrarir")],
                    [InlineKeyboardButton("最後一章",callback_data="crzenxoaskxce")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript：邏輯運算子*\n\n"
                                      "🔹 *什麼是邏輯運算子？*\n"
                                      "— 用來組合多個條件判斷。\n"
                                      "— 可以同時檢查多個條件是否成立。\n\n"
                                      "🔹 *常見的邏輯運算子：*\n"
                                      "`&&` — 且（所有條件都必須為真）\n"
                                      "`||` — 或（至少一個條件為真）\n"
                                      "`!` — 非（取反，改變條件的真假）\n\n"
                                      "🔹 *範例：*\n"
                                      "```js\nlet age = 20;\nlet hasPassport = true;\n\nif (age >= 18 && hasPassport) {\n    console.log(\"允許進入\");\n} else {\n    console.log(\"拒絕進入\");\n}\n```\n\n"
                                      "```js\nlet isOnline = false;\nif (!isOnline) {\n    console.log(\"用戶離線\");\n}\n```\n\n"
                                      "💡 *重要提示：* 括號優先計算，接著才是邏輯運算。",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "crzenxoaskxce":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="porsc")],
                    [InlineKeyboardButton("最後一章", callback_data="kaknasoxranenkaxe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript：條件判斷與比較*\n\n"
                                      "🔹 *什麼是條件？*\n"
                                      "— 是一種檢查，當條件為 `true` 時，區塊內的程式碼會執行。\n"
                                      "— 在 JavaScript 中，使用 `if` 語句來實現。\n\n"
                                      "🔹 *範例：*\n"
                                      "```js\nlet age = 18;\nif (age >= 18) {\n    console.log(\"允許進入\");\n} else {\n    console.log(\"拒絕進入\");\n}\n```\n\n"
                                      "🔹 *比較運算子：*\n"
                                      "`==` — 值相等（會自動轉型）\n"
                                      "`===` — 嚴格相等（類型和值都相等）\n"
                                      "`!=` — 不等於（值比較）\n"
                                      "`!==` — 嚴格不等（類型或值不同）\n"
                                      "`>` — 大於\n"
                                      "`<` — 小於\n"
                                      "`>=` — 大於或等於\n"
                                      "`<=` — 小於或等於\n\n"
                                      "💡 *重要提示：* 建議使用 `===` 和 `!==` 以避免因類型轉換引起的錯誤。",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "ferrarir":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="doddo")],
                    [InlineKeyboardButton("最後一章",callback_data="crchemolvkofdovosmcmoe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript：迴圈*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 用來重複執行一段程式碼多次。\n"
                                      "— 常用於操作陣列、重複任務和自動化。\n\n"
                                      "============================\n"
                                      "🔹 *for 迴圈*\n"
                                      "```js\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n```\n"
                                      "— 印出從 0 到 4 的數字。\n"
                                      "`i++` 表示每次迴圈後計數器加 1。\n\n"
                                      "============================\n"
                                      "🔹 *while 迴圈*\n"
                                      "```js\nlet x = 0;\nwhile (x < 3) {\n    console.log(x);\n    x++;\n}\n```\n"
                                      "— 只要 `x < 3`，就重複執行區塊內的程式碼。\n\n"
                                      "============================\n"
                                      "🔹 *do...while 迴圈*\n"
                                      "```js\nlet y = 0;\ndo {\n    console.log(y);\n    y++;\n} while (y < 2);\n```\n"
                                      "— 無論條件是否成立，至少執行一次程式碼。\n\n"
                                      "============================\n"
                                      "🔹 *範例：迭代陣列元素*\n"
                                      "```js\nlet fruits = [\"🍎\", \"🍌\", \"🍇\"];\nfor (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}\n```\n"
                                      "— 逐一讀取陣列中的所有元素。\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- 小心造成無限迴圈（記得更新計數器！）\n"
                                      "- 使用 `break` 可以跳出迴圈\n"
                                      "- 使用 `continue` 可以跳過本次迭代\n\n"
                                      "💡 迴圈是處理資料結構和自動化任務的關鍵工具！\n"
                                      "試試寫一個迴圈，從 10 倒數到 1！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "crchemolvkofdovosmcmoe":
        keyboard = [[InlineKeyboardButton("下一章➡️️", callback_data="ferrarir")],
                    [InlineKeyboardButton("最後一章", callback_data="crzenxoaskxce")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript：邏輯運算子*\n\n"
                                      "🔹 *什麼是邏輯運算子？*\n"
                                      "— 用來組合多個條件判斷。\n"
                                      "— 可以同時檢查多個條件是否成立。\n\n"
                                      "🔹 *常見的邏輯運算子：*\n"
                                      "`&&` — 且（所有條件都必須為真）\n"
                                      "`||` — 或（至少一個條件為真）\n"
                                      "`!` — 非（取反，改變條件的真假）\n\n"
                                      "🔹 *範例：*\n"
                                      "```js\nlet age = 20;\nlet hasPassport = true;\n\nif (age >= 18 && hasPassport) {\n    console.log(\"允許進入\");\n} else {\n    console.log(\"拒絕進入\");\n}\n```\n\n"
                                      "```js\nlet isOnline = false;\nif (!isOnline) {\n    console.log(\"用戶離線\");\n}\n```\n\n"
                                      "💡 *重要提示：* 括號優先計算，接著才是邏輯運算。",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "doddo":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="srtdemonessa")],
                    [InlineKeyboardButton("最後一章",callback_data="dislikeeverthynlovevelo")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("""⚙️ *JavaScript：函式介紹*\n\n
🔹 *什麼是函式？*\n
— 有名字的程式碼區塊，用來執行特定任務。\n
— 你可以重複呼叫，而不需要重複撰寫相同程式碼。\n
— 它是結構化程式設計的基礎。\n\n
🔹 *為什麼要使用函式？*\n
✔ 避免重複程式碼\n
✔ 將程式分成邏輯模組\n
✔ 可以接收參數（arguments）並回傳結果\n\n
🔹 *簡單的函式範例：*\n
```js
function sayHello() {
  console.log("Hello!");
}

sayHello(); // 呼叫函式
```\n
💡 `sayHello` 每次被呼叫時，會印出 "Hello!"。\n\n
🔹 *有參數的函式：*\n
```js
function greet(name) {
  console.log("Hello, " + name);
}

greet("Tom");
greet("Anna");
```\n
💡 `name` 參數允許你傳入不同的值，靈活控制輸出。\n\n
🔹 *回傳值的函式：*\n
```js
function square(number) {
  return number * number;
}

console.log(square(4)); // 16
```\n
💡 `return` 用來將結果傳回，供其他地方使用。\n\n
🔹 *請記住：*\n
✔ 函式必須先定義再呼叫\n
✔ 內部程式碼只有在呼叫時才會執行\n
✔ 可以傳入多個參數\n\n
函式讓你的程式碼更乾淨、更有彈性，也更容易維護！
""",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "dislikeeverthynlovevelo":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="doddo")],
                    [InlineKeyboardButton("最後一章", callback_data="crchemolvkofdovosmcmoe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript：迴圈*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 用來重複執行一段程式碼多次。\n"
                                      "— 常用於操作陣列、重複任務和自動化。\n\n"
                                      "============================\n"
                                      "🔹 *for 迴圈*\n"
                                      "```js\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n```\n"
                                      "— 印出從 0 到 4 的數字。\n"
                                      "`i++` 表示每次迴圈後計數器加 1。\n\n"
                                      "============================\n"
                                      "🔹 *while 迴圈*\n"
                                      "```js\nlet x = 0;\nwhile (x < 3) {\n    console.log(x);\n    x++;\n}\n```\n"
                                      "— 只要 `x < 3`，就重複執行區塊內的程式碼。\n\n"
                                      "============================\n"
                                      "🔹 *do...while 迴圈*\n"
                                      "```js\nlet y = 0;\ndo {\n    console.log(y);\n    y++;\n} while (y < 2);\n```\n"
                                      "— 無論條件是否成立，至少執行一次程式碼。\n\n"
                                      "============================\n"
                                      "🔹 *範例：迭代陣列元素*\n"
                                      "```js\nlet fruits = [\"🍎\", \"🍌\", \"🍇\"];\nfor (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}\n```\n"
                                      "— 逐一讀取陣列中的所有元素。\n\n"
                                      "============================\n"
                                      "✅ *重要提醒：*\n"
                                      "- 小心造成無限迴圈（記得更新計數器！）\n"
                                      "- 使用 `break` 可以跳出迴圈\n"
                                      "- 使用 `continue` 可以跳過本次迭代\n\n"
                                      "💡 迴圈是處理資料結構和自動化任務的關鍵工具！\n"
                                      "試試寫一個迴圈，從 10 倒數到 1！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "srtdemonessa":
        keyboard = [[InlineKeyboardButton("最後一章",callback_data="noanotherpower")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *JavaScript：物件 (Objects)*\n\n"
                                      "🔹 *什麼是物件？*\n"
                                      "— 用來存放相關資料和功能的結構。\n"
                                      "— 使用「鍵：值」的形式組成。\n\n"
                                      "============================\n"
                                      "🔹 *簡單物件範例：*\n"
                                      "```js\n"
                                      "let person = {\n"
                                      "  name: \"Tom\",\n"
                                      "  age: 25,\n"
                                      "  isStudent: true\n"
                                      "};\n"
                                      "```\n"
                                      "🔸 存取屬性：\n"
                                      "`person.name` → \"Tom\"\n"
                                      "`person[\"age\"]` → 25\n\n"
                                      "============================\n"
                                      "🔹 *包含方法的物件：*\n"
                                      "```js\n"
                                      "let car = {\n"
                                      "  brand: \"Toyota\",\n"
                                      "  start: function() {\n"
                                      "    console.log(\"引擎啟動\");\n"
                                      "  }\n"
                                      "};\n\n"
                                      "car.start();\n"
                                      "```\n"
                                      "============================\n"
                                      "✅ *為什麼使用物件？*\n"
                                      "- 將複雜資料集中管理\n"
                                      "- 模擬現實世界的事物\n"
                                      "- 廣泛用於 DOM 操作、API 處理等\n\n"
                                      "💡 試著建立一個 \"phone\" 物件，包含 \"model\"、\"year\" 屬性與 \"call()\" 方法吧！",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "noanotherpower":
        keyboard = [[InlineKeyboardButton("下一章➡️", callback_data="srtdemonessa")],
                    [InlineKeyboardButton("最後一章", callback_data="dislikeeverthynlovevelo")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("""⚙️ *JavaScript：函式介紹*\n\n
        🔹 *什麼是函式？*\n
        — 有名字的程式碼區塊，用來執行特定任務。\n
        — 你可以重複呼叫，而不需要重複撰寫相同程式碼。\n
        — 它是結構化程式設計的基礎。\n\n
        🔹 *為什麼要使用函式？*\n
        ✔ 避免重複程式碼\n
        ✔ 將程式分成邏輯模組\n
        ✔ 可以接收參數（arguments）並回傳結果\n\n
        🔹 *簡單的函式範例：*\n
        ```js
        function sayHello() {
          console.log("Hello!");
        }

        sayHello(); // 呼叫函式
        ```\n
        💡 `sayHello` 每次被呼叫時，會印出 "Hello!"。\n\n
        🔹 *有參數的函式：*\n
        ```js
        function greet(name) {
          console.log("Hello, " + name);
        }

        greet("Tom");
        greet("Anna");
        ```\n
        💡 `name` 參數允許你傳入不同的值，靈活控制輸出。\n\n
        🔹 *回傳值的函式：*\n
        ```js
        function square(number) {
          return number * number;
        }

        console.log(square(4)); // 16
        ```\n
        💡 `return` 用來將結果傳回，供其他地方使用。\n\n
        🔹 *請記住：*\n
        ✔ 函式必須先定義再呼叫\n
        ✔ 內部程式碼只有在呼叫時才會執行\n
        ✔ 可以傳入多個參數\n\n
        函式讓你的程式碼更乾淨、更有彈性，也更容易維護！
        """,
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "java_start":
        keyboard = [[InlineKeyboardButton("☕ 開始學習 Java", callback_data="valley")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Java", reply_markup=reply_markup)
    elif query.data == "valley":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="rebirtha")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java：安裝與建立第一個項目*\n\n"
                                      "🔹 *步驟 1：下載並安裝 JDK*\n"
                                      "[🔗 官方下載頁面](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— 請選擇適合你作業系統的 Java SE Development Kit (JDK)\n"
                                      "— 安裝時請勾選 `Add JAVA to PATH`（若有選項）\n\n"
                                      "🔹 *步驟 2：驗證安裝是否成功*\n"
                                      "打開終端機（命令提示字元），輸入：\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "若出現版本資訊，代表安裝成功！\n\n"
                                      "🔹 *步驟 3：安裝開發工具（IDE）*\n"
                                      "✅ [IntelliJ IDEA Community（推薦）](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + Java 擴充套件](https://code.visualstudio.com/)\n\n"
                                      "🔹 *步驟 4：寫下你的第一段 Java 程式碼！*\n"
                                      "建立一個名為 `Main.java` 的檔案，輸入：\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "接著在終端機執行：\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ 預期輸出：`Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *你已經準備好開始學習 Java！*\n"
                                      "接下來將學習：變數、條件判斷、迴圈、函式與物件導向程式設計！\n\n"
                                      "👇 點擊下方按鈕，開始下一課！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "rebirtha":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="silikone")],
                    [InlineKeyboardButton("最後一章",callback_data="racecurse")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java：變數與資料型別*\n\n"
                                      "🔹 *什麼是變數？*\n"
                                      "— 變數是用來儲存資料的名字。\n"
                                      "— 每個變數必須先定義它的資料型別。\n\n"
                                      "🔹 *基本資料型別：*\n"
                                      "- `int`：整數，如 `42`\n"
                                      "- `double`：小數，如 `3.14`\n"
                                      "- `char`：單一字元，如 `'A'`\n"
                                      "- `boolean`：邏輯值，`true` 或 `false`\n"
                                      "- `String`：字串，如 `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *宣告與使用變數：*\n"
                                      "```java\nint age = 18;\ndouble pi = 3.14;\nchar grade = 'A';\nboolean isStudent = true;\nString name = \"Tom\";\n```\n\n"
                                      "🔸 使用 `System.out.println()` 印出變數：\n"
                                      "```java\nSystem.out.println(name);\nSystem.out.println(age);\n```\n"
                                      "🔸 輸出：\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *小提醒：*\n"
                                      "- Java 是強型別語言，每個變數都要定義型別。\n"
                                      "- 變數名稱區分大小寫：`Name` ≠ `name`\n"
                                      "- 命名請清楚：`int n = 5;` ❌，`int score = 5;` ✅\n\n"
                                      "💡 嘗試宣告一些自己的變數，並用 `System.out.println()` 印出來吧！",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "racecurse":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="rebirtha")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java：安裝與建立第一個項目*\n\n"
                                      "🔹 *步驟 1：下載並安裝 JDK*\n"
                                      "[🔗 官方下載頁面](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— 請選擇適合你作業系統的 Java SE Development Kit (JDK)\n"
                                      "— 安裝時請勾選 `Add JAVA to PATH`（若有選項）\n\n"
                                      "🔹 *步驟 2：驗證安裝是否成功*\n"
                                      "打開終端機（命令提示字元），輸入：\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "若出現版本資訊，代表安裝成功！\n\n"
                                      "🔹 *步驟 3：安裝開發工具（IDE）*\n"
                                      "✅ [IntelliJ IDEA Community（推薦）](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + Java 擴充套件](https://code.visualstudio.com/)\n\n"
                                      "🔹 *步驟 4：寫下你的第一段 Java 程式碼！*\n"
                                      "建立一個名為 `Main.java` 的檔案，輸入：\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "接著在終端機執行：\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ 預期輸出：`Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *你已經準備好開始學習 Java！*\n"
                                      "接下來將學習：變數、條件判斷、迴圈、函式與物件導向程式設計！\n\n"
                                      "👇 點擊下方按鈕，開始下一課！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "silikone":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="silikon")],
                    [InlineKeyboardButton("最後一章",callback_data="lewiskasdkknknwoe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Java: 條件語句 (if, else, else if)*\n\n"
                                      "🔹 *什麼是條件語句？*\n"
                                      "— 讓程式根據不同條件執行不同的代碼。\n\n"
                                      "============================\n"
                                      "🔹 *範例代碼:*\n"
                                      "```java\n"
                                      "if (age >= 18) {\n"
                                      "    System.out.println(\"你是成年人\");\n"
                                      "} else if (age >= 14) {\n"
                                      "    System.out.println(\"你是青少年\");\n"
                                      "} else {\n"
                                      "    System.out.println(\"你是小孩\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *比較運算符:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
                                      "🔹 *邏輯運算符:* `&&` (且), `||` (或), `!` (非)\n\n"
                                      "✅ *試試看：*\n"
                                      "寫一段程式，根據年齡輸出對應訊息！",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "lewiskasdkknknwoe":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="silikone")],
                    [InlineKeyboardButton("最後一章", callback_data="racecurse")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java：變數與資料型別*\n\n"
                                      "🔹 *什麼是變數？*\n"
                                      "— 變數是用來儲存資料的名字。\n"
                                      "— 每個變數必須先定義它的資料型別。\n\n"
                                      "🔹 *基本資料型別：*\n"
                                      "- `int`：整數，如 `42`\n"
                                      "- `double`：小數，如 `3.14`\n"
                                      "- `char`：單一字元，如 `'A'`\n"
                                      "- `boolean`：邏輯值，`true` 或 `false`\n"
                                      "- `String`：字串，如 `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *宣告與使用變數：*\n"
                                      "```java\nint age = 18;\ndouble pi = 3.14;\nchar grade = 'A';\nboolean isStudent = true;\nString name = \"Tom\";\n```\n\n"
                                      "🔸 使用 `System.out.println()` 印出變數：\n"
                                      "```java\nSystem.out.println(name);\nSystem.out.println(age);\n```\n"
                                      "🔸 輸出：\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *小提醒：*\n"
                                      "- Java 是強型別語言，每個變數都要定義型別。\n"
                                      "- 變數名稱區分大小寫：`Name` ≠ `name`\n"
                                      "- 命名請清楚：`int n = 5;` ❌，`int score = 5;` ✅\n\n"
                                      "💡 嘗試宣告一些自己的變數，並用 `System.out.println()` 印出來吧！",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "silikon":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="silik")],
                    [InlineKeyboardButton("最後一章",callback_data="vistoriyuonvikladivayetgrustniyeblete")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: 迴圈 (Loops)*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 讓程式重複執行某段代碼，直到條件不成立。\n"
                                      "— 常用於處理重複任務和遍歷資料。\n\n"
                                      "============================\n"
                                      "🔹 *for 迴圈範例:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— 輸出 0 到 4。\n\n"
                                      "============================\n"
                                      "🔹 *while 迴圈範例:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *do...while 迴圈範例:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— 無論條件是否成立，至少執行一次。\n\n"
                                      "============================\n"
                                      "✅ *重要提示:*\n"
                                      "- 小心避免無限迴圈\n"
                                      "- 使用 `break` 終止迴圈\n"
                                      "- 使用 `continue` 跳過本次迴圈\n\n"
                                      "💡 嘗試寫一個迴圈，從 10 倒數到 1！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "vistoriyuonvikladivayetgrustniyeblete":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="silikon")],
                    [InlineKeyboardButton("最後一章", callback_data="lewiskasdkknknwoe")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Java: 條件語句 (if, else, else if)*\n\n"
                                      "🔹 *什麼是條件語句？*\n"
                                      "— 讓程式根據不同條件執行不同的代碼。\n\n"
                                      "============================\n"
                                      "🔹 *範例代碼:*\n"
                                      "```java\n"
                                      "if (age >= 18) {\n"
                                      "    System.out.println(\"你是成年人\");\n"
                                      "} else if (age >= 14) {\n"
                                      "    System.out.println(\"你是青少年\");\n"
                                      "} else {\n"
                                      "    System.out.println(\"你是小孩\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *比較運算符:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
                                      "🔹 *邏輯運算符:* `&&` (且), `||` (或), `!` (非)\n\n"
                                      "✅ *試試看：*\n"
                                      "寫一段程式，根據年齡輸出對應訊息！",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "silik":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="siuu")],
                    [InlineKeyboardButton("最後一章",callback_data="tictoxocesnaveshatinogdaddedushku")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java：陣列 (Arrays)*\n\n"
                                      "🔹 *什麼是陣列？*\n"
                                      "— 陣列是同類型元素的集合，順序排列並儲存在記憶體中。\n"
                                      "— 每個元素都有索引（從 0 開始）。\n\n"
                                      "============================\n"
                                      "🔹 *建立一個整數陣列：*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— 建立含有 5 個整數的陣列。\n\n"
                                      "🔸 取得元素：\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *用 for 迴圈輸出所有元素：*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— 使用 `numbers.length` 表示陣列長度。\n\n"
                                      "============================\n"
                                      "🔹 *從用戶輸入元素：*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— 儲存用戶輸入的 3 個數字。\n\n"
                                      "============================\n"
                                      "✅ *重點提示：*\n"
                                      "- 索引從 `0` 到 `n - 1`\n"
                                      "- 陣列大小不可變\n"
                                      "- 超出索引範圍會導致錯誤 (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 陣列是學習資料結構、排序與演算法的起點！試試寫一個陣列並顯示它的內容吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "tictoxocesnaveshatinogdaddedushku":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="silik")],
                    [InlineKeyboardButton("最後一章", callback_data="vistoriyuonvikladivayetgrustniyeblete")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: 迴圈 (Loops)*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 讓程式重複執行某段代碼，直到條件不成立。\n"
                                      "— 常用於處理重複任務和遍歷資料。\n\n"
                                      "============================\n"
                                      "🔹 *for 迴圈範例:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— 輸出 0 到 4。\n\n"
                                      "============================\n"
                                      "🔹 *while 迴圈範例:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *do...while 迴圈範例:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— 無論條件是否成立，至少執行一次。\n\n"
                                      "============================\n"
                                      "✅ *重要提示:*\n"
                                      "- 小心避免無限迴圈\n"
                                      "- 使用 `break` 終止迴圈\n"
                                      "- 使用 `continue` 跳過本次迴圈\n\n"
                                      "💡 嘗試寫一個迴圈，從 10 倒數到 1！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "siuu":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="suii")],
                    [InlineKeyboardButton("最後一章",callback_data="odinbiznesmenustavsiyotsvoyegostarika")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java：方法（Functions）*\n\n"
                                      "🔹 *什麼是方法？*\n"
                                      "— 方法（Method）是一段執行特定任務的程式碼區塊。\n"
                                      "— 你可以多次呼叫它，而不需重複寫代碼。\n\n"
                                      "============================\n"
                                      "🔹 *為什麼要使用方法？*\n"
                                      "✔️ 避免重複代碼\n"
                                      "✔️ 程式更清晰、易於維護\n"
                                      "✔️ 可以接收參數並傳回結果\n\n"
                                      "============================\n"
                                      "🔹 *簡單範例：*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"你好！\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // 呼叫方法\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— `sayHello` 方法會印出 \"你好！\"。\n\n"
                                      "============================\n"
                                      "🔹 *帶參數的方法：*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"你好, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"小明\");\n"
                                      "```\n"
                                      "— 參數讓方法變得更靈活。\n\n"
                                      "============================\n"
                                      "🔹 *有回傳值的方法：*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— 使用 `return` 回傳計算結果。\n\n"
                                      "============================\n"
                                      "✅ *記住：*\n"
                                      "- 所有方法必須放在類別（class）中\n"
                                      "- `main()` 是程式的進入點\n"
                                      "- `void` 表示不回傳任何資料\n\n"
                                      "💡 嘗試自己寫一個方法，印出你的名字或計算兩數相加！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "odinbiznesmenustavsiyotsvoyegostarika":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="siuu")],
                    [InlineKeyboardButton("最後一章", callback_data="tictoxocesnaveshatinogdaddedushku")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java：陣列 (Arrays)*\n\n"
                                      "🔹 *什麼是陣列？*\n"
                                      "— 陣列是同類型元素的集合，順序排列並儲存在記憶體中。\n"
                                      "— 每個元素都有索引（從 0 開始）。\n\n"
                                      "============================\n"
                                      "🔹 *建立一個整數陣列：*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— 建立含有 5 個整數的陣列。\n\n"
                                      "🔸 取得元素：\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *用 for 迴圈輸出所有元素：*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— 使用 `numbers.length` 表示陣列長度。\n\n"
                                      "============================\n"
                                      "🔹 *從用戶輸入元素：*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— 儲存用戶輸入的 3 個數字。\n\n"
                                      "============================\n"
                                      "✅ *重點提示：*\n"
                                      "- 索引從 `0` 到 `n - 1`\n"
                                      "- 陣列大小不可變\n"
                                      "- 超出索引範圍會導致錯誤 (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 陣列是學習資料結構、排序與演算法的起點！試試寫一個陣列並顯示它的內容吧！",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "suii":
        keyboard = [[InlineKeyboardButton("最後一章",callback_data="etojonnyetomoysinle")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🏗️ *Java：類別與物件（Class & Object）*\n\n"
                                      "🔹 *什麼是類別？*\n"
                                      "— 類別是一種藍圖，用來創建物件。\n"
                                      "— 它定義了物件的屬性（資料）與行為（方法）。\n\n"
                                      "🔹 *什麼是物件？*\n"
                                      "— 是依據類別建立的實體，是程式中的實際成員。\n\n"
                                      "============================\n"
                                      "🔹 *簡單範例：*\n"
                                      "```java\n"
                                      "public class Dog {\n"
                                      "    String name;\n"
                                      "    int age;\n\n"
                                      "    void bark() {\n"
                                      "        System.out.println(name + \"：汪汪！\");\n"
                                      "    }\n"
                                      "}\n\n"
                                      "public class Main {\n"
                                      "    public static void main(String[] args) {\n"
                                      "        Dog myDog = new Dog();\n"
                                      "        myDog.name = \"小黑\";\n"
                                      "        myDog.age = 3;\n"
                                      "        myDog.bark();\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— 類別 `Dog` 有兩個屬性和一個方法。\n"
                                      "— `myDog` 是 `Dog` 的物件，可以呼叫方法與設值。\n\n"
                                      "============================\n"
                                      "🔹 *重要概念：*\n"
                                      "- 類別名要大寫：`Person`, `Car`, `Animal` 等\n"
                                      "- `new` 用來創建物件\n"
                                      "- 方法內可存取該物件的屬性\n\n"
                                      "✅ *類別與物件是 Java 的核心*\n"
                                      "— 幾乎所有 Java 程式都是以物件為中心來設計！\n\n"
                                      "💡 接下來我們會深入學習建構子、封裝、繼承與多型！🚀",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "etojonnyetomoysinle":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="suii")],
                    [InlineKeyboardButton("最後一章", callback_data="odinbiznesmenustavsiyotsvoyegostarika")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java：方法（Functions）*\n\n"
                                      "🔹 *什麼是方法？*\n"
                                      "— 方法（Method）是一段執行特定任務的程式碼區塊。\n"
                                      "— 你可以多次呼叫它，而不需重複寫代碼。\n\n"
                                      "============================\n"
                                      "🔹 *為什麼要使用方法？*\n"
                                      "✔️ 避免重複代碼\n"
                                      "✔️ 程式更清晰、易於維護\n"
                                      "✔️ 可以接收參數並傳回結果\n\n"
                                      "============================\n"
                                      "🔹 *簡單範例：*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"你好！\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // 呼叫方法\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— `sayHello` 方法會印出 \"你好！\"。\n\n"
                                      "============================\n"
                                      "🔹 *帶參數的方法：*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"你好, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"小明\");\n"
                                      "```\n"
                                      "— 參數讓方法變得更靈活。\n\n"
                                      "============================\n"
                                      "🔹 *有回傳值的方法：*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— 使用 `return` 回傳計算結果。\n\n"
                                      "============================\n"
                                      "✅ *記住：*\n"
                                      "- 所有方法必須放在類別（class）中\n"
                                      "- `main()` 是程式的進入點\n"
                                      "- `void` 表示不回傳任何資料\n\n"
                                      "💡 嘗試自己寫一個方法，印出你的名字或計算兩數相加！🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "huggywug":
        keyboard = [[InlineKeyboardButton("開始吧！ \n「」*第 1 章：*", callback_data="yveskarlinaka")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("<<>>", reply_markup=reply_markup)
    elif query.data == "yveskarlinaka":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="mybau")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *安裝 C 與設定 CLion IDE*\n\n"
                                      "🔹 *步驟 1：下載 MinGW 編譯器*\n"
                                      "[下載 MinGW](https://sourceforge.net/projects/mingw/) — 安裝 `gcc` 並將 `bin` 資料夾加入系統環境變數 PATH\n\n"
                                      "🔹 *步驟 2：下載 CLion IDE*\n"
                                      "[下載 CLion](https://www.jetbrains.com/clion/download/) — 安裝社群版或試用版\n\n"
                                      "🔹 *步驟 3：驗證安裝是否成功*\n"
                                      "打開終端機並執行：\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *步驟 4：撰寫一個簡單的 C 程式*\n"
                                      "建立名為 `main.c` 的檔案，輸入以下程式碼：\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *步驟 5：編譯並執行程式*\n"
                                      "在終端機輸入：\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "接著執行：\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *確認輸出：*\n"
                                      "你應該會看到：\n"
                                      "```\nHello, world!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "mybau":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="sixthousand")],
                    [InlineKeyboardButton("最後一章",callback_data="blyatutebyanetpravle")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C 語言中的變數與資料型態*\n\n"
                                      "🔹 *什麼是變數？*\n"
                                      "— 用來在記憶體中儲存資料的名稱。\n"
                                      "— 每個變數都有一個資料型態，決定它所儲存的資料種類。\n\n"
                                      "🔹 *常見的資料型態：*\n"
                                      "- `int` — 整數，例如：`42`\n"
                                      "- `float` — 浮點數，例如：`3.14`\n"
                                      "- `char` — 單一字元，例如：`'A'`\n"
                                      "- `double` — 更精確的浮點數\n\n"
                                      "============================\n"
                                      "🔹 *宣告變數：*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *輸出到螢幕：*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"年齡: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *自己試試看：* 宣告幾個變數並輸出它們的值吧！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "blyatutebyanetpravle":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="mybau")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *安裝 C 與設定 CLion IDE*\n\n"
                                      "🔹 *步驟 1：下載 MinGW 編譯器*\n"
                                      "[下載 MinGW](https://sourceforge.net/projects/mingw/) — 安裝 `gcc` 並將 `bin` 資料夾加入系統環境變數 PATH\n\n"
                                      "🔹 *步驟 2：下載 CLion IDE*\n"
                                      "[下載 CLion](https://www.jetbrains.com/clion/download/) — 安裝社群版或試用版\n\n"
                                      "🔹 *步驟 3：驗證安裝是否成功*\n"
                                      "打開終端機並執行：\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *步驟 4：撰寫一個簡單的 C 程式*\n"
                                      "建立名為 `main.c` 的檔案，輸入以下程式碼：\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *步驟 5：編譯並執行程式*\n"
                                      "在終端機輸入：\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "接著執行：\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *確認輸出：*\n"
                                      "你應該會看到：\n"
                                      "```\nHello, world!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "sixthousand":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="idgaf")],
                    [InlineKeyboardButton("最後一章",callback_data="cposlsacmmcnjfdie")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C 語言中的運算子與運算式*\n\n"
                                      "🔹 *什麼是運算子？*\n"
                                      "— 用來對資料執行操作的符號或符號組合。\n\n"
                                      "🔹 *運算子類型：*\n"
                                      "- 算術運算子：`+`、`-`、`*`、`/`、`%`\n"
                                      "- 指派運算子：`=`、`+=`、`-=`、`*=` 等\n"
                                      "- 比較運算子：`==`、`!=`、`<`、`>`、`<=`、`>=`\n"
                                      "- 邏輯運算子：`&&`、`||`、`!`\n\n"
                                      "============================\n"
                                      "🔹 *算術運算範例：*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int sum = a + b;       // 13\n"
                                      "int diff = a - b;      // 7\n"
                                      "int product = a * b;   // 30\n"
                                      "int quotient = a / b;  // 3\n"
                                      "int remainder = a % b; // 1\n"
                                      "```\n\n"
                                      "🔹 *比較與邏輯範例：*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x 小於 y 且 y 是正數\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *自己試試看：* 寫一些包含不同運算子的運算式並輸出結果！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "cposlsacmmcnjfdie":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="sixthousand")],
                    [InlineKeyboardButton("最後一章", callback_data="blyatutebyanetpravle")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C 語言中的變數與資料型態*\n\n"
                                      "🔹 *什麼是變數？*\n"
                                      "— 用來在記憶體中儲存資料的名稱。\n"
                                      "— 每個變數都有一個資料型態，決定它所儲存的資料種類。\n\n"
                                      "🔹 *常見的資料型態：*\n"
                                      "- `int` — 整數，例如：`42`\n"
                                      "- `float` — 浮點數，例如：`3.14`\n"
                                      "- `char` — 單一字元，例如：`'A'`\n"
                                      "- `double` — 更精確的浮點數\n\n"
                                      "============================\n"
                                      "🔹 *宣告變數：*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *輸出到螢幕：*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"年齡: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *自己試試看：* 宣告幾個變數並輸出它們的值吧！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "idgaf":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="frekal")],
                    [InlineKeyboardButton("最後一章",callback_data="sikioxoxcme")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *C 語言中的條件判斷：if、else if、else*\n\n"
                                      "🔹 *什麼是條件判斷？*\n"
                                      "— 根據條件是否成立，來執行不同的程式區塊。\n\n"
                                      "🔹 *if 的語法：*\n"
                                      "```c\n"
                                      "if (條件) {\n"
                                      "    // 當條件為真時執行的程式碼\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *使用 else if 和 else：*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"正數\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"零\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"負數\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *邏輯運算子（用於條件判斷）：*\n"
                                      "- `&&` — 且（AND）\n"
                                      "- `||` — 或（OR）\n"
                                      "- `!` — 非（NOT）\n\n"
                                      "✅ *任務：* 撰寫一個程式，檢查一個數字，並印出它是正數、負數還是零！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "sikioxoxcme":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="idgaf")],
                    [InlineKeyboardButton("最後一章", callback_data="cposlsacmmcnjfdie")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C 語言中的運算子與運算式*\n\n"
                                      "🔹 *什麼是運算子？*\n"
                                      "— 用來對資料執行操作的符號或符號組合。\n\n"
                                      "🔹 *運算子類型：*\n"
                                      "- 算術運算子：`+`、`-`、`*`、`/`、`%`\n"
                                      "- 指派運算子：`=`、`+=`、`-=`、`*=` 等\n"
                                      "- 比較運算子：`==`、`!=`、`<`、`>`、`<=`、`>=`\n"
                                      "- 邏輯運算子：`&&`、`||`、`!`\n\n"
                                      "============================\n"
                                      "🔹 *算術運算範例：*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int sum = a + b;       // 13\n"
                                      "int diff = a - b;      // 7\n"
                                      "int product = a * b;   // 30\n"
                                      "int quotient = a / b;  // 3\n"
                                      "int remainder = a % b; // 1\n"
                                      "```\n\n"
                                      "🔹 *比較與邏輯範例：*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x 小於 y 且 y 是正數\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *自己試試看：* 寫一些包含不同運算子的運算式並輸出結果！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "frekal":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="sybau")],
                    [InlineKeyboardButton("最後一章",callback_data="nkkmlhhnnbbyuooopyytfv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *C 語言中的迴圈：for、while、do-while*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 允許重複執行某段程式碼多次。\n\n"
                                      "🔹 *for 迴圈：*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"第 %d 次迴圈\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *while 迴圈：*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"第 %d 次迴圈\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *do-while 迴圈：*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"第 %d 次迴圈\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *試試看：* 寫一個迴圈，輸出從 1 到 10 的數字！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "nkkmlhhnnbbyuooopyytfv":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="frekal")],
                    [InlineKeyboardButton("最後一章", callback_data="sikioxoxcme")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *C 語言中的條件判斷：if、else if、else*\n\n"
                                      "🔹 *什麼是條件判斷？*\n"
                                      "— 根據條件是否成立，來執行不同的程式區塊。\n\n"
                                      "🔹 *if 的語法：*\n"
                                      "```c\n"
                                      "if (條件) {\n"
                                      "    // 當條件為真時執行的程式碼\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *使用 else if 和 else：*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"正數\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"零\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"負數\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *邏輯運算子（用於條件判斷）：*\n"
                                      "- `&&` — 且（AND）\n"
                                      "- `||` — 或（OR）\n"
                                      "- `!` — 非（NOT）\n\n"
                                      "✅ *任務：* 撰寫一個程式，檢查一個數字，並印出它是正數、負數還是零！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "sybau":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="lmao")],
                    [InlineKeyboardButton("最後一章",callback_data="iouyeryhefyrfvnnvreioaojf2q")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C 語言中的函式（Functions）*\n\n"
                                      "🔹 *什麼是函式？*\n"
                                      "— 是一段執行特定任務的程式碼區塊。\n"
                                      "— 有助於組織程式結構並重複使用代碼。\n\n"
                                      "🔹 *函式的定義與呼叫：*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"哈囉，世界！\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // 呼叫函式\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *帶參數的函式：*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"哈囉, %s！\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Tom\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *有回傳值的函式：*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"5 的平方是 %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *試著寫一個函式，將兩個數相加並回傳結果吧！*\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "iouyeryhefyrfvnnvreioaojf2q":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="sybau")],
                    [InlineKeyboardButton("最後一章", callback_data="nkkmlhhnnbbyuooopyytfv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *C 語言中的迴圈：for、while、do-while*\n\n"
                                      "🔹 *什麼是迴圈？*\n"
                                      "— 允許重複執行某段程式碼多次。\n\n"
                                      "🔹 *for 迴圈：*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"第 %d 次迴圈\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *while 迴圈：*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"第 %d 次迴圈\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *do-while 迴圈：*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"第 %d 次迴圈\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *試試看：* 寫一個迴圈，輸出從 1 到 10 的數字！\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "lmao":
        keyboard = [[InlineKeyboardButton("最後一章",callback_data="crcvjkbkvnbjfgivjfde")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📌 *C 語言中的指標（Pointers）*\n\n"
                                      "🔹 *什麼是指標？*\n"
                                      "— 指標是一種變數，用來儲存另一個變數的記憶體位址。\n"
                                      "— 常用於高效的記憶體操作、陣列與函式處理。\n\n"
                                      "🔹 *基本指標範例：*\n"
                                      "```c\n"
                                      "int x = 10;\n"
                                      "int* ptr = &x;\n"
                                      "printf(\"值：%d\\n\", *ptr); // 解參考\n"
                                      "```\n"
                                      "— `&x` 表示取得變數 `x` 的位址\n"
                                      "— `*ptr` 表示取出該位址所儲存的值\n\n"
                                      "🔹 *說明：*\n"
                                      "- `int* ptr;` — 指向整數的指標\n"
                                      "- `*` — 解參考運算子（取得位址中的值）\n"
                                      "- `&` — 位址運算子（取得變數位址）\n\n"
                                      "============================\n"
                                      "🔹 *透過指標修改值：*\n"
                                      "```c\n"
                                      "int a = 5;\n"
                                      "int* p = &a;\n"
                                      "*p = 100;\n"
                                      "printf(\"%d\\n\", a); // 輸出 100\n"
                                      "```\n"
                                      "✅ 指標可以改變原變數的值。\n\n"
                                      "============================\n"
                                      "🔹 *印出記憶體位址：*\n"
                                      "```c\n"
                                      "int val = 42;\n"
                                      "printf(\"變數的位址：%p\\n\", &val);\n"
                                      "```\n"
                                      "— `%p` 用來印出記憶體位址。\n\n"
                                      "============================\n"
                                      "💡 指標是 C 語言中非常重要的概念。\n"
                                      "它們被廣泛應用於陣列、字串、函式傳遞與動態記憶體管理中。\n\n"
                                      "📎 下一章我們將學習 *陣列與指標（Arrays and Pointers）*！\n",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "crcvjkbkvnbjfgivjfde":
        keyboard = [[InlineKeyboardButton("下一章➡", callback_data="lmao")],
                    [InlineKeyboardButton("最後一章", callback_data="iouyeryhefyrfvnnvreioaojf2q")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C 語言中的函式（Functions）*\n\n"
                                      "🔹 *什麼是函式？*\n"
                                      "— 是一段執行特定任務的程式碼區塊。\n"
                                      "— 有助於組織程式結構並重複使用代碼。\n\n"
                                      "🔹 *函式的定義與呼叫：*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"哈囉，世界！\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // 呼叫函式\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *帶參數的函式：*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"哈囉, %s！\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Tom\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *有回傳值的函式：*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"5 的平方是 %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *試著寫一個函式，將兩個數相加並回傳結果吧！*\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    if query.data == "tuk":
        keyboard = [[InlineKeyboardButton("🔥 Öğrenmeye başlayın", callback_data="mehrab")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Merhaba! Programlama öğrenmeye hazır mısınız?",
            reply_markup=reply_markup)
    elif query.data == "mehrab":
        keyboard = [
            [InlineKeyboardButton("programlama dili", callback_data="zehrab")],
            [InlineKeyboardButton("İnternet güvenliği", callback_data="cyberindo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🚀 Harika! Şimdi ne öğrenmek istediğinizi seçin：",
            reply_markup=reply_markup
        )
    elif query.data == "zehrab":
        keyboard = [
            [InlineKeyboardButton("🐍 Python ", callback_data="ilan")],
            [InlineKeyboardButton("⚙️ C++ ", callback_data="heyvanlar")],
            [InlineKeyboardButton("🟨 Javascript", callback_data="sriplara")],
            [InlineKeyboardButton("☕ Java ", callback_data="java_startings")],
            [InlineKeyboardButton("💻 C", callback_data="priletelivmayami")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Tamam! Şimdi öğrenmek istediğiniz dili seçin",
            reply_markup=reply_markup
        )

    elif query.data == "cyberindo":
        keyboard = [
            [InlineKeyboardButton("📡internet ağı", callback_data="cyberqwak")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Hadi başlayalım! \nBölüm 1:",
            reply_markup=reply_markup
        )

    elif query.data == "cyberqwak":
        keyboard = [
            [InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="nextdat")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 *Ağlar (Networks)* basitçe birbirine bağlı nesnelerdir.\n"
                                      "Örneğin, arkadaş çevren: ortak ilgi alanları, hobiler, beceriler aracılığıyla birbirinize bağlısınız. 🧠🤝\n\n"
                                      "📡 *Ağlar her yerde bulunur:*\n"
                                      "　- 🚇 Şehirdeki toplu taşıma sistemi\n"
                                      "　- ⚡ Ulusal elektrik altyapısı\n"
                                      "　- 🏘️ Komşular arasındaki iletişim\n"
                                      "　- ✉️ Mektup ve kargo gönderen posta sistemleri\n\n"
                                      "💻 *Teknoloji alanında da bu kavram aynıdır, sadece cihazlar arasında uygulanır.*\n"
                                      "Telefonunu düşün 📱: Onu bilgiye erişmek için kullanırsın.\n\n"
                                      "📶 *Cihazların nasıl veri alışverişi yaptığını ve hangi kurallara uyduklarını birlikte öğreneceğiz.*\n\n"
                                      "🖥️ *Bir ağ 2'den milyarlarca cihaza kadar içerebilir:*\n"
                                      "　💻 Dizüstü bilgisayarlar\n"
                                      "　- 📱 Akıllı telefonlar\n"
                                      "　- 📷 Güvenlik kameraları\n"
                                      "　- 🚦 Trafik ışıkları\n"
                                      "　- 🌾 Tarım makineleri\n\n"
                                      "🔌 *Ağlar günlük hayatımızın bir parçası haline gelmiştir:*\n"
                                      "　- ⛅ Hava durumu verilerinin toplanması\n"
                                      "　- ⚡ Evlerin elektrikle beslenmesi\\n"
                                      "　- 🚦 Trafiğin yönetilmesi\n\n"
                                      "🛡️ Ağlar modern hayatın vazgeçilmez bir parçası olduğundan,\n"
                                      "ağın temel prensiplerini anlamak siber güvenlik eğitiminin temelidir.\n\n"
                                      "👥 Aşağıdaki diyagrama bak: Alice, Bob ve Jim kendi küçük ağlarını kurdular!\n"
                                      "Bu konuya daha sonra geri döneceğiz\n\n"
                                      "*İlk bölüm burada başlıyor!*\n*Haydi başlayalım!*",
                                      parse_mode="Markdown"
                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "nextdat":
        keyboard = [
            [InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="twopples")],
            [InlineKeyboardButton("son bölüm", callback_data="chhnbbgbghjve")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Bölüm 2: İnternete Derinlemesine Dalış!*\n\n"
                                      "Artık ağların ne olduğunu biliyorsun — basitçe söylemek gerekirse, birbirine bağlı cihazlardır — şimdi internetin nasıl çalıştığını keşfedelim.\n\n"
                                      "📡 *İnternet*, birbirine bağlı birçok küçük ağdan oluşan *dev bir ağdır*.\n\n"
                                      "👫 Hayal et ki Alice yeni arkadaşlar edindi: Zayn ve Toby\\. Onları Bob ve Jim ile tanıştırmak istiyor. Fakat bir sorun var: sadece Alice her iki grubun dilini anlayabiliyor. Bu yüzden *bir köprü* oluyor ve herkes onun aracılığıyla iletişim kurabiliyor\\. Bu da yeni bir ağ örneğidir\\.\\n\\n"
                                      "📜 İnternetin ilk versiyonu, 1960'ların sonlarında ABD ordusu tarafından finanse edilen *ARPANET* projesi kapsamında ortaya çıktı\n"
                                      "Bu, bilgisayarlar arasında çalışan ilk gerçek ağdı\\.\n\n"
                                      "🌍 1989'da Tim Berners-Lee, interneti bilgi paylaşımı ve depolama için kullanışlı hale getiren *World Wide Web (WWW)* kavramını önerdi\n\n"
                                      "🔌 Bugün internet, binlerce küçük ekipten oluşan büyük bir kulüp gibidir\\. Ağlar iki türe ayrılır:\n"
                                      "　- 🔒 Özel Ağlarn"
                                      "　- 🌐 Genel Ağlar — bu ikisi birlikte internettir\n\n"
                                      "💡 Ağdaki cihazlar, birbirini bulmak ve veri alışverişi yapmak için özel *tanımlayıcılar* kullanır \\(bunu daha sonra ele alacağız).",
                                      parse_mode="Markdown"

                                      ,
                                      reply_markup=reply_markup)
    elif query.data == "chhnbbgbghjve":
        keyboard = [
            [InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="nextdat")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔗 *Ağlar (Networks)* basitçe birbirine bağlı nesnelerdir.\n"
                                      "Örneğin, arkadaş çevren: ortak ilgi alanları, hobiler, beceriler aracılığıyla birbirinize bağlısınız. 🧠🤝\n\n"
                                      "📡 *Ağlar her yerde bulunur:*\n"
                                      "　- 🚇 Şehirdeki toplu taşıma sistemi\n"
                                      "　- ⚡ Ulusal elektrik altyapısı\n"
                                      "　- 🏘️ Komşular arasındaki iletişim\n"
                                      "　- ✉️ Mektup ve kargo gönderen posta sistemleri\n\n"
                                      "💻 *Teknoloji alanında da bu kavram aynıdır, sadece cihazlar arasında uygulanır.*\n"
                                      "Telefonunu düşün 📱: Onu bilgiye erişmek için kullanırsın.\n\n"
                                      "📶 *Cihazların nasıl veri alışverişi yaptığını ve hangi kurallara uyduklarını birlikte öğreneceğiz.*\n\n"
                                      "🖥️ *Bir ağ 2'den milyarlarca cihaza kadar içerebilir:*\n"
                                      "　💻 Dizüstü bilgisayarlar\n"
                                      "　- 📱 Akıllı telefonlar\n"
                                      "　- 📷 Güvenlik kameraları\n"
                                      "　- 🚦 Trafik ışıkları\n"
                                      "　- 🌾 Tarım makineleri\n\n"
                                      "🔌 *Ağlar günlük hayatımızın bir parçası haline gelmiştir:*\n"
                                      "　- ⛅ Hava durumu verilerinin toplanması\n"
                                      "　- ⚡ Evlerin elektrikle beslenmesi\\n"
                                      "　- 🚦 Trafiğin yönetilmesi\n\n"
                                      "🛡️ Ağlar modern hayatın vazgeçilmez bir parçası olduğundan,\n"
                                      "ağın temel prensiplerini anlamak siber güvenlik eğitiminin temelidir.\n\n"
                                      "👥 Aşağıdaki diyagrama bak: Alice, Bob ve Jim kendi küçük ağlarını kurdular!\n"
                                      "Bu konuya daha sonra geri döneceğiz\n\n"
                                      "*İlk bölüm burada başlıyor!*\n*Haydi başlayalım!*",
                                      parse_mode="Markdown"
                                      ,
                                      reply_markup=reply_markup)

    elif query.data == "twopples":
        keyboard = [
            [InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="threepppipi")],
            [InlineKeyboardButton("son bölüm", callback_data="gagrgagfgdgxsfncdee")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📡 *Cihazların ağda iletişim kurabilmesi ve düzeni koruyabilmesi için:*\n"
                                      "— Kendilerini tanıyabilmeleri gerekir\n"
                                      "— Diğer cihazlar tarafından tanınabilir olmaları gerekir\n\n"
                                      "💡 *Cihazlar insanlar gibidir:*\n"
                                      "— Adlarımız vardır (değişebilir)\n"
                                      "— Parmak izimiz vardır (benzersiz ve kalıcı\\)\\n\\n"
                                      "📱 *Cihazların da iki tür kimliği vardır:*\\n"
                                      "— IP adresi (📍 değişebilir)\n"
                                      "— MAC adresi (🔒 kalıcı, parmak izi gibi\\)\\n\\n"
                                      "=====================\\n"
                                      "🔹 *IP Adresleri*\\n"
                                      "IP adresi, cihazın ağdaki geçici adıdır\\.\\n"
                                      "Dört sayıdan \\(oktetten\\) oluşur ve noktalarla ayrılır:\\n"
                                      "Örnek: `192.168.0.1`\\n\\n"
                                      "🔁 Bir IP başka bir cihaza atanabilir ama aynı ağda iki cihaz aynı IP'yi kullanamaz\\.\\n\\n"
                                      "🌍 *İki tür IP adresi vardır:*\\n"
                                      "— Özel IP (ev, ofis içi kullanım\\)\\n"
                                      "— Genel IP (internet üzerinden görülebilir\\)\\n\\n"
                                      "🧾 *Örnek:*\n"
                                      "`Cihaz tÖzel IP t tGenel IP`\n"
                                      "`Bilgisayarım t192.168.1.77\\t86.157.52.21`\n"
                                      "`Diğer PC\\t192.168.1.74\\t86.157.52.21`\\n\\n"
                                      "🔍 Aynı modeme bağlılar \\(genel IP aynı\\), ama özel IP’leri farklıdır\\.\n"
                                      "Bu şekilde aynı ağda iletişim kurabilirler\\.\\n\\n"
                                      "=====================\\n"
                                      "🌐 *Sorun: Yetersiz IP adresi!*\\n"
                                      "IPv4 sadece yaklaşık 4\\.29 milyar adres sağlar \\(2^32\\),\\n"
                                      "ama cihaz sayısı dünyada onlarca milyarı buluyor\\.\\n\\n"
                                      "💡 *Çözüm:*\\n"
                                      "— IPv6 = 340 trilyon+ adres \\(2^128\\)\\n"
                                      "— Daha verimli\\n"
                                      "— Çok daha fazla adres sağlar\\n\\n"
                                      "Örnekler:\\n"
                                      "— IPv4: `192.168.1.1`\\n"
                                      "— IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`\\n\\n"
                                      "=====================\\n"
                                      "🔹 *MAC Adresleri*\\n"
                                      "Her cihazın benzersiz bir MAC adresi olan ağ adaptörü vardır\\.\\n"
                                      "Format: `a4:c3:f0:85:ac:2d` \\(16'lık sistemde 6 bayt)\n\n"
                                      "🛠 İlk 6 karakter üreticiyi temsil eder.\n"
                                      "📌 Son 6 karakter cihazın benzersiz numarasıdır\\.\n\n"
                                      "💥 *Ancak MAC adresi sahte olabilir \\(spoofing\\):*\\n"
                                      "— Bir saldırgan başka bir cihaz gibi davranabilir.\n"
                                      "— Örneğin, bir güvenlik duvarı sadece yöneticinin MAC’ine izin veriyorsa, bu kandırılabilir.\n\n"
                                      "=====================\n"
                                      "📌 *Özet:*\\n"
                                      "🔹 IP — ağa göre değişir.\n"
                                      "🔹 MAC — kalıcı ve benzersiz.\n"
                                      "🔹 Güvenlik açısından, IP veya MAC adresi kimliği %100 doğrulamaz.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "gagrgagfgdgxsfncdee":
        keyboard = [
            [InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="twopples")],
            [InlineKeyboardButton("son bölüm", callback_data="chhnbbgbghjve")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🌐 *Bölüm 2: İnternete Derinlemesine Dalış!*\n\n"
                                      "Artık ağların ne olduğunu biliyorsun — basitçe söylemek gerekirse, birbirine bağlı cihazlardır — şimdi internetin nasıl çalıştığını keşfedelim.\n\n"
                                      "📡 *İnternet*, birbirine bağlı birçok küçük ağdan oluşan *dev bir ağdır*.\n\n"
                                      "👫 Hayal et ki Alice yeni arkadaşlar edindi: Zayn ve Toby\\. Onları Bob ve Jim ile tanıştırmak istiyor. Fakat bir sorun var: sadece Alice her iki grubun dilini anlayabiliyor. Bu yüzden *bir köprü* oluyor ve herkes onun aracılığıyla iletişim kurabiliyor\\. Bu da yeni bir ağ örneğidir\\.\\n\\n"
                                      "📜 İnternetin ilk versiyonu, 1960'ların sonlarında ABD ordusu tarafından finanse edilen *ARPANET* projesi kapsamında ortaya çıktı\n"
                                      "Bu, bilgisayarlar arasında çalışan ilk gerçek ağdı\\.\n\n"
                                      "🌍 1989'da Tim Berners-Lee, interneti bilgi paylaşımı ve depolama için kullanışlı hale getiren *World Wide Web (WWW)* kavramını önerdi\n\n"
                                      "🔌 Bugün internet, binlerce küçük ekipten oluşan büyük bir kulüp gibidir\\. Ağlar iki türe ayrılır:\n"
                                      "　- 🔒 Özel Ağlarn"
                                      "　- 🌐 Genel Ağlar — bu ikisi birlikte internettir\n\n"
                                      "💡 Ağdaki cihazlar, birbirini bulmak ve veri alışverişi yapmak için özel *tanımlayıcılar* kullanır \\(bunu daha sonra ele alacağız).",
                                      parse_mode="Markdown"

                                      ,
                                      reply_markup=reply_markup)
    elif query.data == "threepppipi":
        keyboard = [[InlineKeyboardButton("son bölüm", callback_data="unwewewqwq")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📡 *Ping nedir?*\n\n"
            "*Ping*, iki cihaz arasındaki bağlantının çalışıp çalışmadığını kontrol etmek için kullanılan temel bir ağ aracıdır.\n"
            "Ping komutu, *ICMP* \\(Internet Control Message Protocol\\) kullanarak hedef cihaza bir \"echo request\" (yankı isteği\\) gönderir ve \"echo reply\" \\(yankı cevabı\\) almayı bekler.\n\n"
            "=====================\n"
            "🔍 *Ping ile şunları öğrenebilirsin:*\n"
            "— Bağlantı *var mı yok mu*\\n"
            "— *Ne kadar hızlı* yanıt veriyor \\(gecikme süresi\\)\n"
            "— Veri kaybı olup olmadığını \\(stabilite\\)\\n\\n"
            "=====================\n"
            "💻 *Kullanımı \\(Terminal\\):*\n"
            "```bash\\nping google.com\n```\n"
            "Bu komut google\\.com'a ping gönderir ve cevap sürelerini gösterir\\.\n\n"
            "=====================\\n"
            "✅ *Sonuç:*\\n"
            "— Eğer yanıt geliyorsa, bağlantı *çalışıyor* demektir\\.\n"
            "— Eğer \"timeout\" ya da \"host unreachable\" gibi mesajlar alırsan, bağlantıda sorun olabilir\\.\n\n"
            "💡 Ping, ağ sorunlarını teşhis etmek için *ilk başvurulan araçlardan biridir*.\n"
            "Bir web sitesi açılmıyorsa, önce ping ile test etmeyi deneyebilirsin.\n"
            ,
            parse_mode="Markdown",reply_markup = reply_markup
        )
    elif query.data == "unwewewqwq":
        keyboard = [
            [InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="threepppipi")],
            [InlineKeyboardButton("son bölüm", callback_data="gagrgagfgdgxsfncdee")]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📡 *Cihazların ağda iletişim kurabilmesi ve düzeni koruyabilmesi için:*\n"
                                      "— Kendilerini tanıyabilmeleri gerekir\n"
                                      "— Diğer cihazlar tarafından tanınabilir olmaları gerekir\n\n"
                                      "💡 *Cihazlar insanlar gibidir:*\n"
                                      "— Adlarımız vardır (değişebilir)\n"
                                      "— Parmak izimiz vardır (benzersiz ve kalıcı\\)\\n\\n"
                                      "📱 *Cihazların da iki tür kimliği vardır:*\\n"
                                      "— IP adresi (📍 değişebilir)\n"
                                      "— MAC adresi (🔒 kalıcı, parmak izi gibi\\)\\n\\n"
                                      "=====================\\n"
                                      "🔹 *IP Adresleri*\\n"
                                      "IP adresi, cihazın ağdaki geçici adıdır\\.\\n"
                                      "Dört sayıdan \\(oktetten\\) oluşur ve noktalarla ayrılır:\\n"
                                      "Örnek: `192.168.0.1`\\n\\n"
                                      "🔁 Bir IP başka bir cihaza atanabilir ama aynı ağda iki cihaz aynı IP'yi kullanamaz\\.\\n\\n"
                                      "🌍 *İki tür IP adresi vardır:*\\n"
                                      "— Özel IP (ev, ofis içi kullanım\\)\\n"
                                      "— Genel IP (internet üzerinden görülebilir\\)\\n\\n"
                                      "🧾 *Örnek:*\n"
                                      "`Cihaz tÖzel IP t tGenel IP`\n"
                                      "`Bilgisayarım t192.168.1.77\\t86.157.52.21`\n"
                                      "`Diğer PC\\t192.168.1.74\\t86.157.52.21`\\n\\n"
                                      "🔍 Aynı modeme bağlılar \\(genel IP aynı\\), ama özel IP’leri farklıdır\\.\n"
                                      "Bu şekilde aynı ağda iletişim kurabilirler\\.\\n\\n"
                                      "=====================\\n"
                                      "🌐 *Sorun: Yetersiz IP adresi!*\\n"
                                      "IPv4 sadece yaklaşık 4\\.29 milyar adres sağlar \\(2^32\\),\\n"
                                      "ama cihaz sayısı dünyada onlarca milyarı buluyor\\.\\n\\n"
                                      "💡 *Çözüm:*\\n"
                                      "— IPv6 = 340 trilyon+ adres \\(2^128\\)\\n"
                                      "— Daha verimli\\n"
                                      "— Çok daha fazla adres sağlar\\n\\n"
                                      "Örnekler:\\n"
                                      "— IPv4: `192.168.1.1`\\n"
                                      "— IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`\\n\\n"
                                      "=====================\\n"
                                      "🔹 *MAC Adresleri*\\n"
                                      "Her cihazın benzersiz bir MAC adresi olan ağ adaptörü vardır\\.\\n"
                                      "Format: `a4:c3:f0:85:ac:2d` \\(16'lık sistemde 6 bayt)\n\n"
                                      "🛠 İlk 6 karakter üreticiyi temsil eder.\n"
                                      "📌 Son 6 karakter cihazın benzersiz numarasıdır\\.\n\n"
                                      "💥 *Ancak MAC adresi sahte olabilir \\(spoofing\\):*\\n"
                                      "— Bir saldırgan başka bir cihaz gibi davranabilir.\n"
                                      "— Örneğin, bir güvenlik duvarı sadece yöneticinin MAC’ine izin veriyorsa, bu kandırılabilir.\n\n"
                                      "=====================\n"
                                      "📌 *Özet:*\\n"
                                      "🔹 IP — ağa göre değişir.\n"
                                      "🔹 MAC — kalıcı ve benzersiz.\n"
                                      "🔹 Güvenlik açısından, IP veya MAC adresi kimliği %100 doğrulamaz.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "ilan":
        keyboard = [[
            InlineKeyboardButton("Gitmek", callback_data="numberseven")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Tamam!! Python yolculuğumuza başlayalım🐍»",
            reply_markup=reply_markup)
    elif query.data == "heyvanlar":
        keyboard = [[
            InlineKeyboardButton("*Bölüm 1*", callback_data="CCCCG")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Tamam!! C++ yolculuğumuza başlayalım ⚙️",
            reply_markup=reply_markup)
    elif query.data == "sriplar":
        keyboard = [[
            InlineKeyboardButton("Bölüm 1", callback_data="metalheart")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Tamam!! JavaScript yolculuğumuza başlayalım!",
            reply_markup=reply_markup)
    elif query.data == "numberseven":
        keyboard = [[InlineKeyboardButton("🐍Başlayın", callback_data="saintlaurent")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("<<>>", reply_markup=reply_markup)
    elif query.data == "saintlaurent":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="financebro")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Python 64 Bit Kurulumu ve PyCharm Community Bağlantısı*\n\n"
            "🔹 *Adım 1: Python'u indir*\n"
            "[Python'u indir](https://www.python.org/downloads/) — Windows x86\\-64 çalıştırılabilir yükleyiciyi seç\n\n"
            "🔹 *Adım 2: Kurulum*\n"
            "— \"Add Python to PATH\" kutucuğunu işaretle\n"
            "— Customize installation → Next → Install for all users → Install\n\n"
            "🔹 *Adım 3: Kurulumu doğrula*\n"
            "Terminale şunu yaz: `python --version` — Python 3\\.X\\.X görmelisin\n\n"
            "🔹 *Adım 4: PyCharm'ı indir*\n"
            "[PyCharm'ı indir](https://www.jetbrains.com/pycharm/download) — Community sürümünü yükle\n\n"
            "🔹 *Adım 5: Python'u bağla*\n"
            "Yeni Proje → ⚙️ Yorumlayıcı Ekle → Sistem Yorumlayıcı → Yol:\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *Kontrol:*\n"
            "Bir dosya oluştur ve bu kodu yaz:\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "▶️ Tuşuna basarak çalıştır\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "financebro":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="heteroex")],
                    [InlineKeyboardButton("son bölüm", callback_data="dameungrr")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐍 *Python: Değişkenler ve Veri Türleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Veriyi saklamak için kullanılan isimlerdir, veri türü otomatik belirlenir.\n\n"
                                      "🔹 *Değişken örnekleri:*\n"
                                      "`x = 10` — Tam sayı (int)\n"
                                      "`name = \"Tom\"` — Metin (str)\n"
                                      "`pi = 3.14` — Ondalıklı sayı (float)\n\n"
                                      "🔹 *Temel veri türleri:*\n"
                                      "- `int` — Tam sayılar\n"
                                      "- `float` — Ondalıklı sayılar\n"
                                      "- `str` — Metin\n"
                                      "- `bool` — Mantıksal değerler: `True` veya `False`\n\n"
                                      "🔹 *Veri nasıl yazdırılır?*\n"
                                      "`print(x)`\n"
                                      "`print(name)`\n"
                                      "`print(pi)`\n\n"
                                      "✅ *Sen de dene!*\n"
                                      "```python\n"
                                      "age = 15\n"
                                      "city = \"Moskova\"\n"
                                      "is_student = True\n\n"
                                      "print(\"Yaş:\", age)\n"
                                      "print(\"Şehir:\", city)\n"
                                      "print(\"Öğrenci mi:\", is_student)\n"
                                      "```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "dameungrr":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="financebro")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🐍 *Python 64 Bit Kurulumu ve PyCharm Community Bağlantısı*\n\n"
            "🔹 *Adım 1: Python'u indir*\n"
            "[Python'u indir](https://www.python.org/downloads/) — Windows x86\\-64 çalıştırılabilir yükleyiciyi seç\n\n"
            "🔹 *Adım 2: Kurulum*\n"
            "— \"Add Python to PATH\" kutucuğunu işaretle\n"
            "— Customize installation → Next → Install for all users → Install\n\n"
            "🔹 *Adım 3: Kurulumu doğrula*\n"
            "Terminale şunu yaz: `python --version` — Python 3\\.X\\.X görmelisin\n\n"
            "🔹 *Adım 4: PyCharm'ı indir*\n"
            "[PyCharm'ı indir](https://www.jetbrains.com/pycharm/download) — Community sürümünü yükle\n\n"
            "🔹 *Adım 5: Python'u bağla*\n"
            "Yeni Proje → ⚙️ Yorumlayıcı Ekle → Sistem Yorumlayıcı → Yol:\n"
            "`C:/Program Files/Python3X/python.exe`\n\n"
            "✅ *Kontrol:*\n"
            "Bir dosya oluştur ve bu kodu yaz:\n"
            "```python\nprint(\"Hello, world!\")\n```\n"
            "▶️ Tuşuna basarak çalıştır\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "heteroex":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="mindalnoe")],
                    [InlineKeyboardButton("son bölüm", callback_data="asdasdad")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Python Koşullu İfadeler: if, elif, else*\n\n"
            "🔹 *Koşullu ifade nedir?*\n"
            "— Belirli bir koşul doğru olduğunda kod bloğunu çalıştırır.\n"
            "— if, elif ve else yapıları kullanılır.\n\n"
            "🔹 *Sözdizimi örneği:*\n"
            "```python\n"
            "age = 16\n\n"
            "if age >= 18:\n"
            "    print(\"Yetişkinsin\")\n"
            "elif age >= 14:\n"
            "    print(\"Gençsin\")\n"
            "else:\n"
            "    print(\"Çocuksun\")\n"
            "```\n\n"
            "🔹 *Karşılaştırma operatörleri:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Mantıksal operatörler:* `and`, `or`, `not`\n\n"
            "✅ *Kendin dene:*\n"
            "```python\n"
            "name = input(\"Adın nedir?: \")\n"
            "if name == \"Tom\":\n"
            "    print(\"Merhaba, Tom!\")\n"
            "else:\n"
            "    print(\"Merhaba, misafir!\")\n"
            "```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "asdasdad":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="heteroex")],
                    [InlineKeyboardButton("son bölüm", callback_data="dameungrr")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐍 *Python: Değişkenler ve Veri Türleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Veriyi saklamak için kullanılan isimlerdir, veri türü otomatik belirlenir.\n\n"
                                      "🔹 *Değişken örnekleri:*\n"
                                      "`x = 10` — Tam sayı (int)\n"
                                      "`name = \"Tom\"` — Metin (str)\n"
                                      "`pi = 3.14` — Ondalıklı sayı (float)\n\n"
                                      "🔹 *Temel veri türleri:*\n"
                                      "- `int` — Tam sayılar\n"
                                      "- `float` — Ondalıklı sayılar\n"
                                      "- `str` — Metin\n"
                                      "- `bool` — Mantıksal değerler: `True` veya `False`\n\n"
                                      "🔹 *Veri nasıl yazdırılır?*\n"
                                      "`print(x)`\n"
                                      "`print(name)`\n"
                                      "`print(pi)`\n\n"
                                      "✅ *Sen de dene!*\n"
                                      "```python\n"
                                      "age = 15\n"
                                      "city = \"Moskova\"\n"
                                      "is_student = True\n\n"
                                      "print(\"Yaş:\", age)\n"
                                      "print(\"Şehir:\", city)\n"
                                      "print(\"Öğrenci mi:\", is_student)\n"
                                      "```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "mindalnoe":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="tutpalentiitam")],
                    [InlineKeyboardButton("son bölüm", callback_data="nmvncmvnmckboikgjhbijojortgrdf")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python: for ve while Döngüleri*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Bir kod bloğunu tekrar tekrar çalıştırmak için kullanılır.\n"
                                      "— Genellikle listeler, sayı dizileri veya diğer koleksiyonlarda gezinmek için kullanılır.\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü örneği:*\n"
                                      "```python\n"
                                      "for i in range(5):\n"
                                      "    print(i)\n"
                                      "```\n"
                                      "— 0'dan 4'e kadar sayıları yazdırır.\n\n"
                                      "🔸 `range(5)` 0,1,2,3,4 dizisini oluşturur.\n\n"
                                      "============================\n"
                                      "🔹 *while döngüsü örneği:*\n"
                                      "```python\n"
                                      "x = 0\n"
                                      "while x < 3:\n"
                                      "    print(x)\n"
                                      "    x += 1\n"
                                      "```\n"
                                      "— Koşul doğru olduğu sürece kod bloğu tekrar eder.\n\n"
                                      "============================\n"
                                      "🔹 *Bir liste üzerinde for döngüsü ile gezinme:*\n"
                                      "```python\n"
                                      "fruits = [\"apple\", \"banana\", \"cherry\"]\n"
                                      "for fruit in fruits:\n"
                                      "    print(fruit)\n"
                                      "```\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- `for` koleksiyon öğelerini teker teker işlemek için uygundur\n"
                                      "- `while` koşula bağlı olarak tekrar eder\n"
                                      "- Döngüyü erken sonlandırmak için `break` kullanılır\n\n"
                                      "💡 Döngüler otomasyon ve veri işleme için temel araçlardır!\n"
                                      "Basit bir döngü yazarak sayı veya kelimeleri yazdırmayı dene!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "nmvncmvnmckboikgjhbijojortgrdf":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="mindalnoe")],
                    [InlineKeyboardButton("son bölüm", callback_data="asdasdad")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *Python Koşullu İfadeler: if, elif, else*\n\n"
            "🔹 *Koşullu ifade nedir?*\n"
            "— Belirli bir koşul doğru olduğunda kod bloğunu çalıştırır.\n"
            "— if, elif ve else yapıları kullanılır.\n\n"
            "🔹 *Sözdizimi örneği:*\n"
            "```python\n"
            "age = 16\n\n"
            "if age >= 18:\n"
            "    print(\"Yetişkinsin\")\n"
            "elif age >= 14:\n"
            "    print(\"Gençsin\")\n"
            "else:\n"
            "    print(\"Çocuksun\")\n"
            "```\n\n"
            "🔹 *Karşılaştırma operatörleri:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Mantıksal operatörler:* `and`, `or`, `not`\n\n"
            "✅ *Kendin dene:*\n"
            "```python\n"
            "name = input(\"Adın nedir?: \")\n"
            "if name == \"Tom\":\n"
            "    print(\"Merhaba, Tom!\")\n"
            "else:\n"
            "    print(\"Merhaba, misafir!\")\n"
            "```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "tutpalentiitam":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="yxxkai")],
                    [InlineKeyboardButton("son bölüm", callback_data="sdvfenvbkjgnlbknkmopghk")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python: Listeler (List)*\n\n"
                                      "🔹 *Liste nedir?*\n"
                                      "— Sıralı elemanlar koleksiyonudur.\n"
                                      "— Sayılar, metinler ve hatta başka listeler içerebilir.\n\n"
                                      "============================\n"
                                      "🔹 *Liste örneği:*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\n```\n"
                                      "— Üç metin elemanı içeren bir liste.\n\n"
                                      "🔸 İndeks ile elemanlara erişim:\n"
                                      "`fruits[0]` → \"apple\"\n"
                                      "`fruits[2]` → \"cherry\"\n\n"
                                      "============================\n"
                                      "🔹 *Eleman değiştirme ve ekleme:*\n"
                                      "```python\nfruits[1] = \"kiwi\"  # 'banana'yı 'kiwi' ile değiştirir\nfruits.append(\"pear\")  # Yeni eleman ekler\n```\n\n"
                                      "============================\n"
                                      "🔹 *Listeyi döngü ile gezme:*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 Listedeki elemanları tek tek yazdırır.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- İndeksler 0'dan başlar\n"
                                      "- Liste farklı türden elemanlar içerebilir\n"
                                      "- Listeler değiştirilebilir (eleman ekleyip çıkarabilirsiniz)\n\n"
                                      "💡 Listeler Python'da veri kümeleri ile çalışmak için güçlü araçlardır.\n"
                                      "Kendi listenizi oluşturup bir döngü ile gezmeyi deneyin!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "sdvfenvbkjgnlbknkmopghk":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="tutpalentiitam")],
                    [InlineKeyboardButton("son bölüm", callback_data="nmvncmvnmckboikgjhbijojortgrdf")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Python: for ve while Döngüleri*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Bir kod bloğunu tekrar tekrar çalıştırmak için kullanılır.\n"
                                      "— Genellikle listeler, sayı dizileri veya diğer koleksiyonlarda gezinmek için kullanılır.\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü örneği:*\n"
                                      "```python\n"
                                      "for i in range(5):\n"
                                      "    print(i)\n"
                                      "```\n"
                                      "— 0'dan 4'e kadar sayıları yazdırır.\n\n"
                                      "🔸 `range(5)` 0,1,2,3,4 dizisini oluşturur.\n\n"
                                      "============================\n"
                                      "🔹 *while döngüsü örneği:*\n"
                                      "```python\n"
                                      "x = 0\n"
                                      "while x < 3:\n"
                                      "    print(x)\n"
                                      "    x += 1\n"
                                      "```\n"
                                      "— Koşul doğru olduğu sürece kod bloğu tekrar eder.\n\n"
                                      "============================\n"
                                      "🔹 *Bir liste üzerinde for döngüsü ile gezinme:*\n"
                                      "```python\n"
                                      "fruits = [\"apple\", \"banana\", \"cherry\"]\n"
                                      "for fruit in fruits:\n"
                                      "    print(fruit)\n"
                                      "```\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- `for` koleksiyon öğelerini teker teker işlemek için uygundur\n"
                                      "- `while` koşula bağlı olarak tekrar eder\n"
                                      "- Döngüyü erken sonlandırmak için `break` kullanılır\n\n"
                                      "💡 Döngüler otomasyon ve veri işleme için temel araçlardır!\n"
                                      "Basit bir döngü yazarak sayı veya kelimeleri yazdırmayı dene!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "yxxkai":
        keyboard = [[InlineKeyboardButton("son bölüm", callback_data="csadadsfsav")]]
        reply_markup= InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🛠️ *Python: Fonksiyonlar (Functions)*\n\n"
                                      "🔹 *Fonksiyon nedir?*\n"
                                      "— Belirli bir görevi yerine getiren kod bloğudur.\n"
                                      "— Fonksiyonlar, kod tekrarını önler ve programı daha okunabilir, düzenli yapar.\n\n"
                                      "============================\n"
                                      "🔹 *Basit fonksiyon örneği:*\n"
                                      "```python\ndef say_hello():\n    print(\"Hello, world!\")\n\nsay_hello()  # Fonksiyon çağrılır\n```\n"
                                      "— `def` anahtar kelimesi, fonksiyon adı, parantez ve iki nokta kullanılır.\n"
                                      "— Fonksiyon içindeki kod sadece çağrıldığında çalışır.\n\n"
                                      "============================\n"
                                      "🔹 *Parametre alan fonksiyon:*\n"
                                      "```python\ndef greet(name):\n    print(\"Hello,\", name)\n\ngreet(\"Alice\")\n```\n"
                                      "— Fonksiyona değer (argüman) gönderebilirsiniz.\n\n"
                                      "============================\n"
                                      "🔹 *Değer döndüren fonksiyon (`return`):*\n"
                                      "```python\ndef square(x):\n    return x * x\n\nresult = square(5)\nprint(result)\n```\n"
                                      "— `return` sonucu geri döndürür.\n"
                                      "— Dönen değer bir değişkene atanabilir.\n\n"
                                      "============================\n"
                                      "✅ *Neden fonksiyonlar önemlidir?*\n"
                                      "- Kodu daha kısa ve okunabilir yapar\n"
                                      "- Aynı kod bloğunu tekrar tekrar kullanmanızı sağlar\n"
                                      "- Büyük programları mantıksal parçalara böler\n\n"
                                      "💡 İsminizi yazdıran bir fonksiyon, iki sayının toplamını döndüren bir fonksiyon yazmayı deneyin!\n"
                                      "Fonksiyonlar her programlama dilinin temelidir! 🚀",
                                      parse_mode="Markdown",reply_markup = reply_markup
                                      )
    elif query.data == "csadadsfsav":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="yxxkai")],
                    [InlineKeyboardButton("son bölüm", callback_data="sdvfenvbkjgnlbknkmopghk")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Python: Listeler (List)*\n\n"
                                      "🔹 *Liste nedir?*\n"
                                      "— Sıralı elemanlar koleksiyonudur.\n"
                                      "— Sayılar, metinler ve hatta başka listeler içerebilir.\n\n"
                                      "============================\n"
                                      "🔹 *Liste örneği:*\n"
                                      "```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\n```\n"
                                      "— Üç metin elemanı içeren bir liste.\n\n"
                                      "🔸 İndeks ile elemanlara erişim:\n"
                                      "`fruits[0]` → \"apple\"\n"
                                      "`fruits[2]` → \"cherry\"\n\n"
                                      "============================\n"
                                      "🔹 *Eleman değiştirme ve ekleme:*\n"
                                      "```python\nfruits[1] = \"kiwi\"  # 'banana'yı 'kiwi' ile değiştirir\nfruits.append(\"pear\")  # Yeni eleman ekler\n```\n\n"
                                      "============================\n"
                                      "🔹 *Listeyi döngü ile gezme:*\n"
                                      "```python\nfor fruit in fruits:\n    print(fruit)\n```\n"
                                      "🔸 Listedeki elemanları tek tek yazdırır.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- İndeksler 0'dan başlar\n"
                                      "- Liste farklı türden elemanlar içerebilir\n"
                                      "- Listeler değiştirilebilir (eleman ekleyip çıkarabilirsiniz)\n\n"
                                      "💡 Listeler Python'da veri kümeleri ile çalışmak için güçlü araçlardır.\n"
                                      "Kendi listenizi oluşturup bir döngü ile gezmeyi deneyin!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "CCCCG":
        keyboard = [[InlineKeyboardButton("⚙ Başlayın", callback_data="arang")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("«»", reply_markup=reply_markup)

    elif query.data == "arang":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="brang")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++ Kurulum ve Başlangıç:*\n\n"
            "🔹 *Adım 1: Derleyiciyi Yükleyin*\n"
            "[MinGW İndir](https://sourceforge.net/projects/mingw/)\n"
            "— GCC derleyicisini yükleyin ve `bin` klasörünün yolunu sistem PATH değişkenine ekleyin.\n\n"
            "🔹 *Adım 2: Editörü İndirin*\n"
            "[Visual Studio Code İndir](https://code.visualstudio.com/)\n\n"
            "🔹 *Adım 3: Derleyiciyi Kontrol Edin*\n"
            "`g++ --version`\n\n"
            "🔹 *Adım 4: Basit Kod Yazın*\n"
            "```cpp\n#include <iostream>\nint main() {\n"
            "    std::cout << \"Hello, world!\";\n    return 0;\n}\n```\n"
            "Dosyayı `main.cpp` olarak kaydedin, derlemek için:\n"
            "`g++ main.cpp -o main`\n"
            "Çalıştırmak için:\n"
            "`./main`",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "brang":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="crang")],
                    [InlineKeyboardButton("son bölüm", callback_data="dizdizodi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++: Değişkenler ve Veri Tipleri*\n\n"
            "🔹 *Değişken nedir?*\n"
            "— Veri depolamak için kullanılan isimlendirilmiş bellek alanıdır.\n"
            "— Değişkeni kullanmadan önce tipini belirtmek gerekir.\n\n"
            "🔹 *Örnekler:*\n"
            "`int age = 15;`  // Tam sayı\n"
            "`double pi = 3.14;`  // Ondalıklı sayı\n"
            "`char grade = 'A';`  // Karakter\n"
            "`bool isOnline = true;`  // Boolean (doğru/yanlış)\n"
            "`std::string name = \"Tom\";`  // String (metin)\n\n"
            "🔹 *Çıktı örneği:*\n"
            "```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n"
            "    int age = 15;\n    std::string name = \"Tom\";\n"
            "    std::cout << \"İsim: \" << name << \"\\n\";\n"
            "    std::cout << \"Yaş: \" << age << \"\\n\";\n    return 0;\n}\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "dizdizodi":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="brang")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++ Kurulum ve Başlangıç:*\n\n"
            "🔹 *Adım 1: Derleyiciyi Yükleyin*\n"
            "[MinGW İndir](https://sourceforge.net/projects/mingw/)\n"
            "— GCC derleyicisini yükleyin ve `bin` klasörünün yolunu sistem PATH değişkenine ekleyin.\n\n"
            "🔹 *Adım 2: Editörü İndirin*\n"
            "[Visual Studio Code İndir](https://code.visualstudio.com/)\n\n"
            "🔹 *Adım 3: Derleyiciyi Kontrol Edin*\n"
            "`g++ --version`\n\n"
            "🔹 *Adım 4: Basit Kod Yazın*\n"
            "```cpp\n#include <iostream>\nint main() {\n"
            "    std::cout << \"Hello, world!\";\n    return 0;\n}\n```\n"
            "Dosyayı `main.cpp` olarak kaydedin, derlemek için:\n"
            "`g++ main.cpp -o main`\n"
            "Çalıştırmak için:\n"
            "`./main`",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "crang":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="jinggrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="nudemeeamputirovat")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++: Koşullu İfadeler (if, else, else if)*\n\n"
            "🔹 *Koşul nedir?*\n"
            "— Belirli bir koşul doğru olduğunda ilgili kod bloğu çalışır.\n\n"
            "🔹 *Örnek:*\n"
            "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int age = 16;\n"
            "    if (age >= 18) {\n        cout << \"Yetişkinsiniz\";\n"
            "    } else if (age >= 14) {\n        cout << \"Gençsiniz\";\n"
            "    } else {\n        cout << \"Çocuksunuz\";\n    }\n"
            "    return 0;\n}\n```\n\n"
            "🔹 *Operatörler:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Mantıksal operatörler:* `&&`, `||`, `!`\n\n"
            "✅ *Kendin bir koşullu ifade yazmayı dene!*",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "nudemeeamputirovat":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="crang")],
                    [InlineKeyboardButton("son bölüm", callback_data="dizdizodi")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "⚙️ *C++: Değişkenler ve Veri Tipleri*\n\n"
            "🔹 *Değişken nedir?*\n"
            "— Veri depolamak için kullanılan isimlendirilmiş bellek alanıdır.\n"
            "— Değişkeni kullanmadan önce tipini belirtmek gerekir.\n\n"
            "🔹 *Örnekler:*\n"
            "`int age = 15;`  // Tam sayı\n"
            "`double pi = 3.14;`  // Ondalıklı sayı\n"
            "`char grade = 'A';`  // Karakter\n"
            "`bool isOnline = true;`  // Boolean (doğru/yanlış)\n"
            "`std::string name = \"Tom\";`  // String (metin)\n\n"
            "🔹 *Çıktı örneği:*\n"
            "```cpp\n#include <iostream>\n#include <string>\n\nint main() {\n"
            "    int age = 15;\n    std::string name = \"Tom\";\n"
            "    std::cout << \"İsim: \" << name << \"\\n\";\n"
            "    std::cout << \"Yaş: \" << age << \"\\n\";\n    return 0;\n}\n```\n",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
    elif query.data == "jinggrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="venussrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="vsexoroshoharry")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🔁 *C++: Döngüler (for, while, do while)*\n\n"
            "🔹 *Döngü nedir?*\n"
            "— Belirli bir koşul sağlandığında aynı kod bloğunu tekrar tekrar çalıştırır.\n\n"
            "🔹 *C++'da döngü türleri:*\n"
            "- `for` — Çalışma sayısı önceden biliniyorsa kullanılır\n"
            "- `while` — Koşul doğru olduğu sürece devam eder\n"
            "- `do while` — Önce bir kez çalışır, sonra koşulu kontrol eder\n\n"
            "============================\n"
            "🔹 *for örneği:*\n"
            "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << i << \" \";\n}\n```\n"
            "🔸 Çıktı: `0 1 2 3 4`\n\n"
            "============================\n"
            "🔹 *while örneği:*\n"
            "```cpp\nint i = 0;\nwhile (i < 3) {\n    cout << i << endl;\n    i++;\n}\n```\n"
            "🔸 Çıktı: `0`, `1`, `2`\n\n"
            "============================\n"
            "🔹 *do while örneği:*\n"
            "```cpp\nint i = 0;\ndo {\n    cout << i << endl;\n    i++;\n} while (i < 2);\n```\n"
            "🔸 Çıktı: `0`, `1`\n\n"
            "============================\n"
            "✅ *Ne zaman kullanılır?*\n"
            "- `for` — Çalışma sayısı bilindiğinde (örn: `i = 0; i < N; i++`)\n"
            "- `while` — Çalışma sayısı bilinmediğinde\n"
            "- `do while` — En az bir kere çalışması gerektiğinde\n\n"
            "💡 Kendi döngünü yazmayı dene!",
            parse_mode="Markdown",
            reply_markup=reply_markup)
    elif query.data == "vsexoroshoharry":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="jinggrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="nudemeeamputirovat")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧠 *C++: Koşullu İfadeler (if, else, else if)*\n\n"
            "🔹 *Koşul nedir?*\n"
            "— Belirli bir koşul doğru olduğunda ilgili kod bloğu çalışır.\n\n"
            "🔹 *Örnek:*\n"
            "```cpp\n#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int age = 16;\n"
            "    if (age >= 18) {\n        cout << \"Yetişkinsiniz\";\n"
            "    } else if (age >= 14) {\n        cout << \"Gençsiniz\";\n"
            "    } else {\n        cout << \"Çocuksunuz\";\n    }\n"
            "    return 0;\n}\n```\n\n"
            "🔹 *Operatörler:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
            "🔹 *Mantıksal operatörler:* `&&`, `||`, `!`\n\n"
            "✅ *Kendin bir koşullu ifade yazmayı dene!*",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif query.data == "venussrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="zerorank")],
                    [InlineKeyboardButton("son bölüm", callback_data="mymashine")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++: Diziler (Arrays)*\n\n"
                                      "🔹 *Dizi nedir?*\n"
                                      "— Aynı türden elemanların ardışık olarak bellekte saklanmasıdır.\n"
                                      "— Her elemanın bir indeks numarası vardır (0'dan başlar).\n\n"
                                      "============================\n"
                                      "🔹 *Dizi örneği:*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\n```\n"
                                      "— 5 elemanlı bir int dizisi oluşturur.\n\n"
                                      "🔸 Elemanlara erişim:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Dizinin tüm elemanlarını döngü ile yazdırma:*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << numbers[i] << \" \";\n}\n```\n"
                                      "🔸 Çıktı: `10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *Kullanıcıdan değer alma:*\n"
                                      "```cpp\nint a[3];\nfor (int i = 0; i < 3; i++) {\n    cin >> a[i];\n}\n```\n"
                                      "🔸 3 sayı diziye kaydedilir.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- İndeksler `0` ile `n - 1` arasındadır\n"
                                      "- Dizinin sınırları dışına çıkmak hata (tanımsız davranış) oluşturur ❌\n"
                                      "- Tüm elemanlar aynı türde olmalıdır (int, float, char vb.)\n\n"
                                      "💡 Diziler temeldir. Diziler sayesinde bellek yönetimini, sıralamayı ve algoritmaları öğrenirsin!\n\n"
                                      "Kendi dizini oluştur ve elemanlarını yazdırmayı dene!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "mymashine":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="venussrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="vsexoroshoharry")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🔁 *C++: Döngüler (for, while, do while)*\n\n"
            "🔹 *Döngü nedir?*\n"
            "— Belirli bir koşul sağlandığında aynı kod bloğunu tekrar tekrar çalıştırır.\n\n"
            "🔹 *C++'da döngü türleri:*\n"
            "- `for` — Çalışma sayısı önceden biliniyorsa kullanılır\n"
            "- `while` — Koşul doğru olduğu sürece devam eder\n"
            "- `do while` — Önce bir kez çalışır, sonra koşulu kontrol eder\n\n"
            "============================\n"
            "🔹 *for örneği:*\n"
            "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << i << \" \";\n}\n```\n"
            "🔸 Çıktı: `0 1 2 3 4`\n\n"
            "============================\n"
            "🔹 *while örneği:*\n"
            "```cpp\nint i = 0;\nwhile (i < 3) {\n    cout << i << endl;\n    i++;\n}\n```\n"
            "🔸 Çıktı: `0`, `1`, `2`\n\n"
            "============================\n"
            "🔹 *do while örneği:*\n"
            "```cpp\nint i = 0;\ndo {\n    cout << i << endl;\n    i++;\n} while (i < 2);\n```\n"
            "🔸 Çıktı: `0`, `1`\n\n"
            "============================\n"
            "✅ *Ne zaman kullanılır?*\n"
            "- `for` — Çalışma sayısı bilindiğinde (örn: `i = 0; i < N; i++`)\n"
            "- `while` — Çalışma sayısı bilinmediğinde\n"
            "- `do while` — En az bir kere çalışması gerektiğinde\n\n"
            "💡 Kendi döngünü yazmayı dene!",
            parse_mode="Markdown",
            reply_markup=reply_markup)

    elif query.data == "zerorank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="amburanrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="vnncvnmcmcvmncv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++: Diziler (Strings)*\n\n"
                                      "🔹 *String nedir?*\n"
                                      "— Bir dizi karakter, örneğin isimler veya kelimeler.\n"
                                      "— C++’da karakter dizisi (char array) veya `std::string` sınıfı kullanılabilir.\n\n"
                                      "============================\n"
                                      "🔹 *Karakter dizisi olarak string:*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\n```\n"
                                      "🔸 `\\0` karakteri otomatik olarak sona eklenir ve string sonunu işaret eder.\n"
                                      "🔸 Dizi boyutu string uzunluğundan büyük olmalıdır.\n\n"
                                      "============================\n"
                                      "🔹 *`std::string` kullanımı:*\n"
                                      "```cpp\n#include <string>\n\nstd::string city = \"Baku\";\n```\n"
                                      "— Bu yöntem daha kolay ve güvenlidir.\n\n"
                                      "============================\n"
                                      "🔹 *Temel işlemler:*\n"
                                      "```cpp\nstd::string name = \"Tom\";\n\n"
                                      "cout << name << endl;         // String yazdırma\n"
                                      "cout << name.length() << endl; // String uzunluğu\n"
                                      "name += \" Hardy\";             // String birleştirme\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *Kullanıcıdan string alma:*\n"
                                      "```cpp\nstd::string userName;\ncout << \"İsminizi girin: \";\ncin >> userName;\n```\n"
                                      "❗ `cin` boşlukta durur. Tüm satırı okumak için:\n"
                                      "```cpp\nstd::string fullName;\ngetline(cin, fullName);\n```\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- `std::string` karakter dizisinden daha kolay ve güvenlidir\n"
                                      "- Kolayca birleştirme, uzunluk alma, karakter arama yapabilirsiniz\n"
                                      "- Kiril alfabesi veya Unicode işlemleri için kodlama ayarı gerekebilir\n\n"
                                      "💡 Stringler metin, form ve mesaj işlemenin temelidir!\n"
                                      "Kendi stringinizi oluşturup yazdırmayı deneyin! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "vnncvnmcmcvmncv":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="zerorank")],
                    [InlineKeyboardButton("son bölüm", callback_data="mymashine")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C++: Diziler (Arrays)*\n\n"
                                      "🔹 *Dizi nedir?*\n"
                                      "— Aynı türden elemanların ardışık olarak bellekte saklanmasıdır.\n"
                                      "— Her elemanın bir indeks numarası vardır (0'dan başlar).\n\n"
                                      "============================\n"
                                      "🔹 *Dizi örneği:*\n"
                                      "```cpp\nint numbers[5] = {10, 20, 30, 40, 50};\n```\n"
                                      "— 5 elemanlı bir int dizisi oluşturur.\n\n"
                                      "🔸 Elemanlara erişim:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *Dizinin tüm elemanlarını döngü ile yazdırma:*\n"
                                      "```cpp\nfor (int i = 0; i < 5; i++) {\n    cout << numbers[i] << \" \";\n}\n```\n"
                                      "🔸 Çıktı: `10 20 30 40 50`\n\n"
                                      "============================\n"
                                      "🔹 *Kullanıcıdan değer alma:*\n"
                                      "```cpp\nint a[3];\nfor (int i = 0; i < 3; i++) {\n    cin >> a[i];\n}\n```\n"
                                      "🔸 3 sayı diziye kaydedilir.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- İndeksler `0` ile `n - 1` arasındadır\n"
                                      "- Dizinin sınırları dışına çıkmak hata (tanımsız davranış) oluşturur ❌\n"
                                      "- Tüm elemanlar aynı türde olmalıdır (int, float, char vb.)\n\n"
                                      "💡 Diziler temeldir. Diziler sayesinde bellek yönetimini, sıralamayı ve algoritmaları öğrenirsin!\n\n"
                                      "Kendi dizini oluştur ve elemanlarını yazdırmayı dene!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "amburanrank":
        keyboard = [
                    [InlineKeyboardButton("son bölüm", callback_data="kadisher")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C++: Fonksiyonlar (Functions)*\n\n"
                                      "🔹 *Fonksiyon nedir?*\n"
                                      "— Belirli bir görevi yerine getiren kod bloğudur.\n"
                                      "— Kodun düzenlenmesine yardımcı olur ve tekrarı önler.\n\n"
                                      "============================\n"
                                      "🔹 *Basit fonksiyon örneği:*\n"
                                      "```cpp\nvoid sayHello() {\n    cout << \"Hello, world!\" << endl;\n}\n\nint main() {\n    sayHello();\n    return 0;\n}\n```\n"
                                      "— `void` fonksiyonun geri dönüş değeri olmadığını belirtir.\n"
                                      "— Fonksiyon adıyla çağrılır.\n\n"
                                      "============================\n"
                                      "🔹 *Parametre alan fonksiyon:*\n"
                                      "```cpp\nvoid greet(string name) {\n    cout << \"Hello, \" << name << endl;\n}\n\nint main() {\n    greet(\"Alice\");\n    return 0;\n}\n```\n"
                                      "— Fonksiyona veri gönderebilirsiniz.\n"
                                      "— Parametreler parantez içinde tanımlanır.\n\n"
                                      "============================\n"
                                      "🔹 *Geri dönüş değeri olan fonksiyon:*\n"
                                      "```cpp\nint square(int x) {\n    return x * x;\n}\n\nint main() {\n    int res = square(5);\n    cout << res;\n    return 0;\n}\n```\n"
                                      "— Geri dönüş tipi belirtilir (örneğin `int`).\n"
                                      "— `return` ile sonuç döndürülür.\n\n"
                                      "============================\n"
                                      "✅ *Neden fonksiyonlar önemlidir?*\n"
                                      "- Kodun daha temiz ve anlaşılır olmasını sağlar\n"
                                      "- Aynı kodu tekrar tekrar kullanmaya izin verir\n"
                                      "- Büyük programları küçük parçalara bölmeyi kolaylaştırır\n\n"
                                      "💡 İki sayı alan ve toplamlarını döndüren bir fonksiyon yazmayı dene!\n"
                                      "Fonksiyonlar iyi C++ kodunun temelidir! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "kadisher":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="amburanrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="vnncvnmcmcvmncv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔤 *C++: Diziler (Strings)*\n\n"
                                      "🔹 *String nedir?*\n"
                                      "— Bir dizi karakter, örneğin isimler veya kelimeler.\n"
                                      "— C++’da karakter dizisi (char array) veya `std::string` sınıfı kullanılabilir.\n\n"
                                      "============================\n"
                                      "🔹 *Karakter dizisi olarak string:*\n"
                                      "```cpp\nchar name[6] = \"Tom\";\n```\n"
                                      "🔸 `\\0` karakteri otomatik olarak sona eklenir ve string sonunu işaret eder.\n"
                                      "🔸 Dizi boyutu string uzunluğundan büyük olmalıdır.\n\n"
                                      "============================\n"
                                      "🔹 *`std::string` kullanımı:*\n"
                                      "```cpp\n#include <string>\n\nstd::string city = \"Baku\";\n```\n"
                                      "— Bu yöntem daha kolay ve güvenlidir.\n\n"
                                      "============================\n"
                                      "🔹 *Temel işlemler:*\n"
                                      "```cpp\nstd::string name = \"Tom\";\n\n"
                                      "cout << name << endl;         // String yazdırma\n"
                                      "cout << name.length() << endl; // String uzunluğu\n"
                                      "name += \" Hardy\";             // String birleştirme\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *Kullanıcıdan string alma:*\n"
                                      "```cpp\nstd::string userName;\ncout << \"İsminizi girin: \";\ncin >> userName;\n```\n"
                                      "❗ `cin` boşlukta durur. Tüm satırı okumak için:\n"
                                      "```cpp\nstd::string fullName;\ngetline(cin, fullName);\n```\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- `std::string` karakter dizisinden daha kolay ve güvenlidir\n"
                                      "- Kolayca birleştirme, uzunluk alma, karakter arama yapabilirsiniz\n"
                                      "- Kiril alfabesi veya Unicode işlemleri için kodlama ayarı gerekebilir\n\n"
                                      "💡 Stringler metin, form ve mesaj işlemenin temelidir!\n"
                                      "Kendi stringinizi oluşturup yazdırmayı deneyin! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "sriplara":
        keyboard = [[InlineKeyboardButton("⚙ Başlayın", callback_data="metalsonic")]
                    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Hadi başlayalım! \nBölüm 1:", reply_markup=reply_markup)
    elif query.data == "metalsonic":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="lexxrank")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript Kurulum ve Başlangıç:*\n\n"
                                      "🔹 *Adım 1: Editör İndir*\n"
                                      "[Visual Studio Code'u İndir](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Adım 2: Node.js Kurulumunu Kontrol Et*\n"
                                      "[Node.js'i İndir](https://nodejs.org/)\n"
                                      "— Kurulum sonrası sürümü kontrol et:\n"
                                      "`node --version`\n\n"
                                      "🔹 *Adım 3: Basit Kod Yaz*\n"
                                      "`main.js` dosyasını oluştur ve içine şunu yaz:\n"
                                      "```js\nconsole.log(\"Hello, world!\");\n```\n"
                                      "Terminalde çalıştır:\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript, web sitesi, bot ve uygulama yapmaya başlamak için ilk adımdır!*",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "lexxrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="lexturank")],
                    [InlineKeyboardButton("son bölüm", callback_data="kuzshineko")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Değişkenler ve Veri Tipleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Verileri saklamak için kullanılan isimlendirilmiş konteynerlerdir.\n"
                                      "— `let`, `const` veya eski `var` ile tanımlanır.\n\n"
                                      "🔹 *Örnekler:*\n"
                                      "`let age = 15;`\n"
                                      "`const pi = 3.14;`\n"
                                      "`let name = \"Tom\";`\n"
                                      "`let isOnline = true;`\n\n"
                                      "🔹 *Konsola yazdırmak:*\n"
                                      "```js\nlet age = 15;\nlet name = \"Tom\";\nconsole.log(\"Name:\", name);\nconsole.log(\"Age:\", age);\n```\n"
                                      "💡 *İpucu:* Değişmeyen değerler için `const`, değişebilenler için `let` kullanılır.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "kuzshineko":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="lexxrank")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript Kurulum ve Başlangıç:*\n\n"
                                      "🔹 *Adım 1: Editör İndir*\n"
                                      "[Visual Studio Code'u İndir](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Adım 2: Node.js Kurulumunu Kontrol Et*\n"
                                      "[Node.js'i İndir](https://nodejs.org/)\n"
                                      "— Kurulum sonrası sürümü kontrol et:\n"
                                      "`node --version`\n\n"
                                      "🔹 *Adım 3: Basit Kod Yaz*\n"
                                      "`main.js` dosyasını oluştur ve içine şunu yaz:\n"
                                      "```js\nconsole.log(\"Hello, world!\");\n```\n"
                                      "Terminalde çalıştır:\n"
                                      "`node main.js`\n\n"
                                      "💡 *JavaScript, web sitesi, bot ve uygulama yapmaya başlamak için ilk adımdır!*",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )


    elif query.data == "lexturank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="porscrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="puntik")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Koşullar ve Karşılaştırmalar*\n\n"
                                      "🔹 *Koşul nedir?*\n"
                                      "— Bir kontrol türüdür; koşul `true` olduğunda, kod bloğu çalışır.\n"
                                      "— JavaScript'te `if` deyimi ile yapılır.\n\n"
                                      "🔹 *Örnek:*\n"
                                      "```js\nlet age = 18;\nif (age >= 18) {\n    console.log(\"Giriş izinli\");\n} else {\n    console.log(\"Giriş reddedildi\");\n}\n```\n\n"
                                      "🔹 *Karşılaştırma operatörleri:*\n"
                                      "`==` — Değer eşitliği (tip dönüşümü yapar)\n"
                                      "`===` — Katı eşitlik (tip ve değer eşit)\n"
                                      "`!=` — Eşit değil (değer bazında)\n"
                                      "`!==` — Katı eşit değil (tip veya değer farklı)\n"
                                      "`>` — Büyük\n"
                                      "`<` — Küçük\n"
                                      "`>=` — Büyük veya eşit\n"
                                      "`<=` — Küçük veya eşit\n\n"
                                      "💡 *Önemli:* Tip dönüşümü hatalarını önlemek için `===` ve `!==` kullanılması tavsiye edilir.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "puntik":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="lexturank")],
                    [InlineKeyboardButton("son bölüm", callback_data="kuzshineko")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Değişkenler ve Veri Tipleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Verileri saklamak için kullanılan isimlendirilmiş konteynerlerdir.\n"
                                      "— `let`, `const` veya eski `var` ile tanımlanır.\n\n"
                                      "🔹 *Örnekler:*\n"
                                      "`let age = 15;`\n"
                                      "`const pi = 3.14;`\n"
                                      "`let name = \"Tom\";`\n"
                                      "`let isOnline = true;`\n\n"
                                      "🔹 *Konsola yazdırmak:*\n"
                                      "```js\nlet age = 15;\nlet name = \"Tom\";\nconsole.log(\"Name:\", name);\nconsole.log(\"Age:\", age);\n```\n"
                                      "💡 *İpucu:* Değişmeyen değerler için `const`, değişebilenler için `let` kullanılır.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "porscrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="ferrarirank")],
                    [InlineKeyboardButton("son bölüm", callback_data="gansdifjjdifjkonjffdu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Mantıksal Operatörler*\n\n"
                                      "🔹 *Mantıksal operatör nedir?*\n"
                                      "— Birden fazla koşulu birleştirmek için kullanılır.\n"
                                      "— Aynı anda birden çok koşulun doğru olup olmadığını kontrol eder.\n\n"
                                      "🔹 *Yaygın mantıksal operatörler:*\n"
                                      "`&&` — Ve (tüm koşullar doğru olmalı)\n"
                                      "`||` — Veya (en az bir koşul doğru)\n"
                                      "`!` — Değil (koşulun tersini alır)\n\n"
                                      "🔹 *Örnekler:*\n"
                                      "```js\nlet age = 20;\nlet hasPassport = true;\n\nif (age >= 18 && hasPassport) {\n    console.log(\"Giriş izinli\");\n} else {\n    console.log(\"Giriş reddedildi\");\n}\n```\n\n"
                                      "```js\nlet isOnline = false;\nif (!isOnline) {\n    console.log(\"Kullanıcı çevrimdışı\");\n}\n```\n\n"
                                      "💡 *Önemli:* Öncelik parantez ile belirlenir, sonra mantıksal işlemler gelir.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )
    elif query.data == "gansdifjjdifjkonjffdu":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="porscrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="puntik")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Koşullar ve Karşılaştırmalar*\n\n"
                                      "🔹 *Koşul nedir?*\n"
                                      "— Bir kontrol türüdür; koşul `true` olduğunda, kod bloğu çalışır.\n"
                                      "— JavaScript'te `if` deyimi ile yapılır.\n\n"
                                      "🔹 *Örnek:*\n"
                                      "```js\nlet age = 18;\nif (age >= 18) {\n    console.log(\"Giriş izinli\");\n} else {\n    console.log(\"Giriş reddedildi\");\n}\n```\n\n"
                                      "🔹 *Karşılaştırma operatörleri:*\n"
                                      "`==` — Değer eşitliği (tip dönüşümü yapar)\n"
                                      "`===` — Katı eşitlik (tip ve değer eşit)\n"
                                      "`!=` — Eşit değil (değer bazında)\n"
                                      "`!==` — Katı eşit değil (tip veya değer farklı)\n"
                                      "`>` — Büyük\n"
                                      "`<` — Küçük\n"
                                      "`>=` — Büyük veya eşit\n"
                                      "`<=` — Küçük veya eşit\n\n"
                                      "💡 *Önemli:* Tip dönüşümü hatalarını önlemek için `===` ve `!==` kullanılması tavsiye edilir.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )


    elif query.data == "ferrarirank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="dodorank")],
                    [InlineKeyboardButton("son bölüm", callback_data="crchadasdfgvfrgt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript: Döngüler*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Bir kod bloğunu birden çok kez tekrar çalıştırmak için kullanılır.\n"
                                      "— Genellikle diziler üzerinde işlem yapmak, tekrar eden görevler ve otomasyon için kullanılır.\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü*\n"
                                      "```js\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n```\n"
                                      "— 0'dan 4'e kadar sayıları yazdırır.\n"
                                      "`i++` her döngü sonunda sayacı 1 artırır.\n\n"
                                      "============================\n"
                                      "🔹 *while döngüsü*\n"
                                      "```js\nlet x = 0;\nwhile (x < 3) {\n    console.log(x);\n    x++;\n}\n```\n"
                                      "— `x < 3` koşulu doğru olduğu sürece kod bloğunu tekrarlar.\n\n"
                                      "============================\n"
                                      "🔹 *do...while döngüsü*\n"
                                      "```js\nlet y = 0;\ndo {\n    console.log(y);\n    y++;\n} while (y < 2);\n```\n"
                                      "— Koşul doğru olmasa bile en az bir kez çalışır.\n\n"
                                      "============================\n"
                                      "🔹 *Dizi elemanlarını iterasyon örneği*\n"
                                      "```js\nlet fruits = [\"🍎\", \"🍌\", \"🍇\"];\nfor (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}\n```\n"
                                      "— Dizideki tüm elemanları teker teker okur.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- Sonsuz döngüye dikkat edin (sayacı güncellemeyi unutmayın!)\n"
                                      "- `break` ile döngüyü erken sonlandırabilirsiniz\n"
                                      "- `continue` ile o iterasyonu atlayabilirsiniz\n\n"
                                      "💡 Döngüler, veri yapıları ve otomasyon için kritik araçlardır!\n"
                                      "10'dan 1'e geriye sayan bir döngü yazmayı deneyin! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "crchadasdfgvfrgt":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="ferrarirank")],
                    [InlineKeyboardButton("son bölüm", callback_data="gansdifjjdifjkonjffdu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Mantıksal Operatörler*\n\n"
                                      "🔹 *Mantıksal operatör nedir?*\n"
                                      "— Birden fazla koşulu birleştirmek için kullanılır.\n"
                                      "— Aynı anda birden çok koşulun doğru olup olmadığını kontrol eder.\n\n"
                                      "🔹 *Yaygın mantıksal operatörler:*\n"
                                      "`&&` — Ve (tüm koşullar doğru olmalı)\n"
                                      "`||` — Veya (en az bir koşul doğru)\n"
                                      "`!` — Değil (koşulun tersini alır)\n\n"
                                      "🔹 *Örnekler:*\n"
                                      "```js\nlet age = 20;\nlet hasPassport = true;\n\nif (age >= 18 && hasPassport) {\n    console.log(\"Giriş izinli\");\n} else {\n    console.log(\"Giriş reddedildi\");\n}\n```\n\n"
                                      "```js\nlet isOnline = false;\nif (!isOnline) {\n    console.log(\"Kullanıcı çevrimdışı\");\n}\n```\n\n"
                                      "💡 *Önemli:* Öncelik parantez ile belirlenir, sonra mantıksal işlemler gelir.",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup
                                      )

    elif query.data == "dodorank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="srtrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="zikozikzokzizozokz")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Fonksiyonlara Giriş*\n\n"
                                      "🔹 *Fonksiyon nedir?*\n"
                                      "— Belirli görevleri yerine getiren isimlendirilmiş kod bloğudur.\n"
                                      "— Aynı kodu tekrar yazmadan tekrar tekrar çağırabilirsiniz.\n"
                                      "— Yapısal programlamanın temelidir.\n\n"
                                      "🔹 *Neden fonksiyon kullanmalıyız?*\n"
                                      "✔ Tekrarlayan kodlardan kaçınmak\n"
                                      "✔ Programı mantıksal modüllere ayırmak\n"
                                      "✔ Parametre (arguments) alıp sonuç döndürebilmek\n\n"
                                      "🔹 *Basit fonksiyon örneği:*\n"
                                      "```js\nfunction sayHello() {\n  console.log(\"Hello!\");\n}\n\nsayHello(); // Fonksiyon çağrısı\n```\n"
                                      "💡 `sayHello` her çağrıldığında \"Hello!\" yazar.\n\n"
                                      "🔹 *Parametreli fonksiyon:*\n"
                                      "```js\nfunction greet(name) {\n  console.log(\"Hello, \" + name);\n}\n\ngreet(\"Tom\");\ngreet(\"Anna\");\n```\n"
                                      "💡 `name` parametresi farklı değerler alarak çıktıyı kontrol etmeni sağlar.\n\n"
                                      "🔹 *Değer döndüren fonksiyon:*\n"
                                      "```js\nfunction square(number) {\n  return number * number;\n}\n\nconsole.log(square(4)); // 16\n```\n"
                                      "💡 `return` sonucu geri döndürür ve başka yerlerde kullanılabilir.\n\n"
                                      "🔹 *Unutma:*\n"
                                      "✔ Fonksiyonlar çağrılmadan önce tanımlanmalı\n"
                                      "✔ İçindeki kod sadece çağrıldığında çalışır\n"
                                      "✔ Birden fazla parametre alabilir\n\n"
                                      "Fonksiyonlar kodunu temiz, esnek ve kolay yönetilebilir yapar! 🚀",

                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "zikozikzokzizozokz":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="dodorank")],
                    [InlineKeyboardButton("son bölüm", callback_data="crchadasdfgvfrgt")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔁 *JavaScript: Döngüler*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Bir kod bloğunu birden çok kez tekrar çalıştırmak için kullanılır.\n"
                                      "— Genellikle diziler üzerinde işlem yapmak, tekrar eden görevler ve otomasyon için kullanılır.\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü*\n"
                                      "```js\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}\n```\n"
                                      "— 0'dan 4'e kadar sayıları yazdırır.\n"
                                      "`i++` her döngü sonunda sayacı 1 artırır.\n\n"
                                      "============================\n"
                                      "🔹 *while döngüsü*\n"
                                      "```js\nlet x = 0;\nwhile (x < 3) {\n    console.log(x);\n    x++;\n}\n```\n"
                                      "— `x < 3` koşulu doğru olduğu sürece kod bloğunu tekrarlar.\n\n"
                                      "============================\n"
                                      "🔹 *do...while döngüsü*\n"
                                      "```js\nlet y = 0;\ndo {\n    console.log(y);\n    y++;\n} while (y < 2);\n```\n"
                                      "— Koşul doğru olmasa bile en az bir kez çalışır.\n\n"
                                      "============================\n"
                                      "🔹 *Dizi elemanlarını iterasyon örneği*\n"
                                      "```js\nlet fruits = [\"🍎\", \"🍌\", \"🍇\"];\nfor (let i = 0; i < fruits.length; i++) {\n    console.log(fruits[i]);\n}\n```\n"
                                      "— Dizideki tüm elemanları teker teker okur.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- Sonsuz döngüye dikkat edin (sayacı güncellemeyi unutmayın!)\n"
                                      "- `break` ile döngüyü erken sonlandırabilirsiniz\n"
                                      "- `continue` ile o iterasyonu atlayabilirsiniz\n\n"
                                      "💡 Döngüler, veri yapıları ve otomasyon için kritik araçlardır!\n"
                                      "10'dan 1'e geriye sayan bir döngü yazmayı deneyin! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "srtrank":
        keyboard = [[InlineKeyboardButton("Onceki bölüm", callback_data="cecececececececece")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *JavaScript: Nesneler (Objects)*\n\n"
                                      "🔹 *Nedir nesne?*\n"
                                      "— İlgili veri ve fonksiyonları depolayan yapıdır.\n"
                                      "— \"anahtar: değer\" çiftleri şeklinde oluşturulur.\n\n"
                                      "============================\n"
                                      "🔹 *Basit nesne örneği:*\n"
                                      "```js\n"
                                      "let person = {\n"
                                      "  name: \"Tom\",\n"
                                      "  age: 25,\n"
                                      "  isStudent: true\n"
                                      "};\n"
                                      "```\n"
                                      "🔸 Özelliklere erişim:\n"
                                      "`person.name` → \"Tom\"\n"
                                      "`person[\"age\"]` → 25\n\n"
                                      "============================\n"
                                      "🔹 *Metod içeren nesne:*\n"
                                      "```js\n"
                                      "let car = {\n"
                                      "  brand: \"Toyota\",\n"
                                      "  start: function() {\n"
                                      "    console.log(\"Motor çalıştı\");\n"
                                      "  }\n"
                                      "};\n\n"
                                      "car.start();\n"
                                      "```\n"
                                      "============================\n"
                                      "✅ *Neden nesne kullanmalı?*\n"
                                      "- Karmaşık verileri merkezileştirmek\n"
                                      "- Gerçek dünyadaki nesneleri modellemek\n"
                                      "- DOM işlemleri, API çağrıları gibi geniş uygulama alanları\n\n"
                                      "💡 \"phone\" isimli bir nesne oluştur, \"model\", \"year\" özellikleri ve \"call()\" metodunu ekle!",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "cecececececececece":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="srtrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="zikozikzokzizozokz")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *JavaScript: Fonksiyonlara Giriş*\n\n"
                                      "🔹 *Fonksiyon nedir?*\n"
                                      "— Belirli görevleri yerine getiren isimlendirilmiş kod bloğudur.\n"
                                      "— Aynı kodu tekrar yazmadan tekrar tekrar çağırabilirsiniz.\n"
                                      "— Yapısal programlamanın temelidir.\n\n"
                                      "🔹 *Neden fonksiyon kullanmalıyız?*\n"
                                      "✔ Tekrarlayan kodlardan kaçınmak\n"
                                      "✔ Programı mantıksal modüllere ayırmak\n"
                                      "✔ Parametre (arguments) alıp sonuç döndürebilmek\n\n"
                                      "🔹 *Basit fonksiyon örneği:*\n"
                                      "```js\nfunction sayHello() {\n  console.log(\"Hello!\");\n}\n\nsayHello(); // Fonksiyon çağrısı\n```\n"
                                      "💡 `sayHello` her çağrıldığında \"Hello!\" yazar.\n\n"
                                      "🔹 *Parametreli fonksiyon:*\n"
                                      "```js\nfunction greet(name) {\n  console.log(\"Hello, \" + name);\n}\n\ngreet(\"Tom\");\ngreet(\"Anna\");\n```\n"
                                      "💡 `name` parametresi farklı değerler alarak çıktıyı kontrol etmeni sağlar.\n\n"
                                      "🔹 *Değer döndüren fonksiyon:*\n"
                                      "```js\nfunction square(number) {\n  return number * number;\n}\n\nconsole.log(square(4)); // 16\n```\n"
                                      "💡 `return` sonucu geri döndürür ve başka yerlerde kullanılabilir.\n\n"
                                      "🔹 *Unutma:*\n"
                                      "✔ Fonksiyonlar çağrılmadan önce tanımlanmalı\n"
                                      "✔ İçindeki kod sadece çağrıldığında çalışır\n"
                                      "✔ Birden fazla parametre alabilir\n\n"
                                      "Fonksiyonlar kodunu temiz, esnek ve kolay yönetilebilir yapar! 🚀",

                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "java_startings":
        keyboard = [[InlineKeyboardButton("☕ Java öğrenmeye başlayın", callback_data="valleyrank")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Java", reply_markup=reply_markup)
    elif query.data == "valleyrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="rebirtharank")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java: Kurulum ve İlk Projeyi Oluşturma*\n\n"
                                      "🔹 *Adım 1: JDK İndir ve Kur*\n"
                                      "[🔗 Resmi İndirme Sayfası](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— İşletim sistemine uygun Java SE Development Kit (JDK) seçin\n"
                                      "— Kurulumda `Add JAVA to PATH` seçeneğini işaretleyin (varsa)\n\n"
                                      "🔹 *Adım 2: Kurulumu Doğrula*\n"
                                      "Terminali açıp şunu yazın:\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "Sürüm bilgisi görünüyorsa kurulum başarılıdır!\n\n"
                                      "🔹 *Adım 3: Geliştirme Araçlarını Kur*\n"
                                      "✅ [IntelliJ IDEA Community (Önerilen)](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + Java Uzantısı](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Adım 4: İlk Java Kodunu Yaz*\n"
                                      "`Main.java` dosyası oluşturun ve şu kodu yazın:\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "Sonra terminalde çalıştırın:\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ Beklenen çıktı: `Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *Java öğrenmeye başlamaya hazırsınız!*\n"
                                      "Sırada: değişkenler, koşullar, döngüler, fonksiyonlar ve nesne yönelimli programlama!\n\n"
                                      "👇 Aşağıdaki düğmeye tıklayarak sonraki derse geçin!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "rebirtharank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="silikonerank")],
                    [InlineKeyboardButton("son bölüm", callback_data="crchcrchcrchcrch")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Değişkenler ve Veri Tipleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Verileri saklamak için kullanılan isimdir.\n"
                                      "— Her değişkenin veri tipi önceden tanımlanmalıdır.\n\n"
                                      "🔹 *Temel veri tipleri:*\n"
                                      "- `int`: Tam sayılar, örn. `42`\n"
                                      "- `double`: Ondalıklı sayılar, örn. `3.14`\n"
                                      "- `char`: Tek karakter, örn. `'A'`\n"
                                      "- `boolean`: Mantıksal değer, `true` veya `false`\n"
                                      "- `String`: Metin dizisi, örn. `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *Değişken bildirme ve kullanma:*\n"
                                      "```java\nint age = 18;\ndouble pi = 3.14;\nchar grade = 'A';\nboolean isStudent = true;\nString name = \"Tom\";\n```\n\n"
                                      "🔸 Değişkenleri yazdırmak için `System.out.println()` kullanın:\n"
                                      "```java\nSystem.out.println(name);\nSystem.out.println(age);\n```\n"
                                      "🔸 Çıktı:\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *Hatırlatma:*\n"
                                      "- Java statik olarak tiplenen bir dildir, her değişken tipiyle tanımlanmalıdır.\n"
                                      "- Değişken isimleri büyük-küçük harfe duyarlıdır: `Name` ≠ `name`\n"
                                      "- Anlamlı isimlendirme kullanın: `int n = 5;` ❌, `int score = 5;` ✅\n\n"
                                      "💡 Kendi değişkenlerini tanımlayıp `System.out.println()` ile yazdırmayı dene!",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "crchcrchcrchcrch":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="rebirtharank")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("☕️ *Java: Kurulum ve İlk Projeyi Oluşturma*\n\n"
                                      "🔹 *Adım 1: JDK İndir ve Kur*\n"
                                      "[🔗 Resmi İndirme Sayfası](https://www.oracle.com/java/technologies/javase-downloads.html)\n"
                                      "— İşletim sistemine uygun Java SE Development Kit (JDK) seçin\n"
                                      "— Kurulumda `Add JAVA to PATH` seçeneğini işaretleyin (varsa)\n\n"
                                      "🔹 *Adım 2: Kurulumu Doğrula*\n"
                                      "Terminali açıp şunu yazın:\n"
                                      "```bash\njava -version\njavac -version\n```\n"
                                      "Sürüm bilgisi görünüyorsa kurulum başarılıdır!\n\n"
                                      "🔹 *Adım 3: Geliştirme Araçlarını Kur*\n"
                                      "✅ [IntelliJ IDEA Community (Önerilen)](https://www.jetbrains.com/idea/download/)\n"
                                      "✅ [Visual Studio Code + Java Uzantısı](https://code.visualstudio.com/)\n\n"
                                      "🔹 *Adım 4: İlk Java Kodunu Yaz*\n"
                                      "`Main.java` dosyası oluşturun ve şu kodu yazın:\n"
                                      "```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}\n```\n"
                                      "Sonra terminalde çalıştırın:\n"
                                      "```bash\njavac Main.java\njava Main\n```\n"
                                      "✅ Beklenen çıktı: `Hello, Java!`\n\n"
                                      "============================\n"
                                      "🎯 *Java öğrenmeye başlamaya hazırsınız!*\n"
                                      "Sırada: değişkenler, koşullar, döngüler, fonksiyonlar ve nesne yönelimli programlama!\n\n"
                                      "👇 Aşağıdaki düğmeye tıklayarak sonraki derse geçin!",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "silikonerank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="silikonrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="cemolecrchrchemole")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Java: Koşul İfadeleri (if, else, else if)*\n\n"
                                      "🔹 *Koşul ifadesi nedir?*\n"
                                      "— Programın farklı koşullara göre farklı kodlar çalıştırmasını sağlar.\n\n"
                                      "============================\n"
                                      "🔹 *Örnek kod:*\n"
                                      "```java\n"
                                      "if (age >= 18) {\n"
                                      "    System.out.println(\"Yetişkinsin\");\n"
                                      "} else if (age >= 14) {\n"
                                      "    System.out.println(\"Gençsin\");\n"
                                      "} else {\n"
                                      "    System.out.println(\"Çocuksun\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Karşılaştırma operatörleri:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
                                      "🔹 *Mantıksal operatörler:* `&&` (ve), `||` (veya), `!` (değil)\n\n"
                                      "✅ *Deneyin:*\n"
                                      "Yaşa göre mesaj yazdıran bir program yazın!",
                                      parse_mode="Markdown", reply_markup=reply_markup)
    elif query.data == "cemolecrchrchemole":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="silikonerank")],
                    [InlineKeyboardButton("son bölüm", callback_data="crchcrchcrchcrch")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Değişkenler ve Veri Tipleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Verileri saklamak için kullanılan isimdir.\n"
                                      "— Her değişkenin veri tipi önceden tanımlanmalıdır.\n\n"
                                      "🔹 *Temel veri tipleri:*\n"
                                      "- `int`: Tam sayılar, örn. `42`\n"
                                      "- `double`: Ondalıklı sayılar, örn. `3.14`\n"
                                      "- `char`: Tek karakter, örn. `'A'`\n"
                                      "- `boolean`: Mantıksal değer, `true` veya `false`\n"
                                      "- `String`: Metin dizisi, örn. `\"Hello\"`\n\n"
                                      "============================\n"
                                      "🔹 *Değişken bildirme ve kullanma:*\n"
                                      "```java\nint age = 18;\ndouble pi = 3.14;\nchar grade = 'A';\nboolean isStudent = true;\nString name = \"Tom\";\n```\n\n"
                                      "🔸 Değişkenleri yazdırmak için `System.out.println()` kullanın:\n"
                                      "```java\nSystem.out.println(name);\nSystem.out.println(age);\n```\n"
                                      "🔸 Çıktı:\n"
                                      "`Tom`\n"
                                      "`18`\n\n"
                                      "============================\n"
                                      "✅ *Hatırlatma:*\n"
                                      "- Java statik olarak tiplenen bir dildir, her değişken tipiyle tanımlanmalıdır.\n"
                                      "- Değişken isimleri büyük-küçük harfe duyarlıdır: `Name` ≠ `name`\n"
                                      "- Anlamlı isimlendirme kullanın: `int n = 5;` ❌, `int score = 5;` ✅\n\n"
                                      "💡 Kendi değişkenlerini tanımlayıp `System.out.println()` ile yazdırmayı dene!",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "silikonrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="silikrank")],
                    [InlineKeyboardButton("Önceki Bölüm", callback_data="ligimitirovaniydaunin")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: Döngüler (Loops)*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Bir kod bloğunu belirli koşullar sağlandığı sürece tekrar tekrar çalıştırmak için kullanılır.\n"
                                      "— Tekrarlayan görevlerde ve veri üzerinde işlem yaparken çok faydalıdır.\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü örneği:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— 0'dan 4'e kadar sayıları yazdırır.\n\n"
                                      "============================\n"
                                      "🔹 *while döngüsü örneği:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *do...while döngüsü örneği:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— Koşul sağlanmasa bile en az bir kere çalışır.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- Sonsuz döngülere dikkat edin\n"
                                      "- Döngüyü erken sonlandırmak için `break` kullanın\n"
                                      "- Döngüdeki mevcut iterasyonu atlamak için `continue` kullanın\n\n"
                                      "💡 10'dan 1'e geri sayan bir döngü yazmayı dene! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "ligimitirovaniydaunin":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="silikonrank")],
                    [InlineKeyboardButton("son bölüm", callback_data="cemolecrchrchemole")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 *Java: Koşul İfadeleri (if, else, else if)*\n\n"
                                      "🔹 *Koşul ifadesi nedir?*\n"
                                      "— Programın farklı koşullara göre farklı kodlar çalıştırmasını sağlar.\n\n"
                                      "============================\n"
                                      "🔹 *Örnek kod:*\n"
                                      "```java\n"
                                      "if (age >= 18) {\n"
                                      "    System.out.println(\"Yetişkinsin\");\n"
                                      "} else if (age >= 14) {\n"
                                      "    System.out.println(\"Gençsin\");\n"
                                      "} else {\n"
                                      "    System.out.println(\"Çocuksun\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Karşılaştırma operatörleri:* `==`, `!=`, `>`, `<`, `>=`, `<=`\n"
                                      "🔹 *Mantıksal operatörler:* `&&` (ve), `||` (veya), `!` (değil)\n\n"
                                      "✅ *Deneyin:*\n"
                                      "Yaşa göre mesaj yazdıran bir program yazın!",
                                      parse_mode="Markdown", reply_markup=reply_markup)

    elif query.data == "silikrank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="siuurank")],
                    [InlineKeyboardButton("Önceki Bölüm", callback_data="lastcrecrecrecer")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Diziler (Arrays)*\n\n"
                                      "🔹 *Dizi nedir?*\n"
                                      "— Diziler aynı türdeki elemanların sıralı bir şekilde hafızada saklanmasıdır.\n"
                                      "— Her elemanın bir indeksi vardır (0’dan başlar).\n\n"
                                      "============================\n"
                                      "🔹 *Bir tamsayı dizisi oluşturma:*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— 5 elemanlı bir tamsayı dizisi oluşturur.\n\n"
                                      "🔸 Elemanlara erişim:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü ile tüm elemanları yazdırma:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— `numbers.length` dizi uzunluğunu verir.\n\n"
                                      "============================\n"
                                      "🔹 *Kullanıcıdan dizi elemanı alma:*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— Kullanıcıdan 3 sayı alıp diziye kaydeder.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- İndeksler 0’dan n-1’e kadar gider\n"
                                      "- Diziler sabit boyutludur\n"
                                      "- İndeks sınırlarını aşmak hata verir (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 Diziler veri yapıları, sıralama ve algoritma öğrenmenin temelidir! Kendi dizini oluşturup iç",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "lastcrecrecrecer":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="silikrank")],
                    [InlineKeyboardButton("Önceki Bölüm", callback_data="ligimitirovaniydaunin")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *Java: Döngüler (Loops)*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Bir kod bloğunu belirli koşullar sağlandığı sürece tekrar tekrar çalıştırmak için kullanılır.\n"
                                      "— Tekrarlayan görevlerde ve veri üzerinde işlem yaparken çok faydalıdır.\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü örneği:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    System.out.println(i);\n"
                                      "}\n"
                                      "```\n"
                                      "— 0'dan 4'e kadar sayıları yazdırır.\n\n"
                                      "============================\n"
                                      "🔹 *while döngüsü örneği:*\n"
                                      "```java\n"
                                      "int x = 0;\n"
                                      "while (x < 3) {\n"
                                      "    System.out.println(x);\n"
                                      "    x++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "============================\n"
                                      "🔹 *do...while döngüsü örneği:*\n"
                                      "```java\n"
                                      "int y = 0;\n"
                                      "do {\n"
                                      "    System.out.println(y);\n"
                                      "    y++;\n"
                                      "} while (y < 2);\n"
                                      "```\n"
                                      "— Koşul sağlanmasa bile en az bir kere çalışır.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- Sonsuz döngülere dikkat edin\n"
                                      "- Döngüyü erken sonlandırmak için `break` kullanın\n"
                                      "- Döngüdeki mevcut iterasyonu atlamak için `continue` kullanın\n\n"
                                      "💡 10'dan 1'e geri sayan bir döngü yazmayı dene! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "siuurank":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="suiirank")],
                    [InlineKeyboardButton("Önceki Bölüm", callback_data="dimariadebruynenen")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java: Metodlar (Functions)*\n\n"
                                      "🔹 *Metod nedir?*\n"
                                      "— Belirli bir görevi gerçekleştiren kod bloğudur.\n"
                                      "— Aynı kodu tekrar yazmadan, metod çağırarak kullanabilirsin.\n\n"
                                      "============================\n"
                                      "🔹 *Neden metod kullanmalıyız?*\n"
                                      "✔️ Kod tekrarını önler\n"
                                      "✔️ Kod okunabilir ve bakımı kolay olur\n"
                                      "✔️ Parametre alabilir ve sonuç döndürebilir\n\n"
                                      "============================\n"
                                      "🔹 *Basit örnek:*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"Merhaba!\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // Metod çağrısı\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— `sayHello` metodu \"Merhaba!\" yazdırır.\n\n"
                                      "============================\n"
                                      "🔹 *Parametre alan metod:*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"Merhaba, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"Ahmet\");\n"
                                      "```\n"
                                      "— Parametre metodun daha esnek olmasını sağlar.\n\n"
                                      "============================\n"
                                      "🔹 *Değer döndüren metod:*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— `return` sonucu döndürmek için kullanılır.\n\n"
                                      "============================\n"
                                      "✅ *Unutma:*\n"
                                      "- Tüm metodlar sınıf içinde tanımlanmalıdır\n"
                                      "- `main()` programın giriş noktasıdır\n"
                                      "- `void` geri dönüş değeri olmadığını belirtir\n\n"
                                      "💡 Kendi metodunu yaz, ismini yazdıran veya iki sayıyı toplayan bir metod oluştur! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "dimariadebruynenen":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="siuurank")],
                    [InlineKeyboardButton("Önceki Bölüm", callback_data="lastcrecrecrecer")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *Java: Diziler (Arrays)*\n\n"
                                      "🔹 *Dizi nedir?*\n"
                                      "— Diziler aynı türdeki elemanların sıralı bir şekilde hafızada saklanmasıdır.\n"
                                      "— Her elemanın bir indeksi vardır (0’dan başlar).\n\n"
                                      "============================\n"
                                      "🔹 *Bir tamsayı dizisi oluşturma:*\n"
                                      "```java\n"
                                      "int[] numbers = {10, 20, 30, 40, 50};\n"
                                      "```\n"
                                      "— 5 elemanlı bir tamsayı dizisi oluşturur.\n\n"
                                      "🔸 Elemanlara erişim:\n"
                                      "`numbers[0]` → 10\n"
                                      "`numbers[3]` → 40\n\n"
                                      "============================\n"
                                      "🔹 *for döngüsü ile tüm elemanları yazdırma:*\n"
                                      "```java\n"
                                      "for (int i = 0; i < numbers.length; i++) {\n"
                                      "    System.out.println(numbers[i]);\n"
                                      "}\n"
                                      "```\n"
                                      "— `numbers.length` dizi uzunluğunu verir.\n\n"
                                      "============================\n"
                                      "🔹 *Kullanıcıdan dizi elemanı alma:*\n"
                                      "```java\n"
                                      "Scanner input = new Scanner(System.in);\n"
                                      "int[] a = new int[3];\n"
                                      "for (int i = 0; i < 3; i++) {\n"
                                      "    a[i] = input.nextInt();\n"
                                      "}\n"
                                      "```\n"
                                      "— Kullanıcıdan 3 sayı alıp diziye kaydeder.\n\n"
                                      "============================\n"
                                      "✅ *Önemli notlar:*\n"
                                      "- İndeksler 0’dan n-1’e kadar gider\n"
                                      "- Diziler sabit boyutludur\n"
                                      "- İndeks sınırlarını aşmak hata verir (ArrayIndexOutOfBoundsException)\n\n"
                                      "💡 Diziler veri yapıları, sıralama ve algoritma öğrenmenin temelidir! Kendi dizini oluşturup iç",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "suiirank":
        keyboard = [[InlineKeyboardButton("Önceki Bölüm", callback_data="lastcrenajfningie")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🏗️ *Java: Sınıflar ve Nesneler (Class & Object)*\n\n"
                                      "🔹 *Sınıf nedir?*\n"
                                      "— Nesne oluşturmak için bir şablondur.\n"
                                      "— Nesnenin özelliklerini (veri) ve davranışlarını (metodlar) tanımlar.\n\n"
                                      "🔹 *Nesne nedir?*\n"
                                      "— Sınıfa dayanarak oluşturulan gerçek varlıktır, programdaki somut üyedir.\n\n"
                                      "============================\n"
                                      "🔹 *Basit örnek:*\n"
                                      "```java\n"
                                      "public class Dog {\n"
                                      "    String name;\n"
                                      "    int age;\n\n"
                                      "    void bark() {\n"
                                      "        System.out.println(name + \": Hav Hav!\");\n"
                                      "    }\n"
                                      "}\n\n"
                                      "public class Main {\n"
                                      "    public static void main(String[] args) {\n"
                                      "        Dog myDog = new Dog();\n"
                                      "        myDog.name = \"Kara\";\n"
                                      "        myDog.age = 3;\n"
                                      "        myDog.bark();\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— `Dog` sınıfı iki özellik ve bir metoda sahiptir.\n"
                                      "— `myDog` bir `Dog` nesnesidir; metodları çağırabilir ve değer atayabilir.\n\n"
                                      "============================\n"
                                      "🔹 *Önemli kavramlar:*\n"
                                      "- Sınıf isimleri büyük harfle başlar: `Person`, `Car`, `Animal` gibi\n"
                                      "- `new` anahtar kelimesi nesne oluşturmak için kullanılır\n"
                                      "- Metodlar, nesnenin özelliklerine erişebilir\n\n"
                                      "✅ *Sınıflar ve nesneler Java'nın temelidir*\n"
                                      "— Neredeyse tüm Java programları nesne odaklı tasarlanır!\n\n"
                                      "💡 Sonraki derslerde yapıcılar (constructor), kapsülleme, kalıtım ve çok biçimliliği (polymorphism) öğreneceğiz! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "lastcrenajfningie":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡", callback_data="suiirank")],
                    [InlineKeyboardButton("Önceki Bölüm", callback_data="dimariadebruynenen")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *Java: Metodlar (Functions)*\n\n"
                                      "🔹 *Metod nedir?*\n"
                                      "— Belirli bir görevi gerçekleştiren kod bloğudur.\n"
                                      "— Aynı kodu tekrar yazmadan, metod çağırarak kullanabilirsin.\n\n"
                                      "============================\n"
                                      "🔹 *Neden metod kullanmalıyız?*\n"
                                      "✔️ Kod tekrarını önler\n"
                                      "✔️ Kod okunabilir ve bakımı kolay olur\n"
                                      "✔️ Parametre alabilir ve sonuç döndürebilir\n\n"
                                      "============================\n"
                                      "🔹 *Basit örnek:*\n"
                                      "```java\n"
                                      "public class Main {\n"
                                      "    public static void sayHello() {\n"
                                      "        System.out.println(\"Merhaba!\");\n"
                                      "    }\n\n"
                                      "    public static void main(String[] args) {\n"
                                      "        sayHello(); // Metod çağrısı\n"
                                      "    }\n"
                                      "}\n"
                                      "```\n"
                                      "— `sayHello` metodu \"Merhaba!\" yazdırır.\n\n"
                                      "============================\n"
                                      "🔹 *Parametre alan metod:*\n"
                                      "```java\n"
                                      "public static void greet(String name) {\n"
                                      "    System.out.println(\"Merhaba, \" + name);\n"
                                      "}\n\n"
                                      "greet(\"Ahmet\");\n"
                                      "```\n"
                                      "— Parametre metodun daha esnek olmasını sağlar.\n\n"
                                      "============================\n"
                                      "🔹 *Değer döndüren metod:*\n"
                                      "```java\n"
                                      "public static int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int result = square(4); // 16\n"
                                      "```\n"
                                      "— `return` sonucu döndürmek için kullanılır.\n\n"
                                      "============================\n"
                                      "✅ *Unutma:*\n"
                                      "- Tüm metodlar sınıf içinde tanımlanmalıdır\n"
                                      "- `main()` programın giriş noktasıdır\n"
                                      "- `void` geri dönüş değeri olmadığını belirtir\n\n"
                                      "💡 Kendi metodunu yaz, ismini yazdıran veya iki sayıyı toplayan bir metod oluştur! 🚀",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "priletelivmayami":
        keyboard = [[InlineKeyboardButton("💻 C öğrenmeye başlayın", callback_data="fisher")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("<<>>", reply_markup=reply_markup)
    elif query.data == "fisher":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fishering")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *C Kurulumu ve CLion IDE Ayarları*\n\n"
                                      "🔹 *Adım 1: MinGW Derleyicisini İndirin*\n"
                                      "[MinGW İndir](https://sourceforge.net/projects/mingw/) — `gcc`'yi kurun ve `bin` klasörünü sistem PATH ortam değişkenine ekleyin\n\n"
                                      "🔹 *Adım 2: CLion IDE'yi İndirin*\n"
                                      "[CLion İndir](https://www.jetbrains.com/clion/download/) — Topluluk (Community) veya Deneme (Trial) sürümünü yükleyin\n\n"
                                      "🔹 *Adım 3: Kurulumu Doğrulayın*\n"
                                      "Terminali açın ve şunu yazın:\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *Adım 4: Basit bir C programı yazın*\n"
                                      "`main.c` adında bir dosya oluşturun ve şu kodu yazın:\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Adım 5: Programı derleyin ve çalıştırın*\n"
                                      "Terminalde şunu yazın:\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "Sonra çalıştırın:\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *Çıktıyı kontrol edin:*\n"
                                      "Şunu görmelisiniz:\n"
                                      "```\nHello, world!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "fishering":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fisheringg")],
                    [InlineKeyboardButton("son bölüm", callback_data="crchemolexczxsefv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C Dilinde Değişkenler ve Veri Tipleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Bellekte veri saklamak için kullanılan isimdir.\n"
                                      "— Her değişkenin, ne tür veri tuttuğunu belirleyen bir veri tipi vardır.\n\n"
                                      "🔹 *Yaygın veri tipleri:*\n"
                                      "- `int` — Tam sayılar, örnek: `42`\n"
                                      "- `float` — Ondalıklı sayılar, örnek: `3.14`\n"
                                      "- `char` — Tek bir karakter, örnek: `'A'`\n"
                                      "- `double` — Daha hassas ondalıklı sayılar\n\n"
                                      "============================\n"
                                      "🔹 *Değişken tanımlama:*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *Ekrana yazdırma:*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"Yaş: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Kendin dene:* Birkaç değişken tanımla ve bunların değerlerini yazdır!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "crchemolexczxsefv":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fishering")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🐱‍💻 *C Kurulumu ve CLion IDE Ayarları*\n\n"
                                      "🔹 *Adım 1: MinGW Derleyicisini İndirin*\n"
                                      "[MinGW İndir](https://sourceforge.net/projects/mingw/) — `gcc`'yi kurun ve `bin` klasörünü sistem PATH ortam değişkenine ekleyin\n\n"
                                      "🔹 *Adım 2: CLion IDE'yi İndirin*\n"
                                      "[CLion İndir](https://www.jetbrains.com/clion/download/) — Topluluk (Community) veya Deneme (Trial) sürümünü yükleyin\n\n"
                                      "🔹 *Adım 3: Kurulumu Doğrulayın*\n"
                                      "Terminali açın ve şunu yazın:\n"
                                      "```bash\n"
                                      "gcc --version\n"
                                      "```\n\n"
                                      "🔹 *Adım 4: Basit bir C programı yazın*\n"
                                      "`main.c` adında bir dosya oluşturun ve şu kodu yazın:\n"
                                      "```c\n"
                                      "#include <stdio.h>\n\n"
                                      "int main() {\n"
                                      "    printf(\"Hello, world!\\n\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Adım 5: Programı derleyin ve çalıştırın*\n"
                                      "Terminalde şunu yazın:\n"
                                      "```bash\n"
                                      "gcc main.c -o main\n"
                                      "```\n"
                                      "Sonra çalıştırın:\n"
                                      "```bash\n"
                                      "./main\n"
                                      "```\n\n"
                                      "✅ *Çıktıyı kontrol edin:*\n"
                                      "Şunu görmelisiniz:\n"
                                      "```\nHello, world!\n```\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "fisheringg":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fisheringgg")],
                    [InlineKeyboardButton("son bölüm", callback_data="lalalxlalxdle")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C Dilinde Operatörler ve İfadeler*\n\n"
                                      "🔹 *Operatör nedir?*\n"
                                      "— Veriler üzerinde işlem yapmak için kullanılan sembol ya da sembol kombinasyonudur.\n\n"
                                      "🔹 *Operatör türleri:*\n"
                                      "- Aritmetik operatörler: `+`, `-`, `*`, `/`, `%`\n"
                                      "- Atama operatörleri: `=`, `+=`, `-=`, `*=`, vb.\n"
                                      "- Karşılaştırma operatörleri: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                                      "- Mantıksal operatörler: `&&`, `||`, `!`\n\n"
                                      "============================\n"
                                      "🔹 *Aritmetik işlemlere örnek:*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int toplam = a + b;       // 13\n"
                                      "int fark = a - b;         // 7\n"
                                      "int carpim = a * b;       // 30\n"
                                      "int bolum = a / b;        // 3\n"
                                      "int kalan = a % b;        // 1\n"
                                      "```\n\n"
                                      "🔹 *Karşılaştırma ve mantık örneği:*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x, y'den küçük ve y pozitiftir\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Sen de dene:* Farklı operatörleri içeren ifadeler yaz ve sonuçlarını ekrana bastır!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "lalalxlalxdle":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fisheringg")],
                    [InlineKeyboardButton("son bölüm", callback_data="crchemolexczxsefv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📦 *C Dilinde Değişkenler ve Veri Tipleri*\n\n"
                                      "🔹 *Değişken nedir?*\n"
                                      "— Bellekte veri saklamak için kullanılan isimdir.\n"
                                      "— Her değişkenin, ne tür veri tuttuğunu belirleyen bir veri tipi vardır.\n\n"
                                      "🔹 *Yaygın veri tipleri:*\n"
                                      "- `int` — Tam sayılar, örnek: `42`\n"
                                      "- `float` — Ondalıklı sayılar, örnek: `3.14`\n"
                                      "- `char` — Tek bir karakter, örnek: `'A'`\n"
                                      "- `double` — Daha hassas ondalıklı sayılar\n\n"
                                      "============================\n"
                                      "🔹 *Değişken tanımlama:*\n"
                                      "```c\n"
                                      "int age = 18;\n"
                                      "float pi = 3.14;\n"
                                      "char grade = 'A';\n"
                                      "double largeNum = 123456.789;\n"
                                      "```\n\n"
                                      "🔹 *Ekrana yazdırma:*\n"
                                      "```c\n"
                                      "#include <stdio.h>\n"
                                      "int main() {\n"
                                      "    int age = 18;\n"
                                      "    printf(\"Yaş: %d\\n\", age);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Kendin dene:* Birkaç değişken tanımla ve bunların değerlerini yazdır!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "fisheringgg":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fisheringggg")],
                    [InlineKeyboardButton("son bölüm", callback_data="voutbsdfnkkv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *C Dilinde Koşullu İfadeler: if, else if, else*\n\n"
                                      "🔹 *Koşullu ifade nedir?*\n"
                                      "— Belirli bir koşula göre farklı kod bloklarının çalışmasını sağlar.\n\n"
                                      "🔹 *if sözdizimi:*\n"
                                      "```c\n"
                                      "if (kosul) {\n"
                                      "    // koşul doğruysa çalışacak kod\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *else if ve else kullanımı:*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"Pozitif sayı\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"Sıfır\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"Negatif sayı\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Koşullarda kullanılan mantıksal operatörler:*\n"
                                      "- `&&` — VE (AND)\n"
                                      "- `||` — VEYA (OR)\n"
                                      "- `!` — DEĞİL (NOT)\n\n"
                                      "✅ *Görev:* Bir sayının pozitif, negatif ya da sıfır olup olmadığını kontrol eden bir program yaz!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "voutbsdfnkkv":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fisheringgg")],
                    [InlineKeyboardButton("son bölüm", callback_data="lalalxlalxdle")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C Dilinde Operatörler ve İfadeler*\n\n"
                                      "🔹 *Operatör nedir?*\n"
                                      "— Veriler üzerinde işlem yapmak için kullanılan sembol ya da sembol kombinasyonudur.\n\n"
                                      "🔹 *Operatör türleri:*\n"
                                      "- Aritmetik operatörler: `+`, `-`, `*`, `/`, `%`\n"
                                      "- Atama operatörleri: `=`, `+=`, `-=`, `*=`, vb.\n"
                                      "- Karşılaştırma operatörleri: `==`, `!=`, `<`, `>`, `<=`, `>=`\n"
                                      "- Mantıksal operatörler: `&&`, `||`, `!`\n\n"
                                      "============================\n"
                                      "🔹 *Aritmetik işlemlere örnek:*\n"
                                      "```c\n"
                                      "int a = 10, b = 3;\n"
                                      "int toplam = a + b;       // 13\n"
                                      "int fark = a - b;         // 7\n"
                                      "int carpim = a * b;       // 30\n"
                                      "int bolum = a / b;        // 3\n"
                                      "int kalan = a % b;        // 1\n"
                                      "```\n\n"
                                      "🔹 *Karşılaştırma ve mantık örneği:*\n"
                                      "```c\n"
                                      "int x = 5, y = 10;\n"
                                      "if (x < y && y > 0) {\n"
                                      "    printf(\"x, y'den küçük ve y pozitiftir\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Sen de dene:* Farklı operatörleri içeren ifadeler yaz ve sonuçlarını ekrana bastır!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "fisheringggg":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="isheringggg")],
                    [InlineKeyboardButton("son bölüm", callback_data="misipipiaskakaku")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *C Dilinde Döngüler: for, while, do-while*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Belirli bir kod bloğunu birden fazla kez çalıştırmamızı sağlar.\n\n"
                                      "🔹 *for döngüsü:*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"%d. döngü\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *while döngüsü:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"%d. döngü\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *do-while döngüsü:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"%d. döngü\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *Deneyin:* 1’den 10’a kadar sayıları yazdıran bir döngü yazın!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "misipipiaskakaku":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="fisheringggg")],
                    [InlineKeyboardButton("son bölüm", callback_data="voutbsdfnkkv")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🧠 *C Dilinde Koşullu İfadeler: if, else if, else*\n\n"
                                      "🔹 *Koşullu ifade nedir?*\n"
                                      "— Belirli bir koşula göre farklı kod bloklarının çalışmasını sağlar.\n\n"
                                      "🔹 *if sözdizimi:*\n"
                                      "```c\n"
                                      "if (kosul) {\n"
                                      "    // koşul doğruysa çalışacak kod\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *else if ve else kullanımı:*\n"
                                      "```c\n"
                                      "if (x > 0) {\n"
                                      "    printf(\"Pozitif sayı\\n\");\n"
                                      "} else if (x == 0) {\n"
                                      "    printf(\"Sıfır\\n\");\n"
                                      "} else {\n"
                                      "    printf(\"Negatif sayı\\n\");\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Koşullarda kullanılan mantıksal operatörler:*\n"
                                      "- `&&` — VE (AND)\n"
                                      "- `||` — VEYA (OR)\n"
                                      "- `!` — DEĞİL (NOT)\n\n"
                                      "✅ *Görev:* Bir sayının pozitif, negatif ya da sıfır olup olmadığını kontrol eden bir program yaz!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)

    elif query.data == "isheringggg":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="sheringggg")],
                    [InlineKeyboardButton("son bölüm", callback_data="zigiiiiiiiiisharko")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C Dilinde Fonksiyonlar (Functions)*\n\n"
                                      "🔹 *Fonksiyon nedir?*\n"
                                      "— Belirli bir görevi yerine getiren kod bloğudur.\n"
                                      "— Programı düzenlemeye ve kodu tekrar kullanmaya yardımcı olur.\n\n"
                                      "🔹 *Fonksiyon tanımlama ve çağırma:*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"Merhaba, dünya!\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // Fonksiyon çağrısı\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Parametreli fonksiyon:*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"Merhaba, %s!\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Tom\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Değer döndüren fonksiyon:*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"5 sayısının karesi: %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Sen de dene:* İki sayıyı toplayıp sonucu döndüren bir fonksiyon yaz!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "sheringggg":
        keyboard = [[InlineKeyboardButton("son bölüm", callback_data="pionyerererer")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📌 *C Dilinde Pointer'lar (İşaretçiler)*\n\n"
                                      "🔹 *Pointer nedir?*\n"
                                      "— Pointer, başka bir değişkenin bellek adresini tutan bir değişkendir.\n"
                                      "— Bellek yönetimi, diziler ve fonksiyonlarla çalışmada verimlidir.\n\n"
                                      "🔹 *Temel pointer örneği:*\n"
                                      "```c\n"
                                      "int x = 10;\n"
                                      "int* ptr = &x;\n"
                                      "printf(\"Değer: %d\\n\", *ptr); // dereference (adresin içindeki değeri alır)\n"
                                      "```\n"
                                      "— `&x` → `x` değişkeninin adresini alır\n"
                                      "— `*ptr` → o adresteki değeri verir\n\n"
                                      "🔹 *Açıklamalar:*\n"
                                      "- `int* ptr;` — bir tamsayıya işaret eden pointer\n"
                                      "- `*` — dereference operatörü (adresteki değeri alır)\n"
                                      "- `&` — adres operatörü (değişkenin adresini verir)\n\n"
                                      "============================\n"
                                      "🔹 *Pointer ile değeri değiştirme:*\n"
                                      "```c\n"
                                      "int a = 5;\n"
                                      "int* p = &a;\n"
                                      "*p = 100;\n"
                                      "printf(\"%d\\n\", a); // çıktısı 100 olur\n"
                                      "```\n"
                                      "✅ Pointer, değişkenin değerini doğrudan değiştirebilir.\n\n"
                                      "============================\n"
                                      "🔹 *Bellek adresini yazdırma:*\n"
                                      "```c\n"
                                      "int val = 42;\n"
                                      "printf(\"Değişkenin adresi: %p\\n\", &val);\n"
                                      "```\n"
                                      "— `%p` format belirteci, bellekteki adresleri yazdırmak için kullanılır.\n\n"
                                      "============================\n"
                                      "💡 Pointer'lar C dilinde çok önemli bir konudur.\n"
                                      "Dizi, karakter dizisi, fonksiyon parametreleri ve dinamik bellek yönetiminde sıklıkla kullanılır.\n\n"
                                      "📎 Bir sonraki bölümde *Diziler ve Pointer'ları* öğreneceksin!\n",
                                      parse_mode="Markdown",reply_markup = reply_markup)
    elif query.data == "pionyerererer":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="sheringggg")],
                    [InlineKeyboardButton("son bölüm", callback_data="zig&sharko")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("⚙️ *C Dilinde Fonksiyonlar (Functions)*\n\n"
                                      "🔹 *Fonksiyon nedir?*\n"
                                      "— Belirli bir görevi yerine getiren kod bloğudur.\n"
                                      "— Programı düzenlemeye ve kodu tekrar kullanmaya yardımcı olur.\n\n"
                                      "🔹 *Fonksiyon tanımlama ve çağırma:*\n"
                                      "```c\n"
                                      "void sayHello() {\n"
                                      "    printf(\"Merhaba, dünya!\\n\");\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    sayHello(); // Fonksiyon çağrısı\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Parametreli fonksiyon:*\n"
                                      "```c\n"
                                      "void greet(char name[]) {\n"
                                      "    printf(\"Merhaba, %s!\\n\", name);\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    greet(\"Tom\");\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *Değer döndüren fonksiyon:*\n"
                                      "```c\n"
                                      "int square(int x) {\n"
                                      "    return x * x;\n"
                                      "}\n\n"
                                      "int main() {\n"
                                      "    int result = square(5);\n"
                                      "    printf(\"5 sayısının karesi: %d\\n\", result);\n"
                                      "    return 0;\n"
                                      "}\n"
                                      "```\n\n"
                                      "✅ *Sen de dene:* İki sayıyı toplayıp sonucu döndüren bir fonksiyon yaz!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)
    elif query.data == "zigiiiiiiiiisharko":
        keyboard = [[InlineKeyboardButton("Sonraki Bölüm ➡️", callback_data="isheringggg")],
                    [InlineKeyboardButton("son bölüm", callback_data="misipipi&kakaku")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔄 *C Dilinde Döngüler: for, while, do-while*\n\n"
                                      "🔹 *Döngü nedir?*\n"
                                      "— Belirli bir kod bloğunu birden fazla kez çalıştırmamızı sağlar.\n\n"
                                      "🔹 *for döngüsü:*\n"
                                      "```c\n"
                                      "for (int i = 0; i < 5; i++) {\n"
                                      "    printf(\"%d. döngü\\n\", i);\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *while döngüsü:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "while (i < 5) {\n"
                                      "    printf(\"%d. döngü\\n\", i);\n"
                                      "    i++;\n"
                                      "}\n"
                                      "```\n\n"
                                      "🔹 *do-while döngüsü:*\n"
                                      "```c\n"
                                      "int i = 0;\n"
                                      "do {\n"
                                      "    printf(\"%d. döngü\\n\", i);\n"
                                      "    i++;\n"
                                      "} while (i < 5);\n"
                                      "```\n\n"
                                      "✅ *Deneyin:* 1’den 10’a kadar sayıları yazdıran bir döngü yazın!\n",
                                      parse_mode="Markdown",
                                      reply_markup=reply_markup)


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CallbackQueryHandler(zero, pattern="^start_learning$"))
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(
    lang,
    pattern="^(nunutireihgtj|nbxbhdbschdsivud|xxxxxxxxxxxxxxxxxxxxxxxxx|threep|myayuayuayuadlllllllll|CCCCG|CCCCGCCCCGCCCCGCCCCGCCCCG|amburanmal|amburanmall|amburanmalll|amburanrank|amburanrankamburanrankamburanrankamburanrank|arang|arangarangarangarangarangarangarang|armsakina|armsss|azerbaijan|bananadjo|bejing|bejingg|brands|brandss|brang|brangbrangbrangbrangbrangbrang|cont|continue|continue_learning|cp|cpone|cpones|cponess|cpp|cpp3|cpp4|cpp5|crang|crangcrangcrangcrangcrangcrangcrangcrang|cyber|cyberindo|cyberindocyberindocyberindo|cyberqwak|cyberqwakcyberqwakcyberqwak|cybers|cybersec|cybersecurity|cyberx|cyberxx|dod|doddo|dodgevaper|dodorank|dodorankdostdost|english|englishlessons|f|ferrari|ferrarir|ferrarirank|ferrarirankastonmazdipidazdi|ferraritunar|financebro|firstchinese|fisher|fishering|fisheringg|fisheringgg|fisheringggg|for|fors|frekal|fsociety|fuckincarti|heteroex|heyvanlar|heyvanlarheyvanlarheyvanlarheyvanlarheyvanlarheyvanlar|huggywug|huggywugg|huggywuggy|iaiaiaiaiai|idgaf|if|ifelif|ifelifelse|ilan|isheringggg|its|itss|java_start|java_startings|java_startings_java_startings|jingg|jinggrank|jinggrankjinggrankjinggrankjinggrank|jvone|jvones|jvonesss|krisarank|last|lastcre|lastcrecre|lastcrengie|lastcrengiecrengie|lastthing|lastthingthing|legs|legsaca|lex|lextu|lextural|lexturalss|lexturank|lexturanklexturanklexturanklexturank|lextutu|lexust|lexustt|lexustural|lexx|lexxrank|lexxranklexxranklexxranklexxranklexxrank|lmao|mcqueen|mcqueens|mcqueenss|mehrab|mehrabmehrabmehrabmehrab|men|mens|metalheart|metalheartmetalheartmetalheartmetalheartmetalheartmetalheart|metalsonic|metalsonicexexe|mrbananadjojo|myayuayuayua|mybau|next|nextdat|nextdatnextdatnextdatnextdatnextdat|nextx|nextxx|numberone|numberones|numberoness|numberseven|office|officess|onyx|onyxx|porsc|porsche|porschetunar|porscrank|porscrankporscrankporscrank|poxx|poxxy|priletelivmayami|priletelivmayamipriletelivmayamipriletelivmayami|pt|pyt|python|qew|rankrankrank|rebirtha|rebirtharank|rebirtharankrebirtharank|rezer|rezere|rezeress|russian|ryzee|ryzeeb|ryzrank|saintlaurent|scrip|script|sezer|sezere|sezeresx|sheringggg|sikakakakaka|silik|silikininirank|silikon|silikone|silikonerank|silikoneranksilikoneranksilikonerank|silikonrank|silikonranksilikonrank|silikrank|simmms|simrank|siren|sirens|sirenseacreatu|sirenseacreatur|sirenseacreature|sirenseacreaturrank|siuu|siuurank|siuurankkk|sixthousand|sremon|srip|sriplara|sriplarasososos|srtdemonessa|srtrank|srtrankpuususu|start_learning|style|styles|suii|suiiirank|suiirank|sxazx|sybau|tentiics|tentiicsranking|thebest|three|threep|threepp|threepppipi|threepppipithreepppipithreepppipithreepppipithreepppipi|toomycas|toomycash|tuk|tut|tutpalentiitam|tututu|tututut|two|twop|twopp|twopples|twopplestwopplestwopplestwopplestwopples|ukrainian|valley|valleyrank|valleyrankvalleyrankvalleyrank|venomous|venomouss|venuss|venussrank|venussrankvenussrankvenussrankvenussrankvenussrank|vezer|vezere|vezeress|warmly|xxx|xxxx|xzero|yveskarl|yveskarlina|yveskarlinaka|yxx|yxxkai|zehrab|zehrabzehrabzehrabzehrabzehrab|zerorank|zerorankzerorankzerorankzerorank|zerotrust|zerotrusts|zerotrustss|zzz|pionyerererer|zig&sharko|misipipi&kakaku|voutbsdfnkkv|lalalxlalxdle|crchemolexczxsefv|lastcrenajfningie|dimariadebruynenen|lastcrecrecrecer|ligimitirovaniydaunin|cemolecrchrchemole|crchcrchcrchcrch|cecececececececece|zikozikzokzizozokz|crchadasdfgvfrgt|gansdifjjdifjkonjffdu|puntik|kuzshineko|kadisher|vnncvnmcmcvmncv|mymashine|vsexoroshoharry|nudemeeamputirovat|dizdizodi|csadadsfsav|sdvfenvbkjgnlbknkmopghk|nmvncmvnmckboikgjhbijojortgrdf|dameungrr|unwewewqwq|gagrgagfgdgxsfncdee|chhnbbgbghjve|crcvjkbkvnbjfgivjfde|iouyeryhefyrfvnnvreioaojf2q|nkkmlhhnnbbyuooopyytfv|sikioxoxcme|cposlsacmmcnjfdie|blyatutebyanetpravle|etojonnyetomoysinle|odinbiznesmenustavsiyotsvoyegostarika|tictoxocesnaveshatinogdaddedushku|vistoriyuonvikladivayetgrustniyeblete|lewiskasdkknknwoe|racecurse|noanotherpower|dislikeeverthynlovevelo|crchemolvkofdovosmcmoe|crzenxoaskxce|kaknasoxranenkaxe|zatofotkipizdatiyeele|rytttttt|anasnimetsmenyaremenlousvi|crchemaadsasdadad|yoxagzuvayoxunpoz|imyoungblackandrcihiadnpussylicker|letmeshowwhatyougiveup|yobraputatiriajd|copagangsmysfhnur|vmineocenmnogoonblkjfnv|doctorhannibalpsycho|yapyupizdatiyviskimolodoye|imgladifdjvjfdvnifnvrecvbryyee|eroutuwrfnmzxnj|etocecenskiyflot|goluboysahpmurnejdet|uusuasdaudodsuodaioasdau|hastworexes|baybaybygridlskdfrgreoji|kkhkhhkkjkjhkhkoji|potipotipoti|crchcscddddddddddsdlkjnfhkl|ooptoripitprittoiprt|prptprppeprepeppafroiguhtgksahs|rioioirrrroeoirpire|viytisuximizvodi|popaodkpaskpopofpajmamam|marlonmogspercentofpeople|tiutuosiojimvpsiieee|zinanzinsnedeji|izsamariamsimd|owiworweuwruworwwe|soliiiiiiinaranuebalat|modaiskustvokulinariya|xoxoxooxooxoxeeetoyavovremayaprisel|pizdecebaniystozasmertvnishite|ebaniyzavozastviiii|ebatttttttttt|socsinyourmouthe|bablateperebatpizdec|dvauksazactotisact|outofmymind|diaaaadajgaa|isdippsjjaias|ututututututrejfjwoejfpjqwp|nozamoyeobidniye|tushdlyauveliceniyaobyema|igogoogogogogogog|sitiporosaaututjj|porbugyy|zeoohyfrbn|ghyuhbrdyimmvtygnmybnmutycvbnhhubtrftc|nikadsidjiofsale|pozitivnoyevliyaniyeigr|debroutroutroute|ppsdjoscdjfvojfsnojnsjosonj|zughtjfrhegjhfeuewfwefhwfhu|vprincipeyamogutebepomocye|celuymenyanazlojidfienewjf|drruuuororiridididir|tvoyotecnaoralkatyue|ueleonoriestdoci|zdravstvuytesergeyvladimirovic|soniceandsasyyilimeem|vsevashipismafalyifotki|watisthisdokkwomwmamacoco|kilogramovitsteyke|posletakoyjenshini|zabiliibudemjitdalse|egegeggeeggemeoreoy|nikogonebudetprostopodpishi|crmovefveiuorhoe|creschemolecresclecreschemole|creschekgrfhrihiginggvfgigisthgifenjidhffkdnnvkjb)$"
))
if __name__ == "__main__":
    print("Бот запущен!")
    app.run_polling()
