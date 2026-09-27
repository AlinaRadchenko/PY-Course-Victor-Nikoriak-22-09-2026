from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    priority_label = serializers.CharField(source="get_priority_display", read_only=True)

    class Meta:
        model = Note
        fields = ["id", "title", "content", "is_pinned", "priority", "priority_label", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_title(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError("Заголовок має містити щонайменше 3 символи.")
        return value
