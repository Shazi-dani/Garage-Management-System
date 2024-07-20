from rest_framework import serializers
from .models import Appointment, Service, Vehicle
from users.serializers import CustomUserSerializer

# Serializer for Vehicle model
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'make', 'color', 'license_plate_no', 'vehicle_number', 'vehicle_type', 'description', 'image']  # Customize these fields

# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['description', 'cost']  # Define service-related fields

class AppointmentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True) # Nested serializer for Custom User
    vehicle = VehicleSerializer(read_only=True) # Nested serializer for Vehicle
    service = ServiceSerializer(read_only=True) # Nested serializer for Service

    class Meta:
        model = Appointment
        fields = ['id', 'user', 'vehicle', 'service', 'appointment_date', 'status', 'description']
