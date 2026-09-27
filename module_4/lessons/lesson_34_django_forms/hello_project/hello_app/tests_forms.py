from django.test import Client, TestCase
from django.urls import reverse

from .forms import NoteForm
from .models import Note


class NoteFormTests(TestCase):
    def test_title_is_stripped_and_validated(self):
        form = NoteForm(data={"title": "  Купити квитки  ", "priority": "3"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], "Купити квитки")
        self.assertFalse(NoteForm(data={"title": "ok", "priority": "2"}).is_valid())


class NoteCrudTests(TestCase):
    def test_create_redirects_with_message(self):
        # follow=True — пройти за перенаправленням, як браузер; повідомлення — на цій сторінці
        response = self.client.post(reverse("hello_app:note_create"), {"title": "Нова нотатка", "priority": "2"},
                                    follow=True)
        note = Note.objects.get(title="Нова нотатка")
        self.assertEqual(response.redirect_chain, [(reverse("hello_app:note_detail", args=[note.pk]), 302)])
        self.assertContains(response, "Нотатку «Нова нотатка» створено.")

    def test_invalid_data_rerenders_form(self):
        response = self.client.post(reverse("hello_app:note_create"), {"title": "ok", "priority": "9"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(response.context["form"].errors), {"title", "priority"})
        self.assertEqual(Note.objects.count(), 0)

    def test_delete_only_on_post(self):
        note = Note.objects.create(title="Видали мене")
        url = reverse("hello_app:note_delete", args=[note.pk])
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertTrue(Note.objects.filter(pk=note.pk).exists())
        self.assertRedirects(self.client.post(url), reverse("hello_app:note_list"))
        self.assertFalse(Note.objects.filter(pk=note.pk).exists())

    def test_csrf_is_enforced(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse("hello_app:note_create"), {"title": "Без токена", "priority": "2"})
        self.assertEqual(response.status_code, 403)

    def test_search(self):
        Note.objects.create(title="Вивчити Django Forms")
        Note.objects.create(title="Купити молоко")
        response = self.client.get(reverse("hello_app:note_list"), {"q": "django"})
        self.assertEqual([n.title for n in response.context["notes"]], ["Вивчити Django Forms"])
