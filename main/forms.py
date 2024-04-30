from django import forms
from .models import Vocabulary, Translation

class VocabularyForm(forms.ModelForm):
    vocabulary = forms.CharField(label="Vocabulary", max_length=255, required=True)

    class Meta:
        model = Vocabulary
        fields = ['vocabulary']

    translations = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            translations = "\n".join(
                f"{translation.trans},{translation.wd_type}" for translation in self.instance.translation_set.all()
            )
            self.fields['translations'].initial = translations

    def save(self, commit=True):
        vocabulary = super().save(commit=commit)
        if commit:
            translations_data = self.cleaned_data.get('translations')
            if translations_data:
                for translation_data in translations_data.split("\n"):
                    trans, wd_type = translation_data.split(',')
                    Translation.objects
