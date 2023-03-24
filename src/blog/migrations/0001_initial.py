# Generated by Django 4.1.7 on 2023-03-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('content', models.TextField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='blog.categories')),
            ],
        ),
    ]