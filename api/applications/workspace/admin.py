from django.contrib import admin

from api.applications.membership.models import Membership
from .models import Workspace


class MembershipInline(admin.TabularInline):
    model = Membership
    fields = ('related_login',)


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['related_login', 'description']
    readonly_fields = ['id']
    list_filter = ('related_login',)
    inlines = [
        MembershipInline,
    ]
