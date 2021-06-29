from django.urls import path
from .views import (
    fixed3months_pdf_view,
    fixed6months_pdf_view,
    fixed9months_pdf_view,
    fixed12months_pdf_view,
    salarypackage_pdf_view
)

urlpatterns = [
    path('<int:pk>/3-monts-package/', fixed3months_pdf_view, name="3_months"),
    path('<int:pk>/6-monts-package/', fixed6months_pdf_view, name="6_months"),
    path('<int:pk>/9-monts-package/', fixed9months_pdf_view, name="9_months"),
    path('<int:pk>/12-monts-package/', fixed12months_pdf_view, name="12_months"),
    path('<int:pk>/salary-package/', salarypackage_pdf_view, name="salary_package"),
]
