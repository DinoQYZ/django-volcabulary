from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voc", null=False)
    word = models.TextField()

    def __str__(self) -> str:
        return self.word
    
class Translation(models.Model):
    voc = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    wd_type = models.TextField(max_length=50)
    trans = models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.wd_type + " " + self.trans