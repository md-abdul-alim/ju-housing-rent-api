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
        fields = ('id', 'name', 'code', 'type', 'square_feet', 'bedrooms', 'rent', 'address', 'description', 'status',
                  'to_let_from', 'to_let_date', 'check_in', 'check_in_date', 'check_in_renter', 'check_out',
                  'check_out_date', 'check_out_renter', 'check_in_permission_nid')



