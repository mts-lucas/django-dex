from django.contrib import admin

from .models import Evolutions, PkmType

# Register your models here.


@admin.register(PkmType)
class PkmTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Evolutions)
class EvolutionsAdmin(admin.ModelAdmin):
    ...
