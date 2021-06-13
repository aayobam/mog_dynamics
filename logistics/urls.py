from django.urls import path
from .views import SearchResultView, SearchPageView


urlpatterns = [
    path('search-page/', SearchPageView.as_view(), name="logistics_search"),
    path('tracking-result/', SearchResultView.as_view(), name="logistics_result"),
]
