from django.urls import path
from . import views

app_name = "manufacturer"
urlpatterns = [
    path('', views.manufacturer, name="manufacturer"),
    # path('create/', views.manufacturerCreate, name="manufacturer-create"),
    path('<int:pk>/', views.manufacturerDetail, name="manufacturer-detail"),
    # path('<int:pk>/update/', views.manufacturerDetail, name="manufacturer-update"),
    # path('<int:pk>/delete/', views.manufacturerDetail, name="manufacturer-delete"),
]
