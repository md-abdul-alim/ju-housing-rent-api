from django.contrib import admin
from housing.admin import HousingAdmin
from account.models import MarriedStatus, EmergencyContact, FamilyMember, OtherMember, User, Religion

from account.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
import time


@admin.register(User)
class UserAdmin(HousingAdmin):
    list_display = ['username', 'email', 'phone', 'nid', 'passport', 'present_address', 'permanent_address',
                    'birthday', 'married_status', 'occupation', 'occupation_institution', 'religion',
                    'education_qualification']
    search_fields = ['username__icontains', 'email__icontains']

    def reset_password(self, request, queryset):
        if 'submit' in request.POST:
            new_pass = request.POST['password']
            pk = request.POST['_selected_action']
            if new_pass != "None":
                time.sleep(1)
                user = User.objects.get(pk=pk)
                user.password = make_password(new_pass, salt=None, hasher='default')
                user.save()

            self.message_user(request, f"Password reset successfully.")
            return HttpResponseRedirect(request.get_full_path())
        return render(request, 'admin/password_reset.html', context={"models": queryset})

    reset_password.short_description = "Reset Password"
    actions = ['reset_password']


@admin.register(Religion)
class ReligionAdmin(HousingAdmin):
    list_display = ['name']


@admin.register(MarriedStatus)
class MarriedStatusAdmin(HousingAdmin):
    list_display = ['name']


@admin.register(EmergencyContact)
class EmergencyContactPersonAdmin(HousingAdmin):
    list_display = ['name', 'phone', 'relation', 'address']


@admin.register(FamilyMember)
class FamilyMemberAdmin(HousingAdmin):
    list_display = ['name', 'age', 'phone', 'relation', 'occupation']


@admin.register(OtherMember)
class OtherMemberAdmin(HousingAdmin):
    list_display = ['name', 'age', 'phone', 'nid', 'present_address', 'permanent_address']


