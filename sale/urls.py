from django.urls import path
from . import views

app_name = "sale"
urlpatterns = [
    path('', views.sale, name="sale"),
    path('create/', views.saleCreate, name="sale-create"),
    path('<int:pk>/', views.saleDetail, name="sale-detail"),
    path('<int:pk>/update/', views.saleUpdate, name="sale-update"),
    path('<int:pk>/delete/', views.saleDelete, name="sale-delete"),
]
