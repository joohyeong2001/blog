from django.shortcuts import render
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
