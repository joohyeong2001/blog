from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import Post

from django.http import HttpResponseRedirect


def Index(request):
    post = Post.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        "post": post,
        'num_visits': num_visits,
    }

    return render(request, "index.html", context=context)
    

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
