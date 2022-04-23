import requests

# ditto = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

# k = ditto.json()

# i = 0; 
# while i <= 1:
#     print(k['abilities'][i]['ability']['name'])
#     i += 1

# pok = input('Enter in the name of the pokemon in all lowercase!')
# r = requests.get('https://pokeapi.co/api/v2/pokemon/' + pok)
# k = r.json()
# print(k['types'][0]['type']['name'])

pokemon_name = []

i = 1

while i < 500:
    r = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(i))
    k = r.json()
    pokemon_name.append(k['name'])
    i += 1

print(pokemon_name)