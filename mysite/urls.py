from django.contrib import admin
from django.urls import include, path
import accounts.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('polls/', include('polls.urls')),
   path('politicians/', include('politicians.urls')),
   path('admin/', admin.site.urls),
   path("accounts/", include(accounts.urls)),
   path("facerec/", include("facerec.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)