from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from project.api.serializers import ArtistSerializer, ReleaseSerializer
from project.api.models import Artist, Release


class AllArtistsView(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class AllReleasesView(ListAPIView):
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()