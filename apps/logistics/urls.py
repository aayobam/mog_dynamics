from django.urls import path
from apps.logistics import views


urlpatterns = [
    path('search-page/', views.SearchPageView.as_view(), name="logistics_search"),
    path('tracking-result/', views.SearchResultView.as_view(), name="logistics_result"),
    path('dispatch/login/', views.dispatch_login, name="dispatch_login"),
    path('dispatch/logout/', views.dispatch_logout, name="dispatch_logout"),
    path('dispatch/search/', views.DispatchRiderSearchView.as_view(), name="dispatch_search"),
    path('dispatch/result/', views.DispatchRiderListView.as_view(), name="dispatch_result"),
    path('dispatch/<int:pk>/update/', views.DispatchRiderUpdateView.as_view(), name="dispatch_update"),
]
