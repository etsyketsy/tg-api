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
        null=True
    )   

    def __str__(self):
        return self.name


class IncomeSource(models.Model):
    DIGITAL = 'Digital'
    PHYSICAL = 'Physical'
    OTHER = 'Other'
    INCOME_TYPE_CHOICES = (
            (DIGITAL, DIGITAL),
            (PHYSICAL, PHYSICAL),
            (OTHER, OTHER),
        )
    name = models.CharField(
        verbose_name='Income Type',
        max_length=150,
        choices=INCOME_TYPE_CHOICES,
        blank=True,
        null=True
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
    source = models.ManyToManyField('IncomeSource', blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    album = models.ManyToManyField('Album', blank=True)
    
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
    vendor = models.ManyToManyField('Vendor', blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    album = models.ManyToManyField('Album', blank=True)  
    
    def __str__(self):
        return self.description