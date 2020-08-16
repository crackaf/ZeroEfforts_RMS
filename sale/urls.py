from django.urls import path
from . import views

app_name = "customer"
urlpatterns = [
    path('', views.customer, name="customer"),
    path('create/', views.customerCreate, name="customer-create"),
    path('<int:pk>/', views.customerDetail, name="customer-detail"),
    path('<int:pk>/update/', views.customerUpdate, name="customer-update"),
    path('<int:pk>/delete/', views.customerDelete, name="customer-delete"),
]
