from django.db import models


class MemberPackage(models.Model):
    package_name = models.CharField(max_length=60)
    # resource = models.CharField(max_length=60)  # dedicated desk, shared_space, day_use
    resource = models.ForeignKey('member.MemberResources', on_delete=models.DO_NOTHING)
    monthly_rate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    overage_rate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Semi_annual = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    Annual_rate = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)

    def __unicode__(self):
        return self.package_name


class Membership(models.Model):
    member_name = models.ForeignKey('auth.User', related_name="member_name", on_delete=models.DO_NOTHING)
    bill_day = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    package_name = models.CharField(max_length=60)
    paid_by = models.ForeignKey('auth.User', related_name='member_paid', on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.member_name


class MemberResources(models.Model):
    resource_name = models.CharField(max_length=60)  # dedicated desk,shared_space,day_use,key,locker,mail
    resource_start = models.DateField(null=True, blank=True)
    resource_end = models.DateField(null=True, blank=True)
    resource_fee = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)

    def __unicode__(self):
        return self.resource_name
