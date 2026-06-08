import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
users = response.json()

with open("data/users_raw.json", "w") as file:
    json.dump(users, file, indent=4)

print("Raw API JSON saved to data/users_raw.json")
print(f"Records saved: {len(users)}")