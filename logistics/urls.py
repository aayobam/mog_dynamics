from django.urls import path
from .views import (
    SearchResultView, 
    SearchPageView, 
    dispatch_login,
    dispatch_logout,
    DispatchRiderSearchView,
    DispatchRiderListView,
    DispatchRiderUpdateView,
)


urlpatterns = [
    path('search-page/', SearchPageView.as_view(), name="logistics_search"),
    path('tracking-result/', SearchResultView.as_view(), name="logistics_result"),
    path('dispatch/login/', dispatch_login, name="dispatch_login"),
    path('dispatch/logout/', dispatch_logout, name="dispatch_logout"),
    path('dispatch/search/', DispatchRiderSearchView.as_view(), name="dispatch_search"),
    path('dispatch/result/', DispatchRiderListView.as_view(), name="dispatch_result"),
    path('dispatch/<int:pk>/update/', DispatchRiderUpdateView.as_view(), name="dispatch_update"),
]
