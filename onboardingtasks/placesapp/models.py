from django.contrib.gis.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Places(models.Model):
    title = models.CharField(max_length=100)
    location = models.PointField()
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=20)
    type_of_city = models.CharField(max_length=20)
    tags = TaggableManager()

    def get_unique_cities(self):
        return Places.objects.all().values_list('city', flat=True).distinct()

    def __str__(self):
        return self.title
