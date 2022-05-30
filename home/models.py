from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
import os
import shutil


def user_directory_path(instance, file_name):
    try:
        return f'media/product_{instance.product_name}/{file_name}'
    except AttributeError:
        return f'media/product_{instance.product.product_name}/{file_name}'


class Brand(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'brands'

    def get_absolute_url(self):
        return reverse('shop:brand_list', args=[self.slug])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE, null=True)

    product_name = models.CharField(max_length=255)
    product_text = models.TextField()

    full_hd_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    preview_photo = models.ImageField(upload_to=user_directory_path, null=True)

    available = models.IntegerField(blank=True, null=True, default=0)
    sold = models.IntegerField(blank=True, null=True, default=0)

    slug = models.SlugField(max_length=255, null=True)
    product_cost = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6,
                                       verbose_name='Discount cost')
    old_cost = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6, verbose_name='Normal Cost')

    trends = models.BooleanField(blank=True, default=True)
    new = models.BooleanField(blank=True, default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('is_active',)

    def get_absolute_url(self):
        return reverse('shop:singleproduct', args=[self.slug])

    def __str__(self):
        return self.product_name


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)


class Top_seller(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


@receiver(pre_delete, sender=Product)
def delete_photo_files(sender, instance, **kwargs):
    path = os.path.join(os.path.abspath(os.path.dirname('media')),
                        os.path.join('media', f'product_{instance.product_name}'))
    shutil.rmtree(path)
