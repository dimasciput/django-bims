# Generated by Django 2.2.12 on 2021-05-21 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0289_remove_biologicalcollectionrecord_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxonImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_image', models.ImageField(blank=True, null=True, upload_to='taxon_images')),
                ('taxonomy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bims.Taxonomy')),
            ],
        ),
    ]