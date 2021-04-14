from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from api.models import Movie
from api.models import Review
from api.models import AdditionalUser

from api.add_movie import add_movie

from api.serializers import ReviewSerializer
from api.serializers import AdditionalUserSerializer

class ReviewsAPI(generics.GenericAPIView):
    """
        Class that implements the functionalities to insert new review
        and get all the reviews in the database
    """
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        "The post request adds new review in the database"
        current_user = request.user
        new_movie_id = request.data['movie_id']
        current_content = request.data['content']
        current_rating = request.data['rating']
        current_is_private = request.data['is_private']

        add_movie(new_movie_id) 

        current_movie = Movie.objects.get(movie_id=new_movie_id)

        if(len(current_content) == 0):
            return Response({"error": "Please add some description!"})

        new_review_element = Review(
            author=current_user,
            movie=current_movie,
            content=current_content,
            rating=current_rating,
            is_private=current_is_private,
        )
        
        new_review_element.save()
        return Response({"message": "added new review"})


    def get(self, request):
        "The get requests gets list of all the reviews of users current person follows."
        current_user = request.user
        all_reviews = Review.objects.filter(
            author__follower__following=current_user,
            is_private=False
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
        )

        return Response(all_reviews)


class RemoveReviewAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        current_user = request.user
        review_id = request.data['id']

        if(Review.objects.filter(id=review_id).count() != 1):
            return Response({"Error": "No such review!"})
        
        current_review_object = Review.objects.filter(
            id=review_id, 
            author=current_user
        )

        if(current_review_object.count() != 1):
            return Response({"Error": "Invalid API call!"})
        
        current_review_object.delete()
        return Response({"Message": "Review successfully deleted!"})