# Generated by Django 4.0.6 on 2022-08-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0016_user_inn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='inn',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='ИНН'),
        ),
    ]
