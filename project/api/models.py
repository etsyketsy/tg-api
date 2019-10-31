from django.db import models
from django.conf import settings


class ArtistLink(models.Model):
    artist_nice_name = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=240, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    artist = models.ManyToManyField('Artist', related_name='links', blank=True)

    class Meta:
        db_table = 'artist_links'

    def __str__(self):
        return (self.artist_nice_name + '/ ' + self.name)


class Artist(models.Model):
    artist  = models.CharField(max_length=50)
    artist_location = models.CharField(max_length=50, blank=True, null=True)
    artist_bio = models.TextField(blank=True, null=True)
    artist_nice_name = models.CharField(max_length=50, blank=True, null=True)
    artist_type = models.CharField(max_length=20)
    artist_contact = models.CharField(max_length=50)
    status = models.CharField(max_length=12)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='artists', blank=True, null=True)

    class Meta:
        db_table = 'artists'
    
    def __str__(self):
        return self.artist


class ReleaseLink(models.Model):
    cat_num = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=240, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    release = models.ManyToManyField('Release', related_name='links', blank=True)
    
    class Meta:
        db_table = 'release_links'

    def __str__(self):
        return (self.cat_num + "/ " + self.name)

class Release(models.Model):
    row = models.CharField(max_length=3)
    cat_num = models.CharField(max_length=6)
    fk_artist = models.CharField(max_length=50, blank=True)  # Field name made lowercase.
    release_title = models.CharField(max_length=80, blank=True, null=True)
    release_formats = models.CharField(max_length=24, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    artist_nice_name = models.CharField(max_length=50)
    tracklisting = models.TextField()
    bio = models.TextField(blank=True, null=True)
    ffo = models.TextField(blank=True, null=True)
    target_markets = models.TextField(blank=True)
    upc = models.CharField(max_length=13, blank=True)
    status = models.CharField(max_length=20)
    mediaplayer_html = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    artist = models.ManyToManyField('Artist', related_name='releases', blank=True)
    image = models.ImageField(upload_to='releases/', blank=True, null=True)
    
    class Meta:
        db_table = 'releases'

    def __str__(self):
        return self.cat_num


class Track(models.Model):
    title = models.CharField(max_length=150)
    release = models.ForeignKey(
        related_name='Tracks', 
        to=Release, 
        on_delete=models.SET_NULL,
        null=True
    )

    def __St__(self):
        return self.title