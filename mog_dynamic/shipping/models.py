from django.db import models
from django.contrib.auth.models import User
import random
from ckeditor.fields import RichTextField




def random_numbers():
    return random.randint(1111111111, 2147483647)


class ShippingDetail(models.Model):
    sender_name = models.CharField(max_length=100)
    items_description = RichTextField(blank=True, null=True)
    shipping_fee = models.FloatField(default="#")
    tracking_no = models.BigIntegerField(default=random_numbers)
    received_date = models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=False)
    arrived = models.BooleanField(default=False)
    picked_up = models.BooleanField(default=False)


    class Meta:
        ordering = ("received_date",)


    def __str__(self):
        return f" {self.sender_name} details"
