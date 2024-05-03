from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("addVocabulary/", views.addVocabulary, name="addVocabulary"),
    path("editVocabulary/<int:id>/", views.editVocabulary, name="editVocabulary"),
    path("delete/<int:id>/", views.deleteVocabulary, name='deleteVocabulary'),
]