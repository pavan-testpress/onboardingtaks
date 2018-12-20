from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class UserAccounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_info')
    profile_picture = models.ImageField(upload_to='./accounts_meida', blank=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.user



