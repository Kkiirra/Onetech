# Generated by Django 4.0.4 on 2022-05-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_preview_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
