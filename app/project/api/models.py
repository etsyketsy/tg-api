from django.db import models
from django.conf import settings


class Artist(models.Model):
    name = models.CharField(
        verbose_name='Artist Name',
        max_length=150,
        blank=False,
        null=False,
    )
    tag = models.CharField(
        verbose_name='Artist Tag',
        max_length=5,
        blank=True,
        null=True
    )
    current_balance = models.IntegerField(
        blank=True,
        null=True,
        # Update to a calculated field later 
    )

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    name = models.CharField(
        verbose_name='Album Name',
        max_length=150,
        blank=True,
        null=True,
    )
    artist = models.ManyToManyField('Artist')
    release_number = models.IntegerField(
        verbose_name='Release Number',
        unique=True,
        primary_key=True
    )
    release_date = models.DateField(
        verbose_name='Release Date',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(
        verbose_name='Vendor',
        max_length=150,
        blank=True,
        null=True,
    )   

    def __str__(self):
        return self.name

        
class Source(models.Model):
    name = models.CharField(
        verbose_name='Source',
        max_length=150,
        blank=True,
        null=True,
    )  

    def __str__(self):
        return self.name