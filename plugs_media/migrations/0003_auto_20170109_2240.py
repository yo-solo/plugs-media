# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-09 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('plugs_media', '0002_auto_20170107_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='media',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
