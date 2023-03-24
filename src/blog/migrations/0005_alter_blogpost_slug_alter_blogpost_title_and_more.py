# Generated by Django 4.1.7 on 2023-03-24 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blogpost_category_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, help_text='Slug of the post', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(help_text='Title of the post', max_length=200, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, help_text='Slug of the category', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(help_text='Title of the category', max_length=200, unique=True, verbose_name='Title'),
        ),
    ]
