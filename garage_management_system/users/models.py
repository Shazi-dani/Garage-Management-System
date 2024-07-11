from django.db import models


class BlacklistedToken(models.Model):
    token = models.TextField(unique=True)  # Ensuring that each token can only be blacklisted once
    blacklisted_at = models.DateTimeField(auto_now_add=True)  # Automatically set the time when the token is created

    def __str__(self):
        return f"Blacklisted on {self.blacklisted_at}"
