from django.contrib import admin

from member.models import MemberPackage
from member.models import MemberResources
from member.models import Membership


class MemberPkgAdmin(admin.ModelAdmin):
    list_display = ["package_name"]


class MemberResourcesAdmin(admin.ModelAdmin):
    list_display = ["resource_name"]


class blahInline(admin.TabularInline):
    model = MemberPackage

    # def get_queryset(self, request):
    #     # eturn Child.objects.filter('monthly_rate')
    #     return MemberPackage.monthly_rate


class MembershipAdmin(admin.ModelAdmin):
    # list_display = ["member_name"]
    # inline = [blahInline, ]
    fields = ('member_name', )
    inlines = [blahInline, ]


admin.site.register(MemberPackage, MemberPkgAdmin)
admin.site.register(MemberResources, MemberResourcesAdmin)
admin.site.register(Membership, MembershipAdmin)
