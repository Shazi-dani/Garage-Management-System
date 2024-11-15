import base64
from rest_framework import serializers
from .models import Appointment, Service, Vehicle
from users.serializers import CustomUserSerializer


# Serializer for Vehicle model
class VehicleSerializer(serializers.ModelSerializer):
    """
    A serializer for the Vehicle model that handles serialization and deserialization
    of vehicle data, including encoding images to Base64 for JSON representation.
    """

    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "model",
            "make",
            "color",
            "license_plate_no",
            "vehicle_number",
            "vehicle_type",
            "description",
            "image",
        ]

    def to_representation(self, instance):
        """
        Convert the model instance into JSON format, with image data encoded in Base64 if present.

        Args:
            instance (Vehicle): The Vehicle model instance to serialize.

        Returns:
            dict: A dictionary containing all fields of Vehicle, with image data as a Base64-encoded string.
        """
        representation = super().to_representation(instance)
        if instance.image:
            representation["image"] = base64.b64encode(instance.image).decode(
                "utf-8"
            )  # Encode binary data to Base64
        return representation

    def create(self, validated_data):
        """
        Create and return a new Vehicle instance, given the validated data.

        Args:
            validated_data (dict): Data validated by the serializer.

        Returns:
            Vehicle: The newly created Vehicle object.
        """
        image = validated_data.pop("image", None)
        if image:
            validated_data["image"] = image.read()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Vehicle instance, given the validated data.

        Args:
            instance (Vehicle): The existing Vehicle instance to update.
            validated_data (dict): Data validated by the serializer.

        Returns:
            Vehicle: The updated Vehicle object.
        """
        image = validated_data.pop("image", None)
        if image:
            validated_data["image"] = image.read()
        return super().update(instance, validated_data)


# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Service model, primarily handling the serialization of service-related data.
    """

    class Meta:
        model = Service
        fields = ["description", "cost"]  # Define service-related fields


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Appointment model that incorporates nested serializers for associated
    User, Vehicle, and Service models. It provides detailed view of an appointment including
    all related entities.
    """

    user = CustomUserSerializer(read_only=True)  # Nested serializer for Custom User
    vehicle = VehicleSerializer(read_only=True)  # Nested serializer for Vehicle
    service = ServiceSerializer(read_only=True)  # Nested serializer for Service

    class Meta:
        model = Appointment
        fields = [
            "id",
            "user",
            "vehicle",
            "service",
            "appointment_date",
            "status",
            "description",
        ]
