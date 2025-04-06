# DELETE

import requests

def delete_user():
    url = "https://jsonplaceholder.typicode.com/users/1"  # Sample API
    response = requests.delete(url)  # Sending DELETE request
    if response.status_code == 200:
        print("User Deleted Successfully")
    else:
        print("Failed to delete user")

delete_user()