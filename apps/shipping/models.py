from django.db import models
from django.contrib.auth.models import User
from apps.common import generator
from ckeditor.fields import RichTextField
from apps.common.common_model_fields import TimeStapedModel



class ShippingDetail(TimeStapedModel):
    sender_name = models.CharField(max_length=100, help_text="input name")
    items_description = RichTextField(blank=True, null=True)
    shipping_fee = models.FloatField()
    tracking_no = models.BigIntegerField(default=generator.random_numbers)
    received_date = models.DateField(auto_now_add=False, null=True)
    picked_on = models.DateField(auto_now_add=False, null=True)
    status = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ("received_date",)

    def __str__(self):
        return f" {self.sender_name} details"

