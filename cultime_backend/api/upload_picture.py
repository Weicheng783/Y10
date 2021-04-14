from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from api.models import AdditionalUser

class UploadPictureAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        x = AdditionalUser.objects.get(
            user=request.user
        )
        x.profile_picture = request.data['profile_picture']
        x.save()
        print(x)
        return Response({"message": "here"})
    
    def get(self, request):
        current_user = request.user
        current_picture = AdditionalUser.objects.filter(
            user=current_user,
        ).values(
            'profile_picture'
        )
        return Response(current_picture)

