# script rodado no shell para adicionar todos os objetos no banco de dados

from pokemons.models import Evolutions
from utils.pokemons.poke_api_evolutions import Evo, pokeApiEvolution        # noqa: F401 E501

evosList = pokeApiEvolution()

for evolve in evosList:
    newEvolve = Evolutions.objects.create(
        first_form=evolve.name,
        number=evolve.number
    )
    newEvolve.save()
