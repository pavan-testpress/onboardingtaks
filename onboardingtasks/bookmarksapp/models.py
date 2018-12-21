from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Folders(models.Model):
    folder_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.folder_name


class Bookmarks(models.Model):
    folder_name = models.ForeignKey(Folders, on_delete=models.CASCADE, default=1)
    bookmark_url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
