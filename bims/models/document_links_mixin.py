from django.contrib.gis.db import models
from geonode.documents.models import Document


class DocumentLinksMixin(models.Model):

    documents = models.ManyToManyField(
        Document,
        blank=True)

    class Meta:
        abstract = True
