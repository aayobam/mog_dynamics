from django.db import models
import random



def random_numbers():
    return random.randint(1111111111, 2147483647)


class Logistic(models.Model):
    sender_name = models.CharField(max_length=150)
    sender_address = models.CharField(max_length=500)
    sender_phone_no = models.CharField(max_length=11)
    receiver_name = models.CharField(max_length=150)
    receiver_address = models.CharField(max_length=500)
    receiver_phone_no = models.CharField(max_length=11)
    tracking_no = models.BigIntegerField(default=random_numbers)
    item_description = models.TextField()
    received_date = models.DateTimeField(auto_now_add=False)
    delivery_date = models.DateTimeField(auto_now_add=False)
    received = models.BooleanField(default=False)
    out_for_deliver= models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)


    class Meta:
        ordering = ("-received_date",)


    def __str__(self):
        return "history of {self.sender_name} with tracking no {self.tracking_no}"
    