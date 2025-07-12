
import os
from dotenv import load_dotenv
import tmdbsimple as tmdb

load_dotenv()

TMDB_API_KEY = os.getenv("API_Key")
tmdb.API_KEY = TMDB_API_KEY


def main():
    # movie = tmdb.Movies(550)  # Fight Club ID
    # response = movie.info()
    # print(movie.title)

    search = tmdb.Search()
    # response = search.movie(query='The Bourne')
    response = search.movie(query='Jackie Chan')
    for s in search.results:
        print(s['title'], s['id'], s['release_date'], s['popularity'])


if __name__ == "__main__":
    main()
