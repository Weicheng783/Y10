from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import AdditionalUser
from api.models import Follow

from api.add_movie import add_movie


class RecommendedPeopleAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user = request.user
        current_recommended = User.objects.exclude(
            id__in=Follow.objects.filter(
                following=current_user.id
            ).values_list(
                "follower_id",
                flat=True
            )
        ).exclude(id=current_user.id).values(
            'id',
            'additionaluser__profile_picture',
            'first_name',
            'last_name',
            'username',
        )

        return Response(current_recommended)

         