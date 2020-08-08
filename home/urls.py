from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name="home-index"),
    path('login', views.login, name="home-login"),
    path('logout', views.logout, name="home-logout"),
    path('logout', views.contact, name="home-contact"),
    path('logout', views.about, name="home-about"),
]
