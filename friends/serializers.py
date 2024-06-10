# from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.validators import validate_email as django_validate_email
from django.core.exceptions import ValidationError
from .models import Friends, CustomUser, FriendRequest


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email",  "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }  # Ensures password is write-only

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'fullname']
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        try:
            django_validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            django_validate_email(email)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")

        print(email, password)

        user = authenticate(
            request=self.context.get("request"), email=email, password=password
        )
        if not user:
            raise serializers.ValidationError("Invalid login credentials.")
        data["user"] = user
        return data


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ["id", "user", "friend", "created"]


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["id", "sender", "receiver", "timestamp", "status"]
        read_only_fields = ['sender']

    def create(self, validated_data):
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)

class UserSearchSearializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "fullname"]

        
