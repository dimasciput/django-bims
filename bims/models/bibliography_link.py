from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from td_biblio.models.bibliography import Entry
from bims.models import (
    BiologicalCollectionRecord,
    LocationSite
)


class BibliographyLink(models.Model):
    """Relationship between bibliography models and collection/site"""

    bibliography_entry = models.ForeignKey(
            Entry,
            blank=False,
            null=False
    )

    biological_collection = models.ForeignKey(
            BiologicalCollectionRecord,
            blank=True,
            null=True,
            on_delete=models.SET_NULL
    )

    location_site = models.ForeignKey(
            LocationSite,
            blank=True,
            null=True,
            on_delete=models.SET_NULL
    )

    def _get_bibliography_title(self):
        """
        Get current bibliography title
        """
        return self.bibliography_entry.title

    bibliography_entry_title = property(_get_bibliography_title)

    def _get_relation(self):
        """
        Get this model species name or location site name
        """
        relation_name = ''
        admin_url = '/admin/bims/'

        if self.biological_collection:
            admin_url += 'biologicalcollectionrecord/%s' % \
                         self.biological_collection.id
            relation_name = self.biological_collection.original_species_name
        elif self.location_site:
            admin_url += 'locationsite/%s' % self.location_site.id
            relation_name = self.location_site.name

        html = '<a href=%s>%s</a>' % (admin_url, relation_name)
        return format_html(html)

    relation = property(_get_relation)

    def __unicode__(self):
        return '%s' % self.bibliography_entry_title

    def save(self, *args, **kwargs):
        """Check if one of geometry is not null."""
        if self.biological_collection and self.location_site:
            raise ValidationError(
                    'Only one data allowed from biological '
                    'collection or location site')

        if not self.biological_collection and not self.location_site:
            raise ValidationError(
                    'One data is needed from biological '
                    'collection or location site')
        super(BibliographyLink, self).save(*args, **kwargs)
