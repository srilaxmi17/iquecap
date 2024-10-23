from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
import requests
from django.core.files.base import ContentFile


class RegisterSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15)

    def validate_mobile_number(self, value):
        if User.objects.filter(mobile_number=value).exists():
            raise serializers.ValidationError("Mobile number already registered.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(mobile_number=validated_data['mobile_number'])
        return user


class LoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15)

    def validate(self, data):
        mobile_number = data.get('mobile_number')
        try:
            user = User.objects.get(mobile_number=mobile_number)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid mobile number.")
        data['user'] = user
        return data


class ChangeMobileNumberSerializer(serializers.Serializer):
    new_mobile_number = serializers.CharField(max_length=15)

    def validate_new_mobile_number(self, value):
        if User.objects.filter(mobile_number=value).exists():
            raise serializers.ValidationError("This mobile number is already registered.")
        return value

    def save(self, user):
        new_mobile_number = self.validated_data['new_mobile_number']
        user.mobile_number = new_mobile_number
        user.save()
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception:
            self.fail('bad_token')

    default_error_messages = {
        'bad_token': 'Token is invalid or expired'
    }
    



import re  # For PAN card validation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'mobile_number', 'name', 'date_of_birth', 'email', 'gender', 'pan_card', 'address', 'profile_image', 'billing_address')

    def __init__(self, *args, **kwargs):
        # Call the parent class' initializer
        super().__init__(*args, **kwargs)

        # Check if this is an update operation
        if self.instance:
            # For updates, make the 'uid' read-only
            self.fields['uid'].read_only = True

    gender = serializers.ChoiceField(choices=[('0', 'Male'), ('1', 'Female'), ('2', 'Other')], required=False)


    # Custom validation for PAN card
    def validate_pan_card(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("PAN card must be exactly 10 characters.")
        if value and not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', value):
            raise serializers.ValidationError("Invalid PAN card format.")
        return value

    def to_internal_value(self, data):
        data = data.copy()

        # Allow profile_image to be any string (URL or text)
        profile_image = data.get('profile_image', None)
        if profile_image and isinstance(profile_image, str):
            data['profile_image'] = profile_image

        return super().to_internal_value(data)