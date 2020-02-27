from django.urls import path
from django.views import debug

from . import views

urlpatterns = [
    path("userlist/", views.UserListView, name="user-list"),
    path("<int:pk>", views.UserDetailView, name="user-detail"),
    path("profile", views.UserProfile, name="user-profile"),
]
