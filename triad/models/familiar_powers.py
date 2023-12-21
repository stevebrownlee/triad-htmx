from django.db import models

class FamiliarPowers(models.Model):
    power = models.ForeignKey("Power", on_delete=models.CASCADE)
    familiar = models.ForeignKey("Familiar", on_delete=models.CASCADE)
    class Meta:
        unique_together = ('power', 'familiar')