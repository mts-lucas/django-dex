from pokemons.models import Evolutions

from utils.pokemons.poke_api_evolutions import Evo, pokeApiEvolution

evosList = pokeApiEvolution()

for evolve in evosList:
    newEvolve = Evolutions.objects.create(
        first_form=evolve.name,
        number=evolve.number
    )
    newEvolve.save()
