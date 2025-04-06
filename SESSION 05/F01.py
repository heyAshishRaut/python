"""
APIs Handling
"""



import requests

def fetch():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if(data["success"] and "data" in data):
        userData = data["data"]
        username = userData["login"]["username"]
        country = userData["location"]["country"]
        return username, country
    else:
        raise Exception ("Failed to fetch user data")
    
def main():
    try:
        username, country = fetch()
        print(f"Username -  {username}, Country - {country}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()