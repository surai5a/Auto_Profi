from django.urls import path
from django.contrib.auth import views as views_auth
from . import views


urlpatterns = [
    # Первый путь логина
    # path('login/', views.user_login, name='login',)

    # url-ы для входа и выхода
    path('login/', views_auth.LoginView.as_view(), name='login'),
    path('logout/', views_auth.LogoutView.as_view(), name='logout'),

    # url-ы для изменения пароля
    path('password-change/', views_auth.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', views_auth.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name='dashboard')
]