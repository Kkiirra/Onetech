# Generated by Django 4.0.4 on 2022-05-28 10:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_product_is_faivorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_faivorite',
        ),
        migrations.AddField(
            model_name='product',
            name='is_faivorite',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
