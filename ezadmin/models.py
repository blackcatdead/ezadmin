# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar= models.ImageField(blank=True, null=True, upload_to='users')
    description = models.TextField(blank=True, null=True)
    # image_thumbnail = ImageSpecField(source='avatar', processors=[ResizeToFill(200,200)], format='JPEG', options={'quality':60})

    def __str__(self):
		return str(self.username)+' - '+self.first_name+' '+self.last_name

