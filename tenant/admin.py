from django.contrib import admin
from housing.admin import HousingAdmin
from tenant.models import Tenant


@admin.register(Tenant)
class TenantAdmin(HousingAdmin):
    list_display = ['user', 'previous_house_owner', 'present_house_owner', 'reason_of_house_change', 'rent_of_date']

