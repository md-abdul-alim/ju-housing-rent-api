from django.db import models
from housing.models import HousingModel
from account.models import CommonUserModel
from renter.models import Renter


class Unit(HousingModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    tenant = models.ForeignKey(Renter, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        unique_together = ('name', 'tenant',)
        db_table = 'unit'

    def __str__(self):
        return self.name


class Address(HousingModel):
    house_no = models.CharField(max_length=50, blank=False, null=False)
    block = models.CharField(max_length=50, blank=True, null=True)
    residence = models.CharField(max_length=100, blank=True, null=True)
    street_no = models.CharField(max_length=50, blank=True, null=True)
    city_or_town = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        db_table = 'address'

    def __str__(self):
        return self.house_no


class HouseOwner(HousingModel):
    common_user = models.ForeignKey(CommonUserModel, on_delete=models.PROTECT, blank=False, null=False)
    unit = models.ManyToManyField(Unit, blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'House Owner'
        verbose_name_plural = 'House Owners'
        db_table = 'house_owner'

    def __str__(self):
        return self.user.name


