# Generated by Django 4.0.6 on 2022-08-01 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0007_remove_user_needs_userneeds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='referrers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sports',
        ),
        migrations.AlterField(
            model_name='userneeds',
            name='need',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.needs', verbose_name='Потребность'),
        ),
        migrations.CreateModel(
            name='UserSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.sport', verbose_name='Потребность')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Спорт',
                'verbose_name_plural': 'Спорт',
                'ordering': ['user', 'sport'],
            },
        ),
        migrations.CreateModel(
            name='UserReferrers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrer', to='tgbot.user', verbose_name='Рекомендатель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='tgbot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рекомендатель',
                'verbose_name_plural': 'Рекомендатели',
                'ordering': ['user', 'referrer'],
            },
        ),
        migrations.CreateModel(
            name='UserHobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.hobby', verbose_name='Потребность')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Хобби пользователя',
                'verbose_name_plural': 'Хобби пользователя',
                'ordering': ['user', 'hobby'],
            },
        ),
    ]
