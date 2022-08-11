# Generated by Django 4.0.6 on 2022-08-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0002_alter_tasks_task_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['name'], 'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AlterField(
            model_name='tasks',
            name='day',
            field=models.IntegerField(blank=True, null=True, verbose_name='День месяца'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='interval',
            field=models.IntegerField(blank=True, null=True, verbose_name='интервал выполнения, сек.'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активно'),
        ),
    ]