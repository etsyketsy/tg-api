from django.urls import path

from project.api.views import (
    AllArtistsView,
    CreateArtistView, 
    AllReleasesView,
)
    

app_name = 'api'

urlpatterns = [
    path('artist/', AllArtistsView.as_view(), name='artist_list'),
    path('artist/new/', CreateArtistView.as_view(), name='new_artist'),

    path('release/', AllReleasesView.as_view(), name='release_list'),
]