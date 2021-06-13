from django.urls import path
from .views import SearchResultView,  SearchPageView


urlpatterns = [
    path('track-shipment/', SearchPageView.as_view(), name="shipping_search"),
    path('tracking-result/', SearchResultView.as_view(), name="shipping_result"),
]
