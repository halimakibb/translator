# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0004_remove_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
