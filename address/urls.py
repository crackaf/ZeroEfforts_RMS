from django.urls import path
from . import views

app_name = "address"
urlpatterns = [
    path('', views.address, name="address"),
    path('create/', views.addressCreate, name="address-create"),
    path('<int:pk>/', views.addressDetail, name="address-detail"),
    path('<int:pk>/update/', views.addressUpdate, name="address-update"),
    path('<int:pk>/delete/', views.addressDelete, name="address-delete"),
]
