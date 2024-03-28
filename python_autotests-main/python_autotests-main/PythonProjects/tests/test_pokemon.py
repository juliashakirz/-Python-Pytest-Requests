import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104' 

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers', params= {'trainer_id': 3563}, timeout=5)
    assert response.status_code == 200, 'Unexpeted  status code for /trainers'
    assert response.json()['trainer_name'] == 'Алина The One', ''

CASES = [(3835, 200), (45676, 400)]
@pytest.mark.parametrize('id, code', CASES)
def test_parametrize(id, code):
    response = requests.get(url=f'{HOST}/trainers', params= {'trainer_id': id}, timeout=5)
    assert response.status_code == code, 'Unexpeted  status code for /trainers'
