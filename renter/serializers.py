from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from renter.models import Renter
from account.serializers import UserProfileSerializer


class RenterSerializer(ModelSerializer):
    user = UserProfileSerializer(many=False)
    previous_house_owner = serializers.CharField(source='previous_house_owner.get_full_name')
    present_house_owner = serializers.CharField(source='present_house_owner.get_full_name')

    class Meta:
        model = Renter
        fields = ('id', 'user', 'previous_house_owner', 'present_house_owner', 'reason_of_house_change', 'rent_of_date')


