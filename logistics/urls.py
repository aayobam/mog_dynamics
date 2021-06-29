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
    path('admin/dispatch/login/', dispatch_login, name="dispatch_login"),
    path('admin/dispatch/logout/', dispatch_logout, name="dispatch_logout"),
    path('admin/dispatch/search/', DispatchRiderSearchView.as_view(), name="dispatch_search"),
    path('admin/dispatch/result/', DispatchRiderListView.as_view(), name="dispatch_result"),
    path('admin/dispatch/<int:pk>/update/', DispatchRiderUpdateView.as_view(), name="dispatch_update"),
]
