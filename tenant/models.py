from django.db import models
from housing.models import HousingModel
from account.models import CommonUserModel


class Tenant(HousingModel):
    user = models.ForeignKey(CommonUserModel, on_delete=models.PROTECT, blank=False, null=False)
    previous_house_owner = models.ForeignKey(CommonUserModel, on_delete=models.PROTECT, blank=True, null=True, related_name='previous_house_owner')
    present_house_owner = models.ForeignKey(CommonUserModel, on_delete=models.PROTECT, blank=True, null=True, related_name='present_house_owner')
    reason_of_house_change = models.TextField(blank=True, null=True)
    rent_of_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'
        db_table = 'tenant'

    def __str__(self):
        return self.user.name





