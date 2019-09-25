from django.urls import path

from project.api.views import AllArtistsView, AllReleasesView

app_name = 'api'

urlpatterns = [
    path('artist/', AllArtistsView.as_view(), name='artist_list'),
    path('release/', AllReleasesView.as_view(), name='release_list')
]