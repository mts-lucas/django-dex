# script que adciona todos os pokemons da base de dados

from pokemons.models import (Evolutions, Generation, PkmAbility, PkmType,
                             Pokemon)
from utils.pokemons.poke_api import PokemonClasse, getListPokemon

pkmlist = getListPokemon()

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
    new_pkm.abilities.set([PkmAbility.objects.get(name=ability) for ability in poke.abilities])
    new_pkm.pkm_types.set([PkmType.objects.get(name=tipo) for tipo in poke.types])
    new_pkm.save()
