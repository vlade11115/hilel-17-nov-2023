import uuid

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.signing import Signer, BadSignature
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import UserCreationFormWithEmail, QRInput
from .models import Greeting, QRCode
from .qr_generator import generate_qr


# Create your views here.
def send_activation_email(request, user: User):
    user_signed = Signer().sign(user.id)
    signed_url = request.build_absolute_uri(f"/activate/{user_signed}")
    send_mail(
        "Registration complete",
        "Click here to activate your account: " + signed_url,
        "vlad@kartavets.xyz",
        [user.email],
        fail_silently=False,
    )


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly."
        " If you don't receive an email, "
        "please make sure you've entered the address you registered with, and check your spam folder."
    )
    success_url = reverse_lazy("login")


def activate(request, user_signed):
    try:
        user_id = Signer().unsign(user_signed)
    except BadSignature:
        return redirect("login")
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect("login")
    user.is_active = True
    user.save()
    return redirect("login")


def index(request):
    return render(request, "index.html", {"user": request.user})


def register(request):
    if request.method == "GET":
        form = UserCreationFormWithEmail()
        return render(request, "register.html", {"form": form})

    form = UserCreationFormWithEmail(request.POST)
    if form.is_valid():
        form.instance.is_active = False
        form.save()
        send_activation_email(request, form.instance)
        return redirect("login")
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def generate_qr_code(request):
    form = QRInput(request.POST)
    if request.method == "GET":
        return render(request, "qr_code.html", {"form": form, "qr": None})
    if form.is_valid():
        text = form.cleaned_data["text"]
        qr_image = generate_qr(text)
        qr = QRCode.objects.create(text=text)
        qr.qr_code.save(uuid.uuid4().hex, qr_image)
        return render(request, "qr_code.html", {"form": form, "qr": qr})


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
