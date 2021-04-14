from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import Follow

class UnfollowAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user_1 = request.user

        if(User.objects.filter(username=request.data['username']).count() != 1):
            return Response({
                "message": "no such user!"
            })
        
        user_2 = User.objects.get(username=request.data['username'])

        if(Follow.objects.filter(following=user_1, follower=user_2).count() != 1):
            return Response({
                "message": "you don\'t follow this user!"
            })
        
        current_follow_relation = Follow.objects.get(
            following=user_1,
            follower=user_2
        )

        print(current_follow_relation)

        current_follow_relation.delete()
        return Response({
            "message": "user unfollowed!"
        })
