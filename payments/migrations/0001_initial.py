# Generated by Django 4.0.6 on 2022-08-17 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tgbot', '0020_remove_status_stat_id_status_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Сумма счета')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('invoice_payload', models.CharField(blank=True, max_length=150, null=True, verbose_name='invoice_payload')),
                ('provider_payment_charge_id', models.CharField(blank=True, max_length=150, null=True, verbose_name='provider_payment_charge_id')),
                ('telegram_payment_charge_id', models.CharField(blank=True, max_length=150, null=True, verbose_name='telegram_payment_charge_id')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='name')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='phone_number')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Оплачено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж пользователя',
                'verbose_name_plural': 'Платежи пользователей',
                'ordering': ['created_at', 'user'],
            },
        ),
    ]
