from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.urls import *
from CRUD.views import HomeView
from register.views import RegisterView

app_name = "register"


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='sign_up'),
]
