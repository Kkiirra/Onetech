from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customuser.urls', namespace='customuser')),
    path('', include('home.urls',  namespace='home')),
    path('', include('shop.urls', namespace='shop')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('basket.urls', namespace='basket')),
    path('', include('others.urls', namespace='others')),
]

urlpatterns += i18n_patterns(
    path('', include('customuser.urls', namespace='customuser')),
    path('', include('home.urls', namespace='home')),
    path('', include('shop.urls', namespace='shop')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('basket.urls', namespace='basket')),
    path('', include('others.urls', namespace='others')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
