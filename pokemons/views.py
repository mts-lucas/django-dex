from django.shortcuts import get_list_or_404, get_object_or_404, render

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
            pkm_types__name=name
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


def ability(request, name):

    pkmList = get_list_or_404(
        Pokemon.objects.filter(
            abilities__name=name
        ).order_by('number'))

    title = ''
    for pokemon in pkmList:
        for pkm_ab in pokemon.abilities.all():
            if pkm_ab.name.lower() == name.lower():
                title = pkm_ab.name
                break
        if title:
            break

    if not title and pkmList:
        title = "NotFound"

    return render(request, 'pokemons/pages/ability.html', context={

        'pokemonItens': pkmList,
        'title': title,
    })


def generation(request, name):

    pkmList = get_list_or_404(
        Pokemon.objects.filter(
            generation__name=name
        ).order_by('number'))

    title = ''
    for pokemon in pkmList:
        if pokemon.generation.name == name.lower():
            title = pokemon.generation.name
            break
        if title:
            break

    if not title and pkmList:
        title = "NotFound"

    return render(request, 'pokemons/pages/generation.html', context={

        'pokemonItens': pkmList,
        'title': title,
    })


def pokemon(request, number):
    pkm = get_object_or_404(Pokemon, number=number)
    pkmevo = get_list_or_404(
        Pokemon,
        evolution_chain_number=pkm.evolution_chain_number)

    return render(request, 'pokemons/pages/pokemon-view.html', context={

        'pkm': pkm,
        'title': pkm.name,
        'evos': pkmevo,
    })
