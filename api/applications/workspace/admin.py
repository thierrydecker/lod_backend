from django.contrib import admin

import api.applications.membership.admin
from api.applications.membership.models import Membership
from .models import Workspace


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['related_login', 'description']
    readonly_fields = ['id']
    list_filter = ('related_login',)
    inlines = [
        api.applications.membership.admin.MembershipInline,
    ]
