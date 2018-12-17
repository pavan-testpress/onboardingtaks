from django.db import models
from django.contrib.auth.models import User

class Invitations(models.Model):
    invitor_email = models.EmailField()
    invitee_email = models.EmailField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    registered = models.BooleanField(default="False")
    

    def __str__(self):
        return self.invitee_email