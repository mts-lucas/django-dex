from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pokemons/pages/home.html')


def pokemon(request):
    return render(request, 'pokemons/pages/pokemon-view.html')
