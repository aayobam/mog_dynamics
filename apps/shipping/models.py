from django.db import models
from apps.common import generator
from ckeditor.fields import RichTextField
from apps.common.choices import shipping_choices
from apps.common.common_model_fields import TimeStapedModel



class ShippingDetail(TimeStapedModel):
    sender_name = models.CharField(max_length=100, help_text="input name")
    items_description = RichTextField(blank=True, null=True)
    shipping_fee = models.FloatField()
    tracking_no = models.BigIntegerField(default=generator.random_numbers)
    received_date = models.DateField(auto_now_add=False, null=True)
    picked_on = models.DateField(auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, choices=shipping_choices)

    class Meta:
        ordering = ("received_date",)

    def __str__(self):
        return f" {self.sender_name} details"

