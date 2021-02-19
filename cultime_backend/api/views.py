from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import Follow


# Serializers we need
from .serializers import RegisterSerializer, UserSerializer, FollowSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
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
        following = Follow.objects.filter(following=user.id).prefetch_related('following')
        serializer = FollowSerializer(following, many=True)
        return Response(serializer.data)

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
