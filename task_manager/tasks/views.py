# tasks/views.py

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from .serializers import RegisterSerializer, UserSerializer, PasswordResetSerializer
from django.contrib.auth.models import User

class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)

            send_mail(
                'Bienvenido a la plataforma',
                f'Hola {user.username}, tu cuenta fue creada exitosamente.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            return Response({
                "user": UserSerializer(user).data,
                "token": token.key,
                "message": "Cuenta creada exitosamente. Se ha enviado un correo de bienvenida."
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "message": "Inicio de sesión exitoso."
            }, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas."}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='reset-password')
    def reset_password(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)

                # Generar el enlace para restablecer la contraseña
                reset_link = f"http://localhost:8080/reset-password/{user.id}"  # Ajusta según tu lógica

                # Enviar el correo de restablecimiento
                send_mail(
                    'Restablecer contraseña',
                    f'Hola {user.username}, aquí tienes el enlace para restablecer tu contraseña: {reset_link}',
                    'from@example.com',  # Cambia esto por el correo de origen que desees usar
                    [user.email],
                    fail_silently=False,
                )

                return Response({
                    "message": "Se ha enviado un correo con el enlace para restablecer la contraseña."
                }, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                return Response({"error": "No se encontró un usuario con ese correo."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({
            "message": "Bienvenido al Dashboard",
            "user": UserSerializer(request.user).data
        }, status=status.HTTP_200_OK)

"""
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, RegisterSerializer

# Registro de usuarios
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Permitir el acceso sin autenticación

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Guarda el nuevo usuario
            # Generar el token de autenticación para el nuevo usuario
            token = Token.objects.get_or_create(user=user)

            # Enviar correo de bienvenida
            send_mail(
                'Bienvenido a la plataforma',
                f'Hola {user.username}, tu cuenta fue creada exitosamente.',
                'from@example.com',  # Cambia esto por el correo de origen que desees usar
                [user.email],
                fail_silently=False,
            )

            return Response({
                "user": UserSerializer(user).data,
                "token": token.key,
                "message": "Cuenta creada exitosamente. Se ha enviado un correo de bienvenida."
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Inicio de sesión de usuarios
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "message": "Inicio de sesión exitoso."
            }, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas."}, status=status.HTTP_400_BAD_REQUEST)

# tasks/views.py



# Vista para restablecer contraseña
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .serializers import PasswordResetSerializer  # Asegúrate de importar el serializador

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)

            # Generar el enlace para restablecer la contraseña
            reset_link = f"http://localhost:8080/reset-password/{user.id}"  # Ajusta el enlace según tu lógica

            # Enviar correo para restablecer contraseña
            send_mail(
                'Restablecer contraseña',
                f'Hola {user.username}, aquí tienes el enlace para restablecer tu contraseña: {reset_link}',
                'from@example.com',  # Cambia esto por el correo de origen que desees usar
                [user.email],
                fail_silently=False,
            )

            return Response({
                "message": "Se ha enviado un correo con el enlace para restablecer la contraseña."
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Verificación de si el usuario está autenticado
class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Bienvenido al Dashboard",
            "user": UserSerializer(request.user).data
        }, status=status.HTTP_200_OK)
"""