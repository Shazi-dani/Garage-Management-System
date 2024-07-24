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
from .forms import AppointmentForm, Inquiry
from .serializers import AppointmentSerializer
from .email_utils import send_appointment_creation_email, send_appointment_update_email, send_appointment_delete_email

# Create your views here.
User = get_user_model()

class HomeView(TemplateView):
    """
    View to render the home page of the website.
    """
    template_name = 'home.html'
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

class DashboardView(TemplateView):
    """
    View to render the dashboard page, providing user-specific data if authenticated.
    """
    template_name = 'dashboard.html'
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

    def get_context_data(self, **kwargs):
        """
        Adds user type and username to the context for rendering in the template.
        """
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
    """
    API view to list appointments based on the user type, filtering for specific users if necessary.
    """
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Returns a queryset of appointments based on the user's type and authentication status.
        """
        user = self.request.user
        if user.is_authenticated:
            if user.user_type == 'Customer':
                # Fetch appointments for the logged-in user only
                return Appointment.objects.filter(user=self.request.user)
            elif user.user_type == 'Technician':
               return Appointment.objects.all()
        else:
            return Appointment.objects.none()

class AppointmentCreateView(CreateView):
    """
    View to create a new appointment with an automated email notification upon creation.
    """
    model = Appointment
    fields = ['vehicle', 'service', 'appointment_date', 'description']
    template_name = 'appointment_form.html'

    def form_valid(self, form):
        """
        Processes the form, sends an email on successful creation, and redirects to the dashboard.
        """
        form.instance.user = self.request.user  # Set the user from the request
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
        email.send(fail_silently=True)

        return response

    def get_success_url(self):
        """
        Returns the URL to redirect to after successfully creating an appointment.
        """
        return reverse_lazy('dashboard:dashboard')  # Redirect to the dashboard after creating

class AppointmentUpdateView(UpdateView):
    """
    View to update an existing appointment with an automated email notification upon update.
    """
    model = Appointment
    fields = ['vehicle', 'service', 'appointment_date', 'description']
    template_name = 'appointment_form.html'

    def form_valid(self, form):
        """
        Processes the form, sends an email on successful update, and redirects to the dashboard.
        """
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
        email.send(fail_silently=True)
        
        return response
    
    def get_success_url(self):
        """
        Returns the URL to redirect to after successfully updating an appointment.
        """
        return reverse_lazy('dashboard:dashboard')  # Redirect to the dashboard after updating

class AppointmentDeleteView(DeleteView):
    """
    View to delete an existing appointment with an automated email notification upon deletion.
    """
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('dashboard:dashboard')  # Redirect to the dashboard after deletion

    def delete(self, request, *args, **kwargs):
        """
        Deletes the appointment and sends an email notification to the user.
        """
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
        email.send(fail_silently=True)

        # Proceed with deleting the object
        response = super().delete(request, *args, **kwargs)
        return response

# Handle User Inquiry View submission
def submit_inquiry(request):
    """
    Handles submission of user inquiries via a form, returning JSON responses based on success or failure.
    """
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
