from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import Group
from account.models import User, MarriedStatus, Religion, FamilyMembers, OtherMembers, EmergencyContactPerson
from owner.models import Owner
from renter.models import Renter
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


class UserEmailSerializer(ModelSerializer):
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

        if get_group == 'Owner':
            Owner.objects.create(user=user)
            user.owner_status = True
        else:
            Renter.objects.create(user=user)
            user.renter_status = True

        user.save()

        return user

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class MarriedStatusSerializer(ModelSerializer):
    class Meta:
        model = MarriedStatus
        fields = ('id', 'name')


class ReligionSerializer(ModelSerializer):
    class Meta:
        model = Religion
        fields = ('id', 'name')


class UserProfileSerializer(ModelSerializer):
    married_status_name = serializers.CharField(source='married_status.name')
    religion_name = serializers.CharField(source='religion.name')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'get_full_name', 'email', 'phone', 'nid', 'passport', 'birthday',
                  'present_address', 'permanent_address', 'married_status', 'married_status_name', 'occupation',
                  'occupation_institution', 'religion', 'religion_name', 'education_qualification',
                  'account_complete_status')


class FamilyMembersSerializer(ModelSerializer):
    class Meta:
        model = FamilyMembers
        fields = ('id', 'name', 'age', 'phone', 'relation', 'occupation')


class EmergencyContactPersonSerializer(ModelSerializer):
    class Meta:
        model = EmergencyContactPerson
        fields = ('id', 'name', 'phone', 'relation', 'address')


class OtherMembersSerializer(ModelSerializer):
    class Meta:
        model = OtherMembers
        fields = ('id', 'name', 'age', 'phone', 'nid', 'present_address', 'permanent_address')