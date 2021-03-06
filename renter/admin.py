from django.contrib import admin
from housing.admin import HousingAdmin
from renter.models import Renter, CheckIn


@admin.register(Renter)
class RenterAdmin(HousingAdmin):
    list_display = ['user', 'previous_house_owner', 'present_house_owner', 'reason_of_house_change', 'rent_of_date']


@admin.register(CheckIn)
class CheckInAdmin(HousingAdmin):
    list_display = ['renter', 'check_in_date', 'unit_code', 'remark', 'status']

