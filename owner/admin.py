from django.contrib import admin
from housing.admin import HousingAdmin
from owner.models import Unit, Owner


@admin.register(Unit)
class UnitAdmin(HousingAdmin):
    list_display = ['name', 'type', 'square_feet', 'bedrooms', 'rent', 'status', 'renter']


@admin.register(Owner)
class OwnerAdmin(HousingAdmin):
    list_display = ['user']
