# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0071_taxonidentifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonidentifier',
            name='rank',
            field=models.CharField(blank=True, choices=[(b'CLASS', b'Class'), (b'DOMAIN', b'Domain'), (b'FAMILY', b'Family'), (b'GENUS', b'Genus'), (b'KINGDOM', b'Kingdom'), (b'LIFE', b'Life'), (b'ORDER', b'Order'), (b'PHYLUM', b'Phylum'), (b'SPECIES', b'Species')], max_length=50, verbose_name=b'Taxonomic Rank'),
        ),
        migrations.AlterField(
            model_name='taxonidentifier',
            name='taxonomic_status',
            field=models.CharField(blank=True, choices=[(b'ACCEPTED', b'Accepted'), (b'DOUBTFUL', b'Doubtful'), (b'HETEROTYPIC_SYNONYM', b'Heterotypic Synonym'), (b'HOMOTYPIC_SYNONYM', b'Homotypic Synonym'), (b'MISAPPLIED', b'Misapplied'), (b'PROPARTE_SYNONYM', b'Proparte Synonym'), (b'SYNONYM', b'Synonym')], max_length=50, verbose_name=b'Taxonomic Status'),
        ),
    ]
