# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0024_auto_20160119_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
