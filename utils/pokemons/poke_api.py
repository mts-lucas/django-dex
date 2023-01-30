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
        self.types = None
        self.type = None
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

        return newStatsDict

    def getTypes(self, pokemonjson):
        typeDict = pokemonjson['types']
        typeList = []
        for tipos in typeDict:
            typeList.append(tipos['type']['name'])

        return typeList

    def getSprite(self, pokemonjson):
        spritesDict = pokemonjson['sprites']['other']
        pokemonSprite = spritesDict['official-artwork']['front_default']

        return pokemonSprite

    def getPokemonDetail(self, pokemonurl):

        r = requests.get(pokemonurl)

        pokemonData = r.json()

        self.id = pokemonData['id']
        self.name = pokemonData['name']
        self.types = self.getTypes(pokemonData)
        self.type = self.types[0]
        self.height = pokemonData['height']
        self.weight = pokemonData['weight']
        self.photo = self.getSprite(pokemonData)
        self.stats = self.getStats(pokemonData)
