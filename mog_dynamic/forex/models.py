from django.db import models
from phone_field import PhoneField
import computed_property
import random


def random_numbers():
    return random.randint(1111111111, 2147483647)


class SalaryPackage(models.Model):

    investor_name = models.CharField(max_length=150)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    capital = models.FloatField(null=False, blank=False, default=0)

    percentage = models.CharField(max_length=5, default="15 %")
    duration = models.CharField(max_length=10, default="3 months")

    investment_date = models.DateField(auto_now_add=True)
    monthly_payment = computed_property.ComputedFloatField(
        compute_from='monthly_percentage', null=False, blank=False)

    first_payment = models.CharField(max_length=20, default="Pending")
    payment_date_1 = models.DateField(auto_now_add=False, null=True)

    second_payment = models.CharField(max_length=20, default="Pending")
    payment_date_2 = models.DateField(auto_now_add=False, null=True)

    third_payment = models.CharField(max_length=20, default="Pending")
    payment_date_3 = models.DateField(auto_now_add=False, null=True)

    reference_no = models.IntegerField(default=random_numbers)

    def __str__(self):
        return f"{self.investor_name}'s investment"

    @property
    def monthly_percentage(self):
        return (15 / 100) * self.capital

#############################################################################################################


class FixedPackage3Month(models.Model):

    investor_name = models.CharField(max_length=150)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    capital = models.FloatField(null=False, blank=False, default=0)

    percentage = models.CharField(max_length=5, default="45 %")
    duration = models.CharField(max_length=10, default="3 months")

    date = models.DateField(auto_now=False, blank=True, null=True)
    returns = computed_property.ComputedFloatField(
        compute_from='total_payment', null=False, blank=False)

    returns_payout_date = models.DateField(auto_now=False, null=True)
    payout_status = models.CharField(max_length=20, default="Pending")
    reference_no = models.IntegerField(default=random_numbers)

    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((45 / 100) * self.capital) + self.capital

####################################################################################################


class FixedPackage6Month(models.Model):

    investor_name = models.CharField(max_length=150)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    capital = models.FloatField(null=False, blank=False, default=0)

    percentage = models.CharField(max_length=5, default="90 %")
    duration = models.CharField(max_length=10, default="6 months")

    date = models.DateField(auto_now=False, blank=True, null=True)
    returns = computed_property.ComputedFloatField(
        compute_from='total_payment', null=False, blank=False)

    returns_payout_date = models.DateField(auto_now=False, null=True)
    payout_status = models.CharField(max_length=20, default="Pending")
    reference_no = models.IntegerField(default=random_numbers)

    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((90 / 100) * self.capital) + self.capital
#####################################################################################################


class FixedPackage9Month(models.Model):

    investor_name = models.CharField(max_length=150)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    capital = models.FloatField(null=False, blank=False, default=0)

    percentage = models.CharField(max_length=5, default="140 %")
    duration = models.CharField(max_length=10, default="9 months")

    date = models.DateField(auto_now=False, blank=True, null=True)
    returns = computed_property.ComputedFloatField(
        compute_from='total_payment', null=False, blank=False)

    returns_payout_date = models.DateField(auto_now=False, null=True)
    payout_status = models.CharField(max_length=20, default="Pending")
    reference_no = models.IntegerField(default=random_numbers)

    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((140 / 100) * self.capital) + self.capital

#######################################################################################


class FixedPackage12Month(models.Model):

    investor_name = models.CharField(max_length=150)
    phone_no = PhoneField(blank=True, help_text='Contact phone number')
    capital = models.FloatField(null=False, blank=False, default=0)

    percentage = models.CharField(max_length=5, default="200 %")
    duration = models.CharField(max_length=10, default="12 months")

    date = models.DateField(auto_now=False, blank=True, null=True)
    returns = computed_property.ComputedFloatField(
        compute_from='total_payment', null=False, blank=False)

    returns_payout_date = models.DateField(auto_now=False, null=True)
    payout_status = models.CharField(max_length=20, default="Pending")
    reference_no = models.IntegerField(default=random_numbers)

    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((200 / 100) * self.capital) + self.capital
