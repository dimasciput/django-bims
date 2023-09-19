# Generated by Django 4.1.10 on 2023-08-22 02:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bims', '0341_remove_bimsdocument_profile_locationsite_wetland_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biologicalcollectionrecord',
            name='ecosystem_type',
            field=models.CharField(blank=True, choices=[('River', 'River'), ('Wetland', 'Wetland'), ('Open waterbody', 'Open waterbody')], default='', max_length=128, null=True),
     ), ]
