from django.db import models
from apps.common import generator
from apps.common.common_model_fields import CommonFields



class SalaryPackage(models.Model):
    investor_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=11)
    capital = models.FloatField(null=False, blank=False, default=0)
    percentage = models.CharField(max_length=5, default="15 %")
    duration = models.CharField(max_length=10, default="3 months")
    investment_date = models.DateField(auto_now_add=True)
    monthly_payment = models.FloatField(null=False, blank=False)
    first_payment = models.CharField(max_length=20, default="Pending")
    payment_date_1 = models.DateField(auto_now_add=False, null=True)
    second_payment = models.CharField(max_length=20, default="Pending")
    payment_date_2 = models.DateField(auto_now_add=False, null=True)
    third_payment = models.CharField(max_length=20, default="Pending")
    payment_date_3 = models.DateField(auto_now_add=False, null=True)
    reference_no = models.IntegerField(default=generator.random_numbers)

    def __str__(self):
        return f"{self.investor_name}'s investment"

    @property
    def monthly_percentage(self):
        return (15 / 100) * self.capital

    def save(self, *args, **kwargs):
        self.monthly_payment = self.monthly_percentage()
        return super().save(*args, **kwargs)


class FixedPackage3Month(CommonFields):
    percentage = models.CharField(max_length=5, default="45 %")
    duration = models.CharField(max_length=10, default="3 months")
    returns = models.FloatField(null=False, blank=False)
 

    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((45 / 100) * self.capital) + self.capital

    def save(self, *args, **kwargs):
        self.returns = self.total_payment()
        return super().save(*args, **kwargs)


class FixedPackage6Month(CommonFields):
    percentage = models.CharField(max_length=5, default="90 %")
    duration = models.CharField(max_length=10, default="6 months")
    returns = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((90 / 100) * self.capital) + self.capital

    def save(self, *args, **kwargs):
        self.returns = self.total_payment()
        return super().save(*args, **kwargs)


class FixedPackage9Month(CommonFields):
    percentage = models.CharField(max_length=5, default="140 %")
    duration = models.CharField(max_length=10, default="9 months")
    returns = models.FloatField(null=False, blank=False)
   
    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((140 / 100) * self.capital) + self.capital

    def save(self, *args, **kwargs):
        self.returns = self.total_payment()
        return super().save(*args, **kwargs)


class FixedPackage12Month(CommonFields):
    percentage = models.CharField(max_length=5, default="200 %")
    duration = models.CharField(max_length=10, default="12 months")
    returns = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.investor_name}'s investment profile"

    @property
    def total_payment(self):
        return ((200 / 100) * self.capital) + self.capital

    def save(self, *args, **kwargs):
        self.returns = self.total_payment()
        return super().save(*args, **kwargs)