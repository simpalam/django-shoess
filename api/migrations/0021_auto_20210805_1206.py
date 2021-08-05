# Generated by Django 3.2.5 on 2021-08-05 06:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210804_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120)),
                ('productid', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('image', models.TextField()),
                ('price', models.CharField(max_length=120)),
                ('salePrice', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 6, 36, 15, 394934, tzinfo=utc)),
        ),
    ]