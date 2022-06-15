from django.contrib import admin
from housing.admin import HousingAdmin
from account.models import MarriedStatus, EmergencyContactPerson, FamilyMembers, OtherMembers, CommonUserModel


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


@admin.register(CommonUserModel)
class CommonUserModelAdmin(HousingAdmin):
    list_display = ['user', 'phone', 'email', 'nid', 'passport', 'present_address', 'permanent_address',
                    'birthday', 'married_status', 'occupation', 'occupation_institution', 'religion',
                    'education_qualification', 'emergency_contact', 'family_members', 'house_cleaner', 'driver']

