from django.contrib import admin
from .models import Artist, Album, Vendor, Source


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Vendor)
admin.site.register(Source)