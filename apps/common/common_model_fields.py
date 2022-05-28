import uuid
from django.db import models
from apps.common.generator import random_numbers


class CommonFields(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    investor_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=11, help_text='Contact phone number')
    capital = models.FloatField(null=False, blank=False, default=0)
    returns_payout_date = models.DateField(auto_now=False, null=True)
    payout_status = models.CharField(max_length=20, default="Pending")
    reference_no = models.IntegerField(default=random_numbers)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class TimeStapedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True