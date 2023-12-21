from django.db import models

class SpellWords(models.Model):
    spell = models.ForeignKey("Spell", on_delete=models.CASCADE)
    word = models.ForeignKey("Word", on_delete=models.CASCADE)
    class Meta:
        unique_together = ('spell', 'word')