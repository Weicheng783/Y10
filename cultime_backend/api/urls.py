from django.urls import include, path
from rest_framework import routers
from .views import TestAPI, RegisterAPI

urlpatterns = [
    path('testapi/', TestAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
]


