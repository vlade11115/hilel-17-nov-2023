"""
URL configuration for gettingstarted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, PasswordResetConfirmView

# from django.contrib import admin
from django.urls import path, include

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("qr/", hello.views.generate_qr_code, name="generate_qr_code"),
    path("db/", hello.views.db, name="db"),
    path("register/", hello.views.register, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", hello.views.logout_view, name="logout"),
    path("users/", hello.views.list_users, name="users"),
    path("activate/<user_signed>", hello.views.activate, name="activate"),
    path("forgot_password/", hello.views.ResetPasswordView.as_view(), name="password_reset"),
    path(
        "forgot_password/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html", success_url="/login/"
        ),
        name="password_reset_confirm",
    ),
    path("accounts/", include("allauth.urls")),
]
