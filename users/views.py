from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .email_utils import send_signup_email

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    """
    View for handling user registration.

    Attributes:
        queryset: Queryset of all User objects.
        serializer_class: Serializer class for user registration.
        permission_classes: Permissions for the view.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to render the registration page.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: Rendered registration page.
        """
        return render(request, 'register.html')
    
    def perform_create(self, serializer):
        """
        Save the new user and send a signup email.

        Args:
            serializer: The serializer with validated data.

        Returns:
            None
        """
        user = serializer.save()
        send_signup_email(user)

class UserLoginView(APIView):
    """
    View for handling user login.

    Attributes:
        permission_classes: Permissions for the view.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to render the login page.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: Rendered login page.
        """
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user login.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: Redirects to the dashboard if login is successful.
            Response: Error response if login fails.
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    """
    View for handling user logout.
    """
    def post(self, request):
        """
        Handle POST requests for user logout.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: Redirects to the dashboard after logout.
        """
        logout(request)
        return redirect('dashboard:dashboard')
