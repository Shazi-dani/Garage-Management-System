import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_signup_email(user):
    subject = 'Successful Registration on Shazina Garage Management System'
    html_message = render_to_string('emails/register_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
