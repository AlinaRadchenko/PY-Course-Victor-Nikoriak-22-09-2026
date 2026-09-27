from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        notes = Note.objects.all()
        pinned = self.request.query_params.get("pinned")
        if pinned is not None:
            notes = notes.filter(is_pinned=pinned.lower() in ("1", "true", "yes"))
        search = self.request.query_params.get("search")
        if search:
            notes = notes.filter(title__icontains=search)
        return notes

    @action(detail=True, methods=["post"])
    def pin(self, request, pk=None):
        note = self.get_object()
        note.is_pinned = True
        note.save(update_fields=["is_pinned"])
        return Response(self.get_serializer(note).data)
