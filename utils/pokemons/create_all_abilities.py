from pokemons.models import PkmAbility
from utils.pokemons.poke_api_abilities import pokeApiAbility         # noqa: F401 E501

abilidades = pokeApiAbility()

for abilidade in abilidades:
    ab = PkmAbility.objects.create(name=abilidade)
    ab.save()
