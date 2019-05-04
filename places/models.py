from django.contrib.gis.db import models

# Create your models here.
class Place(models.Model):
    name = models.TextField()
    location = models.PointField()
    why = models.TextField(blank=True, null=True)
    suggestion = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
