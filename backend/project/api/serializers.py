from rest_framework import serializers
from .models import Artist, Release


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'tag']

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Release
        fields = ['name', 'artist', 'release_number']
