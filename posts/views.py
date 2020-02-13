from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import Post

from django.http import HttpResponseRedirect


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
