import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_signup_email(user):
    """
    Send a signup confirmation email to a new user.

    This function sends an email to the user upon successful registration,
    using an HTML template for the email content.

    Args:
        user (User): The user instance for whom the signup email is to be sent.

    Returns:
        None
    """
    subject = 'Successful Registration on DT Autos'
    html_message = render_to_string('register_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = os.environ.get('DEFAULT_FROM_EMAIL')
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
