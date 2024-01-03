# Generated by Django 4.1.10 on 2023-12-19 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
        ('bims', '0371_biologicalcollectionrecord_source_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchprocess',
            name='site',
            field=models.ForeignKey(blank=True, help_text='The site this record is associated with.', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Associated Site'),
        ),
    ]