from django.contrib import admin
from django.urls import path
from . import views

app_name="account"
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('detail/', views.detail, name="account-detail")
]
