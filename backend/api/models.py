# star_map/models.py

from django.db import models

class Exoplanet(models.Model):
    name = models.CharField(max_length=200)
    ra = models.FloatField()
    dec = models.FloatField()

class Star(models.Model):
    name = models.CharField(max_length=200)
    ra = models.FloatField()
    dec = models.FloatField()
    distance = models.FloatField()  # Parallax or other distance measure
