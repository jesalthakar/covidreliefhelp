# Generated by Django 3.2.3 on 2021-05-28 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oxygen', '0002_oxygen_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oxygen',
            old_name='date_of_entry',
            new_name='created',
        ),
    ]
