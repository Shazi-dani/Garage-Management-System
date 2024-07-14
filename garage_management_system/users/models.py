from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('Customer', 'Customer'),
        ('Technician', 'Technician'),
        ('Admin', 'Admin'),
    ]
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='Customer')


class BlacklistedToken(models.Model):
    token = models.TextField(unique=True)  # Ensuring that each token can only be blacklisted once
    blacklisted_at = models.DateTimeField(auto_now_add=True)  # Automatically set the time when the token is created

    def __str__(self):
        return f"Blacklisted on {self.blacklisted_at}"
 