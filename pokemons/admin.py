from django.contrib import admin

from .models import PkmType

# Register your models here.


@admin.register(PkmType)
class PkmTypeAdmin(admin.ModelAdmin):
    ...
