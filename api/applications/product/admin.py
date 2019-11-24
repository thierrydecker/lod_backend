from django.contrib import admin

from .models import Product


@admin.register(Product)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['code', 'related_workspace', 'description']
    readonly_fields = ['id']
    list_filter = ('related_workspace',)
