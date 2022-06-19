from django.contrib import admin
from housing.admin import HousingAdmin
from account.models import MarriedStatus, EmergencyContactPerson, FamilyMembers, OtherMembers, User, Religion


@admin.register(Religion)
class ReligionAdmin(HousingAdmin):
    list_display = ['name']


@admin.register(MarriedStatus)
class MarriedStatusAdmin(HousingAdmin):
    list_display = ['name']


@admin.register(EmergencyContactPerson)
class EmergencyContactPersonAdmin(HousingAdmin):
    list_display = ['name', 'phone', 'relation', 'address']


@admin.register(FamilyMembers)
class FamilyMembersAdmin(HousingAdmin):
    list_display = ['name', 'age', 'phone', 'relation', 'occupation']


@admin.register(OtherMembers)
class OtherMembersAdmin(HousingAdmin):
    list_display = ['name', 'age', 'phone', 'nid', 'present_address', 'permanent_address']


@admin.register(User)
class UserAdmin(HousingAdmin):
    list_display = ['username', 'email', 'phone', 'nid', 'passport', 'present_address', 'permanent_address',
                    'birthday', 'married_status', 'occupation', 'occupation_institution', 'religion',
                    'education_qualification', 'account_complete_status']

