import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)

print(response.json())

data = response.json()

print(data[0]['name'])

for user in data:
    name = user['name']
    print(name)
    