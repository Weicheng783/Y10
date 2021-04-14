from django.urls import include, path
from rest_framework import routers
from .views import TestAPI, RegisterAPI, FollowingAPI
from .movie_search import MovieSearchAPI
from .reviews import ReviewsAPI
from .watchlist import WatchListAPI
from .watchlist import DeleteWatchListElementAPI
from .upload_picture import UploadPictureAPI
from .personal_reviews import PersonalReviewsAPI
from .reviews import RemoveReviewAPI
from .favourite_movies import FavouritesAPI
from .favourite_movies import RemoveFavouriteAPI
from .recommended_people import RecommendedPeopleAPI

from .profile_info import ProfileInfoAPI
from .trending_movies import TrendingMoviesAPI

from .recommend_movies import RecommendedMoviesAPI

from .unfollow import UnfollowAPI

from .update_profile_details import UpdateProfileDetailsAPI

urlpatterns = [
    path('testapi/', TestAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('searchmovie/', MovieSearchAPI.as_view()),

    # Relations with other peoples APIs
    path('following/', FollowingAPI.as_view()),
    path('recommended/', RecommendedPeopleAPI.as_view()),
    path('unfollow/', UnfollowAPI.as_view()),

    # Review APIs
    path('reviews/', ReviewsAPI.as_view()),
    path('personal_reviews/', PersonalReviewsAPI.as_view()),
    path('remove_review/', RemoveReviewAPI.as_view()),

    # Favourites APIs
    path('favourites/', FavouritesAPI.as_view()),
    path('remove_favourites/', RemoveFavouriteAPI.as_view()),

    # WatchList APIs
    path('watchlist/', WatchListAPI.as_view()),
    path('deletewatchlist/', DeleteWatchListElementAPI.as_view()),

    path('uploadphoto/', UploadPictureAPI.as_view()),

    # Get Public User Details API
    path('profile_info/', ProfileInfoAPI.as_view()),
    path('update_profile_details/', UpdateProfileDetailsAPI.as_view()),

    # Trending Movies
    path('trending/', TrendingMoviesAPI.as_view()),
    path('recommendmovies/', RecommendedMoviesAPI.as_view()),
]
