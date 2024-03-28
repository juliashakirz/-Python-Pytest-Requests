import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
                         json={
                             "name": "Бульбазавр",
                             "photo": "https://dolnikov.ru/pokemons/albums/1005.png"
                             },
                        headers= {'trainer_token': 'e6668c76932c101c2b858716090b4677',
                                  'Content-Type': 'application/json'}, timeout=10)
print(f'Code: {response.status_code} - {response.reason}.Message: {response.text}')


response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                         json={
                             "pokemon_id": "21495",
                             "name": "New Name",
                             "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                             },
                         headers= {'trainer_token': 'e6668c76932c101c2b858716090b4677',
                                  'Content-Type': 'application/json'}, timeout=10)
print(f'Code: {response.status_code} - {response.reason}.Message: {response.text}')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                         json={
                             "pokemon_id": "21496"
                             },
                        headers= {'trainer_token': 'e6668c76932c101c2b858716090b4677',
                                  'Content-Type': 'application/json'}, timeout=10)
print(f'Code: {response.status_code} - {response.reason}.Message: {response.text}')
