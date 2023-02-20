import requests


class Evo:

    def __init__(self, number, name):
        self.number = number
        self.name = name

    def __str__(self):
        return str(self.name)


def pokeApiEvolution():

    evoList = []

    r = requests.get(
        'https://pokeapi.co/api/v2/evolution-chain?offset=0&limit=429')

    dataurl = r.json()

    urlList = []
    urlDict = dataurl['results']

    for urls in urlDict:
        urlList.append(urls['url'])

    for lista in urlList:
        req = requests.get(lista)

        evoDict = req.json()

        numero = evoDict['id']
        chain = evoDict['chain']
        especie = chain['species']
        name = especie['name']

        evoList.append(Evo(number=numero, name=name))
        print(numero)

    return evoList
