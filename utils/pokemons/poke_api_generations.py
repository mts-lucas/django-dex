import requests


def pokeApiGen():
    r = requests.get('https://pokeapi.co/api/v2/generation')
    data = r.json()
    results = data['results']
    genList = []

    for result in results:
        gen = result['name']
        genList.append(gen)

    return genList
