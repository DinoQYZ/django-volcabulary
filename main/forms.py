from django import forms
from django.forms import ModelForm
from .models import Translation

class AddForm(ModelForm):
    class Meta:
        model = Translation
        exclude = ['vocabulary']