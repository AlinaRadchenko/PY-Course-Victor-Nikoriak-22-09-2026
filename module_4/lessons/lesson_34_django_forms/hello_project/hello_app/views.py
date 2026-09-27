from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm, NoteSearchForm
from .models import Note


def index(request):
    return redirect("hello_app:note_list")


def about(request):
    return HttpResponse("Це моя перша сторінка на Django!")


def note_list(request):
    search = NoteSearchForm(request.GET)
    notes = Note.objects.all()
    if search.is_valid() and search.cleaned_data["q"]:
        notes = notes.filter(title__icontains=search.cleaned_data["q"])
    return render(request, "hello_app/note_list.html", {"notes": notes, "search": search})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "hello_app/note_detail.html", {"note": note})


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, f"Нотатку «{note.title}» створено.")
            return redirect("hello_app:note_detail", pk=note.pk)
    else:
        form = NoteForm()
    return render(request, "hello_app/note_form.html", {"form": form, "heading": "Нова нотатка"})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Зміни збережено.")
            return redirect("hello_app:note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, "hello_app/note_form.html", {"form": form, "heading": "Редагування", "note": note})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        messages.info(request, f"Нотатку «{note.title}» видалено.")
        return redirect("hello_app:note_list")
    return render(request, "hello_app/note_confirm_delete.html", {"note": note})
