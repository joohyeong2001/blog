from django.db import models
from django.urls import reverse


class Post(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.TextField(default="일상")
    # modified_date = models.DateTimeField(auto_add=True)

    def __str__(self):
        """ String for representing the Model object. """
        return self.title

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this book. """
        return reverse("post-detail", args=[str(self.id)])