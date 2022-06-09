from django.urls import path
from .views import basket_add, basket_page, basket_delete

app_name = 'basket'

urlpatterns = [
    path('', basket_add, name='basket_add'),
    path('basket/', basket_page, name='basket_page'),
    path('basket_delete/', basket_delete, name='basket_delete'),
]
