from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Logistic
from django.utils import timezone



@admin.register(Logistic)
class AdminLogistics(admin.ModelAdmin):

    list_display = (
        "sender_name", "sender_address", "sender_phone_no", "receiver_name", "receiver_address",
        "receiver_phone_no", "tracking_no", "item_description", "received_date", "delivery_date", 
        "status", 'updated_at',"updated_by"
    )

    readonly_fields = ("tracking_no", )
    search_fields = ("tracking_no", "sender_phone_no", "receiver_phone_no")
    actions = ["received", "transit", "delivered", "delivery_date",
               "wrong_delivery_address", "unable_to_locate_address", "unable_to_contact_receiver"]



    # return true for approved fields

    def received(self, request, queryset):
        return queryset.update(status="Received")

    def transit(self, request, queryset):
        return queryset.update(status="In Transit")

    def delivered(self, request, queryset):
        return queryset.update(status="Delivered")

    def delivery_date(self, request, queryset):
        return queryset.update(delivery_date=timezone.now())

    def wrong_delivery_address(self, request, queryset):
        message = "Wrong Delivery Address"
        return queryset.update(status=message)

    def unable_to_locate_address(self, request, queryset):
        message = "Unable to Locate Address"
        return queryset.update(status=message)

    def unable_to_contact_receiver(self, request, queryset):
        message = "Unable to Contact Receiver"
        return queryset.update(status=message)

