# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
