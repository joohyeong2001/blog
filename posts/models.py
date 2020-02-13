from django.db import models


class Post(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.TextField(default="일상")
    tag = models.TextField(default="블로그 챌린지")
    post_views = models.IntegerField(default=0)
    # modified_date = models.DateTimeField(auto_add=True)
