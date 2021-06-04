from django.shortcuts import render
import time


def home_view(request):
    template_name = "home.html"
    time.sleep(1)
    return render(request, template_name)


def contact_view(request):
    template_name = "contact.html"
    time.sleep(1)
    return render(request, template_name)

def about_view(request):
    template_name = "about.html"
    time.sleep(1)
    return render(request, template_name)
