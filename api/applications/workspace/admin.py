from django.contrib import admin

from .models import Workspace


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['related_login', 'description']
    readonly_fields = ['id']
    list_filter = ('related_login',)
