from django.contrib import admin
from housing.admin import HousingAdmin
from owner.models import Unit, Owner


@admin.register(Unit)
class UnitAdmin(HousingAdmin):
    list_display = ['name', 'type', 'square_feet', 'bedrooms', 'rent', 'check_in_permission_nid',
                    'code', 'to_let_from', 'status', 'check_in_renter', 'check_out_renter']


@admin.register(Owner)
class OwnerAdmin(HousingAdmin):
    list_display = ['user']
