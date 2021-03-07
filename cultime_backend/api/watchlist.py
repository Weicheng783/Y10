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

    def get(self, request, *args, **kwargs):
        "Returns all the movies in personal watch list"
        current_user = request.user
        current_watchlist = WatchList.objects.filter(user=current_user).prefetch_related('movie')

        serializer = WatchListSerializer(current_watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
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
            return Response({"Error": "that movie is already present in the watchlist"})
        
        new_watchlist_element.save()
        return Response({"Message": "added new movie"})


class DeleteWatchListElementAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        # if('pk' not in kwargs):
        #     return Response({"Error": "Please send the ID of the movie in the url"})

        current_user = request.user

        if(Movie.objects.filter(id=request.data['id']).count() != 1):
            return Response({"Error": "No such movie"})

        current_movie = Movie.objects.get(id=request.data['id'])

        if(WatchList.objects.filter(user=current_user, movie=current_movie).count() != 1):
            return Response({"Error": "Invalid request"})

        current_watchlist_object = WatchList.objects.get(user=current_user, movie=current_movie)

        print(current_watchlist_object)

        current_watchlist_object.delete()

        return Response({"message": "api call made"})