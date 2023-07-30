from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('accounts.urls')),
    path('freelacersProfiles/', include('freelacersProfiles.urls')),
    path('templates/', include('templates.urls')),
    path('resset/', include('resset.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)