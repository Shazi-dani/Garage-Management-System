from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    """
    Represents a vehicle in the system with various attributes including type, model, and owner.
    
    Attributes:
        model (CharField): The model name of the vehicle.
        make (CharField): The make or manufacturer of the vehicle.
        color (CharField): The color of the vehicle.
        license_plate_no (CharField): A unique identifier for the vehicle, usually the license plate number.
        vehicle_number (CharField): Another unique identifier, potentially an internal or system-specific number.
        vehicle_type (CharField): The type of vehicle (e.g., car, truck, bicycle).
        owner (ForeignKey): A reference to the User model, indicating the owner of the vehicle.
        description (TextField): Optional descriptive text about the vehicle.
        image (BinaryField): An optional binary field to store image data, not editable through admin interfaces.
    """
    VEHICLE_TYPES = [
        ('van', 'Van'),
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('bicycle', 'Bicycle'),
        ('motorcycle', 'Motorcycle'),
        ('other', 'Other'),
    ]

    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    license_plate_no = models.CharField(max_length=15, unique=True)
    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True, editable=False)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate_no})"

class Service(models.Model):
    """
    Describes a service that can be performed on a vehicle, including a cost estimate.
    
    Attributes:
        description (TextField): A textual description of the service provided.
        cost (DecimalField): The cost of the service.
    """
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

class Appointment(models.Model):
    """
    Schedules an appointment for a service on a vehicle, linked to a specific user.
    
    Attributes:
        user (ForeignKey): The user who made the appointment.
        vehicle (ForeignKey): The vehicle for which the service is scheduled.
        service (ForeignKey): The service to be provided during the appointment.
        appointment_date (DateTimeField): The scheduled date and time for the appointment.
        status (CharField): The current status of the appointment (e.g., pending, done).
        description (TextField): An optional description of the appointment details.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Appointment for {self.user.username} with {self.vehicle.license_plate_no} for {self.service.description}"

class Inquiry(models.Model):
    """
    Stores inquiries submitted via the contact form, recording sender details and message content.
    
    Attributes:
        first_name (CharField): The first name of the person making the inquiry.
        last_name (CharField): The last name of the person making the inquiry.
        email (EmailField): The email address of the person making the inquiry.
        subject (CharField): The subject line of the inquiry.
        message (TextField): The textual content of the inquiry message.
        created_at (DateTimeField): The timestamp when the inquiry was created, automatically set to the current time.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
