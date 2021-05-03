from django.contrib import admin
from .models import ShippingDetail

# Register your models here.


@admin.register(ShippingDetail)
class AdminShipping(admin.ModelAdmin):
    list_display = (
        "id", "sender_name", "items_description", "shipping_fee", "tracking_no", "received_date", 
        "pending", "arrived", "picked_up"
    )
    readonly_fields = ("tracking_no",)
    list_filter = ("sender_name", "tracking_no")
    search_fields = ("id", "sender_name", "tracking_no")
    actions = ["pending", "arrived", "picked_up"]


    # return true for approved fields
    def pending(self, request,queryset):
        return queryset.update(pending=True)

    def arrived(self, request, queryset):
        return queryset.update(arrived=True)

    def picked_up(self, request, queryset):
        return queryset.update(picked_up=True)
    