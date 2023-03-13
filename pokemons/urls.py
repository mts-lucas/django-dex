from django.urls import path

from . import views

app_name = 'pokemons'

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search_results, name="search_results"),
    path('type/<str:name>/', views.pkm_type, name="tipo"),
    path('ability/<str:name>/', views.ability, name="ability"),
    path('generation/<str:name>/', views.generation, name="generation"),
    path('pokemon/<int:number>/', views.pokemon, name="pokemon"),
]
