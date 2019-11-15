from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Login

admin.site.register(Login, UserAdmin)
