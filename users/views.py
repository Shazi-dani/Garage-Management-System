from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .email_utils import send_signup_email
from .forms import UserRegistrationForm

User = get_user_model()

def signup_success(request):
    return render(request, 'register_success.html')

def login_success(request):
    return render(request, 'login_success.html')

def logout_success(request):
    return render(request, 'logout_success.html')
class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:register_success')  # Redirect URL after success

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        # Send an email or display a message
        messages.success(self.request, 'You have successfully signed up!')
        send_signup_email(user)
        return response

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
                messages.success(request, 'Logged in successfully.')
                return redirect('users:login_success')
            else:
                messages.error(request, 'Invalid username or password.')
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            for msg in serializer.errors.values():
                messages.error(request, msg[0])
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
        messages.info(request, ' Logged out Successfully')
        return redirect('users:logout_success')
