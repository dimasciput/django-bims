# coding=utf-8
"""Shapefile document model definition.

"""

import os
from django.db import models
from django.dispatch import receiver


class Shapefile(models.Model):
    """Shapefile model
    """
    shapefile = models.FileField(upload_to='shapefile/')

    @property
    def filename(self):
        return self.shapefile.name

    @property
    def fileurl(self):
        return self.shapefile.url

    # noinspection PyClassicStyleClass
    class Meta:
        """Meta class for project."""
        app_label = 'bims'
        verbose_name_plural = 'Shapefiles'
        verbose_name = 'Shapefile'
