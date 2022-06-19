from django.contrib import admin
from housing.admin import HousingAdmin
from renter.models import Renter


@admin.register(Renter)
class RenterAdmin(HousingAdmin):
    list_display = ['common_user', 'previous_house_owner', 'present_house_owner', 'reason_of_house_change', 'rent_of_date']


