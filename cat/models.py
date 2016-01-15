from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import date
from django.db import models

from time import time
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, password, **kwargs):
        user = self.model(
                          name = name,
                          email = self.normalize_email(email),
                          is_manager = False,
                          is_active = True,
                          **kwargs
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, name, password, **kwargs):
        user = self.model(
                          name = name,
                          email = self.normalize_email(email),
                          is_manager = True,
                          is_superuser = True,
                          is_staff = True,
                          is_active = True,
                          **kwargs
        )
        user.set_password(password)
        user.save()
        return user     

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']
    email = models.EmailField(default = 'xx@xx.com', unique = True)
    name = models.CharField(max_length = 20, unique = True)
    is_manager = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    
    objects = UserManager()
    
class OriginalArticle(models.Model):
    title = models.TextField()
    body = models.TextField()
    published = models.DateField(default = date.today, editable = False)
    updated = models.DateField(default = date.today, editable = False)
    manager = models.ForeignKey(User, editable = False)
    is_translated = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.title

class TranslatedArticle(models.Model):
    origin = models.ForeignKey(OriginalArticle)
    title = models.TextField()
    body = models.TextField()
    published = models.DateField(default = date.today, editable = False)
    updated = models.DateField(default = date.today, editable = False)
    translator = models.ForeignKey(User, editable = False)
    is_finished = models.BooleanField(default = False)