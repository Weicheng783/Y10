from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from api.models import Movie
from api.models import Review

class PersonalReviewsAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        current_user = request.user
        all_reviews = Review.objects.filter(
            author=current_user
        ).values(
            'author__first_name',
            'author__last_name',
            'author__additionaluser__profile_picture',
            'movie__poster_path',
            'movie__movie_name',
            'movie__overview',
            'movie__id',
            'movie__movie_id',
            'content',
            'rating',
            'id',
            'is_private',
        )

        return Response(all_reviews)