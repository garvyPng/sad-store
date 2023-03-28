from django.contrib import admin
from django.urls import path, include
from config.views import home
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('apps.blog.urls')),
    path('catalog/', include('apps.catalog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
