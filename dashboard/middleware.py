import re
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from dashboard.models import Appointment  # Import your Appointment model

class CustomAccessControlMiddleware:
    """
    Middleware to restrict access based on user authentication and ownership for specific views.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # Define the URL patterns for different restrictions
        self.restricted_patterns = {
            r'^/dashboard/$': 'dashboard',
            r'^/appointments/new/$': 'create_appointment',
            r'^/appointments/\d+/edit/$': 'edit_appointment',
            r'^/appointments/\d+/delete/$': 'delete_appointment',
        }

    def __call__(self, request):
        # Loop through the restricted patterns to find a match
        for pattern, action in self.restricted_patterns.items():
            if re.match(pattern, request.path):
                if action == 'edit_appointment' or action == 'delete_appointment':
                    # For edit and delete, check user ownership
                    appointment_id = re.search(r'\d+', request.path).group()
                    appointment = get_object_or_404(Appointment, id=appointment_id)

                    # Ensure the appointment belongs to the logged-in user
                    if appointment.user != request.user:
                        raise PermissionDenied  # Return 403 if not the owner

                elif action == 'dashboard' or action == 'create_appointment':
                    # For dashboard or new appointment creation, just raise 403 if not authenticated
                    if not request.user.is_authenticated:
                        raise PermissionDenied  # Return 403 if not authenticated

        # Proceed with the request if no restrictions were violated
        response = self.get_response(request)
        return response
