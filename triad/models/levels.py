from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=255)
    number_of_wins = models.IntegerField()
