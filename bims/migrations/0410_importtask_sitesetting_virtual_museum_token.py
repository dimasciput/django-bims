# Generated by Django 4.2.8 on 2024-06-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0409_taxontag_customtaggedtaxonomy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(choices=[('odonates', 'Odonates'), ('anurans', 'Anurans')], max_length=20)),
                ('start_index', models.IntegerField(default=0)),
                ('total_records', models.IntegerField()),
                ('in_progress', models.BooleanField(default=True)),
                ('celery_task_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('log_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='virtual_museum_token',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]