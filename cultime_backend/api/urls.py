from django.urls import include, path
from rest_framework import routers
from .views import TestAPI, RegisterAPI, FollowingAPI
from .movie_search import MovieSearchAPI
from .reviews import ReviewsAPI
from .watchlist import WatchListAPI
from .watchlist import DeleteWatchListElementAPI
from .upload_picture import UploadPictureAPI

urlpatterns = [
    path('testapi/', TestAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('following/', FollowingAPI.as_view()),
    path('searchmovie/', MovieSearchAPI.as_view()),
    path('reviews/', ReviewsAPI.as_view()),
    path('watchlist/', WatchListAPI.as_view()),
    path('deletewatchlist/', DeleteWatchListElementAPI.as_view() ),
    path('uploadphoto/', UploadPictureAPI.as_view())
]


