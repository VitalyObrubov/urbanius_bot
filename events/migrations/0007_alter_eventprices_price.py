# Generated by Django 4.0.6 on 2022-08-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_eventprices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventprices',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Стоимость мероприятия'),
        ),
    ]