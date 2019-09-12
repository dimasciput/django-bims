# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-12 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bims', '0171_sitesetting_default_data_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioTaxon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio_taxon_name', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('taxonomy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bims.Taxonomy')),
            ],
        ),
    ]
