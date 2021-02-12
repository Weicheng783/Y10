from django.shortcuts import render

# Generic API views
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response

# Serializers we need
from .serializers import RegisterSerializer, UserSerializer

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


class TestAPI(generics.GenericAPIView):
    """
    Test API call just to ensure that we connect with the backend.
    """
    def get(self, request):
        return Response({
            "message": "Successful message",
        })
