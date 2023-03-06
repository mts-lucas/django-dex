# script rodado no shell para adicionar todos os objetos no banco de dados

from pokemons.models import Generation
from utils.pokemons.poke_api_generations import pokeApiGen  # noqa: F401 E501

gens = pokeApiGen()
for gene in gens:
    gen = Generation.objects.create(name=gene)
    gen.save()
