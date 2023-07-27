from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('gallery/', include('gallery.urls')),
    path('admin_for_staff/', include('admin_for_staff.urls')),
    path('user/', include('user.urls')),
    path('captcha/', include('captcha.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
