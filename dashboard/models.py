from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('van', 'Van'),
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('bicycle', 'Bicycle'),
        ('motorcycle', 'Motorcycle'),
        ('rickshaw', 'rickshaw'),
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
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

class Appointment(models.Model):
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
