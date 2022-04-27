import requests

def get_poke_info(pokemon):
    """

    :param pokemon:
    :return:
    """
    print("Getting pokemon information..." " ", end="")
    name = pokemon.lower().strip()
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(name))

    if response.status_code == 200:
        print("Success! You can find the details below!")
        return response.json()

    else:
        print('Connection failed...', response.status_code)

        return
def get_poke_list(limit=200, offset=0):
    """

    :param limit:
    :param offset:
    :return:
    """
    print("Getting image from url...", end='')
    paramdict = {
        'offset': offset,
        'limit': limit,



    }
    response = requests.get("https://pokeapi.co/api/v2/pokemon/",params=paramdict)

    if response.status_code == 200:
        print("Success! You can find the details below!")

        pokedict = response.json()
        return [p['name'] for p in pokedict['results']]

    else:
        print('Connection failed...', response.status_code)

        return
def get_pokemon_image_url(name):
    """

    :param name:
    :return:
    """
    poke_dict = get_poke_info(name)
    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url
