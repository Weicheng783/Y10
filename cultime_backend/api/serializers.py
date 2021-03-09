from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from api.models import Follow
from api.models import Movie
from api.models import WatchList
from api.models import Review
from api.models import AdditionalUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'password': { 'write_only': True },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'id',
        )


class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer()

    class Meta:
        model = Follow
        fields = ('follower',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = WatchList
        fields = ('movie',)


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    author = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class AdditionalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalUser
        fields = '__all__'