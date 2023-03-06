from django.contrib import admin

from .models import Evolutions, Generation, PkmAbility, PkmType

# Register your models here.


@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    ...


@admin.register(PkmAbility)
class PkmAbilityAdmin(admin.ModelAdmin):
    ...


@admin.register(PkmType)
class PkmTypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Evolutions)
class EvolutionsAdmin(admin.ModelAdmin):
    ...
