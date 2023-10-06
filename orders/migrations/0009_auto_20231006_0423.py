# Generated by Django 3.2.18 on 2023-10-05 23:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20231006_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default=datetime.time(4, 23, 47, 97652), verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 4, 23, 47, 97607), verbose_name='Время создания заказа'),
        ),
    ]