from django.urls import path
from apps.shipping import views


urlpatterns = [
    path('track-shipment/', views.SearchPageView.as_view(), name="shipping_search"),
    path('tracking-result/', views.SearchResultView.as_view(), name="shipping_result"),
]