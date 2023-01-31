from django.shortcuts import render

from utils.pokemons.poke_api import getListPokemon

# Create your views here.


def home(request):
    return render(request, 'pokemons/pages/home.html', context={

        'pokemonItens': getListPokemon(0, 10)
    })


def pokemon(request):
    return render(request, 'pokemons/pages/pokemon-view.html')
