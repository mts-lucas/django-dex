from django.shortcuts import render

from .models import Pokemon

# Create your views here.


def home(request):

    pkmList = Pokemon.objects.filter(number__lte=150).order_by('number')

    return render(request, 'pokemons/pages/home.html', context={

        'pokemonItens': pkmList,
    })


def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        results = Pokemon.objects.filter(name__icontains=query)
        return render(request, 'search_results.html', {'results': results})
