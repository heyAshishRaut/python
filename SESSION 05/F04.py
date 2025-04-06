# PUT


import requests

def update_user():
    url = "https://jsonplaceholder.typicode.com/users/1"  # Sample API
    updated_data = {
        "name": "Ashish Raut Updated",
        "username": "ashish_raut",
        "email": "ashish.new@example.com"
    }
    response = requests.put(url, json = updated_data)  # Sending PUT request
    if response.status_code == 200:
        print("User Updated:", response.json())  # Displaying JSON response
    else:
        print("Failed to update user")

update_user()