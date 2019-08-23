from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from serializers import ArtistSerializer
from models import Artist


class AllArtistsView(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
