# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='imagen',
            name='imageFile',
            field=models.ImageField(null=True, upload_to=b'images'),
        ),
        migrations.AddField(
            model_name='imagen',
            name='title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='imagen',
            name='type',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
