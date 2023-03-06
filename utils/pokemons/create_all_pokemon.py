# script que adciona todos os pokemons da base de dados

from pokemons.models import Pokemon, Evolutions, PkmAbility, PkmType, Generation
from utils.pokemons.poke_api import PokemonClasse, getListPokemon

pkmlist = getListPokemon(0, 2)

for poke in pkmlist:

    evo = Evolutions.objects.get(number=poke.evolution_chain_number)
    
    newPkm = Pokemon.objects.create(
        number=poke.id
        picture=poke.photo
        evolution_chain_number=evo
        height=poke.height
        weight=poke.weight
        hp=poke.stats['hp']
        attack=poke.stats['attack']
        defense=poke.stats['defense']
        special_attack=poke.stats['special-attack']
        special_defense=poke.stats['special-defense']
        speed=poke.stats['speed']
        pkm_types=None
        color_type=None
    )
