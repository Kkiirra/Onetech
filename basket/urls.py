from django.urls import path
from .views import basket_add

app_name = 'basket'

urlpatterns = [
    path('', basket_add, name='basket_add')
]
