# Generated by Django 3.2.5 on 2021-08-03 07:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210803_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 7, 8, 49, 921056, tzinfo=utc)),
        ),
    ]
