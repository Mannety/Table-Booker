# Generated by Django 3.0.8 on 2021-06-20 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table_booker', '0002_auto_20210617_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='advance_booking',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='max_guest',
        ),
    ]
