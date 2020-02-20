from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import User

from django.http import HttpResponseRedirect

class UserListView(generic.ListView):
    model = User
    paginate_by = 5


class UserDetailView(generic.DetailView):
    model = User
