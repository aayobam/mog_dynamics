from django.db import models
from apps.common import generator
from ckeditor.fields import RichTextField
from apps.common.choices import shipping_status_choices, shipping_payment_choices
from apps.common.common_model_fields import TimeStapedModel



class Shipping(TimeStapedModel):
    sender_name = models.CharField(max_length=100, help_text="input name")
    sender_email = models.EmailField(help_text="sender email")
    phone_no = models.CharField(max_length=11, blank=True, help_text="sender phone number")
    items_description = RichTextField(blank=True, null=True)
    shipping_fee = models.CharField(choices=shipping_payment_choices, default="Unpaid", max_length=100)
    tracking_no = models.BigIntegerField(default=generator.random_numbers)
    received_date = models.DateField(auto_now_add=False, null=True)
    picked_on = models.DateField(auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=100, choices=shipping_status_choices, default="In Transit")
    attention = models.TextField(blank=True)

    class Meta:
        ordering = ("received_date",)
        verbose_name = "Shipping Item"
        verbose_name_plural = "Shipping Items"

    def __str__(self):
        return f"history of {self.sender_name} with {self.tracking_no}"

