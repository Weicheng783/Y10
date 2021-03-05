from django.shortcuts import render
from api.models import Movie

import requests

TMDB_API_KEY = 'a475b0e3e8df4fd3d037fecb083d1042'

def add_movie(new_movie_id):
    if(Movie.objects.filter(movie_id=new_movie_id).count() != 0):
        return
    
    URL = 'https://api.themoviedb.org/3/movie/' + str(new_movie_id) + '?api_key=' + TMDB_API_KEY + '&language=en-US'
    r = requests.get(url = URL)
    current_request = r.json()

    new_movie = Movie(
        movie_id=new_movie_id,
        movie_name=current_request['title'],
        poster_path=current_request['poster_path'],
        production_year=int(current_request['release_date'][0:4]),
        overview=current_request['overview'],
        rating=int(round(current_request['vote_average']/2))
    )

    new_movie.save()
