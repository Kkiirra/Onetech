# Generated by Django 4.0.4 on 2022-05-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_brand_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
