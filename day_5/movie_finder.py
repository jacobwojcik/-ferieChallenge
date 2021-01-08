import requests
from decouple import config


def search_for_movies(title,api_key):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q":title}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    # print(response.text)
    list_of_movies=[]
    for i in res["d"]:
        if "l" in i and "y" in i:
            list_of_movies.append(i["l"])
    return list_of_movies

def movie_details(movie,api_key):
    url = "http://www.omdbapi.com/?apikey={}&".format(api_key)
    params = {"t": movie }
    
    response = requests.request("GET", url, params=params)
    res = response.json()

    try:
        print(res['Title'])
        print("Released: " + res['Year'])
        print("Genre: " + res['Genre'])
        print("IMDB Rating: " + res['imdbRating'])
        print("Plot: " + res['Plot'])
        print("Cast:")
        for actor in res['Actors'].split(", "):
            print(actor)
        print('\n')
    except:
        pass

def main():
    title = input("Search for: ")
    print("\n")

    API_MOVIES = config('MOVIES_KEY')
    API_DETAILS = config('DETAILS_KEY')

    list_of_movies = list(set(search_for_movies(title,API_MOVIES)))
    
    list_of_movies.sort()

    for movie in list_of_movies:
        movie_details(movie,API_DETAILS)
        
        

if __name__ == "__main__":
       main() 