# hello_project — урок 35 (DRF)

Проєкт нотаток з [уроку 33](../../lesson_33_django_intro/hello_project/) + REST API на Django REST Framework — стан після [уроку 35 «DRF overview + Django vs FastAPI»](https://nikoriakviktot.github.io/PY-Course-Victor-Nikoriak-22-09-2026/modules/m4/lesson_35/).

| Файл | Що в ньому |
|---|---|
| `hello_app/serializers.py` | `NoteSerializer` — модель ↔ JSON, валідація |
| `hello_app/api.py` | `NoteViewSet`: CRUD, фільтри `?pinned=`, `?search=`, дія `POST /api/notes/{id}/pin/` |
| `hello_project/urls.py` | роутер `/api/`, OpenAPI-схема `/api/schema/` |
| `hello_app/tests_api.py` | тести API (`APITestCase`) |
| `fastapi_notes.py` | той самий API на FastAPI — для порівняння |

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver          # http://127.0.0.1:8000/api/notes/ — browsable API
python manage.py test               # тести hello_app
uvicorn fastapi_notes:app --port 8001   # FastAPI-версія: http://127.0.0.1:8001/docs
```
