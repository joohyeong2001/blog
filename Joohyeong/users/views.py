from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from .models import User


# class UserListView(generic.ListView):
#     model = User
#     paginate_by = 5

def UserListView(request):
    users = User.objects.all()

    context = {"users": users}

    return render(request, "user_list.html", context=context)


# class UserDetailView(generic.DetailView):
#     model = User

def UserDetailView(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except user.DoesNotExist:
        raise Http404("user %s does not exist" % pk)

    return render(request, "user_detail.html", {"user": user})
