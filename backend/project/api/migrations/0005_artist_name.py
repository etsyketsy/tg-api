# Generated by Django 2.2.4 on 2019-08-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190820_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(default='TBD', max_length=150, verbose_name='Artist Name'),
            preserve_default=False,
        ),
    ]
