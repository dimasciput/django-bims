# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-03 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0077_auto_20181203_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxonomy',
            options={'verbose_name': 'Taxonomy', 'verbose_name_plural': 'Taxonomies'},
        ),
    ]
