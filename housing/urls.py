from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('owner.urls')),
    path('api/', include('account.urls')),
    path('api/', include('renter.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)