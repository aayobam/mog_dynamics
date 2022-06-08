from .models import Shipping
from django.views.generic import ListView, TemplateView
from django.db.models import Q



class SearchPageView(TemplateView):
    template_name = "shipping/shipping_page.html"


class SearchResultView(ListView):
    model = Shipping
    template_name = "shipping/shipping_result.html"
    context_object_name = "shippingstatus"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            shippingstatus = Shipping.objects.filter(
                Q(tracking_no__icontains=query)
            )
            return shippingstatus
        return False