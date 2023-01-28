from django.urls import path

from . import views

app_name = 'pokemons'

urlpatterns = [
    path('', views.home, name="home"),
    path('pokemons/<int:id>/', views.pokemon, name="pokemon"),
]
