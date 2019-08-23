from django.urls import path
from views import .


urlpatterns = [
    path('artist/', AllArtistView.as_view(), name='artist_list'),
]