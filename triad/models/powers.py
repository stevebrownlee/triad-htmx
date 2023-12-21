from django.db import models

class Power(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    attack_strength = models.IntegerField()
    type = models.ForeignKey("Type", on_delete=models.CASCADE)