# Generated by Django 4.0.4 on 2022-05-12 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_brand_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'brands'},
        ),
    ]
