# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 10:22
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0010_merge_20180625_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundary',
            name='centroid',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
