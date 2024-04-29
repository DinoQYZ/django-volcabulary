from django.shortcuts import render
from .forms import AddForm
from .models import Vocabulary, Translation

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def add(response):
    if response.method == "POST":
        data = response.POST
        translations = data.getlist('translations[]')
        wd_types = data.get('wd_types[]')
        vocabulary = data.get('vocabulary')

        if translations and wd_types:
            new_voc = Vocabulary(user=response.user, word=vocabulary)
            new_voc.save()

        for i in range(len(translations)):
            new_trans = Translation(voc=vocabulary, wd_type=wd_types[i], trans=translations[i])
            new_trans.save()

    return render(response, "main/add.html", {})