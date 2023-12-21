from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    background = models.CharField(max_length=255)
    sorceror_name = models.CharField(max_length=255)
    xp_level = models.ForeignKey("Level", on_delete=models.CASCADE)