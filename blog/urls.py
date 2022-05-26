from django.urls import path
from .views import single_blog, blogs_page

app_name = 'blog'

urlpatterns = [
    path('blog/', blogs_page, name='blogs_page'),
    path('single_blog/<slug:slug_item>', single_blog, name='single_blog')
]
