from django.urls import path

from project.api.views import AllArtistsView

app_name = 'api'

urlpatterns = [
    path('artist/', AllArtistsView.as_view(), name='artist_list'),
]