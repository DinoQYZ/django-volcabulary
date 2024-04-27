from django.contrib import admin
from .models import Vocabulary, Translation

# Register your models here.

admin.site.register(Vocabulary)
admin.site.register(Translation)