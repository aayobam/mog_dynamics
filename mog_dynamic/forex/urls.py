from django.urls import path
from .views import forex_view


urlpatterns = [
    path('', forex_view, name="forex-view")
]