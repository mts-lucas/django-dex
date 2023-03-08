from django.urls import path

from . import views

app_name = 'pokemons'

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search_results, name="search_results"),
    path('type/<str:name>/', views.pkm_type, name="tipo")
]
