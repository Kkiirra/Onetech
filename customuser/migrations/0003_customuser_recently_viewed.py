# Generated by Django 4.0.4 on 2022-06-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_product_is_faivorite'),
        ('customuser', '0002_customuser_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='recently_viewed',
            field=models.ManyToManyField(related_name='Recently_viewed', to='home.product'),
        ),
    ]
