from django.urls import path

from project.api.views import (
    AllArtistsView,
    CreateArtistView, 
    AllReleasesView,
    CreateReleaseView,
    ReleaseByCatNumView,
    ArtistByNiceNameView
)
    

app_name = 'api'

urlpatterns = [
    path('artist/', AllArtistsView.as_view(), name='artist_list'),
    path('artist/new/', CreateArtistView.as_view(), name='new_artist'),
    path('artist/<:pk>/', ArtistByNiceNameView.as_view(), name='artist_by_slug'),

    path('release/', AllReleasesView.as_view(), name='release_list'),
    path('release/new/', CreateReleaseView.as_view(), name='new_release'),
    path('release/<int:pk>/', ReleaseByCatNumView.as_view(), name='release_by_id')
]