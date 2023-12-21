from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    potency = models.IntegerField()
    type = models.ForeignKey("Type", on_delete=models.CASCADE)