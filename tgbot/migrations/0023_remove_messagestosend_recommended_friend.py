# Generated by Django 4.0.6 on 2022-08-18 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0022_messagetemplates_file_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagestosend',
            name='recommended_friend',
        ),
    ]