# Generated by Django 4.0.6 on 2022-08-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0014_alter_tggroups_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tggroups',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Группа пользователей'),
        ),
    ]
