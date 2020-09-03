# Generated by Django 2.2.12 on 2020-09-03 05:50

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('banner', models.ImageField(upload_to='banner')),
                ('title', models.TextField(blank=True, default='', help_text='Title of the carousel')),
                ('description', models.TextField(blank=True, default='', help_text='Paragraph inside carousel', verbose_name='Paragraph')),
                ('text_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Color of the text inside carousel', max_length=18)),
                ('background_color_overlay', colorfield.fields.ColorField(default='#FFFFFF', help_text='Background color overlay behind the text', max_length=18)),
                ('background_overlay_opacity', models.PositiveIntegerField(default=0, help_text='Opacity of the background overlay, in percentage', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Will not appear anywhere', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Will not appear anywhere', null=True)),
                ('site_name', models.CharField(blank=True, default='', help_text='The name of the site', max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='site_logo')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('main_accent_color', colorfield.fields.ColorField(default='#18A090', max_length=18)),
                ('secondary_accent_color', colorfield.fields.ColorField(default='#DBAF00', max_length=18)),
                ('main_button_text_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('navbar_background_color', colorfield.fields.ColorField(default='#343a40', max_length=18)),
                ('navbar_text_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('is_enabled', models.BooleanField(default=True)),
                ('carousels', models.ManyToManyField(blank=True, help_text='Carousels that will appear on the landing page', null=True, to='bims_theme.CarouselHeader')),
            ],
            options={
                'verbose_name_plural': 'Custom Themes',
                'ordering': ('date',),
            },
        ),
    ]
