from django.urls import path

from . import views

app_name = 'pokemons'

urlpatterns = [
    path('', views.home, name="home"),
    path('addpoke', views.add_poke, name="add_poke"),
    path('sucesso', views.sucesso, name="sucesso"),
]
