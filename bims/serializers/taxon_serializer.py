import json

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from rest_framework import serializers
from bims.models import Taxonomy, BiologicalCollectionRecord
from bims.models.iucn_status import IUCNStatus
from bims.models.taxon_group import TaxonGroup
from bims.utils.gbif import get_vernacular_names
from bims.models.taxon_group_taxonomy import TaxonGroupTaxonomy


class TaxonSerializer(serializers.ModelSerializer):
    """
    Serializer for taxon collection model.
    """
    iucn_status_sensitive = serializers.SerializerMethodField()
    iucn_status_name = serializers.SerializerMethodField()
    iucn_status_full_name = serializers.SerializerMethodField()
    iucn_status_colour = serializers.SerializerMethodField()
    record_type = serializers.SerializerMethodField()
    taxon_group = serializers.SerializerMethodField()
    origin_name = serializers.SerializerMethodField()
    endemism_name = serializers.SerializerMethodField()
    common_name = serializers.SerializerMethodField()
    total_records = serializers.SerializerMethodField()
    accepted_taxonomy_name = serializers.SerializerMethodField()
    tag_list = serializers.SerializerMethodField()
    validated = serializers.SerializerMethodField()

    def get_validated(self, obj: Taxonomy):
        taxon_group_id = self.context.get('taxon_group_id', None)
        if taxon_group_id:
            return TaxonGroupTaxonomy.objects.filter(
                taxongroup=taxon_group_id,
                taxonomy=obj,
                is_validated=True
            ).exists()
        return obj.validated

    def get_accepted_taxonomy_name(self, obj):
        if obj.accepted_taxonomy:
            return obj.accepted_taxonomy.canonical_name
        return ''

    def get_total_records(self, obj):
        return BiologicalCollectionRecord.objects.filter(
            taxonomy=obj,
            source_site=Site.objects.get_current()
        ).count()

    def get_common_name(self, obj):
        vernacular_names = list(
            obj.vernacular_names.filter(language='eng').values_list('name', flat=True))
        if len(vernacular_names) == 0:
            return ''
        else:
            return vernacular_names[0]

    def get_tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def get_origin_name(self, obj):
        try:
            return dict(Taxonomy.CATEGORY_CHOICES)[obj.origin]
        except Exception:  # noqa
            return 'Unknown'

    def get_endemism_name(self, obj):
        try:
            return obj.endemism.name
        except AttributeError:
            return '-'

    def get_record_type(self, obj):
        return 'bio'

    def get_taxon_group(self, obj: Taxonomy):
        taxon_group_id = self.context.get('taxon_group_id', None)
        if taxon_group_id:
            taxon_group = TaxonGroup.objects.get(id=taxon_group_id)
            return {
                'logo': taxon_group.logo.name,
                'name': taxon_group.name
            }
        taxon_module = obj.taxongroup_set.first()
        if taxon_module:
            return {
                'logo': taxon_module.logo.name,
                'name': taxon_module.name
            }
        return {}

    def get_iucn_status_sensitive(self, obj):
        if obj.iucn_status:
            return obj.iucn_status.sensitive
        else:
            return False

    def get_iucn_status_name(self, obj):
        if obj.iucn_status:
            return obj.iucn_status.category
        else:
            return 'NE'

    def get_iucn_status_full_name(self, obj):
        if obj.iucn_status:
            for value in IUCNStatus.CATEGORY_CHOICES:
                if value[0] == obj.iucn_status.category:
                    return value[1]
            return 'Not evaluated'
        else:
            return 'Not evaluated'

    def get_iucn_status_colour(self, obj):
        if obj.iucn_status:
            return obj.iucn_status.colour
        else:
            return None

    class Meta:
        model = Taxonomy
        exclude = ('gbif_data', 'vernacular_names')


class TaxonExportSerializer(serializers.ModelSerializer):
    """
    Serializer for taxon collection model.
    """
    iucn_status_sensitive = serializers.SerializerMethodField()
    iucn_status_name = serializers.SerializerMethodField()

    def get_iucn_status_sensitive(self, obj):
        if obj.iucn_status:
            return obj.iucn_status.sensitive
        else:
            return None

    def get_iucn_status_name(self, obj):
        if obj.iucn_status:
            return obj.iucn_status.category
        else:
            return None

    class Meta:
        model = Taxonomy
        fields = [
            'scientific_name', 'class_name',
            'iucn_status_sensitive', 'iucn_status_name'
        ]


class TaxonOccurencesSerializer(serializers.ModelSerializer):
    """
    Serializer for taxon collection model in occurrences format.
    """

    record_type = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    def get_record_type(self, obj):
        return 'taxa'

    def get_count(self, obj):
        if hasattr(obj, 'num_occurrences'):
            return obj.num_occurrences
        else:
            return 0

    class Meta:
        model = Taxonomy
        fields = [
            'id', 'common_name', 'highlighted_common_name',
            'taxon_class', 'record_type',
            'count'
        ]


class TaxonSimpleSerializer(serializers.ModelSerializer):
    cons_status = serializers.SerializerMethodField()

    def get_cons_status(self, obj: Taxonomy):
        return obj.iucn_status.category if obj.iucn_status else '-'

    class Meta:
        model = Taxonomy
        fields = [
            'id', 'canonical_name',
            'scientific_name', 'cons_status']


class TaxonGroupExpertSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj: get_user_model()):
        if obj.first_name and obj.last_name:
            return f'{obj.first_name} {obj.last_name}'
        return obj.username

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'full_name', 'email']


class TaxonGroupSerializer(serializers.ModelSerializer):
    extra_attributes = serializers.SerializerMethodField()
    taxa_count = serializers.SerializerMethodField()
    experts = serializers.SerializerMethodField()
    gbif_parent_species = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    validated_count = serializers.SerializerMethodField()
    unvalidated_count = serializers.SerializerMethodField()

    def get_children(self, obj: TaxonGroup):
        children = TaxonGroup.objects.filter(parent=obj)
        if children.exists():
            return TaxonGroupSerializer(
                children, many=True, context=self.context
            ).data
        return []

    def get_gbif_parent_species(self, obj: TaxonGroup):
        if obj.gbif_parent_species:
            return json.dumps(TaxonSerializer(
                obj.gbif_parent_species
            ).data)
        return ''

    def get_taxa_count(self, obj: TaxonGroup):
        unique_taxonomy_ids = set()

        def collect_taxonomy_ids(taxon_group):
            ids = TaxonGroupTaxonomy.objects.filter(
                taxongroup=taxon_group
            ).values_list('id', flat=True)
            unique_taxonomy_ids.update(ids)
            for child in TaxonGroup.objects.filter(
                    parent=taxon_group):
                collect_taxonomy_ids(child)

        collect_taxonomy_ids(obj)
        return len(unique_taxonomy_ids)

    def get_unvalidated_count(self, obj: TaxonGroup):
        unique_taxonomy_ids = set()

        def collect_taxonomy_ids(taxon_group):
            taxonomies = taxon_group.taxonomies.filter(
                taxongrouptaxonomy__is_validated=False
            ).values_list('id', flat=True)
            unique_taxonomy_ids.update(taxonomies)
            children = TaxonGroup.objects.filter(
                parent=taxon_group)
            for child in children:
                collect_taxonomy_ids(child)

        collect_taxonomy_ids(obj)
        return len(unique_taxonomy_ids)

    def get_validated_count(self, obj: TaxonGroup):
        unique_taxonomy_ids = set()

        def collect_taxonomy_ids(taxon_group):
            taxonomies = taxon_group.taxonomies.filter(
                taxongrouptaxonomy__is_validated=True
            ).values_list('id', flat=True)
            unique_taxonomy_ids.update(taxonomies)
            children = TaxonGroup.objects.filter(
                parent=taxon_group)
            for child in children:
                collect_taxonomy_ids(child)

        collect_taxonomy_ids(obj)
        return len(unique_taxonomy_ids)

    def get_extra_attributes(self, obj):
        return list(
            obj.taxonextraattribute_set.all().values_list('name', flat=True)
        )

    def get_experts(self, obj: TaxonGroup):
        return TaxonGroupExpertSerializer(
            obj.experts.all(),
            many=True
        ).data

    class Meta:
        model = TaxonGroup
        fields = ['id',
                  'parent',
                  'gbif_parent_species',
                  'name', 'category', 'logo', 'extra_attributes',
                  'taxa_count', 'unvalidated_count', 'validated_count',
                  'experts', 'children']
