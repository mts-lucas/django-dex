from django.contrib import admin

from .models import Evolutions, Generation, PkmAbility, PkmType, Pokemon

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


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    filter_horizontal = ('pkm_types', 'abilities',)
