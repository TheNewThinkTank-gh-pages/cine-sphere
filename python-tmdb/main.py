
import os
from pprint import pprint as pp
from dotenv import load_dotenv
import tmdbsimple as tmdb

load_dotenv()

TMDB_API_KEY = os.getenv("API_Key")
tmdb.API_KEY = TMDB_API_KEY


def main():
    # movie = tmdb.Movies(550)  # Fight Club ID
    # response = movie.info()
    # print(movie.title)

    # search = tmdb.Search()
    # response = search.movie(query='The Bourne')
    # for s in search.results:
    #     print(s['title'], s['id'], s['release_date'], s['popularity'])

    # search.person(query='Jackie Chan')
    # for s in search.results:
    #     print(s['name'], s['id'], s['popularity'])  # 18897

    person = tmdb.People(18897)
    person.info()
    # print(person.name)
    # print(person.biography)
    # print(person.place_of_birth)
    # print(person.birthday)
    # print(person.deathday)
    # print(person.also_known_as)
    # print(person.changes())

    # print(type(person.movie_credits()))  # <class 'dict'>
    # print(person.movie_credits().keys())  # dict_keys(['cast', 'crew', 'id'])
    # pp(person.movie_credits()['cast'])
    # pp(person.movie_credits()['crew'])
    # pp(person.movie_credits())

    movies = [
        (movie['title'], movie['release_date'], movie['popularity'])
        for movie in person.movie_credits()['cast']   
        if movie['release_date']
    ]
    movies.sort(key=lambda x: x[1], reverse=True)  # Sort by release date
    pp(movies)


if __name__ == "__main__":
    main()
