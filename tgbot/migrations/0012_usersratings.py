# Generated by Django 4.0.6 on 2022-08-12 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0011_user_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, default=3, null=True, verbose_name='Оценка пользователя')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к оценке')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оценка пользователя',
                'verbose_name_plural': 'Оценки пользователей',
                'ordering': ['user', 'rating'],
            },
        ),
    ]
