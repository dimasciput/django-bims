# Generated by Django 4.2.8 on 2024-02-04 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bims', '0379_locationcontextfilter_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvestsession',
            name='source_site',
            field=models.ForeignKey(blank=True, help_text='The site this record is associated with.', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='Associated Site'),
        ),
    ]