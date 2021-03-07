from django.contrib import admin
from api.models import Follow
from api.models import AdditionalUser


# Register your models here.
admin.site.register(Follow)
admin.site.register(AdditionalUser)
