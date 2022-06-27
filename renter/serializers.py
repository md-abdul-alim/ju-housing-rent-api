from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from renter.models import Renter
from account.serializers import UserProfileSerializer


class RenterSerializer(ModelSerializer):
    user = UserProfileSerializer(many=False)

    class Meta:
        model = Renter
        fields = ('id', 'user', 'previous_house_owner', 'present_house_owner', 'reason_of_house_change', 'rent_of_date')


