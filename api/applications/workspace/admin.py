from django.contrib import admin

from .models import Workspace


@admin.register(Workspace)
class LoginAdmin(admin.ModelAdmin):
    pass
