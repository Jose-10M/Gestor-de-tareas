# tasks/urls.py
from django.urls import path
from .views import RegisterView, LoginView, DashboardView, PasswordResetView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
