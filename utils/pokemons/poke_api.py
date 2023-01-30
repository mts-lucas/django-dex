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


class Pokemon():
    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.types = None
        self.height = None
        self.width = None
        self.photo = None
        self.stats = None

    def getStats(self, pokemonjson):
        statsDict = pokemonjson['stats']
        newStatsDict = {}
        for status in statsDict:
            statusName = status['stat']['name']
            statusNumber = status['base_stat']
            newStatsDict[statusName] = statusNumber

        self.stats = newStatsDict
