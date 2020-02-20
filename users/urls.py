from django.urls import path
from django.views import debug

from . import views

urlpatterns = [
    path("userlist/", views.UserListView.as_view(), name="user-list"),
    path("<int:pk>", views.UserDetailView.as_view(), name="user-detail"),
]
