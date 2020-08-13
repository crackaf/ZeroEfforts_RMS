from django.urls import path
from . import views

app_name = "inventory"
urlpatterns = [
    path('', views.inventory, name="inventory"),
    path('create/', views.customerCreate, name="inventory-create"),
    path('<int:pk>/', views.customerDetail, name="inventory-detail"),
    path('<int:pk>/update/', views.customerUpdate, name="inventory-update"),
    path('<int:pk>/delete/', views.customerDelete, name="inventory-delete"),
]
