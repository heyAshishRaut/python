import requests

load_dotenv()
def main():
    CITY = input("Enter city name - ")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    res = requests.get(url)
    data = res.json()
    print("-----------------------------")
    if res.status_code == 200:
        print(data["weather"][0]["main"])
        print(data["weather"][0]["description"])
        print(data["main"]["temp"])

    else:
        print("Invalid city name")
    print("-----------------------------")

if __name__ == "__main__":
    main()