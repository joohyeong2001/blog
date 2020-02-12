from django.urls import path
from django.views import debug

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
]