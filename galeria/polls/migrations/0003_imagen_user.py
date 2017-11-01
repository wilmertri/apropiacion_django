# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_auto_20170817_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
