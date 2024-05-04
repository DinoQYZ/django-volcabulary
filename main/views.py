import random
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VocabularyForm, TranslationForm
from .models import Vocabulary, Translation

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def addVocabulary(response):
    if response.method == 'POST':
        form = VocabularyForm(response.POST)
        if form.is_valid():
            if Vocabulary.objects.filter(word=form.cleaned_data['word']).exists():
                return render(response, 'main/addVocabulary.html', {'form': form, 'err_msg': 'Vocabulary already exists!'})

            else:
                form.instance.user = response.user
                vocabulary = form.save(commit=False)
                msg = f'Successfully add \"{vocabulary.word}\"'
                vocabulary.save()
                return render(response, 'main/home.html', {'msg': msg})
        
    else:
        form = VocabularyForm()

    return render(response, 'main/addVocabulary.html', {'form': form})

def editVocabulary(response, id):
    vocabulary = get_object_or_404(Vocabulary, id=id)
    translations = Translation.objects.filter(voc=vocabulary)
    if response.method == 'POST':
        form = TranslationForm(response.POST)
        if form.is_valid():
            translations = form.cleaned_data['translation']
            wd_type = form.cleaned_data['wd_type']
            vocabulary.translation_set.create(trans=translations, wd_type=wd_type)
            msg = f'Successfully update \"{vocabulary.word}\"'
            return render(response, 'main/home.html', {'msg': msg})
        else:
            form = TranslationForm()
    else:
        form = TranslationForm()

    return render(response, 'main/editVocabulary.html', {'form': form, 'vocabulary': vocabulary, 'translations': translations})

def deleteVocabulary(response, id):
    vocabulary = get_object_or_404(Vocabulary, id=id)
    msg = f'Successfully delete \"{vocabulary.word}\"'
    vocabulary.delete()
    return render(response, 'main/home.html', {'msg': msg})

def deleteTranslation(response, translation_id):
    translation = get_object_or_404(Translation, id=translation_id)
    id = translation.voc.id 
    msg = f'Successfully delete \"{translation.voc} - {translation.trans}\"'
    translation.delete()
    return render(response, 'main/home.html', {'id':id, 'msg': msg})

def randomVocabulary(response):
    vocabularies = Vocabulary.objects.all()

    vocabulary = random.choice(vocabularies)
    translations = vocabulary.translation_set.all()

    return render(response, 'main/random.html', {'vocabulary': vocabulary, 'translations': translations})