from django.urls import path
from .views import home_page, product_detail

app_name = 'home'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('item/<slug:slug>/', product_detail, name='product_detail'),
]
