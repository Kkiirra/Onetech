# Generated by Django 4.0.4 on 2022-05-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_faivorite',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
