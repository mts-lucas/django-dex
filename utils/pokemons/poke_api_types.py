import requests


def pokeApiType():

    r = requests.get('https://pokeapi.co/api/v2/type?offset=0&limit=20')

    data = r.json()

    typesList = []

    typesDict = data['results']

    for tipo in typesDict:
        typesList.append(tipo['name'])

    return typesList


teste = pokeApiType()

print(teste)
