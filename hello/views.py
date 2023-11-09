from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Greeting


# Create your views here.


def index(request):
    return render(request, "index.html", {"user": request.user})


def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def db(request):
    print(request.user)
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


@login_required
def list_users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})
