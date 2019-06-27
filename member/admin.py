from django.contrib import admin

from member.models import MemberPackage
from member.models import MemberResources
from member.models import Membership
from member.models import UserBill
from member.models import BillLineItem


class MemberPkgAdmin(admin.ModelAdmin):
    list_display = ["package_name"]


class MemberResourcesAdmin(admin.ModelAdmin):
    list_display = ["resource_name"]


class MembershipAdmin(admin.ModelAdmin):
    model = MemberPackage
    list_display = ['member_name', 'monthly', 'semi', 'annual', 'active']

    def monthly(self, obj):
        return obj.package_name.monthly_rate

    def semi(self, obj):
        return obj.package_name.Semi_annual

    def annual(self, obj):
        return obj.package_name.Annual_rate


class BillLineItemInline(admin.TabularInline):
    model = BillLineItem
    extra = 0


class UserBillAdmin(admin.ModelAdmin):
    model = UserBill
    list_display = ['id', 'user', 'period_start', 'period_end', 'amount',]
    search_fields = ('user__username', 'user__first_name')
    raw_id_fields = ('user', )
    readonly_fields = ('id', 'created_ts', )
    fields = (
        ('id', 'created_ts', 'closed_ts'),
        ('due_date', 'period_start', 'period_end'),
        'user',
        'in_progress',
        'mark_paid',
        'comment',
        'note',
    )
    ordering = ['-period_start', ]
    inlines = [BillLineItemInline, ]


admin.site.register(MemberPackage, MemberPkgAdmin)
admin.site.register(MemberResources, MemberResourcesAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserBill, UserBillAdmin)
