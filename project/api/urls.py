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
    path('artist/<str:artist_nice_name>/', ArtistByNiceNameView.as_view(), name='artist_by_nice_name'),

    path('release/', AllReleasesView.as_view(), name='release_list'),
    path('release/new/', CreateReleaseView.as_view(), name='new_release'),
    path('release/<str:cat_num>/', ReleaseByCatNumView.as_view(), name='release_by_id')
]