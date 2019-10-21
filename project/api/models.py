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


class Vendor(models.Model):
    name = models.CharField(
        verbose_name='Vendor',
        max_length=150,
        blank=True,
        null=True
    )   


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


class ProductVariant(models.Model):
    product_id = models.CharField(
        verbose_name='UPC/SKU',
        max_length=15,
        blank=True,
        null=True,
    )
    description = models.CharField(
        verbose_name='Description',
        max_length=100,
        blank=True,
        null=True,
    )
    price = models.FloatField(
        verbose_name='Price',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.description


class Product(models.Model):
    name = models.CharField(
        verbose_name='Product',
        max_length=100,
        blank=True,
        null=True,
    )
    product_variant = models.ForeignKey(
        verbose_name='Variant',
        related_name='Products',
        to=ProductVariant,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    artist = models.ManyToManyField('Artist', blank=True)
    release = models.ManyToManyField('Release', blank=True)
    vendor = models.ManyToManyField('Vendor', blank=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    description = models.CharField(
        verbose_name='Description',
        max_length=200,
        blank=True,
        null=True
    )
    amount = models.FloatField(
        verbose_name='Amount',
        blank=True,
        null=True,
    )
    source = models.ManyToManyField('IncomeSource', blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    release = models.ManyToManyField('Release', blank=True)
    product = models.ManyToManyField('Product', blank=True) 
    
    def __str__(self):
        return self.description


class Expense(models.Model):
    description = models.CharField(
        verbose_name='Description',
        max_length=200,
        blank=True,
        null=True,
    )
    amount = models.FloatField(
        verbose_name='Amount',
        blank=True,
        null=True,
    )
    vendor = models.ManyToManyField('Vendor', blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    release = models.ManyToManyField('Release', blank=True) 
    product = models.ManyToManyField('Product', blank=True) 
    
    def __str__(self):
        return self.description
