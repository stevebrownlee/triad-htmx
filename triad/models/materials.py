from django.db import models

class Material(models.Model):
    material = models.CharField(max_length=255)
    potency = models.IntegerField()
    type = models.ForeignKey("Type", on_delete=models.CASCADE)