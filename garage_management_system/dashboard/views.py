from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, get_user_model

# Create your views here.
User = get_user_model()


class DashboardView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # Serve the dashboard page
        return render(request, 'dashboard.html')
