import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3b77bff8a612edd743f5f7500b69d94d'
HEADER = {'Content-type': 'application/json',
      'trainer_token': TOKEN}
TRAINER_ID = '22628'

def test_status_code():
    response = requests.get(url = f' {URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_my_name():
    response_name = requests.get(url = f' {URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_name.json() ["data"] [0] ["trainer_name"] == "Sh1pZe"