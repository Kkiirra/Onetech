from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customuser.urls', namespace='customuser')),
    path('', include('home.urls',  namespace='home')),
    path('', include('shop.urls', namespace='shop')),
    path('', include('blog.urls', namespace='blog'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
