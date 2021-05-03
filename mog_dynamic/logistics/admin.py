from django.contrib import admin
from .models import Logistic
from django.utils import timezone



@admin.register(Logistic)
class AdminLogistics(admin.ModelAdmin):

    list_display = (
        "id","sender_name","sender_address","sender_phone_no",
        "receiver_name","receiver_address","receiver_phone_no",
        "tracking_no","item_description","received_date","delivery_date","received",
        "out_for_deliver","delivered",
    )
    readonly_fields = ("tracking_no", "received_date", "delivery_date")
    list_filter = ("tracking_no",)
    search_fields = ("tracking_no", "sender_address", "receiver_name")
    actions = ["received", "out_for_delivery", "delivered","received_date","delivery_date"]


    # return true for approved fields
    def received(self, request,queryset):
        return queryset.update(received=True)


    def delivery(self, request, queryset):
        return queryset.update(out_for_delivery=True)


    def delivered(self, request, queryset):
        return queryset.update(delivered=True)


    def received_date(self, request, queryset):
        auto_now_add = True
        return queryset.update(received_date=True)


    def delivery_date(self, request, queryset):
        return queryset.update(delivery_date=True)
