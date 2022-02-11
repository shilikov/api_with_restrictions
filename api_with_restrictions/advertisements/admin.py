from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advertisement, AdvertisementAdmin)

