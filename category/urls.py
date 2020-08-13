from django.urls import path
from . import views

app_name = "category"
urlpatterns = [
    path('', views.category, name="category"),
    path('create/', views.categoryCreate, name="category-create"),
    path('<int:pk>/', views.categoryDetail, name="category-detail"),
    path('<int:pk>/update/', views.categoryUpdate, name="category-update"),
    path('<int:pk>/delete/', views.categoryDelete, name="category-delete"),
]
