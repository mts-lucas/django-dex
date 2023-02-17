import requests


# def requestUrlAbilities(abilityDict):

#     pkmUrl = abilityDict['url']
#     r = requests.get(pkmUrl)

#     return pkmUrl


def pokeApiAbility(offset=0, limit=298):

    r = requests.get(
        f'https://pokeapi.co/api/v2/ability?offset={offset}&limit={limit}')

    data = r.json()

    abilityList = []

    abilitiesDict = data['results']

    for results in abilitiesDict:
        abilityList.append(results['name'])

    return abilityList
