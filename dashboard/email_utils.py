import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_appointment_creation_email(user):
    subject = 'Appointment Booked !!!!'
    html_message = render_to_string('emails/appointment_create_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def send_appointment_update_email(user):
    subject = 'Appointment Details Updated !!!!'
    html_message = render_to_string('emails/appointment_update_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def send_appointment_delete_email(user):
    subject = 'Appointment Deleted !!!!'
    html_message = render_to_string('email/appointment_delete_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
