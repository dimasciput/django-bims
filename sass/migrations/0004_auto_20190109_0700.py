# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 07:00
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sass', '0003_auto_20190109_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitevisit',
            name='additional_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]
