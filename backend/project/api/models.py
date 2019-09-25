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


class Release(models.Model):
    name = models.CharField(
        verbose_name='Release Name',
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
        return str(self.name)

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
