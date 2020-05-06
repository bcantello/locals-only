from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'token',
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  # ** means that the method takes a key-word argument


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'token',
        )

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('A username is required to login')
        if password is None:
            raise serializers.ValidationError('A password is required to login')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Incorrect username or password')
        if not user.is_active:
            raise serializers.ValidationError('User account has been deactivated. Contact support to reactivate')

        return {
            "username": user.username,
            "email": user.email,
            "token": user.token
        }
