from django.db import models
from housing.models import HousingModel
from account.models import User


class Renter(HousingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    previous_house_owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='previous_house_owner')
    present_house_owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='present_house_owner')
    reason_of_house_change = models.TextField(blank=True, null=True)
    rent_of_date = models.DateField(blank=True, null=True)
    check_out_admin_approve = models.BooleanField(default=False)
    check_in_admin_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Renter'
        verbose_name_plural = 'Renters'
        db_table = 'renter'

    def __str__(self):
        return self.user.username

    # @property
    # def present_house_owner_name(self):
    #     return self.present_house_owner.user

    # @property
    # def previous_house_owner_name(self):
    #     return "{}-{}".format(self.previous_house_owner.first_name, self.previous_house_owner.last_name)


class CheckIn(HousingModel):
    renter = models.ForeignKey(Renter, on_delete=models.PROTECT, blank=True, null=True)
    unit_code = models.IntegerField(blank=True, null=True)
    check_in_date = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Check In'
        verbose_name_plural = 'Check Ins'
        db_table = 'checkin'

    def __str__(self):
        return self.renter.user.username

    @property
    def check_in(self):
        return str(self.check_in_date).split(' ')[0]


