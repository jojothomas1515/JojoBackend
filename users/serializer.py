from rest_framework import serializers

from users.models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "profile_image",
            "email",
            "username",
            "firstname",
            "lastname", ]


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_image']
