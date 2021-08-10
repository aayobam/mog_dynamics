from django.contrib import admin
from .models import ShippingDetail



@admin.register(ShippingDetail)
class AdminShipping(admin.ModelAdmin):
    list_display = ("sender_name", "items_description", "shipping_fee", "tracking_no", "received_date", "picked_on",
        "status"
    )
    readonly_fields = ("tracking_no", "status")
    list_filter = ("sender_name", "tracking_no",)
    search_fields = ("sender_name", "tracking_no")
    actions = ["pending", "arrived", "picked_up"]

    # return true for approved fields
    def pending(self, request, queryset):
        return queryset.update(status="Pending")

    def arrived(self, request, queryset):
        return queryset.update(status="Arrived")

    def picked_up(self, request, queryset):
        return queryset.update(status="Picked Up")
