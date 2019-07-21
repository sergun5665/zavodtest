from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zavodnews.urls')),
    path('allnews', include('zavodnews.urls')),
    path('news/', include('zavodnews.urls')),
    path('tagnews/', include('zavodnews.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
