from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from .models import Post


def Index(request):
    post = Post.objects.all()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "post": post,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=context)


# CBV PostListView
# class PostListView(generic.ListView):
#     model = Post
#     paginate_by = 5

# FBV - PostListView
def PostListView(request):
    posts = Post.objects.all()

    context = {"posts": posts}

    return render(request, "post_list.html", context=context)


def PostDetailView(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except post.DoesNotExist:
        raise Http404("Post %s does not exist" % pk)

    return render(request, "post_detail.html", {"post": post})

