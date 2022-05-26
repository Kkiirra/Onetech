from django.urls import path
from .views import home_page, product_detail, search_product

app_name = 'home'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('search_product/', search_product, name='search_product'),
    path('item/<slug:slug>/', product_detail, name='product_detail'),
]
