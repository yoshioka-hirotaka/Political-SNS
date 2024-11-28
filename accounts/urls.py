from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("index/", views.index, name="index"),
]
