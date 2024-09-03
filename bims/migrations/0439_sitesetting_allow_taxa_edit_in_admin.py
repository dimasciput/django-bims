# Generated by Django 4.2.15 on 2024-09-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0438_taggroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='allow_taxa_edit_in_admin',
            field=models.BooleanField(default=False, help_text='Enable this to allow superusers to edit taxa directly from the admin popup in the taxa management page'),
        ),
    ]
