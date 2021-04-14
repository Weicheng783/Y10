from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.add_movie import add_movie

from api.models import Movie
from api.models import Favourites


class FavouritesAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user = request.user

        current_favourites = Favourites.objects.filter(
            user=current_user
        ).values(
            'id',
            'movie__poster_path',
            'movie__movie_name',
            'movie__id',
            'movie__movie_id',
        )

        return Response(current_favourites)

    def post(self, request):
        current_user = request.user
        current_movie_id = request.data['movie_id']

        add_movie(current_movie_id)

        current_movie = Movie.objects.get(
            movie_id=current_movie_id
        )

        current_favourites = Favourites.objects.filter(
            user=current_user
        )

        if(current_favourites.count() == 3):
            return Response({
                "message": "too_much_entries"
            })
        
        new_favourites_entry = Favourites(
            user=current_user,
            movie=current_movie,
        )

        new_favourites_entry.save()
        return Response({
            "message": "added"
        })


class RemoveFavouriteAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        current_user = request.user
        current_id = request.data['id']

        current_favourite_entry = Favourites.objects.filter(
            id=current_id,
            user=current_user    
        )

        if(current_favourite_entry.count() != 1):
            return Response({"error": "invalid API call!"})
        
        current_favourite_entry.delete()
        return Response({"message": "entry deleted successfully!"})
