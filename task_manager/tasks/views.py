from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.mail import send_mail

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if username and password and email:
        user = User.objects.create_user(username=username, password=password, email=email)
        # Enviar correo de bienvenida
        send_mail(
            'Bienvenido a la plataforma',
            f'Hola {username}, tu cuenta fue creada exitosamente.',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response({"msg": "Cuenta creada exitosamente"}, status=status.HTTP_201_CREATED)
    return Response({"error": "Datos inválidos"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def password_reset(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
        # Lógica para enviar un correo con el enlace de restablecimiento de contraseña
        send_mail(
            'Restablecer contraseña',
            'Aquí tienes el enlace para restablecer tu contraseña.',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response({"msg": "Correo de restablecimiento enviado"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Correo no registrado"}, status=status.HTTP_400_BAD_REQUEST)
