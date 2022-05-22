from django.urls import path
from .views import shop_page, category_list, brand_list, singleproduct

app_name = 'shop'

urlpatterns = [
    path('shop_page/', shop_page, name='shop_page'),
    path('search/category/<slug:category_slug>/', category_list, name='category_list'),
    path('search/brand/<slug:brand_slug>/', brand_list, name='brand_list'),
    path('search/singleproduct/<slug:product_slug>/', singleproduct, name='singleproduct')
]
