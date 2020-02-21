from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class AbsBaseUser(AbstractBaseUser):
    custom_username = models.CharField(max_length=20, verbose_name='name', null=True)
    USERNAME_FIELD = 'custom_username'
    avatar = models.ImageField(blank=True)

    def __str__(self):
    # """ String for representing the Model object."""
        return self.custom_username

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this user. """
        return reverse("user-detail", args=[str(self.id)])