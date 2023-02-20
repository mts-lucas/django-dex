# script rodado no shell para adicionar todos os objetos no banco de dados

from pokemons.models import PkmType

from utils.pokemons.poke_api_types import pokeApiType       # noqa: F401 E501

tiposList = pokeApiType()

for tipo in tiposList:
    newType = PkmType.objects.create(name=tipo)
    newType.save()
