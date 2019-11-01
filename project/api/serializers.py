from rest_framework import serializers
from .models import Artist, Release, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Track
        fields = ['title', 'release']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist', 'artist_nice_name', 'artist_location', 'artist_bio','artist_type', 'artist_contact', 'status','id', 'image' ]


class ArtistNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist']


class ReleaseSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    artist = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        if instance.tracks:
            return instance.tracks

    def get_artist(self, instance):
        if instance.artist:
            return instance.artist.values_list('artist', flat=True)

    class Meta: 
        model = Release
        fields = ['row', 'cat_num', 'fk_artist', 'release_title', 'release_formats', 'release_date', 'artist_nice_name', 'tracks', 'bio', 'ffo', 'target_markets', 'upc', 'status', 'mediaplayer_html', 'artist', 'image', 'id']
