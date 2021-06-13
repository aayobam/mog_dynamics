from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import random
from ckeditor.fields import RichTextField


def random_numbers():
    return random.randint(1111111111, 2147483647)


class ShippingDetail(models.Model):
    sender_name = models.CharField(max_length=100, help_text="input name")
    items_description = RichTextField(blank=True, null=True)
    shipping_fee = models.FloatField()
    tracking_no = models.BigIntegerField(default=random_numbers)
    received_date = models.DateField(auto_now_add=False, null=True)
    picked_on = models.DateField(auto_now_add=False, null=True)
    status = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ("received_date",)

    def __str__(self):
        return f" {self.sender_name} details"
