# Generated by Django 2.1.1 on 2018-09-08 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180908_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productorder',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]
