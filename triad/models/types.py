from django.db import models

class Type(models.Model):
    description = models.CharField(max_length=255)