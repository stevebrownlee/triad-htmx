from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    potency = models.IntegerField()
    date_created = models.DateTimeField()
    artifact = models.ForeignKey("Artifact", on_delete=models.CASCADE)
    spell = models.ForeignKey("Spell", on_delete=models.CASCADE)
    potion = models.ForeignKey("Potion", on_delete=models.CASCADE)