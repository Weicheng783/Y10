from django.contrib import admin
from api.models import Follow
from api.models import AdditionalUser
from api.models import Review


# Register your models here.
admin.site.register(Follow)
admin.site.register(AdditionalUser)
admin.site.register(Review)
