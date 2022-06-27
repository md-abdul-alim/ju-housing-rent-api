from django.db import models
from housing.models import HousingModel
from account.models import User
from renter.models import Renter
from housing.utils import unique_code_generator
from django.db.models.signals import pre_save


class Unit(HousingModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=100, blank=True, null=True)
    square_feet = models.CharField(max_length=50, blank=True, null=True)
    bedrooms = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=9, blank=True)
    status = models.BooleanField(default=False)
    renter = models.ForeignKey(Renter, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        unique_together = ('name', 'renter',)
        db_table = 'unit'

    def __str__(self):
        return self.name


class Owner(HousingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    unit = models.ManyToManyField(Unit, blank=True, related_name='units')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
        db_table = 'owner'

    def __str__(self):
        return self.user.username


def unit_pre_save(sender, instance, *args, **kwargs):
    if not instance.code:
        instance.code = unique_code_generator(instance)


pre_save.connect(unit_pre_save, sender=Unit)

