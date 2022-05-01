from django.contrib import admin
from .models import Product, Photo


class PhotoAdmin(admin.StackedInline):
    model = Photo


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Product


admin.site.register(Photo)
admin.site.register(Product, ProductAdmin)
