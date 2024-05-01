from django import forms
from .models import Vocabulary

class VocabularyForm(forms.ModelForm):
    word = forms.CharField(label="Vocabulary", max_length=255, required=True)
    translations = forms.CharField(label="Translations", widget=forms.Textarea, required=False)

    class Meta:
        model = Vocabulary
        fields = ['word']
