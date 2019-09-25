from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

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