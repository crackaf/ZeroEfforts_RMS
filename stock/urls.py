from django.urls import path, include
from . import views

app_name = "stock"
urlpatterns = [
    path('', views.stock, name="stock"),
    path('create/', views.stockCreate, name="stock-create"),
    path('<int:pk>/', views.stockDetail, name="stock-detail"),
    path('<int:pk>/update/', views.stockUpdate, name="stock-update"),
    path('<int:pk>/delete/', views.stockDelete, name="stock-delete"),
    # path('inventory/', include('inventory.urls', namespace="inventory"), name="inventory"),
]
