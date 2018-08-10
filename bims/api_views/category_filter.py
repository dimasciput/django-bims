# coding=utf-8
import json
from django.http.response import HttpResponse
from rest_framework.views import APIView
from bims.models.biological_collection_record import BiologicalCollectionRecord


class CategoryList(APIView):
    """API for listing all biological collection record category."""

    def get(self, request, *args):
        category = \
            BiologicalCollectionRecord.objects.all().values_list(
                'category', flat=True).distinct().order_by('category')
        return HttpResponse(
            json.dumps(list(category)), content_type='application/json')
