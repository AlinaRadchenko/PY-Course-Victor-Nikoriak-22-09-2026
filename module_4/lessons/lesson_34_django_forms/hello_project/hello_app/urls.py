from django.urls import path

from . import views

app_name = "hello_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("notes/", views.note_list, name="note_list"),
    path("notes/new/", views.note_create, name="note_create"),
    path("notes/<int:pk>/", views.note_detail, name="note_detail"),
    path("notes/<int:pk>/edit/", views.note_edit, name="note_edit"),
    path("notes/<int:pk>/delete/", views.note_delete, name="note_delete"),
]
