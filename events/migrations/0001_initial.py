# Generated by Django 4.0.6 on 2022-08-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата мероприятия')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время мероприятия')),
                ('name', models.CharField(max_length=150, verbose_name='Название мероприятия')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('place', models.CharField(blank=True, max_length=150, null=True, verbose_name='Место проведения')),
                ('event_link', models.URLField(blank=True, null=True, verbose_name='Страница события')),
                ('regisration_link', models.URLField(blank=True, null=True, verbose_name='Страница формы регистрации')),
                ('file', models.FileField(blank=True, null=True, upload_to='events', verbose_name='Фото/Видео')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['date', 'time'],
            },
        ),
        migrations.CreateModel(
            name='EventTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Код типа мероприятия')),
                ('name', models.CharField(max_length=150, verbose_name='Тип мероприятия')),
            ],
            options={
                'verbose_name': 'Тип мероприятия',
                'verbose_name_plural': 'Типы мероприятий',
                'ordering': ['name'],
            },
        ),
    ]