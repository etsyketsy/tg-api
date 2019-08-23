from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistfields = ['name', 'tag']
