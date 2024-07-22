from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import BlacklistedToken
from .email_utils import send_signup_email


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # Serve the login form template
        return render(request, 'register.html')
    
    def perform_create(self, serializer):
        user = serializer.save()
        send_signup_email(user)

class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # Serve the login form template
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        BlacklistedToken.objects.create(token=token)  # Storing the token in a blacklist model
        return Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
