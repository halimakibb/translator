# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0028_auto_20160119_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalarticle',
            name='original_language',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_original_language', to='cat.Language'),
        ),
        migrations.AddField(
            model_name='originalarticle',
            name='target_language',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_target_language', to='cat.Language'),
        ),
        migrations.AddField(
            model_name='translatedarticle',
            name='original_language',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translate_original_language', to='cat.Language'),
        ),
        migrations.AddField(
            model_name='translatedarticle',
            name='target_language',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translate_target_language', to='cat.Language'),
        ),
        migrations.AddField(
            model_name='user',
            name='original_language',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_original_language', to='cat.Language'),
        ),
        migrations.AddField(
            model_name='user',
            name='target_language',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_target_language', to='cat.Language'),
        ),
    ]
