# Generated by Django 3.2.3 on 2021-06-03 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oxygen', '0011_remove_oxygen_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='oxygen',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 7, 47, 2, 977097, tzinfo=utc)),
        ),
    ]
