from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

from project.api.serializers import (
    ArtistSerializer, 
    ReleaseSerializer, 
    ArtistNiceNameSerializer,
    ArtistNameSerializer,
    ReleaseCatNumSerializer
)
from project.api.models import Artist, Release

User = get_user_model()

class AllArtistsView(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class AllArtistsNiceNameView(ListAPIView):
    serializer_class = ArtistNiceNameSerializer
    queryset = Artist.objects.all()


class ArtistByNiceNameView(ListAPIView):
    """
    api/artists/<str:nice_name>/
    GET: access artist by nice name passed in url
    """
    serializer_class = ArtistSerializer

    def get_queryset(self, *args, **kwargs):
        nice_name = self.kwargs['artist_nice_name']
        return Artist.objects.filter(artist_nice_name=nice_name)

class CreateArtistView(CreateAPIView):
    """
    api/artists/new/
    POST: user can create a new Artist entry by sending post data
    """
    serializer_class = ArtistSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()

    def perform_create(self, serializer):
        return serializer.save()


class AllReleasesView(ListAPIView):
    """
    api/releases/
    GET: See all releases 
    """
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()


class AllReleasesCatNum(ListAPIView):
    """
    api/releases/check/
    GET: List cat_nums of all releases
    """
    serializer_class = ReleaseCatNumSerializer
    queryset = Release.objects.all()

class AllReleasesByArtist(ListAPIView):
    """
    api/releases/<str:nice_name>/
    GET: List all releases by the artist nice name passed in url
    """
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()

    def get_queryset(self, *args, **kwargs):
        nice_name = self.kwargs['artist_nice_name']
        return Release.objects.filter(artist_nice_name=nice_name)

class CreateReleaseView(CreateAPIView):
    """
    api/release/new/
    POST: user can create a new Release entry by sending post data
    """
    serializer_class = ReleaseSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Release.objects.all()

    def perform_create(self, serializer):
        return serializer.save()


class ReleaseByCatNumView(ListAPIView):
    """
    api/release/cat_num/
    GET: access release by catalog number passed in url
    """
    serializer_class = ReleaseSerializer
    
    def get_queryset(self, *args, **kwargs):
        cat_num = self.kwargs['cat_num']
        return Release.objects.filter(cat_num=cat_num)


