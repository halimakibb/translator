# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 03:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0012_auto_20160115_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatedarticle',
            name='translator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
