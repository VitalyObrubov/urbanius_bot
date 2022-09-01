# Generated by Django 4.0.6 on 2022-08-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0028_user_segment_user_turnover'),
    ]

    operations = [
        migrations.AddField(
            model_name='tggroups',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='events', verbose_name='Фото/Видео'),
        ),
        migrations.AddField(
            model_name='tggroups',
            name='file_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='file_id'),
        ),
        migrations.AddField(
            model_name='tggroups',
            name='for_all_users',
            field=models.BooleanField(default=False, verbose_name='Для всех пользователей'),
        ),
        migrations.AddField(
            model_name='tggroups',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Описание группыt'),
        ),
    ]