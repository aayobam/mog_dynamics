from django.urls import path
from .views import logistics_view



urlpatterns = [
     path('tracking/', logistics_view, name="logisitics")
]