# Generated by Django 2.0.3 on 2019-10-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191008_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='artists'),
        ),
        migrations.AddField(
            model_name='release',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='releases/'),
        ),
    ]