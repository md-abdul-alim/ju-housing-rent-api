from django.contrib import admin
from housing.admin import HousingAdmin
from owner.models import Unit, Address, HouseOwner


@admin.register(Unit)
class UnitAdmin(HousingAdmin):
    list_display = ['name', 'tenant']


@admin.register(Address)
class AddressAdmin(HousingAdmin):
    list_display = ['house_no', 'block', 'residence', 'street_no', 'city_or_town', 'postcode']


@admin.register(HouseOwner)
class HouseOwnerAdmin(HousingAdmin):
    list_display = ['common_user', 'address']
