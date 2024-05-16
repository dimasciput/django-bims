# Generated by Django 4.2.8 on 2024-05-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0400_taxonomyupdateproposal_taxon_group_under_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonomy',
            name='rank',
            field=models.CharField(blank=True, choices=[('SUBSPECIES', 'Sub Species'), ('SPECIES', 'Species'), ('GENUS', 'Genus'), ('FAMILY', 'Family'), ('SUPERFAMILY', 'Super Family'), ('ORDER', 'Order'), ('CLASS', 'Class'), ('SUBCLASS', 'Sub Class'), ('PHYLUM', 'Phylum'), ('SUBPHYLUM', 'SubPhylum'), ('KINGDOM', 'Kingdom'), ('DOMAIN', 'Domain'), ('SUBORDER', 'Sub Order'), ('INFRAORDER', 'Infra Order'), ('SUBFAMILY', 'Sub Family'), ('VARIETY', 'Variety'), ('FORMA', 'Forma')], max_length=50, verbose_name='Taxonomic Rank'),
        ),
    ]