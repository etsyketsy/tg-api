from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from project.api.serializers import ArtistSerializer
from project.api.models import Artist


class AllArtistsView(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
