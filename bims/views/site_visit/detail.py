from django.views.generic.detail import DetailView
from bims.views.site_visit.base import SiteVisitBaseView
from bims.models.survey import Survey
from bims.models.basemap_layer import BaseMapLayer


class SiteVisitDetailView(SiteVisitBaseView, DetailView):
    template_name = 'site_visit/site_visit_detail.html'
    model = Survey
    pk_url_kwarg = 'sitevisitid'

    def get_context_data(self, **kwargs):
        context = super(SiteVisitDetailView, self).get_context_data(**kwargs)
        context['detail'] = True
        try:
            context['bing_key'] = (
                BaseMapLayer.objects.get(source_type='bing').key
            )
        except BaseMapLayer.DoesNotExist:
            context['bing_key'] = ''
        return context
