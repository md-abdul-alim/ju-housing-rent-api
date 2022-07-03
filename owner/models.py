from django.db import models
from housing.models import HousingModel
from account.models import User
from renter.models import Renter
from housing.utils import unique_code_generator
from django.db.models.signals import pre_save
from django.utils import timezone


class Unit(HousingModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=100, blank=True, null=True)
    square_feet = models.CharField(max_length=50, blank=True, null=True)
    bedrooms = models.IntegerField(default=0)
    phone = models.CharField(max_length=14, blank=True, null=True)
    rent = models.IntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=9, blank=True)
    status = models.BooleanField(default=False)
    to_let_from = models.DateTimeField(blank=True, null=True)
    check_in_date = models.DateTimeField(blank=True, null=True)
    check_in_renter = models.ForeignKey(Renter, on_delete=models.PROTECT, blank=True, null=True, related_name='check_in_renter')
    check_in_status = models.BooleanField(default=False)
    check_out_date = models.DateTimeField(blank=True, null=True)
    check_out_renter = models.ForeignKey(Renter, on_delete=models.PROTECT, blank=True, null=True, related_name='check_out_renter')
    check_out_status = models.BooleanField(default=False)
    check_in_permission_nid = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        unique_together = ('check_in_renter', 'check_out_renter',)
        db_table = 'unit'

    def __str__(self):
        return self.name

    @property
    def check_in(self):
        return str(self.check_in_date).split(' ')[0]

    @property
    def check_out(self):
        return str(self.check_out_date).split(' ')[0]

    @property
    def to_let_date(self):
        return str(self.to_let_from).split(' ')[0]


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

