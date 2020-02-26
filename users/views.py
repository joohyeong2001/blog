from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import AbsBaseUser


class UserListView(generic.ListView):
    model = AbsBaseUser
    paginate_by = 5


class UserDetailView(generic.DetailView):
    model = AbsBaseUser


def UserProfile(request):
    return render(request, "users/user_profile.html")
