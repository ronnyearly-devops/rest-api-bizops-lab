import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Number of Users:", len(data))

print("\nFirst User:")

print(data[0])