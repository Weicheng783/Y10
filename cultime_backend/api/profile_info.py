from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from api.models import Review
from api.models import AdditionalUser
from api.models import Favourites


class ProfileInfoAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        current_user = User.objects.get(
            id=request.data['id']
        )

        current_reviews = Review.objects.filter(
            author=current_user,
            is_private=False,
        ).values(
            'movie__movie_name',
            'movie__poster_path',
            'content',
            'rating',
        )

        current_favourites = Favourites.objects.filter(
            user=current_user,
        ).values(
            'movie__movie_name',
            'movie__poster_path',
        )

        additional_info = AdditionalUser.objects.filter(
            user=current_user
        ).values(
            'profile_picture',
            'user_bio',
            'user__first_name',
            'user__last_name',
        )

        dictionary = {}
        dictionary['reviews'] = current_reviews
        dictionary['favourites'] = current_favourites
        dictionary['info'] = additional_info

        return Response(dictionary)