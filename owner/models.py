from django.db import models
from housing.models import HousingModel
from account.models import User
from renter.models import Renter


class Unit(HousingModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        unique_together = ('name', 'renter',)
        db_table = 'unit'

    def __str__(self):
        return self.name


class Owner(HousingModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
    unit = models.ManyToManyField(Unit, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
        db_table = 'owner'

    def __str__(self):
        return self.user.username


