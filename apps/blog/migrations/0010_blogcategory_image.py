# Generated by Django 4.1.1 on 2023-01-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_add_blog_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]
