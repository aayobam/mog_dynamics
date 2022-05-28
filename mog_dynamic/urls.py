from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .views import home_view, contact_view, about_view

admin.site.site_header = "Mog Dynamics Administration"
admin.site.site_title = "Mog Dynamics"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('contact/', contact_view, name="contact-us"),
    path('about/', about_view, name="feature"),
    path('shipping/', include("apps.shipping.urls")),
    path('logistics/', include("apps.logistics.urls")),
    path('forex/', include("apps.forex.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
