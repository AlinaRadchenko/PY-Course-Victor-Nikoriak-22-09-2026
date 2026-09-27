from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Note


class NoteApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", password="alice-pass")
        Note.objects.create(title="Перша нотатка")

    def test_list_is_public(self):
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_requires_login(self):
        response = self.client.post("/api/notes/", {"title": "Без входу"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_and_validation(self):
        self.client.force_authenticate(self.user)
        created = self.client.post("/api/notes/", {"title": "Нова", "priority": 4}, format="json")
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        self.assertEqual(created.data["priority_label"], "Терміновий")
        bad = self.client.post("/api/notes/", {"title": "x"}, format="json")
        self.assertEqual(bad.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", bad.data)
