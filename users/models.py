from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=20, verbose_name="name", null=True, unique=True
    )
    USERNAME_FIELD = "username"
    avatar = models.ImageField(blank=True)

    def __str__(self):
        # """ String for representing the Model object."""
        return self.username

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this user. """
        return reverse("user-detail", args=[str(self.id)])
