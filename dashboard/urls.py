from django.urls import path

from .views import HomeView, DashboardView
from .views import AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView, test_view
from .views import submit_inquiry, vehicle_list, submit_interest
from django.conf.urls import handler404, handler403, handler500
from dashboard import views

handler404 = 'dashboard.views.custom_404'
handler403 = 'dashboard.views.custom_403'
handler500 = 'dashboard.views.custom_500'

app_name = "dashboard"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("vehicles/", vehicle_list, name="vehicle_list"),
    path("submit-inquiry/", submit_inquiry, name="submit_inquiry"),
    path("submit-interest/<int:vehicle_id>/", submit_interest, name="submit_interest"),
    path(
        "appointments/new/", AppointmentCreateView.as_view(), name="create_appointment"
    ),
    path(
        "appointments/<int:pk>/edit/",
        AppointmentUpdateView.as_view(),
        name="edit_appointment",
    ),
    path(
        "appointments/<int:pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="delete_appointment",
    ),
     path('test/', test_view, name='test_view'),
]


import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging  # Using logger to log email task result

logger = logging.getLogger()  #  get default logger to log values


def send_appointment_creation_email(user):
    """
    Sends an email notification to a user regarding the creation of an appointment.

    This function constructs an HTML email from a template, converts it to plain text, and sends it.

    Args:
        user (User): The user object to whom the email will be sent. Assumes the user object has an 'email' attribute.

    Uses:
        - 'emails/appointment_create_email.html': Template used for generating the HTML content of the email.
    """/home/dev/Downloads/django-up/Garage-Management-System/dashboard/templates/403.html /home/dev/Downloads/django-up/Garage-Management-System/dashboard/templates/404.html /home/dev/Downloads/django-up/Garage-Management-System/dashboard/templates/500.html
    subject = "Appointment Booked !!!!"
    html_message = render_to_string(
        "emails/appointment_create_email.html", {"user": user}
    )
    plain_message = strip_tags(html_message)
    from_email = os.environ.get("DEFAULT_FROM_EMAIL")
    to = user.email

    # Validating email credentials before sending the mail
    if os.environ.get("EMAIL_HOST_USER") and os.environ.get("EMAIL_HOST_PASSWORD"):
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    else:
        logger.debug("No Email credentials Found. Skipped email generation task.")


def send_appointment_update_email(user):
    """
    Sends an email notification to a user regarding the update of an existing appointment.

    Args:
        user (User): The user object to whom the email will be sent. The user must have an 'email' attribute.

    Uses:
        - 'emails/appointment_update_email.html': Template used for the HTML content of the email.
    """
    subject = "Appointment Details Updated !!!!"
    html_message = render_to_string(
        "emails/appointment_update_email.html", {"user": user}
    )
    plain_message = strip_tags(html_message)
    from_email = os.environ.get("DEFAULT_FROM_EMAIL")
    to = user.email

    # Validating email credentials before sending the mail
    if os.environ.get("EMAIL_HOST_USER") and os.environ.get("EMAIL_HOST_PASSWORD"):
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    else:
        logger.debug("No Email credentials Found. Skipped email generation task.")


def send_appointment_delete_email(user):
    """
    Sends an email notification to a user regarding the deletion of an appointment.

    Args:
        user (User): The user object to whom the email will be sent. This object should have an 'email' attribute.

    Uses:
        - 'email/appointment_delete_email.html': Template used for generating the HTML content of the email. 
        Note the correct path might be 'emails/appointment_delete_email.html'.
    """
    subject = "Appointment Deleted !!!!"
    html_message = render_to_string(
        "email/appointment_delete_email.html", {"user": user}
    )
    plain_message = strip_tags(html_message)
    from_email = os.environ.get("DEFAULT_FROM_EMAIL")
    to = user.email

    # Validating email credentials before sending the mail
    if os.environ.get("EMAIL_HOST_USER") and os.environ.get("EMAIL_HOST_PASSWORD"):
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    else:
        logger.debug("No Email credentials Found. Skipped email generation task.")
