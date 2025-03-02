import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3b77bff8a612edd743f5f7500b69d94d'
HEADER = {'Content-type': 'application/json',
      'trainer_token': TOKEN}

BODY_CREATE = {
    "name": "Питон",
    "photo_id": 1
}

BODY_CHANGE = {
    "pokemon_id": "248984",
    "name": "Новый питон",
    "photo_id": 2
}

BODY_CATCH = {
    "pokemon_id": "248984"
}

'''response_create = requests.post(url = f' {URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print (response_create.text) 

response_change = requests.put(url = f' {URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print (response_change.text) '''

response_catch = requests.post(url = f' {URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CHANGE)
print (response_catch.text) 

#/trainers/add_pokeball и /pokemons