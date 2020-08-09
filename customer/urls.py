from django.urls import path
from . import views

app_name = "customer"
urlpatterns = [
    path('', views.customer, name="customer"),
    path('<int:pk>/', views.customerDetail, name="customer-detail"),
]
