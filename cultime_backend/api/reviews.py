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
    
    """
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        "The post request adds new review in the database"
        current_user = request.user
        new_movie_id = request.data['movie_id']
        current_content = request.data['content']
        current_rating = request.data['rating']

        add_movie(new_movie_id) 

        current_movie = Movie.objects.get(movie_id=new_movie_id)

        if(len(current_content) == 0):
            return Response({"error": "Please add some description!"})

        new_review_element = Review(
            author=current_user,
            movie=current_movie,
            content=current_content,
            rating=current_rating
        )
        
        new_review_element.save()
        return Response({"message": "added new review"})


    def get(self, request):
        "The get requests gets list of all the reviews of users current person follows."
        current_user=request.user
        all_reviews = Review.objects.filter(author__follower__following=current_user).prefetch_related('author')

        serializer = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)
