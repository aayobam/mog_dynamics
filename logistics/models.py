from django.db import models
import random
from ckeditor.fields import RichTextField
from phone_field import PhoneField
from django.contrib.auth.models import User



def random_numbers():
    return random.randint(1111111111, 2147483647)

data = [
    ("Received", "Received"),
    ("In Transit", "In Transit"),
    ("Delivered", "Delivered"),
    ("Wrong Delivery Address", "Wrong Delivery Address"),
    ("Unable to Locate Address", "Unable to Locate Address"),
    ("Unable to Contact Receiver", "Unable to Contact Receiver"),
]
class Logistic(models.Model):
    sender_name = models.CharField(max_length=150)
    sender_address = models.CharField(max_length=500)
    sender_phone_no = PhoneField(blank=True)
    receiver_name = models.CharField(max_length=150)
    receiver_address = models.CharField(max_length=500)
    receiver_phone_no = PhoneField(
        blank=True, help_text='Contact phone number')
    tracking_no = models.CharField(default=random_numbers, max_length=10)
    item_description = RichTextField(blank=True, null=True)
    received_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    delivery_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=data,max_length=100, null=True, help_text="Update Delivery Status")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ("-received_date",)

    def __str__(self):
        return f"history of {self.sender_name} with tracking no {self.tracking_no}"

