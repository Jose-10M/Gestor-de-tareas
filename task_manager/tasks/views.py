# tasks/views.py
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
            token, created = Token.objects.get_or_create(user=user)

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
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "message": "Inicio de sesión exitoso."
            }, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas."}, status=status.HTTP_400_BAD_REQUEST)

# tasks/views.py



# Vista para restablecer contraseña
class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            # Aquí podrías generar un token o un enlace único para el restablecimiento
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
        except User.DoesNotExist:
            return Response({"error": "No se encontró un usuario con ese correo."}, status=status.HTTP_400_BAD_REQUEST)

# Verificación de si el usuario está autenticado
class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Bienvenido al Dashboard",
            "user": UserSerializer(request.user).data
        }, status=status.HTTP_200_OK)