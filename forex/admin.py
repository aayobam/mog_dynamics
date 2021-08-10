from django.contrib import admin
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


from .models import (
    SalaryPackage,
    FixedPackage3Month,
    FixedPackage6Month,
    FixedPackage9Month,
    FixedPackage12Month,
    
)


def send_email_to_investment(self):
    return mark_safe('<a href="{}" style="background:red;" class="button">SEND MAIL</a>'.format(reverse('send-email', args=[self.pk])))
send_email_to_investment.short_description = 'send investment mail'


# This displays the PDf link to print record of the row using the row id or pk
def investment_pdf_salary(self):
    return mark_safe('<a href="{}" style="background:red;" class="button">PRINT RECORD</a>'.format(reverse('salary_package', args=[self.pk])))
investment_pdf_salary.short_description = 'Investment Invoice'


@admin.register(SalaryPackage)
class AdminSalary3month(admin.ModelAdmin):
    list_display = ("investor_name", "phone_no", "email","capital", "percentage", "duration", "investment_date", "monthly_payment",
                    "first_payment", "payment_date_1", "second_payment", "payment_date_2", "third_payment", "payment_date_3", "reference_no", investment_pdf_salary)

    readonly_fields = ("percentage", "monthly_payment", "first_payment", "payment_date_1", "second_payment",
                       "payment_date_2", "third_payment", "payment_date_3", "reference_no", "duration")

    list_filter = ("reference_no", "investment_date", "investor_name")
    search_fields = ("reference_no", "phone_no")

    actions = ["first_payment", "payment_date_1", "second_payment",
               "payment_date_2", "third_payment", "payment_date_3"]

    list_per_page = 10

    # This handles payment, and payment date approval by the admin to respective investor
    def first_payment(self, request, queryset):
        return queryset.update(first_payment="Paid")

    def second_payment(self, request, queryset):
        return queryset.update(second_payment="Paid")

    def third_payment(self, request, queryset):
        return queryset.update(third_payment="Paid")

    def payment_date_1(self, request, queryset):
        return queryset.update(payment_date_1=timezone.now())

    def payment_date_2(self, request, queryset):
        return queryset.update(payment_date_2=timezone.now())

    def payment_date_3(self, request, queryset):
        return queryset.update(payment_date_3=timezone.now())


# This displays the PDf link to print record of the row using the row id or pk
def investment_pdf_3months(self):
    return mark_safe('<a href="{}" style="background:red;" class="button">PRINT RECORD</a>'.format(reverse('3_months', args=[self.pk])))
investment_pdf_3months.short_description = 'Investment Invoice'


@admin.register(FixedPackage3Month)
class AdminFixedPackage3Month(admin.ModelAdmin):
    list_display = ("investor_name", "phone_no", "email", "capital", "percentage", "duration",
                    "date", "returns", "returns_payout_date", "payout_status", "reference_no", investment_pdf_3months)

    list_filter = ("reference_no", "investor_name", "date")

    readonly_fields = ("percentage", "date", "payout_status",
                       "returns", "duration", "reference_no",)

    search_fields = ("reference_no", "phone_no")

    actions = ["update_payout_status"]

    list_per_page = 10

    def update_payout_status(self, request, queryset):
        return queryset.update(payout_status="Paid")


# This displays the PDf link to print record of the row using the row id or pk
def investment_pdf_6months(self):
    return mark_safe('<a href="{}" style="background:red;" class="button">PRINT RECORD</a>'.format(reverse('6_months', args=[self.pk])))
investment_pdf_6months.short_description = 'Investment Invoice'


@admin.register(FixedPackage6Month)
class AdminFixedPackage6Month(admin.ModelAdmin):
    list_display = ("investor_name", "phone_no", "email", "capital", "percentage", "duration",
                    "date", "returns", "returns_payout_date", "payout_status", "reference_no", investment_pdf_6months)

    list_filter = ("reference_no", "investor_name", "date")

    readonly_fields = ("percentage", "date", "payout_status",
                       "returns", "duration", "reference_no",)

    search_fields = ("reference_no", "phone_no")

    actions = ["update_payout_status"]

    list_per_page = 10

    def update_payout_status(self, request, queryset):
        return queryset.update(payout_status="Paid")


# This displays the PDf link to print record of the row using the row id or pk
def investment_pdf_9months(self):
    return mark_safe('<a href="{}" style="background:red;" class="button">PRINT RECORD</a>'.format(reverse('9_months', args=[self.pk])))
investment_pdf_9months.short_description = 'Investment Invoice'


@admin.register(FixedPackage9Month)
class AdminFixedPackage9Month(admin.ModelAdmin):
    list_display = ("investor_name", "phone_no", "email", "capital", "percentage", "duration",
                    "date", "returns", "returns_payout_date", "payout_status", "reference_no", investment_pdf_9months)

    list_filter = ("reference_no", "investor_name", "date")

    readonly_fields = ("percentage", "date", "payout_status",
                       "returns", "duration", "reference_no",)

    search_fields = ("reference_no", "phone_no")

    actions = ["update_payout_status"]

    list_per_page = 10

    def update_payout_status(self, request, queryset):
        return queryset.update(payout_status="Paid")


# This displays the PDf link to print record of the row using the row id or pk
def investment_pdf_12months(self):
    return mark_safe('<a href="{}" style="color:red">PRINT RECORD</a>'.format(reverse('12_months', args=[self.pk])))
investment_pdf_12months.short_description = 'Investment Invoice'


@admin.register(FixedPackage12Month)
class AdminFixedPackage12Month(admin.ModelAdmin):
    list_display = ("investor_name", "phone_no", "email", "capital", "percentage", "duration",
                    "date", "returns", "returns_payout_date", "payout_status", "reference_no", investment_pdf_12months)

    list_filter = ("reference_no", "investor_name", "date")

    readonly_fields = ("percentage", "date", "payout_status",
                       "returns", "duration", "reference_no",)

    search_fields = ("reference_no", "phone_no")

    actions = ["update_payout_status"]

    list_per_page = 10

    def update_payout_status(self, request, queryset):
        return queryset.update(payout_status="Paid")
