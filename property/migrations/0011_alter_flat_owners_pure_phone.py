# Generated by Django 3.2.22 on 2023-10-14 17:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20231013_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='нормализованный номер владельца'),
        ),
    ]
