# Generated by Django 4.0.6 on 2022-08-25 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('tgbot', '0029_tggroups_file_tggroups_file_id_and_more'),
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackagePrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Стоимость')),
                ('period', models.IntegerField(verbose_name='Период, мес.')),
                ('for_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tgbot.status', verbose_name='Для статуса')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscribe.clubpackages', verbose_name='Пакет')),
            ],
            options={
                'verbose_name': 'Стоимость пакета',
                'verbose_name_plural': 'Стоимость пакетов',
                'ordering': ['package'],
            },
        ),
        migrations.CreateModel(
            name='PackageRequests',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, verbose_name='Номер заявки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Стоимость пакета')),
                ('date_from', models.DateField(verbose_name='Период с')),
                ('date_to', models.DateField(verbose_name='Период по')),
                ('payed', models.BooleanField(default=False, verbose_name='Оплачена')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Подтверждена')),
                ('for_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tgbot.status', verbose_name='Для статуса')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscribe.clubpackages', verbose_name='Пакет участия')),
                ('package_price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscribe.packageprices', verbose_name='Цена пакета')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payments.payments', verbose_name='Документ платежа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка на пакет участия',
                'verbose_name_plural': 'Заявки на пакет участия',
                'ordering': ['created_at', 'package', 'user'],
            },
        ),
    ]