from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer handles the conversion of User model instances to 
    and from representations such as JSON. It includes fields for 
    username, email, first name, last name, and contact number.

    Attributes:
        Meta (class): Metadata options for the serializer.
    """
    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name', 'contact_no')

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    This serializer handles the conversion of user registration data 
    to and from representations such as JSON. It includes fields for 
    username, password, email, first name, last name, and contact number.

    Attributes:
        password (CharField): Password field for write-only operations.
        Meta (class): Metadata options for the serializer.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'contact_no')

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.

        Args:
            validated_data (dict): The validated data for the new user.

        Returns:
            User: The newly created user instance.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            contact_no=validated_data['contact_no'],
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    This serializer handles the conversion of user login data 
    to and from representations such as JSON. It includes fields for 
    username and password.

    Attributes:
        username (CharField): Username field for the user.
        password (CharField): Password field for write-only operations.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
