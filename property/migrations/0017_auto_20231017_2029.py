# Generated by Django 3.2.22 on 2023-10-17 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20231015_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owned_flats',
            new_name='flats',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_pure_phone',
            new_name='pure_phone',
        ),
    ]
