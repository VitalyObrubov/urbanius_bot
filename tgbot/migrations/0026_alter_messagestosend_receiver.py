# Generated by Django 4.0.6 on 2022-08-19 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0025_messagestosend_receiver_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagestosend',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='tgbot.user', verbose_name='Получатель'),
        ),
    ]
