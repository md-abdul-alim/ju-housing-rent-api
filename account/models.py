from django.db import models
from django.contrib.auth.models import User
from housing.models import HousingModel


class MarriedStatus(HousingModel):
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Married Status'
        verbose_name_plural = 'Married Statuses'
        db_table = 'married_status'

    def __str__(self):
        return self.name


class EmergencyContactPerson(HousingModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    relation = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Emergency Contact Person'
        verbose_name_plural = 'Emergency Contact Persons'
        db_table = 'emergency_contact_person'

    def __str__(self):
        return self.name


class FamilyMembers(HousingModel):
    name = models.CharField(max_length=255, blank=False, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    relation = models.CharField(max_length=255, blank=False, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Family Member'
        verbose_name_plural = 'Family Members'
        db_table = 'family_member'

    def __str__(self):
        return self.name


class OtherMembers(HousingModel):
    name = models.CharField(max_length=255, blank=False, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    nid = models.IntegerField(blank=False, null=False)
    present_address = models.CharField(max_length=100, blank=True, null=True)
    permanent_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Other Member'
        verbose_name_plural = 'Other Members'
        db_table = 'other_member'

    def __str__(self):
        return self.name


class CommonUserModel(HousingModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=False)
    nid = models.IntegerField(blank=False, null=False)
    passport = models.CharField(max_length=100, blank=True, null=True)
    present_address = models.CharField(max_length=100, blank=True, null=True)
    permanent_address = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField()
    married_status = models.ForeignKey(MarriedStatus, on_delete=models.CASCADE, blank=False, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    occupation_institution = models.CharField(max_length=255, blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    education_qualification = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact = models.ForeignKey(EmergencyContactPerson, on_delete=models.CASCADE, blank=True, null=True)
    family_members = models.ForeignKey(FamilyMembers, on_delete=models.PROTECT, blank=True, null=True)
    house_cleaner = models.ForeignKey(OtherMembers, on_delete=models.CASCADE, blank=True, null=True, related_name='house_cleaner')
    driver = models.ForeignKey(OtherMembers, on_delete=models.CASCADE, blank=True, null=True, related_name='driver')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Common User'
        verbose_name_plural = 'Common Users'
        db_table = 'common_user'

    def __str__(self):
        return self.user

