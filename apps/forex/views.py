from django.shortcuts import get_object_or_404, HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
import weasyprint
from .models import (
    FixedPackage3Month,
    FixedPackage6Month,
    FixedPackage9Month,
    FixedPackage12Month,
    SalaryPackage
)


@staff_member_required
def fixed3months_pdf_view(request, pk):
    template_name = "forex/pdf.html"
    fixed = get_object_or_404(FixedPackage3Month, id=pk)
    context = {"fixed": fixed}
    html = render_to_string(template_name, context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="{0}-{1}"'.format(
        fixed.investor_name, fixed.reference_no)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
    return response


@ staff_member_required
def fixed6months_pdf_view(request, pk):
    template_name = "forex/pdf.html"
    fixed = get_object_or_404(FixedPackage6Month, id=pk)
    context = {"fixed": fixed}
    html = render_to_string(template_name, context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="{0}-{1}"'.format(
        fixed.investor_name, fixed.reference_no)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
    return response


@ staff_member_required
def fixed9months_pdf_view(request, pk):
    template_name = "forex/pdf.html"
    fixed = get_object_or_404(FixedPackage9Month, id=pk)
    context = {"fixed": fixed}
    html = render_to_string(template_name, context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="{0}-{1}"'.format(
        fixed.investor_name, fixed.reference_no)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
    return response


@ staff_member_required
def fixed12months_pdf_view(request, pk):
    template_name = "forex/pdf.html"
    fixed = get_object_or_404(FixedPackage12Month, id=pk)
    context = {"fixed": fixed}
    html = render_to_string(template_name, context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="{0}-{1}"'.format(
        fixed.investor_name, fixed.reference_no)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
    return response



def salarypackage_pdf_view(request, pk):
    template_name = "forex/pdfsalarypackage.html"
    fixed = get_object_or_404(SalaryPackage, id=pk)
    context = {"fixed": fixed}
    html = render_to_string(template_name, context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="{0}-{1}"'.format(fixed.investor_name, fixed.reference_no)
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, 
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
    return response
    