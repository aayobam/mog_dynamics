from django.contrib import admin
from .models import Logistic




@admin.register(Logistic)
class AdminLogistics(admin.ModelAdmin):

    list_display = (
        "id","sender_name","sender_address","sender_phone_no","receiver_name","receiver_address",
        "receiver_phone_no","tracking_no","item_description","received_date","delivery_date",
        "received","in_transit","delivered"
    )
    
    readonly_fields = ("tracking_no", "received_date", "delivery_date")
    list_filter = ("tracking_no",)
    search_fields = ("tracking_no", "sender_phone_no", "receiver_phone_no")
    actions = ["received", "transit","delivered"]


    # return true for approved fields
    def received(self, request,queryset):
        return queryset.update(received=True)


    def transit(self, request, queryset):
        return queryset.update(in_transit=True)


    def delivered(self, request, queryset):
        return queryset.update(delivered=True)




