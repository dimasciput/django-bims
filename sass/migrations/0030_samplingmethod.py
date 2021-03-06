# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sass', '0029_auto_20190121_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sampling_method', models.CharField(max_length=200)),
                ('effort_measure', models.CharField(blank=True, max_length=300, null=True)),
                ('normalisation_factor', models.IntegerField(blank=True, null=True)),
                ('factor_description', models.CharField(blank=True, max_length=300, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
