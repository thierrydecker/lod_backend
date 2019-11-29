from django.contrib import admin

from .models import Child
from .models import Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'related_parent')
