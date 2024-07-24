import os

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.utils.timezone import now
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from .models import Appointment
from .forms import AppointmentForm
from .serializers import AppointmentSerializer
from .email_utils import send_appointment_creation_email, send_appointment_update_email, send_appointment_delete_email

# Create your views here.
User = get_user_model()

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

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

class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
        # Fetch appointments for the logged-in user only
            return Appointment.objects.filter(user=self.request.user)
        else:
            return Appointment.objects.all()

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['user', 'vehicle', 'service', 'appointment_date', 'description']
    template_name = 'appointment_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Prepare the email message
        context = {
            'user': self.object.user,
            'vehicle': self.object.vehicle.license_plate_no,
            'service': self.object.service.description,
            'appointment_date': self.object.appointment_date,
            'description': self.object.description
        }
        html_content = render_to_string('emails/appointment_create_email.html', context)
        text_content = strip_tags(html_content)  # This is to create a plain-text version of the HTML email
        
        # Send an email notification
        email = EmailMessage(
            'DT Autos - Appointment Confirmation',
            html_content,
            os.environ.get('DEFAULT_FROM_EMAIL'),
            [self.object.user.email]
        )
        email.content_subtype = "html"  # Main content is now text/html
        email.send(fail_silently=False)

        return response

    def get_success_url(self):
        return reverse_lazy('dashboard:dashboard')  # Redirect to the dashboard after creating

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['vehicle', 'service', 'appointment_date', 'description']
    template_name = 'appointment_form.html'

    def form_valid(self, form):
        # Save the form instance
        response = super().form_valid(form)

        # Prepare the email message
        context = {
            'user': self.object.user,
            'vehicle': self.object.vehicle.license_plate_no,
            'service': self.object.service.description,
            'appointment_date': self.object.appointment_date,
            'description': self.object.description
        }
        html_content = render_to_string('emails/appointment_update_email.html', context)
        text_content = strip_tags(html_content)  # Plain-text version
        
        # Send an email notification
        email = EmailMessage(
            'DT Autos - Appointment Update Confirmation',
            html_content,
            os.environ.get('DEFAULT_FROM_EMAIL'),
            [self.object.user.email]
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)
        
        return response
    
    def get_success_url(self):
        return reverse_lazy('dashboard:dashboard')  # Redirect to the dashboard after updating

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('dashboard:dashboard')  # Redirect to the dashboard after deletion

    def delete(self, request, *args, **kwargs):
        # Fetch the object to be deleted
        self.object = self.get_object()
        context = {
            'user': self.object.user,
            'vehicle': self.object.vehicle.license_plate_no,
            'appointment_date': self.object.appointment_date,
        }
        html_content = render_to_string('emails/appointment_delete_email.html', context)
        text_content = strip_tags(html_content)  # Plain-text version
        
        # Send an email notification
        email = EmailMessage(
            'DT Autos - Appointment Cancellation Confirmation',
            html_content,
            os.environ.get('DEFAULT_FROM_EMAIL'),
            [self.object.user.email]
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)

        # Proceed with deleting the object
        response = super().delete(request, *args, **kwargs)
        return response
