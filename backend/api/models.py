from django.db import models

class Star(models.Model):
    name = models.CharField(max_length=100)  # Name of the star
    ra = models.FloatField()                 # Right Ascension (degrees)
    dec = models.FloatField()                # Declination (degrees)
    distance = models.FloatField()           # Distance in parsecs

    def __str__(self):
        return self.name

class Exoplanet(models.Model):
    name = models.CharField(max_length=100)  # Name of the exoplanet
    ra = models.FloatField()                 # Right Ascension (degrees)
    dec = models.FloatField()                # Declination (degrees)
    distance = models.FloatField()           # Distance in parsecs

    def __str__(self):
        return self.name
