from rest_framework import serializers
from account.serializers import UserProfileSerializer
from owner.models import Owner, Unit
from rest_framework.serializers import ModelSerializer


class OwnerSerializer(ModelSerializer):
    user = UserProfileSerializer(many=False)

    class Meta:
        model = Owner
        fields = ('id', 'user', 'unit')


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'type', 'square_feet', 'bedrooms', 'rent',
                  'address', 'description', 'status', 'renter')

