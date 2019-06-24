from django.contrib import admin

from member.models import MemberPackage


class MemberAdmin(admin.ModelAdmin):
    list_display = ["package_name"]


admin.site.register(MemberPackage, MemberAdmin)
