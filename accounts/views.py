from django.shortcuts import render

from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy



# Create your views here.

class SignupView(CreateView):

    success_url = reverse_lazy("polls:index")

    template_name = "accounts/signup.html"

    form_class = UserCreationForm
