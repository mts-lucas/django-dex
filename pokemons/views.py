from django.shortcuts import redirect, render

from utils.pokemons.poke_api import PokemonClasse, getListPokemon  # noqa: F401

from .models import Evolutions, Generation, PkmAbility, PkmType, Pokemon

# Create your views here.


def home(request):
    return render(request, 'pokemons/pages/home.html', context={

        'pokemonItens': getListPokemon(0, 10)
    })


def add_poke(request):
    if request.method == 'POST':
        pkmlist = getListPokemon(700, 109)

        for poke in pkmlist:

            gen = Generation.objects.get(name=poke.generation)

            chainNumber = Evolutions.objects.get(
                number=poke.evolution_chain_number)

            new_pkm = Pokemon.objects.create(
                name=poke.name,
                number=poke.id,
                picture=poke.photo,
                height=poke.height,
                weight=poke.weight,
                hp=poke.stats['hp'],
                attack=poke.stats['attack'],
                defense=poke.stats['defense'],
                special_attack=poke.stats['special-attack'],
                special_defense=poke.stats['special-defense'],
                speed=poke.stats['speed'],
                color_type=poke.type,
                generation=gen,
                evolution_chain_number=chainNumber
            )
            new_pkm.abilities.set([PkmAbility.objects.get(
                name=ability) for ability in poke.abilities])
            new_pkm.pkm_types.set([PkmType.objects.get(name=tipo)
                                  for tipo in poke.types])

        return redirect('pokemons/pages/sucesso.html')
    return render(request, 'pokemons/pages/botao.html')


def sucesso(request):
    return render(request, 'pokemons/pages/sucesso.html')
