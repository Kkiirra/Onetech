from django.urls import path
from .views import home_page, product_detail, category_list

app_name = 'home'

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('item/<slug:slug>/', product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', category_list, name='category_list')
]
