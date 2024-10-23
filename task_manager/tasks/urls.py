# tasks/urls.py
from django.urls import path,include
from rest_framework import routers
from .views import RegisterViewSet, LoginViewSet, PasswordResetViewSet, DashboardViewSet

"""
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
"""

router=routers.DefaultRouter()
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'password_reset', PasswordResetViewSet, basename='password_reset')
router.register(r'dashborad', DashboardViewSet, basename='dashborad' )

urlpatterns = [
    path('api/', include(router.urls)),
    ]