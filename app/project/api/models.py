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
    known_balance= models.DecimalField(
        verbose_name='Current Balance',
        max_digits=10,
        decimal_places=2,
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


class Income(models.Model):
    description = models.CharField(
        verbose_name='Description',
        max_length=200,
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        verbose_name='Amount',
        max_digits=10,
        decimal_places=2,
    )
    source = models.ManyToManyField('Source')
    vendor = models.ManyToManyField('Vendor')
    artist = models.ManyToManyField('Artist')
    album = models.ManyToManyField('Album')

    def __str__(self):
        return self.description


class Expense(models.Model):
    description = models.CharField(
        verbose_name='Description',
        max_length=200,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        verbose_name='Amount',
        max_digits=10,
        decimal_places=2,
    )
    source = models.ManyToManyField('Source')
    vendor = models.ManyToManyField('Vendor')
    artist = models.ManyToManyField('Artist')
    album = models.ManyToManyField('Album')  
    
    def __str__(self):
        return self.description