from django.contrib import admin
from .models import Shipping



@admin.register(Shipping)
class AdminShipping(admin.ModelAdmin):
    list_display = ('sender_name', 'items_description', 'shipping_fee', 'tracking_no', 'received_date', 'picked_on', 'status')
    readonly_fields = ('tracking_no',)
    list_filter = ('sender_name', 'tracking_no')
    search_fields = ('id', 'sender_name', 'tracking_no')
    actions = ['pending', 'arrived', 'picked_up', 'us_custom', 'uk_custom', 'ca_custom', 'enroute_nigeria']

    # return true for approved fields
    def pending(self, request, queryset):
        return queryset.update(status="Pending")

    def arrived(self, request, queryset):
        return queryset.update(status="Arrived")

    def picked_up(self, request, queryset):
        return queryset.update(status="Picked Up")

    def us_custom(self, request, queryset):
        return queryset.update(status="shipment undergoing US customs routine inspection")

    def uk_custom(self, request, queryset):
        return queryset.update(status="shipment undergoing UK customs routine inspection")

    def ca_custom(self, request, queryset):
        return queryset.update(status="shipment undergoing CA customs routine inspection")

    def enroute_nigeria(self, request, queryset):
        return queryset.update(status="Shipment is now in transit to Lagos, Nigeria")
