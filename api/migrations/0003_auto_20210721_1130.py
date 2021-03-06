# Generated by Django 3.2.5 on 2021-07-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_children_gallery_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='children',
        ),
        migrations.AddField(
            model_name='category',
            name='children',
            field=models.ManyToManyField(to='api.Children'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='api.Product'),
        ),
        migrations.RemoveField(
            model_name='children',
            name='products',
        ),
        migrations.AddField(
            model_name='children',
            name='products',
            field=models.ManyToManyField(to='api.Product'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='gallery',
        ),
        migrations.AddField(
            model_name='product',
            name='gallery',
            field=models.ManyToManyField(to='api.Gallery'),
        ),
    ]
