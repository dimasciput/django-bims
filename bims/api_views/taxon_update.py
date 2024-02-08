from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import transaction

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bims.models.taxonomy import Taxonomy
from bims.models.taxonomy_update_proposal import (
    TaxonomyUpdateProposal
)
from bims.models.taxon_group import TaxonGroup


class UpdateTaxon(UserPassesTestMixin, APIView):
    """
    Provides an API endpoint for updating taxon information. Only superusers or
    experts of the specified taxon group are allowed to propose updates to a taxonomy.
    """

    def test_func(self) -> bool:
        """Check if the user has permissions to update the taxon."""
        if self.request.user.is_superuser:
            return True
        taxon_group = get_object_or_404(
            TaxonGroup,
            pk=self.kwargs.get('taxon_group_id')
        )
        return taxon_group.experts.filter(
            id=self.request.user.id
        ).exists()

    def is_taxon_edited(self, taxon: Taxonomy) -> bool:
        """Check if the taxon is currently being edited (has a pending update proposal)."""
        return TaxonomyUpdateProposal.objects.filter(
            original_taxonomy=taxon,
            status='pending'
        ).exists()

    def put(self, request, taxon_id, taxon_group_id, *args) -> Response:
        """Handle PUT request to propose an update to a taxonomy."""
        taxon = get_object_or_404(
            Taxonomy,
            pk=taxon_id
        )
        taxon_group = get_object_or_404(
            TaxonGroup,
            pk=taxon_group_id
        )
        # Check if taxon is still being edited
        if self.is_taxon_edited(taxon):
            return Response({
                'message': 'Taxon is still being edited'
            }, status=status.HTTP_403_FORBIDDEN)

        data = request.data

        with transaction.atomic():
            proposal = TaxonomyUpdateProposal.objects.create(
                original_taxonomy=taxon,
                taxon_group=taxon_group,
                status='pending',
                scientific_name=data.get('scientific_name', taxon.scientific_name),
                canonical_name=data.get('canonical_name', taxon.canonical_name)
            )

        return Response(
            {
                'message': 'Taxonomy update proposal created successfully',
                'proposal_id': proposal.pk
            },
            status=status.HTTP_202_ACCEPTED)
