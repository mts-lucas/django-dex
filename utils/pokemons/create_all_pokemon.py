# script que adciona todos os pokemons da base de dados

from pokemons.models import Pokemon, Evolutions, PkmAbility, PkmType, Generation
from utils.pokemons.poke_api import PokemonClasse, getListPokemon

pkmlist = getListPokemon()

for poke in pkmlist:


    newPkm = Pokemon.objects.create(
        number=poke.id
        picture=poke.photo
        height=poke.height
        weight=poke.weight
        hp=poke.stats['hp']
        attack=poke.stats['attack']
        defense=poke.stats['defense']
        special_attack=poke.stats['special-attack']
        special_defense=poke.stats['special-defense']
        speed=poke.stats['speed']
        color_type=poke.type
    )
    for abilidade in poke.abilities:
        newPkm.abilities.add(PkmAbility.objects.get(name=abilidade))
    for tipo in poke.types:
        newPkm.pkm_types.add(PkmType.objects.get(name=tipo))
    newPkm.generation = Generation.objects.get(name=poke.generation)
    newPkm.evolution_chain_number = Evolutions.objects.get(
        number=poke.evolution_chain_number)
