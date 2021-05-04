from django.shortcuts import render, HttpResponse
from .models import ShippingDetail



def home_view(request):
    template_name = "shipping/search_page.html"
    return render(request, template_name)