from django.urls import include, path
from rest_framework import routers
from .views import TestAPI, RegisterAPI, FollowingAPI
from .movie_search import MovieSearchAPI

urlpatterns = [
    path('testapi/', TestAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('following/', FollowingAPI.as_view()),
    path('searchmovie/', MovieSearchAPI.as_view()),
]


