# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-13 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0173_auto_20190913_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biologicalcollectionrecord',
            name='documents',
        ),
    ]
