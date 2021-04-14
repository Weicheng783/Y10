from django.contrib import admin
from api.models import Follow
from api.models import AdditionalUser
from api.models import Review
from api.models import WatchList
from api.models import Movie
from api.models import Favourites


# Register your models here.
admin.site.register(Follow)
admin.site.register(AdditionalUser)
admin.site.register(Review)
admin.site.register(WatchList)
admin.site.register(Movie)
admin.site.register(Favourites)