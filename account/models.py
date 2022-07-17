from django.db import models
from housing.models import HousingModel
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete


class Religion(HousingModel):
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Religion'
        verbose_name_plural = 'Religions'
        db_table = 'religion'

    def __str__(self):
        return self.name


class MarriedStatus(HousingModel):
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Married Status'
        verbose_name_plural = 'Married Statuses'
        db_table = 'married_status'

    def __str__(self):
        return self.name


class EmergencyContact(HousingModel):
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


class FamilyMember(HousingModel):
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


class OtherMember(HousingModel):
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


class User(AbstractUser, HousingModel):
    phone = models.CharField(max_length=11, blank=False, null=True)
    nid = models.IntegerField(blank=False, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    present_address = models.CharField(max_length=100, blank=True, null=True)
    permanent_address = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    married_status = models.ForeignKey(MarriedStatus, on_delete=models.PROTECT, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    occupation_institution = models.CharField(max_length=255, blank=True, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.PROTECT, blank=True, null=True)
    education_qualification = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact = models.ManyToManyField(EmergencyContact, blank=True, related_name='emergency_contacts')
    family_member = models.ManyToManyField(FamilyMember, blank=True, related_name='family_members')
    cleaner = models.ManyToManyField(OtherMember, blank=True, related_name='cleaners')
    driver = models.ManyToManyField(OtherMember, blank=True, related_name='drivers')
    owner_status = models.BooleanField(default=False)
    renter_status = models.BooleanField(default=False)
    admin_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'

    def __str__(self):
        return self.username

    @property
    def married_status_name(self):
        return self.married_status.name

    @property
    def religion_name(self):
        return self.religion.name

    @property
    def birthday_date(self):
        return str(self.birthday).split(' ')[0]


def emergency_contact_pre_delete(sender, instance, *args, **kwargs):
    all_emergency_contacts = instance.emergency_contact.all()
    all_emergency_contacts.delete()


def family_member_pre_delete(sender, instance, *args, **kwargs):
    all_family_members = instance.family_member.all()
    all_family_members.delete()


def cleaner_pre_delete(sender, instance, *args, **kwargs):
    all_cleaners = instance.cleaner.all()
    all_cleaners.delete()


def driver_pre_delete(sender, instance, *args, **kwargs):
    all_drivers = instance.driver.all()
    all_drivers.delete()


pre_delete.connect(emergency_contact_pre_delete, sender=User)
pre_delete.connect(family_member_pre_delete, sender=User)
pre_delete.connect(cleaner_pre_delete, sender=User)
pre_delete.connect(driver_pre_delete, sender=User)

