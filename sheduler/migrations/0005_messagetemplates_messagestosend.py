# Generated by Django 4.0.6 on 2022-08-20 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0027_remove_messagestosend_receiver_and_more'),
        ('sheduler', '0004_remove_tasks_task_type_delete_tasktypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, verbose_name='Код')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('file', models.FileField(blank=True, null=True, upload_to='templates', verbose_name='Файл')),
                ('file_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='file_id')),
            ],
            options={
                'verbose_name': 'Шаблон сообщения',
                'verbose_name_plural': 'Шаблоны сообщений',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='MessagesToSend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_user_id', models.BigIntegerField(blank=True, null=True, verbose_name='ID пользователя')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('sended_at', models.DateTimeField(blank=True, null=True, verbose_name='Отослано в')),
                ('sended', models.BooleanField(default=False, verbose_name='Отослано')),
                ('file', models.FileField(blank=True, null=True, upload_to='messages', verbose_name='Файл')),
                ('file_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='file_id')),
                ('reply_markup', models.JSONField(blank=True, null=True)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='tgbot.user', verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Сообщение к отсылке',
                'verbose_name_plural': 'Сообщения к отсылке',
                'ordering': ['created_at'],
            },
        ),
    ]
