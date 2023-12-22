from django.urls import path
from django.contrib.auth import views as views_auth
from . import views
from django.conf.urls import include


urlpatterns = [
    # Первый путь логина
    # path('login/', views.user_login, name='login',)

    # url-ы для входа и выхода
    #path('login/', views_auth.LoginView.as_view(), name='login'),
    #path('logout/', views_auth.LogoutView.as_view(), name='logout'),

    # url-ы для изменения пароля
    #path('password-change/', views_auth.PasswordChangeView.as_view(), name='password_change'),
    #path('password-change/done', views_auth.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #url-ы для сброса пароля
    #path('password-reset/', views_auth.PasswordResetView.as_view(), name='password_reset'),
    #path('password-reset/done/', views_auth.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>/', views_auth.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password-reset/complete/', views_auth.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register')
]