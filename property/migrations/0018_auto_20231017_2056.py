# Generated by Django 3.2.22 on 2023-10-17 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0017_auto_20231017_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='text',
            field=models.TextField(default='default text', verbose_name='текст жалобы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.flat', verbose_name='квартира, на которую жаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='кто жаловался'),
        ),
    ]
