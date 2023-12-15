from django.urls import path
from django.contrib.auth import views as views_auth
from . import views


urlpatterns = [
    # Первый путь логина
    # path('login/', views.user_login, name='login',)
    path('login/', views_auth.LoginView.as_view(), name='login'),
    path('logout/', views_auth.LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard')
]