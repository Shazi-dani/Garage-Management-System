import os
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from django.utils.timezone import now
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from .models import Appointment, Vehicle, PurchaseInterest
from .forms import AppointmentForm, Inquiry
from .serializers import AppointmentSerializer, VehicleSerializer
from .email_utils import (
    send_appointment_creation_email,
    send_appointment_update_email,
    send_appointment_delete_email,
)
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_500(request):
    return render(request, '500.html', status=500)


# Create your views here.
User = get_user_model()


class HomeView(TemplateView):
    """
    View to render the home page of the website.
    """

    template_name = "home.html"
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    View to render the dashboard page, providing user-specific data if authenticated.
    """

    template_name = "dashboard.html"
    authentication_classes = [SessionAuthentication]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_type = getattr(user, "user_type", "Customer")
        if user_type == "Customer":
            appointments = Appointment.objects.filter(user=user)
        elif user_type == "Technician":
            appointments = Appointment.objects.all()
        else:
            appointments = []

            # Check for success message in query parameters
        success_message = self.request.GET.get("success", None)
        if success_message:
            context['success_message'] = success_message

        context.update(
            {
                "user_type": user_type,
                "username": user.username,
                "appointments": appointments,
                "messages": messages.get_messages(self.request),
            }
        )
        return context


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new appointment with an automated email notification upon creation.
    """

    model = Appointment
    fields = ["vehicle", "service", "appointment_date", "description"]
    template_name = "appointment_form.html"

    def form_valid(self, form):
        """
        Processes the form, sends an email on successful creation, and redirects to the dashboard.
        """
        form.instance.user = self.request.user  # Set the user from the request
        response = super().form_valid(form)

        # Prepare the email message
        context = {
            "user": self.object.user,
            "vehicle": self.object.vehicle.license_plate_no,
            "service": self.object.service.description,
            "appointment_date": self.object.appointment_date,
            "description": self.object.description,
        }
        html_content = render_to_string("emails/appointment_create_email.html", context)
        text_content = strip_tags(
            html_content
        )  # This is to create a plain-text version of the HTML email

        # Send an email notification
        email = EmailMessage(
            "DT Autos - Appointment Confirmation",
            html_content,
            os.getenv("DEFAULT_FROM_EMAIL"),
            [self.object.user.email],
        )
        email.content_subtype = "html"  # Main content is now text/html
        email.send(fail_silently=True)
        messages.success(self.request, "Your appointment has been successfully created")
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        """
        Returns the URL to redirect to after successfully creating an appointment.
        """
        return reverse_lazy(
            "dashboard:dashboard"
        )  # Redirect to the dashboard after creating


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update an existing appointment with an automated email notification upon update.
    """

    model = Appointment
    fields = ["vehicle", "service", "appointment_date", "description"]
    template_name = "appointment_form.html"

    def form_valid(self, form):
        """
        Processes the form, sends an email on successful update, and redirects to the dashboard.
        """
        response = super().form_valid(form)

        # Prepare the email message
        context = {
            "user": self.object.user,
            "vehicle": self.object.vehicle.license_plate_no,
            "service": self.object.service.description,
            "appointment_date": self.object.appointment_date,
            "description": self.object.description,
        }
        html_content = render_to_string("emails/appointment_update_email.html", context)
        text_content = strip_tags(html_content)  # Plain-text version

        # Send an email notification
        email = EmailMessage(
            "DT Autos - Appointment Update Confirmation",
            html_content,
            os.getenv("DEFAULT_FROM_EMAIL"),
            [self.object.user.email],
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)
        messages.success(self.request, "Your appointment has been successfully updated.")
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        """
        Returns the URL to redirect to after successfully updating an appointment.
        """
        return reverse_lazy(
            "dashboard:dashboard"
        )  # Redirect to the dashboard after updating


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete an existing appointment with an automated email notification upon deletion.
    """
    model = Appointment
    template_name = "appointment_confirm_delete.html"

    def form_valid(self, form):
        """
        Processes the deletion, sends an email on successful deletion, and redirects to the dashboard.
        """
        self.object = self.get_object()
        
        # Prepare the email message
        context = {
            "user": self.object.user,
            "vehicle": self.object.vehicle.license_plate_no,
            "appointment_date": self.object.appointment_date,
        }
        html_content = render_to_string("emails/appointment_delete_email.html", context)
        text_content = strip_tags(html_content)  # Plain-text version

        # Send an email notification
        email = EmailMessage(
            "DT Autos - Appointment Cancellation Confirmation",
            html_content,
            os.getenv("DEFAULT_FROM_EMAIL"),
            [self.object.user.email],
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)

        # Proceed with deleting the object
        response = super().form_valid(form)

        messages.success(self.request, "Your appointment has been successfully deleted.")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        Returns the URL to redirect to after successfully deleting an appointment.
        """
        return reverse_lazy("dashboard:dashboard")  # Redirec"


# Handle User Inquiry View submission
def submit_inquiry(request):
    """
    Handles submission of user inquiries via a form, returning JSON responses based on success or failure.
    """
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            # Email content
            email_subject = f"New Inquiry from {first_name} {last_name}"
            email_message = f"Subject: {subject}\nFrom: {first_name} {last_name} ({email})\n\nMessage:\n{message}"
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = settings.EMAIL_HOST_USER  # Send email to admin as a record

            # Send email
            send_mail(
                email_subject, email_message, email_from, recipient_list
            )  # Redirect or indicate success
            messages.success(
                request, "Your purchase interest has been successfully submitted."
            )
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


# List all Vehicles for Sale section
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    vehicle_data = VehicleSerializer(vehicles, many=True).data
    return render(request, "vehicle_list.html", {"vehicles": vehicle_data})


def submit_interest(request, vehicle_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to submit a purchase request.")
        return redirect(
            "users:register"
        )  # Redirect to login if user is not authenticated

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    # Check if the user has already submitted an interest for this vehicle
    existing_interest = PurchaseInterest.objects.filter(
        user=request.user, vehicle=vehicle
    ).exists()

    if not existing_interest:
        # Create a new interest since it does not exist
        PurchaseInterest.objects.create(user=request.user, vehicle=vehicle)
        # Send an email to the admin
        subject = "New Purchase Interest Submitted"
        message = f"User {request.user.username} has shown interest in purchasing {vehicle.model} {vehicle.make}."
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = settings.EMAIL_HOST_USER  # Send email to admin as a record
        send_mail(subject, message, email_from, recipient_list)
        # Redirect or indicate success
        messages.success(
            request, "Your purchase interest has been successfully submitted."
        )
        return redirect(
            "dashboard:home"
        )  # Redirect to a success page or the same page with a success message

    # Redirect or indicate failure (already requested)
    messages.info(request, "You have already submitted an interest for this vehicle.")
    return redirect(
        "dashboard:home"
    )  # Redirect to a failure page or the same page with an error message

def test_view(request):
    messages.success(request, "This is a test message.")
    return render(request, 'test_template.html')