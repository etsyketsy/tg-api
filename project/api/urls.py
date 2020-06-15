from django.urls import path

from project.api.views import (
    AllArtistsView,
    CreateArtistView, 
    AllReleasesView,
    CreateReleaseView,
    ReleaseByCatNumView,
    ArtistByNiceNameView,
    AllArtistsNiceNameView,
    AllReleasesCatNum,
    AllReleasesByArtist
)
    

app_name = 'api'

urlpatterns = [
    # Artist endpoints
    path('artists/', AllArtistsView.as_view(), name='artist_list'),
    path('artists/new/', CreateArtistView.as_view(), name='new_artist'),
    path(
        'artists/check/', 
        AllArtistsNiceNameView.as_view(), 
        name='all_artist_nice_name'
    ),

    path(
        'artists/<str:artist_nice_name>/', 
        ArtistByNiceNameView.as_view(), 
        name='artist_by_nice_name'
    ),

    # Release endpoints
    path('releases/', AllReleasesView.as_view(), name='release_list'),
    path('releases/new/', CreateReleaseView.as_view(), name='new_release'),
    path(
        'releases/check/', 
        AllReleasesCatNum.as_view(), 
        name='all_releases_cat_nums'
    ),
    path(
        'releases/<str:cat_num>/', 
        ReleaseByCatNumView.as_view(), 
        name='release_by_id'
    ),
    path(
        'releases/artist/<str:artist_nice_name>/',
        AllReleasesByArtist.as_view(),
        name='releases_by_artist'),
]