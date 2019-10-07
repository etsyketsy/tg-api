# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArtistLinks(models.Model):
    artist = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=240, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_links'


class Artists(models.Model):
    artist = models.CharField(primary_key=True, max_length=50)
    artist_location = models.CharField(max_length=50, blank=True, null=True)
    artist_bio = models.TextField(blank=True, null=True)
    artist_nice_name = models.CharField(max_length=50)
    artist_type = models.CharField(max_length=20)
    artist_contact = models.CharField(max_length=50)
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'artists'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class ReleaseLinks(models.Model):
    cat_num = models.CharField(max_length=6, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=240, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_links'


class Releases(models.Model):
    row = models.CharField(max_length=3)
    cat_num = models.CharField(primary_key=True, max_length=6)
    fk_artist = models.CharField(db_column='FK_artist', max_length=50)  # Field name made lowercase.
    release_title = models.CharField(max_length=80, blank=True, null=True)
    release_formats = models.CharField(max_length=24, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    artist_nice_name = models.CharField(max_length=50)
    tracklisting = models.TextField()
    bio = models.TextField()
    ffo = models.TextField()
    target_markets = models.TextField()
    upc = models.CharField(max_length=13)
    status = models.CharField(max_length=20)
    mediaplayer_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'releases'
