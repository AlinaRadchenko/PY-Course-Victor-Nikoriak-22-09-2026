from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "priority", "is_pinned"]
        widgets = {"content": forms.Textarea(attrs={"rows": 4})}

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("Заголовок має містити щонайменше 3 символи.")
        return title


class NoteSearchForm(forms.Form):
    q = forms.CharField(label="Пошук", required=False, max_length=100)
