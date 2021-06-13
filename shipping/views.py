from .models import ShippingDetail
from django.views.generic import ListView, TemplateView
from django.db.models import Q
import time


class SearchPageView(TemplateView):
    #time.sleep(1)
    template_name = "shipping/shipping_page.html"


class SearchResultView(ListView):
    model = ShippingDetail
    template_name = "shipping/shipping_result.html"
    context_object_name = "shippingstatus"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            shippingstatus = ShippingDetail.objects.filter(
                Q(tracking_no__icontains=query)
            )
            #time.sleep(1)
            return shippingstatus
        return False