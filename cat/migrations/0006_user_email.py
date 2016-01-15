# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0005_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='xx@xx.com', max_length=254, unique=True),
        ),
    ]
