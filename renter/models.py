from django.db import models
from housing.models import HousingModel
from account.models import User


class Renter(HousingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    previous_house_owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='previous_house_owner')
    present_house_owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='present_house_owner')
    reason_of_house_change = models.TextField(blank=True, null=True)
    rent_of_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Renter'
        verbose_name_plural = 'Renters'
        db_table = 'renter'

    def __str__(self):
        return self.user.username





