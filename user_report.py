import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

print(f"Users Retrieved: {len(users)}")

with open("reports/users_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "id",
        "name",
        "username",
        "email",
        "company"
    ])

    for user in users:
        writer.writerow([
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["company"]["name"]
        ])

print("CSV report saved to reports/users_report.csv")