from django.shortcuts import render
from .forms import VocabularyForm
from .models import Vocabulary, Translation

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def add(response):
    if response.method == 'POST':
        form = VocabularyForm(response.POST)
        if form.is_valid():
            form.instance.user = response.user
            vocabulary = form.save(commit=False) 
            vocabulary.save() 
            translations_data = form.cleaned_data.get('translations')
            if translations_data:
                for line in translations_data.split("\n"):
                    trans, wd_type = line.split(',')
                    vocabulary.translation_set.create(trans=trans.strip(), wd_type=wd_type.strip())
            return render(response, 'main/home.html', {})
        
    else:
        form = VocabularyForm()

    return render(response, 'main/add.html', {'form': form})