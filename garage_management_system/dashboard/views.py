from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.utils.timezone import now

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Appointment
from .forms import AppointmentForm
from .serializers import AppointmentSerializer

# Create your views here.
User = get_user_model()

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add more context variables if needed
        user = self.request.user
        if user.is_authenticated:
            user_type = getattr(user, 'user_type', 'customer')
            username = user.username
        else:
            user_type = 'guest'
            username = 'Guest'
        context.update({
            'user_type': user_type,
            'username': username,
        })

        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            self.authentication_classes = [JWTAuthentication]
            self.permission_classes = [AllowAny]
            return APIView.dispatch(self, request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)


class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Fetch appointments for the logged-in user only
        return Appointment.objects.filter(user=self.request.user)

class AppointmentAllView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Fetch appointments for the logged-in user only
        return Appointment.objects.all()

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['vehicle', 'service', 'appointment_date', 'status']
    template_name = 'appointment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')  # Redirect to the dashboard after creating

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['vehicle', 'service', 'appointment_date', 'status']
    template_name = 'appointment_form.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')  # Redirect to the dashboard after updating

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('dashboard')  # Redirect to the dashboard after deletion
