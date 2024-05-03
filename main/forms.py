from django import forms
from .models import Vocabulary, Translation

class VocabularyForm(forms.ModelForm):
    word = forms.CharField(label="Vocabulary", max_length=255, required=True)

    class Meta:
        model = Vocabulary
        fields = ['word']

class TranslationForm(forms.ModelForm):
    translation = forms.CharField(label="translation", max_length=255, required=True)
    wd_type =forms.CharField(label="wd_type", max_length=255, required=True)

    class Meta:
        model = Translation
        fields = ['translation', 'wd_type']