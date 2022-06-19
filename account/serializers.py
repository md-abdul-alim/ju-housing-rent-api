from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import Group
from account.models import User
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    permission_classes = []
    authentication_classes = []

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        data.update({'is_superuser': self.user.is_superuser})
        data.update({'user_type': [group.name for group in Group.objects.filter(user=self.user)]})
        data.update({'account_complete_status': self.user.account_complete_status})
        return data


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def update(self, instance, validated_data):
        new_pass = validated_data.pop('password')
        instance.password = make_password(new_pass, salt=None, hasher='default')
        instance.save()
        return instance


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'role', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        get_group = Group.objects.get(id=validated_data['role'])
        user = User.objects.create(
            username=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            is_active=True
        )

        user.set_password(validated_data['password'])
        user.groups.add(get_group)
        user.save()

        return user

