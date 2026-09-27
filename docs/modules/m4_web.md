# М4. Web (+ Web Advanced)

Програми говорять мережею: спершу — як клієнт до чужих API, далі — власні сервери на Django і FastAPI.

Уроки модуля:

- [Урок 31. HTTP: requests, httpx, aiohttp](m4/lesson_31.md) — шлях запиту: URL, IP і DNS, порти, TCP-рукостискання, TLS; HTTP як текст (запит сокетом), методи й статус-коди; `requests`: `params`, `json`, заголовки й токен, `raise_for_status`, тайм-аути й ієрархія винятків, повторні спроби з backoff і чому не для `POST`, `Session`; справжній API PyPI; `httpx` і `AsyncClient` + `gather`, `aiohttp`, потоки; архітектура: свій клієнт до API з доменними винятками, вибір бібліотеки. Практика — на навчальному API диспетчерської `smachno_api.py`.
- [Урок 32. REST: принципи дизайну API](m4/lesson_32.md) — метео-API викладача (телеграми SYNOP з ogimet.com, `pymetdecoder`): усі типи API на одних даних — HTTP+CSV, JSON-RPC, GraphQL, SOAP, gRPC, WebSocket, SSE, webhook з підписом HMAC — і як обрати; REST: ресурси й URL, методи й ідемпотентність, статус-коди й формат помилок, фільтри, `fields`, пагінація, `PATCH`, `202 Accepted`, OpenAPI; кейс v1 → v2; архітектура: репозиторій → FastAPI → клієнт-клас → Streamlit-карта погоди, Docker Compose.
- [Урок 33. Django intro: MVT, ORM, admin](m4/lesson_33.md) — перший крок застосунку нотаток, що виросте до [Notes Chat App](https://github.com/NikoriakViktot/notes_chat_app) викладача (кроки 1–2 маршруту [Zero to Hero](https://nikoriakviktot.github.io/notes_chat_app/tutorials/) Django-книги): `startproject` / `startapp`, `settings.py`, MVT і шлях запиту, view, `path` / `include`, модель `Note`, `makemigrations` / `sqlmigrate` / `migrate`, ORM (`create`, `filter`, lookups, `get`, лінивий QuerySet, `.query`, `update`, `delete`), шаблон, адмінка й суперкористувач; практика — `is_pinned`, `priority`, блокноти.
- [Урок 34. Django: forms, HTML practice](m4/lesson_34.md) — два рефакторинги проєкту уроку 33 на коді старого курсу (кроки 2 і 4 Django-книги): голий HTML → Bootstrap CRUD (`ModelForm`, PRG, `messages`, `base.html`, CSRF) і Bootstrap → crispy dashboard (3-рівневі шаблони, `FormHelper` + `Layout`, context processor); «Знайди помилку» — справжній баг старого коду: `is_pinned` губився при створенні.
- [Урок 35. DRF overview + Django vs FastAPI](m4/lesson_35.md) — REST API до нотаток уроку 33: налаштування `REST_FRAMEWORK`, `ModelSerializer` (явні `fields`, `read_only_fields`, `validate_<поле>`, `many=True`), `ModelViewSet` + `DefaultRouter`, пагінація, `IsAuthenticatedOrReadOnly` і чому `403`, а не `401`, фільтри в `get_queryset`, `@action` `pin`, browsable API, OpenAPI через drf-spectacular, `APITestCase`; той самий API на FastAPI і як обрати; «Знайди помилку» — `fields = "__all__"` віддає хеш пароля.

Решта уроків — 🚧 у розробці.

**Django-книга викладача.** Уроки М4 про Django ведуть по маршруту Zero to Hero [Django-книги](https://nikoriakviktot.github.io/notes_chat_app/): урок 33 — кроки 1–2, 34 — кроки 2 і 4, 35 — API до нотаток, 38 і 44 — крок 3, 40 — крок 5, 41 — крок 6, 45 — крок 7, 48–49 — кроки 8–9. Код — зі старого курсу, кожен урок — рефакторинг проєкту попереднього (що змінилося, діфи, архітектура до/після); сторінки курсу — стислий урок із практикою, книга — поглиблення (посилання «Поглиблено» в кожному розділі).

17 уроків (лекції #31–47 у навігаційній таблиці v5.0): HTTP/REST → Django intro → DRF/FastAPI → повний CRUD → middlewares/кешування → auth/security basics → тестування API (лекції #31–41, «Web»), потім AI-інструменти розробника, інтеграція LLM API, архітектура застосунків, WebSockets, security advanced, Telegram Bot API (лекції #42–47, «Web Advanced»).

«Web Advanced» — це продовження М4, не окремий модуль: обидва блоки йдуть під одним наскрізним номером уроку, а модулі М5/М6 зберігають свої номери одразу після «Web Advanced» без зсуву.
