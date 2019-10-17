from rest_framework import serializers
from .models import Artist, Release


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist', 'artist_nice_name', 'artist_location', 'artist_bio','artist_type', 'artist_contact', 'status','id', 'image' ]



class ReleaseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Release
        fields = ['row', 'cat_num', 'fk_artist', 'release_title', 'release_formats', 'release_date', 'artist_nice_name', 'tracklisting', 'bio', 'ffo', 'target_markets', 'upc', 'status', 'mediaplayer_html', 'artist', 'image', 'id']
