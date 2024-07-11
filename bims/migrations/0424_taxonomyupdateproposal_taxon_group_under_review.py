# Generated by Django 4.2.11 on 2024-07-10 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0423_remove_taxonomyupdateproposal_taxonomy_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonomyupdateproposal',
            name='taxon_group_under_review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxon_group_under_review', to='bims.taxongroup', verbose_name='Taxon Group Under Review'),
        ),
    ]