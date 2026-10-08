import requests


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

print(response.json())

data = response.json()

print(data[0]['name'])

print("Username: " + data[0]['username'])

print("Zipcode: " + data[0]['address']['zipcode'])

for user in data:
    name = user['name']
    username = user['username']
    email = user['email']
    company_name = user['company']['name']
    phone = user['phone']
    if " x" in phone:
        number, extension = phone.split(" x", 1)
    else:
        number = phone
        extension = None
    
    print(f"Name: {name}, Username: {username}, Email: {email}, Company: {company_name}, Phone: {number}, Extension: {extension}")
    