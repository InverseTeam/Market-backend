# Generated by Django 3.2.18 on 2023-10-05 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20231005_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default=datetime.time(10, 41, 44, 167522), verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.time(10, 41, 44, 167476), verbose_name='Время создания заказа'),
        ),
    ]