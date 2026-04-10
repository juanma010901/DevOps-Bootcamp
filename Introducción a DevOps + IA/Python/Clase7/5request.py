import requests

request = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

print(request.status_code)
print(request.headers['content-type'])
print(request.encoding)
print(request.text)
print(request.json())
