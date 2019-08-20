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


