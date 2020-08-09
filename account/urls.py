from django.urls import path
from . import views

app_name="account"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('detail/', views.detail, name="account-detail")
]
