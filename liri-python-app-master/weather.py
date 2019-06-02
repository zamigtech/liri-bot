import requests
def search_weather(cityName):
    APIKey = "a94d1807a8ea5a0b3750f1d481048984"
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=imperial&appid={APIKey}")
    search = requests.get(url)
    if search.status_code == 200:
       a = search.json()
       print(a)