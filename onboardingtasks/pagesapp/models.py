from model_utils.models import TimeStampedModel
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Pages(TimeStampedModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content_html = models.TextField()
    ordering = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pages, self).save(*args, **kwargs)
