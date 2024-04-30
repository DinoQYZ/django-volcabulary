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
            vocabulary = form.save()
            for i, translation_text in enumerate(response.POST.getlist('translations[]')):
                wd_type = response.POST.getlist('wd_types[]')[i]
                Translation.objects.create(vocabulary=vocabulary, trans=translation_text, wd_type=wd_type)
            return render(response, 'main/home.html', {})

    else:
        form = VocabularyForm()

    return render(response, 'main/add.html', {'form': form})