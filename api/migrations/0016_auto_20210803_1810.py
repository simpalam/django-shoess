# Generated by Django 3.2.5 on 2021-08-03 12:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 12, 40, 17, 547673, tzinfo=utc)),
        ),
    ]
