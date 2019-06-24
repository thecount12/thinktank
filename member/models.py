from django.db import models


class MemberPackage(models.Model):
    package_name = models.CharField(max_length=60)
    resource = models.CharField(max_length=60)  # dedicated desk, shared_space, day_use
    monthly_rate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    overage_rate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Semi_annual = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    Annual_rate = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)

    def __unicode__(self):
        return self.package_name


class Membership(models.Model):
    member = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    bill_day = models.IntegerField(max_length=2, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
