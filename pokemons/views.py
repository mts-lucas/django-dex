from django.shortcuts import get_list_or_404, render

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
    return render(request, 'pokemons/pages/search-results.html', context={
        'results': results,
    })


def pkm_type(request, name):

    pkmList = get_list_or_404(
        Pokemon.objects.filter(
            pkm_types__name__icontains=name
        ).order_by('number'))

    title = ''
    for pokemon in pkmList:
        for pkm_type in pokemon.pkm_types.all():
            if pkm_type.name.lower() == name.lower():
                title = pkm_type.name
                break
        if title:
            break

    if not title and pkmList:
        title = "NotFound"

    return render(request, 'pokemons/pages/tipos.html', context={

        'pokemonItens': pkmList,
        'title': title,
    })
