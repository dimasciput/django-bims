# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-02 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0148_auto_20190630_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='category',
            field=models.CharField(blank=True, choices=[(b'alien', b'Non-Native'), (b'indigenous', b'Native')], max_length=50, null=True),
        ),
    ]