from django.contrib import admin

from .models import Membership


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['related_workspace', 'related_login']
    readonly_fields = ['id']
    list_filter = ('related_login', 'related_workspace')


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0
