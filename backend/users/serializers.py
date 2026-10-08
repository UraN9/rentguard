from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Validate registration data and create a new user."""

    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'password', 'password2')
        read_only_fields = ('id',)

    def validate(self, attrs):
        """Ensure both password fields match."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return attrs

    def create(self, validated_data):
        """Create the user through the manager so the password is hashed."""
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    """Profile of the current user."""

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'created_at')
        read_only_fields = ('id', 'email', 'created_at')