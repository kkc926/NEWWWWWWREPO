from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy
# Create your views here.

class RegisterView(CreateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy('register:login')
    form_class = UserCreationForm
