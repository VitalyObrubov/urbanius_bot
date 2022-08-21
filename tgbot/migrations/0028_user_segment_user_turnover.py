# Generated by Django 4.0.6 on 2022-08-21 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0027_remove_messagestosend_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='segment',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Сегмент'),
        ),
        migrations.AddField(
            model_name='user',
            name='turnover',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Оборот компании'),
        ),
    ]
