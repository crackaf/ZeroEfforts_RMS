from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('login', views.login, name="home-login"),
    path('logout', views.logout, name="home-logout"),
]
