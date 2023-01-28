import requests


def requestUrl(pokemonDict):

    pkmUrl = pokemonDict['url']

    return pkmUrl


def pokeApi(offset=0, limit=25):

    r = requests.get(
        f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}')

    data = r.json()

    pokemonDict = data['results']

    pokemonList = list(map(requestUrl, pokemonDict))

    return pokemonList


# class Pokemon():
#     def __init__(self, pokemonListItem):
#         self.url = pokemonListItem[url]


