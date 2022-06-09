from django.urls import path
from .views import recently_viewed, add_delete_wishlist

app_name = 'others'

urlpatterns = [
    path('recently_add/', recently_viewed, name='recently'),
    path('wish_add/', add_delete_wishlist, name='wish_add'),
]
