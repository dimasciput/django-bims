# Generated by Django 4.2.8 on 2024-06-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0405_sitesetting_park_wfs_attribute_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CITESListingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appendix', models.CharField(choices=[('I', 'Appendix I'), ('II', 'Appendix II'), ('III', 'Appendix III')], max_length=3)),
                ('annotation', models.TextField()),
                ('effective_at', models.DateField()),
                ('taxonomy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cites_listing_infos', to='bims.taxonomy')),
            ],
        ),
    ]