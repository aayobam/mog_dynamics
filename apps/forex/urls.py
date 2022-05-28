from apps.forex import views
from django.urls import path



urlpatterns = [
    path('<int:pk>/3-monts-package/', views.fixed3months_pdf_view, name="3_months"),
    path('<int:pk>/6-monts-package/', views.fixed6months_pdf_view, name="6_months"),
    path('<int:pk>/9-monts-package/', views.fixed9months_pdf_view, name="9_months"),
    path('<int:pk>/12-monts-package/', views.fixed12months_pdf_view, name="12_months"),
    path('<int:pk>/salary-package/', views.salarypackage_pdf_view, name="salary_package")
]