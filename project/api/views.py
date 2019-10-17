from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView,     RetrieveAPIView 

from project.api.serializers import ArtistSerializer, ReleaseSerializer
from project.api.models import Artist, Release

User = get_user_model()

class AllArtistsView(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class CreateArtistView(CreateAPIView):
    """
    api/artist/new/
    POST: user can create a new Artist entry by sending post data
    """
    serializer_class = ArtistSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()

    def perform_create(self, serializer):
        return serializer.save()


class AllReleasesView(ListAPIView):
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()


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


class ReleaseByCatNumView(RetrieveAPIView):
    """
    api/release/cat_num/
    GET: access release by catalog number passed in url
    *** Note that currently cat_num aligns with PK/ID. 
    This will need to be adjusted to control for misalignments ***
    """
    serializer_class = ReleaseSerializer
    
    def get_queryset(self):
        raw_num = str(self.kwargs['pk'])
        cat_num = 'TG-0'+raw_num
        return Release.objects.filter(cat_num=cat_num)


class ArtistByNiceNameView(ListAPIView):
    """
    api/artist/<str:nice_name>/
    GET: access artist by nice name passed in url
    """
    serializer_class = ArtistSerializer

    def get_queryset(self, *args, **kwargs):
        nice_name = self.kwargs['artist_nice_name']
        return Artist.objects.filter(artist_nice_name=nice_name)
