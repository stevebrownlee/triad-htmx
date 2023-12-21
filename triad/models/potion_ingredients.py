from django.db import models

class PotionIngredients(models.Model):
    potion = models.ForeignKey("Potion", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    class Meta:
        unique_together = ('potion', 'ingredient')