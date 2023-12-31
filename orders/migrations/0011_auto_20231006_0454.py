# Generated by Django 3.2.18 on 2023-10-05 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20231006_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default='', verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default=datetime.time(4, 54, 30, 82146), verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 4, 54, 30, 82113), verbose_name='Время создания заказа'),
        ),
    ]
