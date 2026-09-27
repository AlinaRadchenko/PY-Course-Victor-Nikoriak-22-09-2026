# hello_project — урок 34 (форми, CRUD)

Проєкт нотаток з [уроку 33](../../lesson_33_django_intro/hello_project/) + сторінки для людей — стан після [уроку 34 «Django: forms, HTML practice»](https://nikoriakviktot.github.io/PY-Course-Victor-Nikoriak-22-09-2026/modules/m4/lesson_34/) (кроки 2 і 4 маршруту [Zero to Hero](https://nikoriakviktot.github.io/notes_chat_app/tutorials/) Django-книги).

| Файл | Що в ньому |
|---|---|
| `hello_app/forms.py` | `NoteForm` (ModelForm, `clean_title`), `NoteSearchForm` |
| `hello_app/views.py` | `note_list` з пошуком, `note_detail`, `note_create`, `note_edit`, `note_delete` (PRG, `messages`) |
| `hello_app/templates/base.html` | спільний шаблон: Bootstrap 5 (CDN), навігація, повідомлення |
| `hello_app/templates/hello_app/` | список, нотатка, форма (crispy), підтвердження видалення |
| `hello_app/tests_forms.py` | тести форм, CRUD, PRG, CSRF і пошуку |

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver          # http://127.0.0.1:8000/notes/
python manage.py test               # тести hello_app
```
