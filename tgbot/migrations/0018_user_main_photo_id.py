# Generated by Django 4.0.6 on 2022-08-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0017_alter_user_inn'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='main_photo_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='id основного фото'),
        ),
    ]