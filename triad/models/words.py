from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=255)
    potency = models.IntegerField()
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
