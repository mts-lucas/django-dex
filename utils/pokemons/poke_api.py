# import json

import requests


def pokeApi(offset=0, limit=25):
    # requisição
    r = requests.get(
        f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}')

    # tranformando o json em dict
    data = r.json()

    # tranformando a chave results em uma lista de dicionarios(name, url)
    pokemonList = data['results']

    return pokemonList

