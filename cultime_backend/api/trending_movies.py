from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import Movie

# Allows API calls to be made from Python
import requests

def process_query(query_in):
    query_in = query_in.replace(' ', '%20')
    return query_in

class TrendingMoviesAPI(generics.GenericAPIView):
    """
    Returns Trending Movies
    """
    def get(self, request):
        "The get request returns trending movies"

        print(request.data)
        
        URL = "https://api.themoviedb.org/3/trending/movie/week?api_key=a475b0e3e8df4fd3d037fecb083d1042"

        r = requests.get(url = URL)
        current_request = r.json()

        trending_movies = []
        for movie in current_request['results']:
            if('release_date' in movie):
                trending_movies.append(
                    {
                        "title": movie['title'],
                        "release_date": movie['release_date'][0:4],
                        "id": movie['id'],
                        "genres": movie['genre_ids'],
                        "poster_path": movie['poster_path'],
                        "overview": movie['overview']
                    }
                )

        return Response(trending_movies)