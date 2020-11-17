from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ocr_app/", include("ocr_app.urls")),
    path("", RedirectView.as_view(url='/ocr_app/list/', permanent=True)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
