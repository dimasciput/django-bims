# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-02 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0057_auto_20181102_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biologicalcollectionrecord',
            old_name='message',
            new_name='validation_message',
        ),
    ]
