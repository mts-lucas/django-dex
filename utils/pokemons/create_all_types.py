# script rodado no shell para adicionar todos os objetos no banco de dados

from pokemons.models import PkmType

from .poke_api_types import pokeApiType

tiposList = pokeApiType()

for tipo in tiposList:
    newType = PkmType.objects.create(name=tipo)
    newType.save()
