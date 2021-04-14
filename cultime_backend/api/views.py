from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import Follow
from api.models import AdditionalUser

# Serializers we need
from .serializers import RegisterSerializer, UserSerializer, FollowSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()

        additional_user = AdditionalUser(
            user=new_user
        )
        additional_user.save()

        return Response({
            "message": "User Created Successfully. Now perform Login to get your token",
        })


class FollowingAPI(generics.GenericAPIView):
    """
    FollowingAPI returns list of users that the logged user is following on Cultime
    It needs that the user is authenticated with valid JWT token.
    No things in body are needed to be sent, the user is automatically generated from the JWT token

    TO DO: UNFOLLOW API, DON'T ALLOW MULTIPLE FOLLOWS IN DATABASE
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        "The get request returns all the users followed by the current logged user"
        user = request.user
        following = Follow.objects.filter(
            following=user.id
        ).prefetch_related(
            'follower'
        ).values(
            'follower__first_name',
            'follower__last_name',
            'follower__additionaluser__profile_picture',
            'follower__id',
            'follower__username',
        )

        return Response(following)

    def post(self, request):
        "Given username: ... in the body in adds follow instruction"
        user1 = request.user

        # Checks if user with specific username exists
        # Check how we can send this as error instead of response

        try:
            user2 = User.objects.get(username=request.data['username'])
        except:
            return Response({
                "error": "No user with such username",
            })
        
        new_follow_relation = Follow(following = user1, follower = user2)

        if(Follow.objects.filter(following = user1, follower = user2).count() != 0):
            return Response({
                "message": "You already follow that person!",
            })

        new_follow_relation.save()

        return Response({
            "message": "New follow added successfully",
        })


class TestAPI(generics.GenericAPIView):
    """
    Test API call just to ensure that we connect with the backend.
    """
    def get(self, request):
        return Response({
            "message": "Successful message",
        })