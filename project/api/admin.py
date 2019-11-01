from django.contrib import admin
from .models import Artist, ArtistLink, Release, ReleaseLink, Track

admin.site.register(Artist)
admin.site.register(ArtistLink)
admin.site.register(Release)
admin.site.register(ReleaseLink)
admin.site.register(Track)