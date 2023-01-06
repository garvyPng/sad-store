from django.contrib import admin
from django.urls import path, include
from config.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('apps.blog.urls'))
]
