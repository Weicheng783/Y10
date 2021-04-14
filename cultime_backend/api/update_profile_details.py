from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from api.models import AdditionalUser


class UpdateProfileDetailsAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user = request.user

        current_additional_user = AdditionalUser.objects.get(
            user=current_user
        )

        return Response(
            {
                "first_name": current_user.first_name,
                "last_name": current_user.last_name,
                "user_bio": current_additional_user.user_bio
            }
        )
    def post(self, request):
        print("HERE!")
        current_user = request.user
        current_user.first_name = request.data['new_first_name']
        current_user.last_name = request.data['new_last_name']

        current_user.save()

        current_additional_user = AdditionalUser.objects.get(
            user=current_user
        )
        current_additional_user.user_bio = request.data['new_user_bio']

        current_additional_user.save()

        return Response({
            "message": "Changed!",
        })

