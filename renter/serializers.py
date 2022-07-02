from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from renter.models import Renter, CheckIn
from account.serializers import UserProfileSerializer


class RenterSerializer(ModelSerializer):
    user = UserProfileSerializer(many=False)

    class Meta:
        model = Renter
        fields = ('id', 'user', 'previous_house_owner', 'present_house_owner', 'reason_of_house_change', 'rent_of_date')


class CheckInSerializer(ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('id', 'renter', 'unit_code', 'check_in_date', 'remark')

