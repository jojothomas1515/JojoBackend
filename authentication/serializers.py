from typing import Dict, Any

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        from users.models import CustomUser
        email = attrs.get('email')
        password = attrs.get('password')

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            raise exceptions.NotFound(
                {'message': 'No user associated with this email', 'status': 'Unauthorized',
                 'code': 'no_user'}, code='no_user')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed({'message': 'Incorrect password',
                                                   'status': 'Unauthorized',
                                                   'code': 'incorrect_password'}, 'incorrect_password')

        return super().validate(attrs)


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, )

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'firstname', 'lastname')
        extra_kwargs = {
            'firstname': {'required': True},
            'lastname': {'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if CustomUser.objects.filter(email=email).first():
            raise exceptions.AuthenticationFailed({'message': 'email already exists', 'code': 'email_exists',
                                                   'status': 'Unauthorized'}, 'email_exists')

        if password != password2:
            raise serializers.ValidationError({"message": "Password fields does match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class SuccessfulSignUpMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200, default='<username> account created successfully')
    status = serializers.CharField(max_length=30, default='Success')
    code = serializers.CharField(max_length=30, default='registration_success')


class UserAlreadyExistsMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200, default='user already exist')
    status = serializers.CharField(max_length=30, default='email or username already exists')
    code = serializers.CharField(max_length=30, default='user_already_exists')
