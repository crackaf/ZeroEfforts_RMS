from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pos'
urlpatterns = [
    path('', views.BrandCreateView.as_view()),
]
