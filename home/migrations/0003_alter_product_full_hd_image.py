# Generated by Django 4.0.4 on 2022-05-08 18:53

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_options_alter_product_full_hd_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='full_hd_image',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path),
        ),
    ]
