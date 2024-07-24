from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model extending the default Django user model.

    This model adds additional fields for contact number and user type.
    
    Attributes:
        USER_TYPES (list): List of tuples containing user type choices.
        contact_no (CharField): Optional contact number for the user.
        user_type (CharField): Type of user, with choices 'Customer', 'Technician', and 'Admin'.
    """
    USER_TYPES = [
        ('Customer', 'Customer'),
        ('Technician', 'Technician'),
        ('Admin', 'Admin'),
    ]
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='Customer')
