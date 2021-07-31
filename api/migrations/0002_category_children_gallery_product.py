# Generated by Django 3.2.5 on 2021-07-20 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('type', models.CharField(choices=[('grocery', 'Grocery'), ('bakery', 'Bakery'), ('restaurant', 'Restaurant')], max_length=50)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('salePrice', models.IntegerField()),
                ('discountInPercent', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('type', models.CharField(choices=[('grocery', 'Grocery'), ('bakery', 'Bakery'), ('restaurant', 'Restaurant')], max_length=50)),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('type', models.CharField(choices=[('grocery', 'Grocery'), ('bakery', 'Bakery'), ('restaurant', 'Restaurant')], max_length=50)),
                ('children', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.children')),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product')),
            ],
        ),
    ]
