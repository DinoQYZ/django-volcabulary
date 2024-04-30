from django import forms
from .models import Vocabulary

class VocabularyForm(forms.ModelForm):
    vocabulary = forms.CharField(label="Vocabulary", max_length=255, required=True)
    translations = forms.CharField(label="Translations", widget=forms.Textarea, required=False)

    class Meta:
        model = Vocabulary
        fields = ['word']

    def save(self, commit=True):
        vocabulary = super().save(commit=commit)
        if commit:
            translations_data = self.cleaned_data.get('translations')
            if translations_data:
                for line in translations_data.split("\n"):
                    trans, wd_type = line.split(',')
                    vocabulary.translation_set.create(trans=trans.strip(), wd_type=wd_type.strip())
        return vocabulary
