from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

import api.applications.membership.admin
from .models import Login


@admin.register(Login)
class LoginAdmin(UserAdmin):
    inlines = [
        api.applications.membership.admin.MembershipInline,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()
        if (
                not is_superuser
                and obj is not None
                and obj == request.user
        ):
            disabled_fields |= {
                'username',
                'is_superuser',
                'groups',
                'user_permissions',
            }
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form
