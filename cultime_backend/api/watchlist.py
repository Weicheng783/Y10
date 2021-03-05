from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView 

from django.contrib.auth.models import User
from api.models import Movie
from api.models import WatchList

from api.serializers import WatchListSerializer
from api.add_movie import add_movie


class WatchListAPI(APIView):
    """
    
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        "Returns all the movies in personal watch list"
        current_user = request.user
        current_watchlist = WatchList.objects.filter(user=current_user).prefetch_related('movie')

        serializer = WatchListSerializer(current_watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        current_user = request.user
        new_movie_id = request.data['movie_id']

        # In case we don't have current movie in our database
        add_movie(new_movie_id) 

        current_movie = Movie.objects.get(movie_id=new_movie_id)

        new_watchlist_element = WatchList(
            user=current_user,
            movie=current_movie
        )

        if(WatchList.objects.filter(user=current_user, movie=current_movie).count() != 0):
            return Response({"error": "that movie is already present in the watchlist"})
        
        new_watchlist_element.save()
        return Response({"message": "added new movie"})
