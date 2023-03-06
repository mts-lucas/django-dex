import requests


def requestUrl(pokemonDict):

    pkmUrl = pokemonDict['url']

    return pkmUrl


def pokeApi(offset=0, limit=809):

    r = requests.get(
        f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}')

    data = r.json()

    pokemonDict = data['results']

    pokemonList = list(map(requestUrl, pokemonDict))

    return pokemonList


class PokemonClasse():
    def __init__(self, pokemonurl):
        self.url = pokemonurl
        self.id = None
        self.name = None
        self.types = None
        self.type = None
        self.height = None
        self.width = None
        self.photo = None
        self.stats = None
        self.abilities = None
        self.evolution_chain_number = None
        # adicionar evolucoes usando o pokemon-species/id
        # evolution-chain/429

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

    def getAbilities(self, pokemonjson):
        abilitiesDict = pokemonjson['abilities']
        abltList = []
        for ablty in abilitiesDict:
            abilityN = ablty['ability']
            ability = abilityN['name']
            abltList.append(ability)
        return abltList

    def getEvolutionChain(self, pokemonjson):
        specieUrl = pokemonjson['species']['url']
        r = requests.get(specieUrl)
        data = r.json()
        urlEvo = data['evolution_chain']['url']
        r2 = requests.get(urlEvo)
        data2 = r2.json()
        evoNumber = data2['id']
        return evoNumber

    def getPokemonDetail(self):

        r = requests.get(self.url)

        pokemonData = r.json()

        self.id = pokemonData['id']
        self.name = pokemonData['name']
        self.types = self.getTypes(pokemonData)
        self.type = self.types[0]
        self.height = pokemonData['height']
        self.weight = pokemonData['weight']
        self.photo = self.getSprite(pokemonData)
        self.stats = self.getStats(pokemonData)


def getListPokemon(offset=0, limit=25):

    if limit > 1008:
        offset = 1008
        limit: 0

    pokemonUrlList = pokeApi(offset, limit)

    pokemonList = []

    for pokemonItem in pokemonUrlList:

        newPokemon = PokemonClasse(pokemonItem)
        newPokemon.getPokemonDetail()
        pokemonList.append(newPokemon)

    return pokemonList
