import requests
def search_movie(movieName):
    search = requests.get(f"http://www.omdbapi.com/?s={movieName}&y=&plot=short&apikey=trilogy")
    if search.status_code == 200:
        a = search.json()
        print(a["Search"])