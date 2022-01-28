# Generated by Django 2.2.16 on 2022-01-26 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0298_auto_20220124_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='biotope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bims.Biotope'),
        ),
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='specific_biotope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specific_biotope', to='bims.Biotope'),
        ),
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='substratum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biotope_substratum', to='bims.Biotope'),
        ),
    ]