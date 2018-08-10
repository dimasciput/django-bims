# Generated by Django 2.0.6 on 2018-06-21 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bims', '0008_category_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('first_initial', models.CharField(blank=True, max_length=10, verbose_name='First Initial(s)')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='AuthorEntryRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(help_text='Author rank in entry authors sequence', verbose_name='Rank')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bims.Author')),
            ],
            options={
                'verbose_name': 'Author Entry Rank',
                'verbose_name_plural': 'Author Entry Ranks',
                'ordering': ('rank',),
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Short description')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('first_initial', models.CharField(blank=True, max_length=10, verbose_name='First Initial(s)')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Editor',
                'verbose_name_plural': 'Editors',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('article', 'Article'), ('book', 'Book'), ('booklet', 'Book (no publisher)'), ('conference', 'Conference'), ('inbook', 'Book chapter'), ('incollection', 'Book from a collection'), ('inproceedings', 'Conference proceedings article'), ('manual', 'Technical documentation'), ('mastersthesis', "Master's Thesis"), ('misc', 'Miscellaneous'), ('phdthesis', 'PhD Thesis'), ('proceedings', 'Conference proceedings'), ('techreport', 'Technical report'), ('unpublished', 'Unpublished work')], default='article', max_length=50, verbose_name='Entry type')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('publication_date', models.DateField(null=True, verbose_name='Publication date')),
                ('is_partial_publication_date', models.BooleanField(default=True, help_text='Check this if the publication date is incomplete (for example if only the year is valid)', verbose_name='Partial publication date?')),
                ('volume', models.CharField(blank=True, help_text='The volume of a journal or multi-volume book', max_length=50, verbose_name='Volume')),
                ('number', models.CharField(blank=True, help_text="The '(issue) number' of a journal, magazine, or tech-report, if applicable. (Most publications have a 'volume', but no 'number' field.)", max_length=50, verbose_name='Number')),
                ('pages', models.CharField(blank=True, help_text='Page numbers, separated either by commas or double-hyphens', max_length=50, verbose_name='Pages')),
                ('url', models.URLField(blank=True, help_text='The WWW address where to find this resource', verbose_name='URL')),
                ('doi', models.CharField(blank=True, help_text='Digital Object Identifier for this resource', max_length=100, verbose_name='DOI')),
                ('issn', models.CharField(blank=True, help_text='International Standard Serial Number', max_length=20, verbose_name='ISSN')),
                ('isbn', models.CharField(blank=True, help_text='International Standard Book Number', max_length=20, verbose_name='ISBN')),
                ('pmid', models.CharField(blank=True, help_text='Pubmed ID', max_length=20, verbose_name='PMID')),
                ('booktitle', models.CharField(blank=True, help_text='The title of the book, if only part of it is being cited', max_length=50, verbose_name='Book title')),
                ('edition', models.CharField(blank=True, help_text="The edition of a book, long form (such as 'First' or 'Second')", max_length=100, verbose_name='Edition')),
                ('chapter', models.CharField(blank=True, max_length=50, verbose_name='Chapter number')),
                ('school', models.CharField(blank=True, help_text='The school where the thesis was written', max_length=50, verbose_name='School')),
                ('organization', models.CharField(blank=True, help_text='The conference sponsor', max_length=50, verbose_name='Organization')),
                ('address', models.CharField(blank=True, help_text="Publisher's address (usually just the city, but can be the full address for lesser-known publishers)", max_length=250, verbose_name='Address')),
                ('annote', models.CharField(blank=True, help_text='An annotation for annotated bibliography styles (not typical)', max_length=250, verbose_name='Annote')),
                ('note', models.TextField(blank=True, help_text='Miscellaneous extra information', verbose_name='Note')),
                ('authors', models.ManyToManyField(related_name='entries', through='bims.AuthorEntryRank', to='bims.Author')),
                ('crossref', models.ManyToManyField(blank=True, related_name='_entry_crossref_+', to='bims.Entry')),
                ('editors', models.ManyToManyField(blank=True, related_name='entries', to='bims.Editor')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
                'ordering': ('-publication_date',),
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('abbreviation', models.CharField(blank=True, help_text='e.g. Proc Natl Acad Sci U S A', max_length=100, verbose_name='Entity abbreviation')),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journals',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('abbreviation', models.CharField(blank=True, help_text='e.g. Proc Natl Acad Sci U S A', max_length=100, verbose_name='Entity abbreviation')),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='bims.Journal'),
        ),
        migrations.AddField(
            model_name='entry',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='bims.Publisher'),
        ),
        migrations.AddField(
            model_name='collection',
            name='entries',
            field=models.ManyToManyField(related_name='collections', to='bims.Entry'),
        ),
        migrations.AddField(
            model_name='authorentryrank',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bims.Entry'),
        ),
    ]
