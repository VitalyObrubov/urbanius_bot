# Generated by Django 4.0.6 on 2022-08-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0010_messagetemplates_alter_messagestosend_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(blank=True, default=3, null=True, verbose_name='Итоговый ретинг'),
        ),
    ]