from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import Review

import random
import requests


class RecommendedMoviesAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user = request.user

        current_reviews = Review.objects.filter(
            author=current_user,
            rating__gte=3,
        ).values(
            'movie__movie_id',
            'movie__movie_name',
        )

        current_reviews = current_reviews[
            current_reviews.count() - min(current_reviews.count(), 3):
        ]

        API_KEY = 'a475b0e3e8df4fd3d037fecb083d1042'
        recommended_movies = []
        for review in current_reviews:
            API_LINK = "https://api.themoviedb.org/3/movie/" + str(review['movie__movie_id']) + "/similar?api_key=" + API_KEY + "&language=en-US&page=1"
            
            r = requests.get(url = API_LINK)
            current_request = r.json()

            temp_count = 0
            for movie in current_request['results']:
                if(temp_count > 5):
                    break
                if('release_date' in movie):
                    recommended_movies.append(
                        {
                            "title": movie['title'],
                            "release_date": movie['release_date'][0:4],
                            "id": movie['id'],
                            "genres": movie['genre_ids'],
                            "poster_path": movie['poster_path'],
                            "overview": movie['overview']
                        }
                    )
                temp_count += 1
        
        random.shuffle(recommended_movies)
                
        return Response(recommended_movies)
