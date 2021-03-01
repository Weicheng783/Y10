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

class MovieSearchAPI(generics.GenericAPIView):
    """
    Performs Search on movies operation
    """
    def post(self, request):
        "The get request returns all the movies with similar names as user input"

        print(request.data)
        
        URL = "https://api.themoviedb.org/3/search/movie?api_key=a475b0e3e8df4fd3d037fecb083d1042&language=en-US&query=" + process_query(request.data['title']) + "&page=1&include_adult=false"

        r = requests.get(url = URL)
        current_request = r.json()

        similar_named_movies = []
        for movie in current_request['results']:
            if(len(similar_named_movies) == 10):
                break

            if('release_date' in movie):
                similar_named_movies.append(
                    {
                        "title": movie['title'],
                        "release_date": movie['release_date'][0:4],
                        "id": movie['id']
                    }
                )

        return Response(similar_named_movies)