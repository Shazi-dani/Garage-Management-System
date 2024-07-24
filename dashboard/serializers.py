import base64
from rest_framework import serializers
from .models import Appointment, Service, Vehicle
from users.serializers import CustomUserSerializer

# Serializer for Vehicle model
class VehicleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'make', 'color', 'license_plate_no', 'vehicle_number', 'vehicle_type', 'description', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = base64.b64encode(instance.image).decode('utf-8')  # Encode binary data to Base64
        return representation

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        if image:
            validated_data['image'] = image.read()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            validated_data['image'] = image.read()
        return super().update(instance, validated_data)

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
