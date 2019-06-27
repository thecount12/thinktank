from django.db import models
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce


class MemberPackage(models.Model):  # Month-to-month, semi-annual
    package_name = models.CharField(max_length=60, blank=True)
    resource = models.ForeignKey('member.MemberResources', related_name='foo', on_delete=models.DO_NOTHING)
    monthly_rate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    overage_rate = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    Semi_annual = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    Annual_rate = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)
    # foo = models.ManyToManyField('Membership')

    def __unicode__(self):
        return self.package_name

    def __str__(self):
        return self.package_name


class MemberResources(models.Model):
    resource_name = models.CharField(max_length=60)  # dedicated desk,shared_space,day_use,key,locker,mail
    resource_start = models.DateField(null=True, blank=True)
    resource_end = models.DateField(null=True, blank=True)
    resource_fee = models.DecimalField(decimal_places=2, max_digits=10,  blank=True, null=True)

    def __unicode__(self):
        return self.resource_name

    def __str__(self):
        return self.resource_name


class Membership(models.Model):
    member_name = models.ForeignKey('auth.User', related_name="member_name", on_delete=models.DO_NOTHING)
    bill_day = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    package_name = models.ForeignKey('member.MemberPackage', related_name='pkg_name', on_delete=models.DO_NOTHING)
    paid_by = models.ForeignKey('auth.User', related_name='member_paid', on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=60, blank=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.member_name

    def month_rate(self, ):
        return self.package_name.monthly_rate

    def semi_rate(self, ):
        return self.package_name.Semi_annual

    def annual_rate(self, ):
        return self.package_name.Annual_rate


class UserBill(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True)
    closed_ts = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('auth.User', related_name='bills', on_delete=models.DO_NOTHING)
    period_start = models.DateField()
    period_end = models.DateField()
    due_date = models.DateField()
    comment = models.TextField(blank=True, null=True, help_text="Public comments visible by user")
    note = models.TextField(blank=True, null=True, help_text="Private notes about this bill")
    in_progress = models.BooleanField(default=False,
                                      blank=False,
                                      null=False,
                                      help_text="Mark a bill as 'in progress' indicating someone "
                                                "is working on it")
    mark_paid = models.BooleanField(default=False,
                                    blank=False,
                                    null=False,
                                    help_text="Mark a bill as paid even if it is not")
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_tax_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_owed = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    mem_name = models.ForeignKey('member.Membership', related_name='m_name', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __unicode__(self):
        return self.created_ts

    def amount(self):
        return self.line_items.aggregate(amount=Coalesce(Sum('amount'), Value(0.00)))['amount']


class BillLineItem(models.Model):
    bill = models.ForeignKey(UserBill, related_name="line_items", null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    custom = models.BooleanField(default=False)
