from django.urls import path
from django.views import debug

from . import views


urlpatterns = [
    path("", views.Index, name="index"),
    path("postlist/", views.PostListView, name="post-list"),
    path("post/<int:pk>", views.PostDetailView, name="post-detail"),
]
