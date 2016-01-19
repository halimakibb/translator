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
                          is_superuser = True,
                          is_staff = True,
                          is_active = True,
                          **kwargs
        )
        user.set_password(password)
        user.save()
        return user     

class User(AbstractBaseUser, PermissionsMixin):
    JOB_CHOICES = (("CL", "Client"),
                   ("MG", "Manager"),
                    ("TR", "Translator"),)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']
    email = models.EmailField(default = 'xx@xx.com', unique = True)
    name = models.CharField(max_length = 20, unique = True)
    job = models.CharField(max_length = 2,
                           choices = JOB_CHOICES,
                           default = "TR")
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    
    objects = UserManager()
    
class OriginalManager(models.Manager):
    def create_article(self, title, body, word_count, price):
        article = self.create(title = title, body = body, word_count=word_count, price=price)

        return article
    
class OriginalArticle(models.Model):
    title = models.TextField()
    body = models.TextField()
    published = models.DateField(default = date.today, editable = False)
    updated = models.DateField(default = date.today, editable = False)
    manager = models.ForeignKey(User, blank = True, null = True, default = None)
    word_count = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    is_assigned = models.BooleanField(default = False)
    is_translated = models.BooleanField(default = False)
    
    objects = OriginalManager()
    
    def __unicode__(self):
        return self.title
    
class TranslatedManager(models.Manager):
    def create_article(self, origin, translator):
        article = self.create(origin = origin, translator = translator)
        return article
    
class TranslatedArticle(models.Model):
    origin = models.ForeignKey(OriginalArticle, editable = False)
    title = models.TextField(default = '')
    body = models.TextField(default = '')
    published = models.DateField(default = date.today, editable = False)
    updated = models.DateField(default = date.today, editable = False)
    translator = models.ForeignKey(User)
    is_translated = models.BooleanField(default = False)
    is_checked = models.BooleanField(default = False)
    
    objects = TranslatedManager()
    
    def __unicode__(self):
        return self.origin.title