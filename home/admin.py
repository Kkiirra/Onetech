from django.contrib import admin
from .models import Product, Photo, Category, Top_seller


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


class PhotoAdmin(admin.StackedInline):
    model = Photo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]
    list_display = ['product_name', 'category', 'is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('product_name',)}

    class Meta:
        model = Product


@admin.register(Top_seller)
class Top_seller(admin.ModelAdmin):
    list_display = ['product', ]
