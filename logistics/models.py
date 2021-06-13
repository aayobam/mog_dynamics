from django.db import models
import random
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from phone_field import PhoneField


def random_numbers():
    return random.randint(1111111111, 2147483647)


class Logistic(models.Model):
    sender_name = models.CharField(max_length=150)
    sender_address = models.CharField(max_length=500)
    sender_phone_no = PhoneField(blank=True, help_text='Contact phone number')
    receiver_name = models.CharField(max_length=150)
    receiver_address = models.CharField(max_length=500)
    receiver_phone_no = PhoneField(
        blank=True, help_text='Contact phone number')
    tracking_no = models.BigIntegerField(default=random_numbers)
    item_description = RichTextField(blank=True, null=True)
    received_date = models.DateTimeField(auto_now=False)
    delivery_date = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ("-received_date",)

    def __str__(self):
        return f"history of {self.sender_name} with tracking no {self.tracking_no}"
