from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import AbsBaseUser

from django.http import HttpResponseRedirect

class UserListView(generic.ListView):
    model = AbsBaseUser
    paginate_by = 5


class UserDetailView(generic.DetailView):
    model = AbsBaseUser
