

from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from django.conf import settings


urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    # Path de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),

    # paths de messenger
    path('messenger/', include(messenger_patterns)),

]

if settings.DEBUG:
    from django.conf.urls.static import static
   # Esta es una característica de Django que le permite servir archivos multimedia durante el
   # desarrollo.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)