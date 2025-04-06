# POST


import requests

def create_user():
    url = "https://jsonplaceholder.typicode.com/users"  # Sample API
    user_data = {
        "name": "Ashish Raut",
        "username": "ashish_raut",
        "email": "ashish@example.com"
    }
    response = requests.post(url, json = user_data)  # Sending POST request
    if response.status_code == 201:
        print("User Created:", response.json())  # Displaying JSON response
    else:
        print("Failed to create user")

create_user()