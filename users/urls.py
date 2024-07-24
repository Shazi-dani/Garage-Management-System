from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegistrationView, UserLoginView, UserLogoutView

app_name = 'users'

"""
URL patterns for user-related views.

This module defines the URL patterns for user registration, login, logout, and 
JWT token handling. Each URL pattern is associated with a specific view class 
or function to handle the corresponding HTTP requests.

Attributes:
    urlpatterns (list): A list of URL patterns for the user-related views.
"""

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
