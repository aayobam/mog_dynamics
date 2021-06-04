from django.shortcuts import render, HttpResponse, redirect
from .models import Logistic
from django.views.generic import ListView, TemplateView
from django.db.models import Q
import time


class SearchPageView(TemplateView):
    time.sleep(1)
    template_name = "logistics/logistic_page.html"


class SearchResultView(ListView):
    model = Logistic
    template_name = "logistics/logistic_result.html"
    context_object_name = "logistics"
    successful_url = "not_found"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            logistics = Logistic.objects.filter(
                Q(tracking_no__icontains=query)
            )
            time.sleep(1)
            return logistics
        return None
