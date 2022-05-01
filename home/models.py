from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
import shutil


def user_directory_path(instance, file_name):
    return f'media/product_{instance.product.product_name}/{file_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=40)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    product_text = models.TextField()
    # product_color = models.CharField()
    # product_cost = models.PositiveIntegerField()
    # old_cost = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)


@receiver(pre_delete, sender=Product)
def update_cart(sender, instance, **kwargs):
    path = os.path.join(os.path.abspath(os.path.dirname('media')),
                        os.path.join('media', f'product_{instance.product_name}'))
    shutil.rmtree(path)
