# GET


import requests

def get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"  # Sample API
    response = requests.get(url)  # Sending a GET request
    if response.status_code == 200:
        res = response.json()  # Displaying JSON response
        name = res["name"]
        email = res["email"]
        cpy = res["company"]["name"]

        print(f"{name}, email - {email}, Company - {cpy} ", name, email, cpy)
    else:
        print("Failed to fetch user data")

get_user()