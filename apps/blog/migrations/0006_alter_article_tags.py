# Generated by Django 4.1.1 on 2022-09-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(null=True, to='blog.tag', verbose_name='Тэги'),
        ),
    ]
