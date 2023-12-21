from django.db import models
from django.contrib.auth.models import User

class Potion(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    potency = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)