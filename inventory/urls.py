from django.urls import path
from . import views

app_name = "inventory"
urlpatterns = [
    path('', views.inventory, name="inventory"),
    path('create/', views.inventoryCreate, name="inventory-create"),
    path('<int:pk>/', views.inventoryDetail, name="inventory-detail"),
    path('<int:pk>/update/', views.inventoryUpdate, name="inventory-update"),
    path('<int:pk>/delete/', views.inventoryDelete, name="inventory-delete"),
]
