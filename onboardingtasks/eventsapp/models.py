from model_utils.models import TimeStampedModel
from placesapp.models import Places
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Events(TimeStampedModel):
    title = models.CharField(max_length = 100)
    place = models.ForeignKey(Places,on_delete = models.CASCADE)
    tags = TaggableManager()
    created_by = models.CharField(max_length=50)

    def __str__(slef):
        return self.title

class EventTime(models.Model):
    event_start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    event_end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    event = models.ForeignKey(Events,on_delete = models.CASCADE,related_name="event_times")


