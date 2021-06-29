from django.contrib import admin
from .models import ShippingDetail
from django.contrib.admin.models import LogEntry




# Register your models here.
@admin.register(LogEntry)
class AdminLogLogEntry(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = ('user', 'content_type', )

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = ('object_repr', 'change_message')

    list_display = ('action_time','user','content_type','action_flag')

    actions = ["Delete_log_entery"]

    def delete_log_entery():
        LogEntry.objects.all().delete()



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
